#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Digital_Technic_Logic meeting 17 and
Digital_Technic_Micro meeting 17 (Final Review), in lectures/meeting17/exercise/,
following the same structure as build_exercises_micro_14_16.py."""
from build_exercises import build_exercise_tex, compile_exercise

LOGIC = dict(
    course_name="Digital Technic: Digital Logic Fundamentals",
    course_code="AV0301DT",
    topic="Final Review: Flip-Flops, ADC/DAC \\& Microcomputer Architecture",
    subcpmk="Mampu mengintegrasikan flip-flop, ADC/DAC, dan arsitektur mikrokomputer dalam satu rantai kendali digital.",
    cpmk="CPMK-4, CPMK-5 (CPL-1)",
    problems=[
        ("Foundational",
         r"A T flip-flop starts at $Q=0$. It is clocked 5 times with $T=1$ held constant throughout. What is $Q$ after the 5th clock edge?",
         r"Sebuah flip-flop T mulai dari $Q=0$. Ia di-clock 5 kali dengan $T=1$ dipertahankan konstan sepanjang waktu. Berapa $Q$ setelah edge clock ke-5?",
         r"$T=1$ toggles $Q$ every edge: $0\to1\to0\to1\to0\to1$. After 5 edges, $Q=1$ (odd number of toggles from 0).",
         r"$T=1$ men-toggle $Q$ setiap edge: $0\to1\to0\to1\to0\to1$. Setelah 5 edge, $Q=1$ (jumlah toggle ganjil dari 0)."),
        ("Application",
         r"A 10-bit ADC with $V_{ref}=3.3$V samples a sensor voltage of $2.1$V. Compute the resulting digital code (nearest integer) and the quantization step size.",
         r"ADC 10-bit dengan $V_{ref}=3{,}3$V mencuplik tegangan sensor $2{,}1$V. Hitung kode digital hasil (bilangan bulat terdekat) dan besar step size kuantisasi.",
         r"Step size $=3.3/2^{10}=3.3/1024\approx3.22$mV. Code $\approx 2.1/0.00322\approx652_{10}$, i.e.\ $1010001100_2$.",
         r"Step size $=3{,}3/2^{10}=3{,}3/1024\approx3{,}22$mV. Kode $\approx2{,}1/0{,}00322\approx652_{10}$, yaitu $1010001100_2$."),
        ("Analytical",
         r"An avionics control loop reads a sensor with a 12-bit ADC, processes the value with a microcomputer using an 8-bit-wide data bus, then outputs through a 12-bit DAC. Identify where a bottleneck or data-width mismatch could occur in this chain, and propose a fix.",
         r"Sebuah loop kendali avionik membaca sensor dengan ADC 12-bit, memproses nilainya dengan mikrokomputer memakai bus data lebar 8-bit, lalu keluar lewat DAC 12-bit. Identifikasi di mana bottleneck atau ketidakcocokan lebar data bisa terjadi pada rantai ini, dan usulkan perbaikannya.",
         r"The mismatch is between the 12-bit ADC output and the 8-bit-wide data bus: a single bus transfer cannot move the full 12-bit sample in one cycle, forcing the microcomputer to read it in two transfers (e.g.\ split into high/low bytes) and reassemble it in software before processing -- adding latency and firmware complexity. \textbf{Fix:} either use a microcomputer/bus with a native word width $\geq$12 bits, or explicitly budget two-cycle reads in the control loop's timing so the added latency does not violate the loop's real-time deadline.",
         r"Ketidakcocokan terjadi antara output ADC 12-bit dan bus data lebar 8-bit: satu transfer bus tidak bisa memindahkan sampel 12-bit penuh dalam satu siklus, memaksa mikrokomputer membacanya dalam dua transfer (mis.\ dipecah byte tinggi/rendah) dan menyusunnya kembali di software sebelum diproses -- menambah latensi dan kompleksitas firmware. \textbf{Perbaikan:} gunakan mikrokomputer/bus dengan lebar word asli $\geq$12 bit, atau secara eksplisit anggarkan pembacaan dua-siklus dalam pewaktuan loop kendali agar tambahan latensi tidak melanggar tenggat waktu real-time loop tersebut."),
    ])

MICRO = dict(
    course_name="Digital Technic: Microprocessor Systems",
    course_code="AV0302DT",
    topic="Final Review: IC Selection, Display Formulas \\& Interfacing",
    subcpmk="Mampu mengintegrasikan pemilihan IC, karakteristik elektris, dan antarmuka display dalam satu jejak desain lengkap.",
    cpmk="CPMK-3 (CPL-1), CPMK-4 (CPL-2)",
    problems=[
        ("Foundational",
         r"State the two logic families compared throughout this course, and one electrical characteristic that must be checked whenever they are mixed in one design.",
         r"Sebutkan dua keluarga logika yang dibandingkan sepanjang mata kuliah ini, dan satu karakteristik elektris yang harus diperiksa saat keduanya dicampur dalam satu desain.",
         r"TTL and CMOS. When mixed, the output voltage levels ($V_{OH}/V_{OL}$) of the driving chip must be checked against the input voltage thresholds ($V_{IH}/V_{IL}$) of the receiving chip to avoid a logic-level mismatch.",
         r"TTL dan CMOS. Saat dicampur, level tegangan output ($V_{OH}/V_{OL}$) chip penggerak harus diperiksa terhadap ambang tegangan input ($V_{IH}/V_{IL}$) chip penerima agar tidak terjadi ketidakcocokan level logika."),
        ("Application",
         r"A common-anode seven-segment display needs a series resistor computed for $V_{supply}=5$V, $V_{LED}=2.0$V, $I_{LED}=15$mA. Compute $R$, and state whether the decoder driving it should sink or source current on active segments.",
         r"Display seven-segment common-anode membutuhkan resistor seri dihitung untuk $V_{supply}=5$V, $V_{LED}=2{,}0$V, $I_{LED}=15$mA. Hitung $R$, dan sebutkan apakah decoder yang menggerakkannya harus menyerap (sink) atau mengalirkan (source) arus pada segmen aktif.",
         r"$R=(5-2.0)/0.015\approx200\,\Omega$. Common-anode drives segments LOW to light them, so the decoder must sink current on active segment outputs.",
         r"$R=(5-2{,}0)/0{,}015\approx200\,\Omega$. Common-anode menyalakan segmen dengan LOW, sehingga decoder harus menyerap (sink) arus pada output segmen aktif."),
        ("Analytical",
         r"A design multiplexes 6 seven-segment digits and must avoid visible flicker (minimum 60 Hz per digit). Compute the minimum full-cycle refresh frequency and the maximum time each digit may be lit per cycle. Then explain one interfacing-level pitfall that could still cause flicker even if this rate is met.",
         r"Sebuah desain memultipleks 6 digit seven-segment dan harus menghindari kedipan terlihat (minimum 60 Hz per digit). Hitung frekuensi refresh siklus penuh minimum dan waktu maksimum tiap digit boleh menyala per siklus. Lalu jelaskan satu jebakan tingkat antarmuka yang tetap bisa menyebabkan kedipan meski laju ini terpenuhi.",
         r"Full-cycle frequency $\geq 6\times60=360$Hz, so each digit is lit for at most $1/360\text{s}\approx2.78$ms per cycle. \textbf{Pitfall:} even at a compliant refresh rate, a logic-level mismatch between the digit-select driver and the microcomputer (e.g.\ TTL driver output below the CMOS controller's $V_{IH,min}$) can cause some digit-select transitions to be missed or delayed, producing irregular, position-dependent flicker unrelated to the refresh-rate calculation itself.",
         r"Frekuensi siklus penuh $\geq6\times60=360$Hz, sehingga tiap digit menyala paling lama $1/360\text{s}\approx2{,}78$ms per siklus. \textbf{Jebakan:} meski laju refresh sudah memenuhi syarat, ketidakcocokan level logika antara driver digit-select dan mikrokomputer (mis.\ output driver TTL di bawah $V_{IH,min}$ pengendali CMOS) bisa menyebabkan sebagian transisi digit-select terlewat atau tertunda, menghasilkan kedipan tidak beraturan yang bergantung posisi, tidak terkait perhitungan refresh rate itu sendiri."),
    ])

if __name__ == "__main__":
    results = []
    for course, m in [("Digital_Technic_Logic", LOGIC), ("Digital_Technic_Micro", MICRO)]:
        tex = build_exercise_tex(m["course_name"], m["course_code"], 17, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise(course, 17, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] {course} meeting 17 exercise: {res['size_kb']} KB errors={res['errors']}")
