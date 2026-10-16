import sys, re, json, time, datetime
sys.path.insert(0, "/tmp")
from cdp_helpers import get_ws, CDP

MONTHS = {
    "Jan":1,"Feb":2,"Mar":3,"Apr":4,"Mei":5,"Jun":6,
    "Jul":7,"Agt":8,"Sep":9,"Okt":10,"Nov":11,"Des":12
}

def wib_now():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=7)

def parse_cards(text):
    """Parse the Beranda 'Jadwal Dosen > Hari Ini' block from body.innerText."""
    if "Hari Ini" not in text:
        return []
    section = text.split("Hari Ini", 1)[1]
    section = section.split("Kalender Akademik", 1)[0]
    # Each card roughly matches this pattern
    pattern = re.compile(
        r"\d{4}\s*-\s*(?P<code>\S+)\s+(?P<course>.+?)\s*-\s*\n\(\d+\s*SKS\)\s*-\s*(?P<kelas>.+?)\nJadwal Kuliah\nPertemuan ke-(?P<pertemuan>\d+)\n"
        r"(?P<start>\d{2}:\d{2})\s*-\s*(?P<end>\d{2}:\d{2})\n(?P<date>\d{1,2}\s+\w+\s+\d{4})\n.+?\n\n(?P<materi>.+?)\n\n(?P<status>Telah Berakhir|Akhiri Kuliah)",
        re.DOTALL
    )
    cards = []
    for m in pattern.finditer(section):
        d = m.groupdict()
        day, mon, year = d["date"].split()
        dt_end = datetime.datetime(int(year), MONTHS.get(mon, 1), int(day),
                                    int(d["end"][:2]), int(d["end"][3:]))
        cards.append({
            "course": d["course"].strip(),
            "kelas": d["kelas"].strip(),
            "pertemuan": d["pertemuan"],
            "end_dt": dt_end,
            "materi": d["materi"].strip(),
            "status": d["status"].strip(),
        })
    return cards

def main():
    page_id = get_ws()
    cdp = CDP(page_id)
    cdp.call("Page.enable")
    cdp.call("Runtime.enable")
    cdp.call("Page.navigate", {"url": "https://politeknikkirana.portaldosen.siakad.tech/"})
    time.sleep(3)

    text = cdp.eval("document.body.innerText")
    cards = parse_cards(text)
    now = wib_now()

    report = {"checked_at_wib": now.isoformat(), "cards": [], "actions": []}

    for c in cards:
        overdue_min = (now - c["end_dt"]).total_seconds() / 60.0
        c_report = {
            "course": c["course"], "kelas": c["kelas"], "pertemuan": c["pertemuan"],
            "end_time": c["end_dt"].isoformat(), "status": c["status"],
            "overdue_min": round(overdue_min, 1)
        }
        report["cards"].append(c_report)

        if c["status"] == "Akhiri Kuliah" and overdue_min > 10:
            # Fix presensi for Abdul Hakim if TRA 26C, then close the class.
            course_js = json.dumps(c["course"])
            if "26C" in c["kelas"]:
                fix = cdp.eval(f"""
                (function(){{
                  const links = Array.from(document.querySelectorAll('a'))
                    .filter(a => a.href && (a.href.includes('presensi-mahasiswa')) );
                  for (const a of links) {{
                    let el = a, courseMatch = false;
                    for (let i=0;i<10 && el;i++) {{
                      if (el.innerText && el.innerText.includes({course_js})) {{ courseMatch = true; break; }}
                      el = el.parentElement;
                    }}
                    if (courseMatch) return a.href;
                  }}
                  return null;
                }})()
                """)
                if fix:
                    cdp.call("Page.navigate", {"url": fix})
                    time.sleep(3)
                    mark = cdp.eval("""
                    (function(){
                      const rows = Array.from(document.querySelectorAll('*')).filter(el =>
                        el.children.length === 0 && el.innerText && el.innerText.trim() === 'ABDUL HAKIM'.toUpperCase() ? false : false);
                      // locate the block containing the student's name text, then its 'A' button
                      const all = Array.from(document.querySelectorAll('*'));
                      let target = null;
                      for (const el of all) {
                        if (el.children.length === 0 && /ABDUL HAKIM/i.test(el.textContent || '')) { target = el; break; }
                      }
                      if (!target) return 'name-not-found';
                      let container = target;
                      for (let i=0;i<6 && container; i++) container = container.parentElement;
                      if (!container) return 'container-not-found';
                      const btns = Array.from(container.querySelectorAll('button, div')).filter(b => b.innerText && b.innerText.trim() === 'A');
                      if (!btns.length) return 'A-button-not-found';
                      btns[0].click();
                      return 'marked-A';
                    })()
                    """)
                    c_report["abdul_hakim_fix"] = mark
                    time.sleep(1)
                    cdp.call("Page.navigate", {"url": "https://politeknikkirana.portaldosen.siakad.tech/"})
                    time.sleep(3)

            clicked = cdp.eval(f"""
            (function(){{
              const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Akhiri Kuliah');
              for (const b of btns) {{
                let el = b, match = false;
                for (let i=0;i<10 && el; i++) {{
                  if (el.innerText && el.innerText.includes({course_js})) {{ match = true; break; }}
                  el = el.parentElement;
                }}
                if (match) {{ b.click(); return 'clicked'; }}
              }}
              return 'button-not-found';
            }})()
            """)
            c_report["akhiri_click"] = clicked
            time.sleep(1.5)

            if clicked == "clicked":
                copy_res = cdp.eval("""
                (function(){
                  const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Salin dari Rencana Pertemuan');
                  if (!btns.length) return 'copy-button-not-found';
                  btns[0].click();
                  return 'copied';
                })()
                """)
                c_report["copy_rencana"] = copy_res
                time.sleep(1)

                save_res = cdp.eval("""
                (function(){
                  const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Simpan & Akhiri Kuliah');
                  if (!btns.length) return 'save-button-not-found';
                  btns[0].click();
                  return 'saved';
                })()
                """)
                c_report["save_akhiri"] = save_res
                time.sleep(2)

                final_text = cdp.eval("document.body.innerText.slice(0,500)")
                c_report["after_text_snippet"] = final_text

            report["actions"].append(c_report)

    print(json.dumps(report, default=str))

if __name__ == "__main__":
    main()
