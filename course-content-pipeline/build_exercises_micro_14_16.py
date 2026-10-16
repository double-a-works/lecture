#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Digital_Technic_Micro meetings 14-16,
in lectures/meeting<N>/exercise/ (separate from exercises/ assignment PDFs),
following the same structure as build_exercises_micro_10_13.py."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Digital Technic: Microprocessor Systems"
COURSE_CODE = "AV0302DT"

MEETINGS = {
    14: {
        "topic": "LEDs \\& Seven-Segment Displays",
        "subcpmk": "Mampu menjelaskan prinsip kerja LED dan tampilan tujuh-segmen serta antarmukanya dengan sistem mikrokomputer.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"An LED has $V_{LED}=1.8$V and must be driven at $I_{LED}=12$mA from a 5V supply. Compute the required series current-limiting resistor.",
             r"Sebuah LED memiliki $V_{LED}=1{,}8$V dan harus digerakkan pada $I_{LED}=12$mA dari suplai 5V. Hitung resistor seri pembatas arus yang dibutuhkan.",
             r"$R=(V_{supply}-V_{LED})/I_{LED}=(5-1.8)/0.012=266.7\,\Omega$ (round up to the nearest standard value, e.g.\ $270\,\Omega$, to stay safely under the rated current).",
             r"$R=(V_{supply}-V_{LED})/I_{LED}=(5-1{,}8)/0{,}012=266{,}7\,\Omega$ (dibulatkan ke nilai standar terdekat, mis.\ $270\,\Omega$, agar tetap aman di bawah arus terukur)."),
            ("Application",
             r"A technician wires a common-cathode seven-segment display but drives it with a BCD decoder IC designed to sink current on each active segment output (i.e.\ intended for common-anode displays). Will the display show the correct digits? Explain.",
             r"Seorang teknisi mengkabel display tujuh-segmen common-cathode tetapi menggerakkannya dengan IC decoder BCD yang dirancang untuk menyerap arus (sink) pada tiap output segmen aktif (yaitu ditujukan untuk display common-anode). Apakah display akan menampilkan digit yang benar? Jelaskan.",
             r"No. A common-cathode display needs each active segment driven HIGH (sourcing current into the segment, whose cathode sits at GND), but a decoder built for common-anode displays sinks (pulls LOW) its active outputs. Connecting them directly causes every segment behaviour to invert -- segments that should be on stay off and vice versa. \textbf{Fix:} use a decoder/driver IC matched to common-cathode polarity, or add inverting buffers between decoder and display.",
             r"Tidak. Display common-cathode membutuhkan tiap segmen aktif digerakkan HIGH (mengalirkan arus ke segmen yang katodanya berada di GND), tetapi decoder yang dibangun untuk display common-anode menyerap (menarik LOW) output aktifnya. Menghubungkannya langsung membuat perilaku setiap segmen terbalik -- segmen yang seharusnya menyala justru mati, dan sebaliknya. \textbf{Perbaikan:} gunakan IC decoder/driver yang sesuai polaritas common-cathode, atau tambahkan buffer pembalik di antara decoder dan display."),
            ("Analytical",
             r"An avionics annunciator panel uses eight seven-segment digits, each individually wired (no multiplexing), each needing 8 segment lines plus a dedicated common line. Calculate the total I/O lines needed, then explain how multiplexing reduces this and what trade-off it introduces.",
             r"Sebuah panel annunciator avionik memakai delapan digit tujuh-segmen, masing-masing dikabel individual (tanpa multiplexing), masing-masing membutuhkan 8 jalur segmen ditambah satu jalur common khusus. Hitung total jalur I/O yang dibutuhkan, lalu jelaskan bagaimana multiplexing mengurangi ini dan trade-off apa yang muncul.",
             r"Without multiplexing: $8\text{ digits}\times(8\text{ segment lines}+1\text{ common line})=72$ lines. With multiplexing, all digits' segment lines are wired in parallel (8 shared segment lines) and each digit gets only its own common-enable line: $8\text{ segment lines}+8\text{ common lines}=16$ lines -- a large reduction. \textbf{Trade-off:} only one digit can be lit at any instant, so the controller must cycle through all eight digits fast enough (well above the eye's flicker-fusion rate) to make them all appear simultaneously lit; this adds software/timing complexity and reduces the average per-digit ON time (and thus perceived brightness) compared to driving every digit continuously.",
             r"Tanpa multiplexing: $8\text{ digit}\times(8\text{ jalur segmen}+1\text{ jalur common})=72$ jalur. Dengan multiplexing, jalur segmen semua digit dikabel paralel (8 jalur segmen bersama) dan tiap digit hanya mendapat satu jalur common-enable sendiri: $8\text{ jalur segmen}+8\text{ jalur common}=16$ jalur -- pengurangan besar. \textbf{Trade-off:} hanya satu digit yang bisa menyala pada satu saat, sehingga controller harus berputar melalui kedelapan digit cukup cepat (di atas laju flicker-fusion mata) agar semuanya tampak menyala serentak; ini menambah kompleksitas software/timing dan mengurangi rata-rata waktu ON per digit (sehingga kecerahan yang dirasakan berkurang) dibanding menggerakkan setiap digit terus-menerus."),
        ],
    },
    15: {
        "topic": "Dot-Matrix \\& LCD Displays",
        "subcpmk": "Mampu menjelaskan prinsip kerja display dot-matrix dan LCD serta membandingkan karakteristiknya.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"An $8\times8$ dot-matrix display needs how many row and column control lines, and how many total control lines (using row/column multiplexed wiring)?",
             r"Display dot-matrix $8\times8$ membutuhkan berapa jalur kendali baris dan kolom, dan berapa total jalur kendali (memakai pengkabelan multiplexed baris/kolom)?",
             r"8 row lines + 8 column lines = \textbf{16 total control lines} (versus $8\times8=64$ lines if every LED were wired individually).",
             r"8 jalur baris + 8 jalur kolom = \textbf{total 16 jalur kendali} (dibanding $8\times8=64$ jalur bila setiap LED dikabel individual)."),
            ("Application",
             r"A 16x2 character LCD built around the HD44780 controller displays garbage characters right after power-up, but works correctly a moment later without any code change. What is the most likely cause?",
             r"LCD karakter 16x2 berbasis controller HD44780 menampilkan karakter kacau tepat setelah power-up, tetapi bekerja dengan benar sesaat kemudian tanpa perubahan kode apa pun. Apa penyebab yang paling mungkin?",
             r"The software is likely sending the initialization/setup command sequence before the HD44780 has finished its internal power-on reset and stabilization delay -- the controller's datasheet specifies a minimum wait time after power-up before it can reliably accept commands. \textbf{Fix:} insert the datasheet-specified startup delay before issuing the first initialization command.",
             r"Software kemungkinan mengirim urutan perintah inisialisasi/setup sebelum HD44780 selesai melakukan power-on reset internal dan delay stabilisasinya -- datasheet controller menetapkan waktu tunggu minimum setelah power-up sebelum ia dapat menerima perintah secara andal. \textbf{Perbaikan:} sisipkan delay startup sesuai datasheet sebelum mengirim perintah inisialisasi pertama."),
            ("Analytical",
             r"A cockpit multi-function display must remain readable in direct sunlight and show detailed graphical maps. Compare an LED dot-matrix panel and a passive-matrix LCD for this role, and recommend which technology (including active-matrix TFT as a third option) best fits, justifying your choice.",
             r"Sebuah multi-function display kokpit harus tetap terbaca di bawah sinar matahari langsung dan menampilkan peta grafis rinci. Bandingkan panel dot-matrix LED dan LCD passive-matrix untuk peran ini, dan rekomendasikan teknologi mana (termasuk TFT active-matrix sebagai opsi ketiga) yang paling sesuai, sertai justifikasi.",
             r"LED dot-matrix: self-luminous so it can stay readable in direct sun, but at the resolution/power needed for detailed graphical maps it becomes power-hungry and coarse compared to LCD. Passive-matrix LCD: low power and can show fine detail, but its slower response and lower contrast make it prone to washing out in bright sunlight and looking sluggish for dynamic map updates. \textbf{Recommendation: active-matrix (TFT) LCD} -- each pixel's dedicated transistor gives much better contrast and response time than passive-matrix while retaining LCD's fine resolution for detailed graphics; paired with a high-brightness backlight it can be made sunlight-readable, which is why TFT is the standard choice for modern glass-cockpit multi-function displays.",
             r"Dot-matrix LED: self-luminous sehingga tetap terbaca di bawah sinar matahari langsung, tetapi pada resolusi/daya yang dibutuhkan untuk peta grafis rinci menjadi boros daya dan kasar dibanding LCD. LCD passive-matrix: daya rendah dan bisa menampilkan detail halus, tetapi respons lebih lambat dan kontras lebih rendah membuatnya rentan memudar di bawah sinar matahari terang dan terasa lamban untuk pembaruan peta dinamis. \textbf{Rekomendasi: LCD active-matrix (TFT)} -- transistor khusus tiap piksel memberi kontras dan waktu respons jauh lebih baik dibanding passive-matrix sambil mempertahankan resolusi halus LCD untuk grafis rinci; dipadukan dengan backlight kecerahan tinggi, ia bisa dibuat terbaca di bawah matahari, itulah sebabnya TFT menjadi pilihan standar untuk multi-function display glass-cockpit modern."),
        ],
    },
    16: {
        "topic": "Display Interfacing: Parallel, Serial \\& Drivers",
        "subcpmk": "Mampu menjelaskan antarmuka paralel dan serial untuk display serta merancang langkah software penggeraknya.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"State one advantage of a serial (e.g.\ I2C) display interface over a parallel interface, and one advantage of parallel over serial.",
             r"Sebutkan satu keunggulan antarmuka display serial (mis.\ I2C) dibanding paralel, dan satu keunggulan paralel dibanding serial.",
             r"Serial advantage: uses far fewer I/O pins (e.g.\ 2 for I2C vs.\ 8+ for parallel), valuable when pins are scarce. Parallel advantage: transfers a full data word in a single bus cycle, making it faster per transfer than sending the same word bit-by-bit.",
             r"Keunggulan serial: memakai jauh lebih sedikit pin I/O (mis.\ 2 untuk I2C vs 8+ untuk paralel), berharga saat pin terbatas. Keunggulan paralel: mentransfer satu word data penuh dalam satu siklus bus, lebih cepat per transfer dibanding mengirim word yang sama bit demi bit."),
            ("Application",
             r"A microcontroller drives an HD44780-based LCD in 4-bit mode with R/W tied to GND (write-only, no busy-flag polling). What must the software do instead to ensure each command has finished before the next one is sent?",
             r"Sebuah mikrokontroler menggerakkan LCD berbasis HD44780 dalam mode 4-bit dengan R/W diikat ke GND (write-only, tanpa polling busy-flag). Apa yang harus dilakukan software sebagai gantinya untuk memastikan tiap perintah selesai sebelum perintah berikutnya dikirim?",
             r"The software must insert a fixed software delay after each command/data write, sized to be at least as long as the controller's worst-case (datasheet-specified) command execution time -- since the busy flag cannot be read (R/W is grounded), timing must be guaranteed statically rather than checked dynamically.",
             r"Software harus menyisipkan delay tetap (fixed) setelah tiap penulisan perintah/data, berdurasi setidaknya sepanjang waktu eksekusi perintah terburuk (sesuai datasheet) controller -- karena busy flag tidak bisa dibaca (R/W diground), timing harus dijamin secara statis, bukan diperiksa secara dinamis."),
            ("Analytical",
             r"An avionics LRU must drive both a seven-segment digit bank and a character LCD, but the microcontroller has only 10 free I/O pins in total. Propose a pin-budget allocation across both displays using the interfacing options covered this meeting, and justify your choice of parallel vs.\ serial for each.",
             r"Sebuah LRU avionik harus menggerakkan bank digit tujuh-segmen dan LCD karakter, tetapi mikrokontroler hanya memiliki total 10 pin I/O bebas. Usulkan alokasi anggaran pin di antara kedua display memakai opsi antarmuka yang dibahas pertemuan ini, dan justifikasi pilihan paralel vs serial untuk masing-masing.",
             r"\textbf{LCD:} drive it over a serial-to-parallel I2C backpack (2 pins: SDA, SCL) instead of native 4-bit/8-bit parallel -- frees up most of the pin budget since character updates are infrequent and I2C's lower speed is not a bottleneck for human-readable text. \textbf{Seven-segment bank:} drive it via a BCD-to-seven-segment decoder/driver IC with multiplexing, needing only 4 BCD data lines plus digit-select lines (e.g.\ 4 digits = 4 select lines) -- 4+4=8 lines, but combined with the LCD's 2 lines that is already 10. \textbf{Allocation:} LCD = 2 pins (I2C), seven-segment = 4 BCD lines + 4 digit-select lines = 8 pins; total = 10 pins, exactly matching the budget. Parallel BCD is justified for the segment bank because the decoder IC needs a real-time 4-bit code per refresh cycle (multiplexing timing is tight), while the LCD's infrequent, non-time-critical updates make serial I2C's pin savings the better trade.",
             r"\textbf{LCD:} gerakkan lewat backpack I2C serial-ke-paralel (2 pin: SDA, SCL) alih-alih paralel native 4-bit/8-bit -- membebaskan sebagian besar anggaran pin karena pembaruan karakter jarang terjadi dan kecepatan I2C yang lebih rendah bukan bottleneck untuk teks yang dibaca manusia. \textbf{Bank tujuh-segmen:} gerakkan lewat IC decoder/driver BCD-to-seven-segment dengan multiplexing, hanya butuh 4 jalur data BCD ditambah jalur digit-select (mis.\ 4 digit = 4 jalur select) -- 4+4=8 jalur, digabung dengan 2 jalur LCD menjadi 10. \textbf{Alokasi:} LCD = 2 pin (I2C), tujuh-segmen = 4 jalur BCD + 4 jalur digit-select = 8 pin; total = 10 pin, persis sesuai anggaran. Paralel BCD dijustifikasi untuk bank segmen karena IC decoder butuh kode 4-bit real-time tiap siklus refresh (timing multiplexing ketat), sementara pembaruan LCD yang jarang dan tidak time-critical membuat penghematan pin I2C serial menjadi trade-off yang lebih baik."),
        ],
    },
}

if __name__ == "__main__":
    import sys
    meetings = [int(x) for x in sys.argv[1:]] or list(MEETINGS.keys())
    results = []
    for n in meetings:
        m = MEETINGS[n]
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Digital_Technic_Micro", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
