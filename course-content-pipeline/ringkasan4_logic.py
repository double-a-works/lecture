#!/usr/bin/env python3
"""ID ringkasan strings, one per TOPICAL slide, in document order, for
Digital_Technic_Logic meetings 14-16 (real content extracted from the
deployed lecture.tex via extract_slides.py / splice_bilingual.py)."""

RINGKASAN = {}

# Meeting 14 -- Digital-to-Analog Conversion (DAC)
RINGKASAN[14] = [
 r"DAC (Digital-to-Analog Converter) mengubah kode digital kembali menjadi tegangan atau arus analog yang proporsional -- kebalikan dari ADC yang dipelajari pertemuan lalu; dipakai untuk menggerakkan aktuator, servo permukaan kendali, output audio, dan tampilan analog -- setiap sistem kendali digital loop tertutup (autopilot, kendali mesin) butuh DAC untuk mengubah perintah digital hasil komputasi menjadi sinyal fisik analog.",
 r"DAC resistor binary-weighted: tiap bit input menyalakan arus lewat resistor berskala kelipatan dua ($R, R/2, R/4,\dots,R/2^{n-1}$), lalu op-amp menjumlahkan arus tersebut; bit paling signifikan memakai resistor terkecil (kontribusi arus terbesar); kelemahannya butuh rentang nilai resistor yang presisi dan lebar -- makin besar $n$ makin sulit difabrikasi akurat (DAC 8-bit butuh rasio resistor hingga 128:1).",
 r"DAC R-2R ladder hanya memakai dua nilai resistor ($R$ dan $2R$) yang disusun dalam jaringan tangga; kontribusi tiap bit diturunkan dengan cara yang sama tanpa memandang posisinya, sehingga fabrikasi cukup akurat pada satu rasio resistor saja -- jauh lebih mudah dan murah dibuat presisi dibanding binary-weighted, menjadikannya arsitektur dominan pada DAC terintegrasi praktis.",
 r"Untuk DAC $n$-bit dengan kode digital input $D$ (bilangan bulat $0$ hingga $2^n-1$): $V_{out}=V_{ref}\cdot D/2^n$; contoh: DAC 8-bit, $V_{ref}=5$V, kode $10000000_2=128_{10}$ menghasilkan $V_{out}=5\times128/256=2{,}5$V.",
 r"Step size (1 LSB) $=V_{ref}/2^n$ -- bentuk rumus yang sama seperti resolusi ADC; output full-scale (semua bit = 1) sedikit lebih kecil dari $V_{ref}$: $V_{FS}=V_{ref}\cdot(2^n-1)/2^n$, tidak pernah mencapai $V_{ref}$ persis; resolusi lebih halus (bit lebih banyak) menghasilkan gelombang rekonstruksi yang lebih mulus.",
 r"Settling time: waktu yang dibutuhkan output untuk stabil dalam batas error tertentu setelah kode input berubah -- membatasi laju update maksimum DAC; glitch: lonjakan output salah sesaat saat transisi kode (mis.\ $0111\to1000$) karena saklar-saklar tidak berubah tepat bersamaan; filter rekonstruksi (low-pass) setelah DAC menghaluskan tangga dan glitch menjadi gelombang analog kontinu.",
 r"Di avionik: komputer autopilot mengeluarkan sinyal DAC untuk menggerakkan aktuator servo permukaan kendali; indikator analog kokpit (bila masih dipakai) digerakkan dari sumber digital lewat DAC; nada peringatan/annunciator audio sering disintesis secara digital lalu dikonversi lewat DAC.",
 r"Kesalahan umum: lupa bahwa output full-scale tidak pernah mencapai $V_{ref}$ persis (berhenti di $(2^n{-}1)/2^n$ dari nilainya); tertukar antara step size DAC dengan error kuantisasi ADC -- rumus mirip tapi arah konversi berlawanan; mengira output DAC langsung bersih tanpa jeda, padahal settling time dan glitch nyata terjadi, terutama saat banyak bit berubah bersamaan di batas kode.",
 r"Soal: hitung output DAC 6-bit ($V_{ref}=3{,}3$V) untuk kode $101000_2$.",
 r"Solusi: $101000_2=40_{10}$. $V_{out}=3{,}3\times40/64\approx2{,}06$V.",
 r"Soal: sebutkan satu keunggulan DAC R-2R ladder dibanding DAC resistor binary-weighted.",
 r"Solusi: R-2R hanya butuh dua nilai resistor ($R$, $2R$) untuk resolusi berapa pun, sehingga jauh lebih mudah difabrikasi dengan presisi tinggi dibanding binary-weighted yang butuh rentang nilai resistor berskala lebar dan presisi.",
 r"Soal: berapa banyak level output DAC 10-bit, dan berapa output full-scale-nya untuk $V_{ref}=5$V?",
 r"Solusi: Level $=2^{10}=1024$. Full-scale $V_{FS}=5\times(1024-1)/1024\approx4{,}995$V (tidak pernah mencapai 5V persis).",
 r"Soal: DAC 4-bit ($V_{ref}=8$V) harus menghasilkan output sekitar $5{,}0$V. Kode digital apa yang harus diberikan, dan berapa output sebenarnya?",
 r"Solusi: Step size $=8/16=0{,}5$V. Kode target $D\approx5{,}0/0{,}5=10$, yaitu $1010_2$. Output sebenarnya $=8\times10/16=5{,}0$V persis -- kode $1010_2$ adalah pilihan yang tepat.",
]

# Meeting 15 -- Microcomputer Terminology
RINGKASAN[15] = [
 r"Pertemuan 10--14 membahas flip-flop dan ADC/DAC -- blok bangunan tingkat rendah; sebelum merakitnya menjadi mikrokomputer (Pertemuan 16), dibutuhkan kosakata bersama untuk satuan data, penyimpanan, dan jalur komunikasi yang terlibat -- terminologi ini juga muncul di setiap manual perawatan avionik dan datasheet yang akan dibaca secara profesional.",
 r"Satuan data: Bit -- satu digit biner (0 atau 1), satuan informasi terkecil; Nibble -- 4 bit (satu digit heksadesimal); Byte -- 8 bit, satuan standar untuk pengalamatan memori; Word -- lebar data alami CPU, misalnya 8, 16, 32, atau 64 bit, tergantung keluarga prosesor.",
 r"CPU (Central Processing Unit) -- mengambil (fetch), menerjemahkan (decode), dan menjalankan (execute) instruksi; Memory -- menyimpan instruksi program maupun data yang diolahnya (RAM = penyimpanan kerja, ROM = firmware permanen); Register -- lokasi penyimpanan sangat cepat yang dibangun langsung di dalam CPU, dipakai untuk operand dan hasil antara.",
 r"Bus adalah sekumpulan kabel bersama yang membawa sinyal antara CPU, memori, dan I/O; Data bus -- membawa nilai yang sedang dibaca/ditulis, bersifat dua arah; Address bus -- membawa lokasi memori/I-O yang ingin diakses CPU, bersifat satu arah (CPU yang menggerakkannya); Control bus -- membawa sinyal pewaktuan dan perintah (baca/tulis, clock, permintaan interrupt).",
 r"Peripheral -- perangkat apa pun yang terhubung ke CPU di luar memori inti (sensor, display, aktuator, port komunikasi); Port -- titik antarmuka yang bisa dialamati tempat peripheral terhubung ke bus; Interrupt -- sinyal yang menghentikan sementara eksekusi normal CPU untuk melayani kejadian mendesak (mis.\ ambang batas sensor terlampaui), lalu melanjutkan dari titik terakhir.",
 r"Address -- label numerik yang mengidentifikasi satu lokasi memori atau port I/O; Address space -- seluruh rentang alamat yang bisa dihasilkan sistem, $2^m$ lokasi untuk address bus $m$-bit; Memory-mapped I/O -- peripheral berbagi ruang alamat yang sama dengan memori, diakses dengan instruksi baca/tulis biasa.",
 r"Instruction -- satu operasi CPU yang dikodekan sebagai pola biner (opcode + operand); Program -- urutan instruksi yang tersusun; Firmware -- perangkat lunak yang disimpan di memori non-volatile (ROM/Flash), terikat erat dengan perangkat keras tertentu -- hal yang lazim pada LRU avionik.",
 r"Kesalahan umum: tertukar antara \"byte\" (selalu 8 bit) dengan \"word\" (bervariasi tergantung arsitektur CPU); mencampur address bus (memilih \emph{di mana}) dengan data bus (membawa \emph{apa}); menganggap \"software\" dan \"firmware\" sama, padahal firmware menyiratkan penyimpanan non-volatile yang spesifik ke perangkat keras.",
 r"Soal: berapa byte dalam satu word 32-bit?",
 r"Solusi: $32\text{ bit}/8\text{ bit per byte}=4$ byte.",
 r"Soal: sebutkan tiga jenis bus dan fungsinya.",
 r"Solusi: Data bus -- membawa nilai yang sedang ditransfer. Address bus -- memilih lokasi memori/I-O mana yang diakses. Control bus -- membawa sinyal pewaktuan dan perintah (baca/tulis, clock, interrupt).",
 r"Soal: jelaskan perbedaan antara register dan RAM.",
 r"Solusi: Register adalah sejumlah kecil lokasi penyimpanan sangat cepat yang dibangun di dalam chip CPU itu sendiri, menyimpan operand/hasil selama eksekusi. RAM adalah memori kerja eksternal (atau on-chip tapi terpisah), berkapasitas lebih besar namun lebih lambat diakses dibanding register, menyimpan data program yang lebih luas.",
 r"Soal: sebuah sistem memiliki address bus 16-bit. Berapa total ruang alamatnya, dan berapa byte memori yang bisa dialamati langsung?",
 r"Solusi: Ruang alamat $=2^{16}=65.536$ lokasi. Jika tiap alamat memilih satu byte, sistem bisa mengalamati langsung $65.536$ byte $=64$ KB.",
]

# Meeting 16 -- Microcomputer Architecture
RINGKASAN[16] = [
 r"Pertemuan 10--15 memberikan bagian-bagiannya: flip-flop (memori), ADC/DAC (antarmuka analog), dan terminologi (bit/byte/word/bus); pertemuan ini merakit semuanya menjadi arsitektur mikrokomputer klasik -- model yang mendasari hampir setiap komputer digital, dari telepon genggam hingga komputer penerbangan.",
 r"Model Von Neumann: mikrokomputer memiliki CPU, memori, dan I/O yang terhubung lewat system bus bersama, dengan instruksi dan data berbagi ruang memori yang \emph{sama}; CPU -- control unit + ALU + register; Memory -- menyimpan program (instruksi) sekaligus datanya; I/O -- sensor, display, aktuator, yaitu antarmuka ke dunia luar.",
 r"Von Neumann: satu memori, satu bus untuk instruksi maupun data -- lebih sederhana dan murah, tapi fetch instruksi dan akses data berebut bus yang sama; Harvard: memori/bus terpisah untuk instruksi dan data -- memungkinkan fetch dan akses data bersamaan, umum pada DSP dan mikrokontroler yang butuh pewaktuan yang dapat diprediksi (mis.\ loop kendali penerbangan).",
 r"Siklus fetch-execute: (1) Fetch -- Program Counter (PC) menyalurkan alamat instruksi ke address bus; memori mengembalikan instruksi lewat data bus ke Instruction Register (IR); PC bertambah. (2) Decode -- control unit menerjemahkan opcode di IR, mengenali operasi dan operandnya. (3) Execute -- ALU/register/memori menjalankan operasi; hasil ditulis kembali dan status flag diperbarui; siklus ini berulang terus-menerus selama program berjalan.",
 r"Setiap fase siklus (fetch, decode, execute) memakan satu atau lebih periode clock, tergantung desain CPU; CPU sederhana menjalankan fase secara berurutan ketat; CPU canggih melakukan pipeline pada fase-fase tersebut sehingga beberapa instruksi berada di fase berbeda secara bersamaan, meningkatkan throughput; frekuensi clock $\times$ siklus-per-instruksi menentukan kecepatan eksekusi.",
 r"Microprocessor -- chip CPU saja; Microcontroller -- CPU + memori + I/O terintegrasi dalam satu chip, umum pada node sensor tertanam; Microcomputer -- sistem lengkap yang dibangun di sekitar CPU dengan papan memori/I-O eksternal, seperti model Von Neumann di atas.",
 r"Di avionik: FCC (Flight Control Computer) membaca data sensor, menghitung hukum kendali, menggerakkan aktuator; FMC (Flight Management Computer) melakukan komputasi navigasi dan performa; FADEC (Full Authority Digital Engine Control) melakukan kendali mesin digital loop tertutup, mencuplik sensor dan memerintah output bahan bakar/aktuator tiap siklus fetch-execute; ketiganya mengikuti model CPU--memori--I-O--bus yang sama dari pertemuan ini.",
 r"Kesalahan umum: tertukar antara fase \emph{fetch} (mengambil instruksi) dengan fase \emph{execute} (menjalankannya) -- keduanya memakai bus untuk tujuan berbeda; menganggap arsitektur Harvard selalu \"lebih baik\", padahal ia butuh perangkat keras lebih banyak (memori/bus terpisah) demi keuntungan pewaktuan; lupa bahwa PC bertambah saat fetch, bahkan sebelum instruksi di-decode.",
 r"Soal: sebutkan tiga langkah siklus fetch-execute dan apa yang terjadi pada PC di tiap langkah.",
 r"Solusi: Fetch -- alamat dari PC dibaca dari memori ke IR; PC bertambah. Decode -- control unit menerjemahkan isi IR; PC tidak berubah. Execute -- ALU/register/memori menjalankan operasi; PC tidak berubah kecuali instruksinya adalah jump/branch.",
 r"Soal: sebutkan sub-unit CPU dan perannya masing-masing.",
 r"Solusi: Control unit -- mengambil/menerjemahkan instruksi dan menghasilkan sinyal pengurutan. ALU -- melakukan operasi aritmatika dan logika. Register -- penyimpanan cepat on-chip untuk operand, hasil, dan nilai kendali (PC, IR, dsb.).",
 r"Soal: berikan dua contoh mikrokomputer di avionik dan satu sensor/aktuator yang berinteraksi dengan masing-masing.",
 r"Solusi: FADEC -- membaca sensor RPM/suhu mesin, memerintah aktuator pengukur bahan bakar. FCC -- membaca giroskop sikap/rate, memerintah aktuator servo permukaan kendali.",
 r"Soal: jelaskan mengapa arsitektur Harvard mungkin dipilih dibanding Von Neumann untuk mikrokontroler kendali penerbangan real-time.",
 r"Solusi: Bus instruksi dan data yang terpisah pada Harvard memungkinkan CPU mengambil instruksi berikutnya sambil bersamaan mengakses memori data, menghindari perebutan bus; ini memberi pewaktuan siklus yang lebih dapat diprediksi dan lebih cepat -- kritis untuk loop kendali real-time keras di mana lewat tenggat waktu bisa mendestabilkan pesawat.",
]
