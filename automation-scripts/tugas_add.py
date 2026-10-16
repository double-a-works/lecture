import asyncio, sys, json
sys.path.insert(0, "/tmp")
from cdp_ws import connect

NAMA = "Latihan Soal Trigonometri - Pertemuan 4 (25 Soal)"
KETERANGAN = ("Kerjakan 25 soal latihan trigonometri (rasio SOH-CAH-TOA, konversi derajat-radian, "
              "sudut istimewa, identitas trigonometri, lingkaran satuan, menyelesaikan segitiga "
              "siku-siku, dan aplikasi trigonometri dalam teknik). Unggah jawaban dalam format PDF "
              "sebelum batas waktu.")
FILE_PATH = "/tmp/NS1_Meeting4_Soal25.pdf"
MAX_MB = "50"
TERSEDIA_DATE = "14/10/2026"
TERSEDIA_TIME = "00:00"


async def main():
    kelas_url, batas_date, batas_time = sys.argv[1], sys.argv[2], sys.argv[3]
    d = await connect()
    await d.send("Page.enable")
    await d.send("Page.navigate", {"url": kelas_url})
    await asyncio.sleep(3)

    r = await d.eval("""
      (function(){
        const els = Array.from(document.querySelectorAll("a, div, li, span"));
        const target = els.find(e => e.textContent.trim() === "Tugas Kuliah" && e.children.length===0);
        if (target) { target.click(); return "clicked"; }
        return "not found";
      })()
    """)
    print("tab:", r)
    await asyncio.sleep(2)

    existing = await d.eval("""
      (function(){
        const rows = Array.from(document.querySelectorAll("table tbody tr"));
        return JSON.stringify(rows.map(r => r.innerText.split("\\n")[0]));
      })()
    """)
    print("existing tugas:", existing)
    if "Trigonometri" in existing:
        print("ABORT: tugas trigonometri sudah ada, skip")
        return

    r = await d.eval("""
      (function(){
        const btns = Array.from(document.querySelectorAll("button"));
        const btn = btns.find(b => b.textContent.trim() === "Tambah Tugas Kuliah");
        if (btn) { btn.click(); return "clicked"; }
        return "not found";
      })()
    """)
    print("open dialog:", r)
    await asyncio.sleep(1.5)

    r = await d.eval("""
      (function(nama){
        const dialog = document.querySelector(".q-dialog, [role=dialog]");
        const inputs = Array.from(dialog.querySelectorAll("input"));
        const target = inputs.find(i => i.type === "text");
        if (!target) return "nama input not found";
        const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        setter.call(target, nama);
        target.dispatchEvent(new Event("input", {bubbles:true}));
        target.dispatchEvent(new Event("change", {bubbles:true}));
        return "nama filled: " + target.value;
      })(%s)
    """ % json.dumps(NAMA))
    print("nama:", r)

    r2 = await d.send("DOM.getDocument", {"depth": -1, "pierce": True})
    root_id = r2["result"]["root"]["nodeId"]
    r2 = await d.send("DOM.querySelector", {"nodeId": root_id, "selector": ".ql-editor"})
    editor_node_id = r2["result"]["nodeId"]
    if editor_node_id == 0:
        print("ql-editor not found")
    else:
        r2 = await d.send("DOM.resolveNode", {"nodeId": editor_node_id})
        obj_id = r2["result"]["object"]["objectId"]
        r2 = await d.send("Runtime.callFunctionOn", {
            "objectId": obj_id,
            "functionDeclaration": """
                function(desk){
                    this.focus();
                    document.execCommand('selectAll', false, null);
                    document.execCommand('insertText', false, desk);
                    return this.innerText;
                }
            """,
            "arguments": [{"value": KETERANGAN}],
            "returnByValue": True
        })
        print("keterangan:", r2["result"]["result"]["value"][:80])
    await asyncio.sleep(0.3)

    r2 = await d.send("DOM.querySelector", {"nodeId": root_id, "selector": "input[type=file]"})
    file_node_id = r2["result"]["nodeId"]
    r2 = await d.send("DOM.setFileInputFiles", {"files": [FILE_PATH], "nodeId": file_node_id})
    print("file set")
    await asyncio.sleep(1.0)

    r = await d.eval("""
        (function(sd, st, ed, et, mb){
            const dialog = document.querySelector(".q-dialog, [role=dialog]");
            const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            function setVal(input, val) {
                setter.call(input, val);
                input.dispatchEvent(new Event("input", {bubbles:true}));
                input.dispatchEvent(new Event("change", {bubbles:true}));
                input.dispatchEvent(new Event("blur", {bubbles:true}));
            }
            const allInputs = Array.from(dialog.querySelectorAll("input"));
            const dateInputs = allInputs.filter(i => i.placeholder === "dd/mm/yyyy");
            const timeInputs = allInputs.filter(i => i.placeholder === "Select time" || (i.value && /^\\d{2}:\\d{2}$/.test(i.value)));
            let log = [];
            if (dateInputs[0]) { setVal(dateInputs[0], sd); log.push("date0 set"); }
            if (dateInputs[1]) { setVal(dateInputs[1], ed); log.push("date1 set"); }
            if (timeInputs[0]) { setVal(timeInputs[0], st); log.push("time0 set"); }
            if (timeInputs[1]) { setVal(timeInputs[1], et); log.push("time1 set"); }
            const mbInput = allInputs.find(i => i.type === "number");
            if (mbInput) { setVal(mbInput, mb); log.push("mb set"); }
            return JSON.stringify({dateCount: dateInputs.length, timeCount: timeInputs.length, log});
        })(%s, %s, %s, %s, %s)
    """ % (json.dumps(TERSEDIA_DATE), json.dumps(TERSEDIA_TIME), json.dumps(batas_date), json.dumps(batas_time), json.dumps(MAX_MB)))
    print("dates:", r)
    await asyncio.sleep(0.5)

    # verify fields before submitting
    verify = await d.eval("""
      (function(){
        const dialog = document.querySelector(".q-dialog, [role=dialog]");
        const inputs = Array.from(dialog.querySelectorAll("input"));
        return JSON.stringify(inputs.map(i => ({type:i.type, val:i.value})));
      })()
    """)
    print("verify inputs:", verify)


asyncio.run(main())
