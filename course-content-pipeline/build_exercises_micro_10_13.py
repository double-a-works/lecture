#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Digital_Technic_Micro meetings 10-13,
in lectures/meeting<N>/exercise/ (separate from exercises/ assignment PDFs)."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Digital Technic: Microprocessor Systems"
COURSE_CODE = "AV0302DT"

MEETINGS = {
    10: {
        "topic": "Integrated Circuits (IC) \\& Integration Scale",
        "subcpmk": "Mampu mengklasifikasikan integrated circuit dan skala integrasinya.",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"A chip is a single package containing an 8-bit microprocessor core (thousands of gates). Which integration scale does it belong to?",
             r"Sebuah chip adalah satu paket berisi inti mikroprosesor 8-bit (ribuan gerbang). Termasuk skala integrasi apakah chip ini?",
             r"LSI (Large-Scale Integration): an 8-bit microprocessor core falls in the 100--10,000 gate range, well above MSI but below the $>10{,}000$-gate VLSI threshold. \textbf{Answer: LSI.}",
             r"LSI (Large-Scale Integration): inti mikroprosesor 8-bit berada pada rentang 100--10.000 gerbang, di atas MSI tetapi di bawah ambang VLSI ($>10.000$ gerbang). \textbf{Jawaban: LSI.}"),
            ("Application",
             r"An avionics team must replace 40 discrete SSI logic-gate chips with a single VLSI microcontroller performing the same overall function. List two concrete benefits this brings to an aircraft LRU.",
             r"Tim avionik harus mengganti 40 chip gerbang logika SSI diskrit dengan satu mikrokontroler VLSI yang menjalankan fungsi keseluruhan yang sama. Sebutkan dua manfaat konkret hal ini bagi LRU pesawat.",
             r"(1) Reduced size and weight -- one VLSI chip replaces 40 packages plus their interconnecting wiring/solder joints, directly cutting LRU mass. (2) Improved reliability -- far fewer solder joints and external wires means far fewer potential failure points in a flight-critical box.",
             r"(1) Ukuran dan berat berkurang -- satu chip VLSI menggantikan 40 paket beserta kabel/sambungan solder penghubungnya, langsung memangkas massa LRU. (2) Keandalan meningkat -- jauh lebih sedikit sambungan solder dan kabel eksternal berarti jauh lebih sedikit titik potensi kegagalan pada kotak flight-critical."),
            ("Analytical",
             r"A VLSI chip and an SSI chip both fail intermittently in the field. Explain why the repair approach differs between the two, and what this implies for spares strategy on an aircraft.",
             r"Sebuah chip VLSI dan chip SSI sama-sama gagal secara intermiten di lapangan. Jelaskan mengapa pendekatan perbaikan berbeda antara keduanya, dan apa implikasinya bagi strategi suku cadang pesawat.",
             r"An SSI chip's few internal gates can sometimes be diagnosed and, in older discrete-board designs, isolated/replaced at the component level with a probe. A VLSI chip's millions of internal gates cannot be probed or repaired at the transistor level -- a faulty VLSI chip must simply be swapped for a whole new unit. \textbf{Implication:} aircraft maintenance for VLSI-based LRUs relies on line-replaceable-unit (LRU) swap-and-test strategies with spare whole units, rather than component-level bench repair.",
             r"Beberapa gerbang internal chip SSI kadang bisa didiagnosis dan, pada desain papan diskrit lama, diisolasi/diganti di level komponen dengan probe. Jutaan gerbang internal chip VLSI tidak bisa diprobe atau diperbaiki di level transistor -- chip VLSI yang rusak harus diganti seluruhnya. \textbf{Implikasi:} perawatan pesawat untuk LRU berbasis VLSI mengandalkan strategi tukar-dan-uji unit pengganti utuh (line-replaceable-unit), bukan perbaikan level komponen di bengkel."),
        ],
    },
    11: {
        "topic": "Logic Families: TTL vs CMOS",
        "subcpmk": "Mampu membandingkan karakteristik TTL dan CMOS serta merancang antarmuka antar keduanya.",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Which logic family, TTL or CMOS, has near-zero static power consumption, and why?",
             r"Logic family mana, TTL atau CMOS, yang memiliki konsumsi daya statis hampir nol, dan mengapa?",
             r"CMOS. Its complementary PMOS/NMOS pair means one transistor is always off in each steady logic state, so almost no current flows except momentarily during switching -- unlike TTL's bipolar transistors, which draw continuous static current even when idle.",
             r"CMOS. Pasangan PMOS/NMOS komplementernya membuat satu transistor selalu mati pada setiap keadaan logika stabil, sehingga hampir tidak ada arus mengalir kecuali sesaat saat switching -- berbeda dari transistor bipolar TTL yang menarik arus statis terus-menerus bahkan saat idle."),
            ("Application",
             r"A CMOS output with $I_{OL}=8\text{mA}$ drives TTL inputs that each require $I_{IL}=1.6\text{mA}$ to guarantee a LOW. What is the fan-out on the LOW side?",
             r"Output CMOS dengan $I_{OL}=8\text{mA}$ menggerakkan input TTL yang masing-masing membutuhkan $I_{IL}=1{,}6\text{mA}$ untuk menjamin LOW. Berapa fan-out pada sisi LOW?",
             r"Fan-out $=I_{OL}/I_{IL}=8/1.6=5$. \textbf{Answer: the output can reliably drive 5 TTL inputs} on the LOW side (the HIGH-side limit must also be checked and the smaller value used).",
             r"Fan-out $=I_{OL}/I_{IL}=8/1{,}6=5$. \textbf{Jawaban: output dapat menggerakkan andal 5 input TTL} pada sisi LOW (batas sisi HIGH juga harus diperiksa dan nilai yang lebih kecil yang dipakai)."),
            ("Analytical",
             r"An engineer mixes 3.3V CMOS and 5V TTL chips on the same avionics board without any level-shifting, arguing \"both are digital logic so it should work.\" Identify the two distinct risks in this design and how to fix each.",
             r"Seorang insinyur mencampur chip CMOS 3,3V dan TTL 5V pada papan avionik yang sama tanpa level-shifting, beralasan ``keduanya logika digital jadi seharusnya bekerja.'' Identifikasi dua risiko berbeda dalam desain ini dan cara memperbaiki masing-masing.",
             r"(1) Logic-level mismatch: 5V TTL outputs can exceed the 3.3V CMOS input's absolute maximum rating, risking permanent damage to the CMOS chip -- fix by inserting a level-shifter/translator IC between the two supply domains. (2) Insufficient $V_{OH}$ from the lower-voltage side driving the higher-voltage side's $V_{IH}$ threshold (undriven/floating inputs at the interface are also a CMOS risk) -- fix by matching $V_{IH}/V_{IL}$ vs.\ $V_{OH}/V_{OL}$ explicitly and adding pull-ups/pull-downs on any CMOS input that might float.",
             r"(1) Ketidakcocokan level logika: output TTL 5V bisa melampaui rating maksimum absolut input CMOS 3,3V, berisiko merusak chip CMOS secara permanen -- perbaiki dengan menyisipkan IC level-shifter/translator di antara kedua domain suplai. (2) $V_{OH}$ dari sisi tegangan lebih rendah tidak cukup untuk memenuhi ambang $V_{IH}$ sisi tegangan lebih tinggi (input yang tidak digerakkan/mengambang di antarmuka juga risiko bagi CMOS) -- perbaiki dengan mencocokkan $V_{IH}/V_{IL}$ vs $V_{OH}/V_{OL}$ secara eksplisit dan menambahkan pull-up/pull-down pada input CMOS mana pun yang berpotensi mengambang."),
        ],
    },
    12: {
        "topic": "Electrical Characteristics \\& IC Packaging",
        "subcpmk": "Mampu membaca dan menerapkan parameter elektrik datasheet serta memilih kemasan IC yang sesuai.",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Define propagation delay and state which of $t_{PLH}$ or $t_{PHL}$ a designer should use as the worst-case timing-budget value.",
             r"Definisikan propagation delay dan sebutkan mana dari $t_{PLH}$ atau $t_{PHL}$ yang harus dipakai desainer sebagai nilai anggaran waktu terburuk.",
             r"Propagation delay is the time from a valid input change to the corresponding output change. \textbf{Use the larger of $t_{PLH}$ and $t_{PHL}$} as the worst-case value for timing budgets.",
             r"Propagation delay adalah waktu dari perubahan input yang valid hingga perubahan output yang bersesuaian. \textbf{Gunakan nilai yang lebih besar antara $t_{PLH}$ dan $t_{PHL}$} sebagai nilai terburuk untuk anggaran waktu."),
            ("Application",
             r"A gate has $I_{OH}=200\,\mu A$, $I_{IH}=20\,\mu A$, $I_{OL}=4\text{mA}$, $I_{IL}=0.4\text{mA}$. Compute the fan-out limit from both sides and state the overall fan-out.",
             r"Sebuah gerbang memiliki $I_{OH}=200\,\mu A$, $I_{IH}=20\,\mu A$, $I_{OL}=4\text{mA}$, $I_{IL}=0{,}4\text{mA}$. Hitung batas fan-out dari kedua sisi dan sebutkan fan-out keseluruhan.",
             r"HIGH-side: $200/20=10$. LOW-side: $4/0.4=10$. Both sides agree, so \textbf{overall fan-out $=10$} (in general, take the minimum of the two).",
             r"Sisi HIGH: $200/20=10$. Sisi LOW: $4/0{,}4=10$. Kedua sisi sama, sehingga \textbf{fan-out keseluruhan $=10$} (secara umum, ambil nilai minimum dari keduanya)."),
            ("Analytical",
             r"A new avionics display controller has 208 pins and must survive continuous vibration in the aircraft's instrument panel. Recommend a package type and justify it against both the pin-count and vibration constraints, contrasting it with DIP.",
             r"Sebuah kontroler display avionik baru memiliki 208 pin dan harus bertahan terhadap getaran terus-menerus di panel instrumen pesawat. Rekomendasikan satu jenis kemasan dan justifikasi terhadap kendala jumlah pin maupun getaran, dibandingkan dengan DIP.",
             r"\textbf{QFP or BGA.} At 208 pins, DIP (two rows of through-hole pins on two edges only) would be impractically long and mechanically fragile. QFP places pins densely on all four sides; BGA achieves even higher density with solder balls under the whole footprint, and its shorter, more numerous solder connections plus lower profile generally give better vibration resistance than a long, leaded DIP or even a leaded QFP -- an important factor for a vibrating instrument-panel environment.",
             r"\textbf{QFP atau BGA.} Pada 208 pin, DIP (dua baris pin through-hole hanya di dua sisi) akan menjadi tidak praktis panjang dan rapuh secara mekanis. QFP menempatkan pin secara padat di keempat sisi; BGA mencapai kepadatan lebih tinggi lagi dengan bola solder di bawah seluruh footprint, dan sambungan solder yang lebih pendek dan lebih banyak serta profil lebih rendah umumnya memberi ketahanan getaran lebih baik dibanding DIP berkaki panjang atau bahkan QFP berkaki -- faktor penting untuk lingkungan panel instrumen yang bergetar."),
        ],
    },
    13: {
        "topic": "Datasheet Lab: Reading \\& Verifying Components",
        "subcpmk": "Mampu membaca datasheet IC secara sistematis dan memverifikasi kesesuaian komponen untuk aplikasi avionik.",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"List, in order, the first three sections you would check in a datasheet before even looking at electrical characteristics.",
             r"Sebutkan, secara berurutan, tiga bagian pertama yang harus diperiksa dalam datasheet sebelum melihat karakteristik elektrik sama sekali.",
             r"(1) Functional description / block diagram -- confirm the chip does the right logic function. (2) Pin configuration (pinout) -- confirm pin count and layout fit the board. (3) Absolute maximum ratings -- confirm the design's rails won't exceed the chip's hard survival limits.",
             r"(1) Deskripsi fungsional / diagram blok -- memastikan chip menjalankan fungsi logika yang benar. (2) Konfigurasi pin (pinout) -- memastikan jumlah dan tata letak pin cocok dengan papan. (3) Absolute maximum ratings -- memastikan rel desain tidak melampaui batas bertahan keras chip."),
            ("Application",
             r"A datasheet lists recommended operating supply as $4.75$--$5.25$V and absolute maximum supply as $-0.5$ to $7$V. Your board rail measures $5.4$V due to a regulator fault. Is the chip still within absolute maximum, and is this an acceptable operating condition?",
             r"Sebuah datasheet mencantumkan suplai operasi rekomendasi $4{,}75$--$5{,}25$V dan suplai maksimum absolut $-0{,}5$ hingga $7$V. Rel papan Anda terukur $5{,}4$V akibat kegagalan regulator. Apakah chip masih dalam batas maksimum absolut, dan apakah ini kondisi operasi yang dapat diterima?",
             r"Yes, $5.4$V is still below the $7$V absolute maximum, so the chip will not be immediately destroyed. \textbf{However, it is not acceptable} -- $5.4$V exceeds the recommended operating range ($4.75$--$5.25$V), so correct electrical behaviour (timing, noise margins, guaranteed output levels) is no longer guaranteed by the datasheet even though survival is. The regulator fault must be fixed.",
             r"Ya, $5{,}4$V masih di bawah maksimum absolut $7$V, sehingga chip tidak langsung rusak. \textbf{Namun, ini tidak dapat diterima} -- $5{,}4$V melampaui rentang operasi rekomendasi ($4{,}75$--$5{,}25$V), sehingga perilaku elektrik yang benar (timing, noise margin, level output yang dijamin) tidak lagi dijamin oleh datasheet meskipun chip tidak rusak. Kegagalan regulator harus diperbaiki."),
            ("Analytical",
             r"You are qualifying a 74-series gate IC for a new avionics design. The datasheet only specifies commercial temperature grade ($0$--$70^\circ$C) and lists only \"typical\" electrical values, not min/max. Explain why this part fails avionics qualification on two separate grounds, and what documents you would request from the manufacturer instead.",
             r"Anda sedang mengkualifikasi IC gerbang seri 74 untuk desain avionik baru. Datasheet hanya mencantumkan grade suhu komersial ($0$--$70^\circ$C) dan hanya nilai elektrik ``typical'', bukan min/max. Jelaskan mengapa komponen ini gagal kualifikasi avionik atas dua alasan terpisah, dan dokumen apa yang seharusnya Anda minta dari pabrikan.",
             r"\textbf{Ground 1 -- temperature:} commercial grade ($0$--$70^\circ$C) does not cover the wider extremes an avionics bay can see; an industrial or military/aerospace-qualified grade version is required. \textbf{Ground 2 -- guarantees:} \"typical\" values are not guaranteed across manufacturing variation, supply, and temperature -- a reliable design must be verified against the datasheet's \"min\"/\"max\" columns, which this datasheet lacks. \textbf{Request:} a full datasheet (or qualification/reliability report) from the manufacturer giving guaranteed min/max electrical characteristics at the extended/military temperature range, plus any aerospace qualification certificate (e.g.\ AEC-Q100 or equivalent) for the part.",
             r"\textbf{Alasan 1 -- suhu:} grade komersial ($0$--$70^\circ$C) tidak mencakup suhu ekstrem yang lebih lebar yang bisa dialami ruang avionik; diperlukan versi grade industrial atau militer/aerospace-qualified. \textbf{Alasan 2 -- jaminan:} nilai ``typical'' tidak dijamin di seluruh variasi manufaktur, suplai, dan suhu -- desain yang andal harus diverifikasi terhadap kolom ``min''/``max'' datasheet, yang tidak dimiliki datasheet ini. \textbf{Permintaan:} datasheet lengkap (atau laporan kualifikasi/keandalan) dari pabrikan yang mencantumkan karakteristik elektrik min/max yang dijamin pada rentang suhu extended/militer, ditambah sertifikat kualifikasi aerospace (mis.\ AEC-Q100 atau setara) untuk komponen tersebut."),
        ],
    },
}

if __name__ == "__main__":
    results = []
    for n, m in MEETINGS.items():
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Digital_Technic_Micro", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
