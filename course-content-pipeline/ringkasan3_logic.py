#!/usr/bin/env python3
"""ID ringkasan strings, one per TOPICAL slide, in document order, for
Digital_Technic_Logic meetings 10-13 (real content extracted from the
deployed lecture.tex via extract_slides.py / splice_bilingual.py)."""

RINGKASAN = {}

# Meeting 10 -- Flip-Flops: Terminology & Types (SR, D)
RINGKASAN[10] = [
 r"Semua rangkaian yang dipelajari sebelumnya (Pertemuan 1--8) bersifat kombinasional (output hanya bergantung pada input saat ini); sistem nyata seperti pencacah dan register butuh mengingat nilai sebelumnya, sehingga elemen memori (latch/flip-flop) menyimpan satu bit lewat feedback loop.",
 r"Latch bersifat level-sensitive (output bisa berubah kapan saja saat enable aktif), sedangkan flip-flop bersifat edge-triggered (output hanya berubah tepat saat transisi clock naik/turun); output diberi label $Q$ dan komplemennya $\overline{Q}$.",
 r"SR latch dibangun dari dua gerbang NOR/NAND yang saling silang (cross-coupled); S (Set) memaksa $Q=1$, R (Reset) memaksa $Q=0$, dan saat $S=R=0$ latch menahan nilai terakhirnya -- feedback inilah yang menjadi memori.",
 r"Tabel kebenaran SR flip-flop: $S{=}0,R{=}0$ hold; $S{=}0,R{=}1$ reset ($Q{=}0$); $S{=}1,R{=}0$ set ($Q{=}1$); $S{=}1,R{=}1$ terlarang karena memaksa $Q$ dan $\overline{Q}$ ke level logika yang sama.",
 r"Menambahkan input clock (CLK) menggerbangi sinyal S dan R sehingga hanya berlaku saat edge/level aktif ($S'=S\cdot CLK$, $R'=R\cdot CLK$); di luar periode clock aktif flip-flop menahan statusnya -- jembatan dari latch asinkron ke sistem sinkron.",
 r"Flip-flop D (Data/Delay) menghilangkan kondisi terlarang dengan menyalurkan satu input melalui inverter untuk membangkitkan S dan R secara internal; $Q_{next}=D$, menjadikannya elemen penyimpan standar untuk register dan pipeline.",
 r"Persamaan karakteristik merangkum perilaku next-state: flip-flop D adalah $Q_{next}=D$, flip-flop SR adalah $Q_{next}=S+\overline{R}\,Q$; diagram waktu menunjukkan $Q$ hanya berubah tepat pada edge clock, tidak di antaranya.",
 r"Kesalahan umum: menganggap enable latch sebagai clock edge-triggered, lupa memeriksa kondisi terlarang $S=R=1$, membaca $Q_{next}$ pada waktu yang salah (seharusnya setelah edge aktif), dan mencampur D dengan S/R.",
 r"Soal: lengkapi tabel kebenaran flip-flop SR untuk keempat kombinasi $(S,R)$ dan tandai baris yang tidak valid.",
 r"Solusi: $00\to Q$ (hold); $01\to0$ (reset); $10\to1$ (set); $11\to$ terlarang karena memaksa $Q$ dan $\overline{Q}$ sama-sama 0, melanggar syarat $Q\neq\overline{Q}$ begitu $S,R$ kembali ke 0.",
 r"Soal: diberikan pulsa CLK pada $t=1,3,5,7$ dengan $D=1,0,1,1$ (mulai $Q=0$), tentukan nilai $Q$ setelah tiap edge clock.",
 r"Solusi: $t{=}1$: $Q{=}1$; $t{=}3$: $Q{=}0$; $t{=}5$: $Q{=}1$; $t{=}7$: $Q{=}1$ (tidak berubah) -- $Q$ hanya diperbarui tepat pada tiap rising edge.",
 r"Soal: jelaskan menggunakan tabel kebenaran SR mengapa $S=1,R=1$ tidak boleh terjadi pada rangkaian yang bekerja dengan benar.",
 r"Solusi: saat $S=R=1$ kedua gerbang NOR menghasilkan 0 sehingga $Q=\overline{Q}=0$ bersamaan; jika S,R lalu turun ke 0 bersamaan, next state menjadi tidak dapat diprediksi (race condition) -- kombinasi ini karena itu dilarang.",
 r"Soal: flip-flop D sedang menyimpan $Q=1$ dan input D-nya dihubungkan ke $\overline{Q}$ (komplemen dirinya sendiri). Jelaskan apa yang terjadi pada tiap edge clock.",
 r"Solusi: karena $Q_{next}=D=\overline{Q}$, flip-flop akan toggle setiap edge clock ($1\to0\to1\to0\dots$) -- inilah cara membangun flip-flop T (toggle) dari flip-flop D, akan dibahas pertemuan berikutnya.",
]

# Meeting 11 -- Flip-Flops: JK, T & Applications
RINGKASAN[11] = [
 r"Flip-flop SR pertemuan lalu memiliki kelemahan: $S=R=1$ terlarang; flip-flop JK (dinamai dari Jack Kilby) mengatasi ini dengan mengumpankan balik $Q$ dan $\overline{Q}$ untuk menggerbangi input, sehingga saat kedua input aktif, flip-flop justru toggle -- menjadikan JK flip-flop paling serbaguna karena bisa meniru perilaku SR, D, maupun T.",
 r"Tabel kebenaran JK: $J{=}0,K{=}0$ hold; $J{=}0,K{=}1$ reset; $J{=}1,K{=}0$ set; $J{=}1,K{=}1$ toggle ($\overline{Q}$); persamaan karakteristiknya $Q_{next}=J\overline{Q}+\overline{K}\,Q$.",
 r"JK dengan satu latch bisa mengalami race jika $J=K=1$ dan level clock aktif cukup lama untuk toggle lebih dari sekali; konstruksi master-slave (dua latch berseri) atau desain edge-triggered modern menghindari race ini dengan menyampel input tepat pada edge clock.",
 r"Menghubungkan $J=K=T$ menyederhanakan tabel JK menjadi flip-flop T dengan satu input: $T{=}0$ hold, $T{=}1$ toggle; persamaan karakteristik $Q_{next}=T\oplus Q$ -- ideal untuk pembagi frekuensi dan pencacah (counter).",
 r"Tabel eksitasi menjawab pertanyaan kebalikan: untuk transisi $Q\to Q_{next}$ tertentu, input apa yang dibutuhkan? Nilai X berarti don't-care; tabel eksitasi menjadi titik awal untuk mendesain rangkaian sekuensial.",
 r"Setiap flip-flop T (atau JK yang di-toggle) membagi frekuensi clock-nya dengan 2: 1 tahap $\to f/2$, 2 tahap $\to f/4$, $n$ tahap $\to f/2^n$; rangkaian toggle flip-flop berseri inilah dasar pencacah biner ripple.",
 r"Register menggunakan flip-flop D (satu per bit) dengan clock bersama untuk menyimpan kata multi-bit secara serentak; register 8-bit = 8 flip-flop D yang semuanya diperbarui pada edge clock yang sama, menyimpan operand, alamat, dan data pipeline CPU.",
 r"Kesalahan umum: lupa baris toggle JK ($J=K=1$) dan mengiranya terlarang seperti SR, memakai JK level-sensitive tanpa mempertimbangkan race condition, serta tertukar antara tabel eksitasi (arah desain) dengan tabel kebenaran (arah analisis).",
 r"Soal: lengkapi tabel kebenaran flip-flop JK termasuk baris toggle, dan berikan persamaan karakteristiknya.",
 r"Solusi: $00\to Q$, $01\to0$, $10\to1$, $11\to\overline{Q}$; persamaan karakteristik $Q_{next}=J\overline{Q}+\overline{K}Q$.",
 r"Soal: tunjukkan bagaimana tiga flip-flop T (masing-masing diclock oleh $Q$ tahap sebelumnya) membagi clock input dengan 8.",
 r"Solusi: setiap tahap dengan $T=1$ toggle sekali per edge clock yang diterimanya, membagi dua frekuensi tiap tahap: tahap 1 $=f/2$, tahap 2 $=f/4$, tahap 3 $=f/8$; tiga tahap toggle berseri membagi dengan $2^3=8$.",
 r"Soal: menggunakan tabel eksitasi, tentukan $J,K$ yang dibutuhkan untuk membawa flip-flop dari $Q=1$ ke $Q_{next}=0$.",
 r"Solusi: dari baris $1\to0$ tabel eksitasi: $J=X$ (don't care), $K=1$; nilai $J$ apa pun berlaku selama $K=1$, karena $K=1$ memaksa reset/toggle-ke-0 dari $Q=1$.",
 r"Soal: jelaskan cara membangun perilaku flip-flop D menggunakan flip-flop JK (tentukan $J,K$ dalam bentuk $D$).",
 r"Solusi: agar $Q_{next}=D$ selalu, tetapkan $J=D$ dan $K=\overline{D}$: jika $D=1$, $J{=}1,K{=}0\Rightarrow Q_{next}=1$; jika $D=0$, $J{=}0,K{=}1\Rightarrow Q_{next}=0$ -- sehingga $J=D,K=\overline{D}$ membuat JK berperilaku persis seperti flip-flop D.",
]

# Meeting 12 -- Shift Registers & Counters
RINGKASAN[12] = [
 r"Kombinasional: output hanya bergantung input saat ini (Pertemuan 5--8); sekuensial: output bergantung input saat ini dan status tersimpan (flip-flop, Pertemuan 10--11) -- rangkaian sekuensial selalu memiliki elemen memori dan clock; pertemuan ini membangun dua blok sekuensial klasik: shift register dan counter.",
 r"Perilaku rangkaian sekuensial digambarkan lewat state diagram (lingkaran = status, panah berlabel input/output = transisi); mesin Moore: output hanya bergantung status saat ini; mesin Mealy: output bergantung status dan input saat ini; tabel status mendaftar next state dan output untuk tiap pasangan (status, input).",
 r"Shift register: flip-flop D dihubungkan berseri, $Q$ tiap tahap menjadi $D$ tahap berikutnya, berbagi satu clock; tiap edge clock menggeser seluruh bit satu posisi -- dipakai untuk konversi serial-ke-paralel, delay line, dan komunikasi serial.",
 r"Varian shift register: SISO (serial masuk-serial keluar), SIPO (serial masuk-paralel keluar, umum untuk menggerakkan display dari satu jalur data serial), PISO (paralel masuk-serial keluar, umum untuk membaca saklar paralel lewat satu jalur serial), dan PIPO (paralel masuk-paralel keluar).",
 r"Ripple (asynchronous) counter: flip-flop toggle berseri, $Q$ tiap tahap men-clock tahap berikutnya; counter $n$-tahap menghitung 0 hingga $2^n-1$ lalu berulang; disebut ripple karena perubahan merambat bertahap dengan delay, dan total delay propagasi (jumlah delay tiap flip-flop) membatasi kecepatan maksimum.",
 r"Synchronous counter: semua flip-flop berbagi clock yang sama, logika kombinasional menentukan input $J,K$ (atau $T$) tiap flip-flop agar semua bit diperbarui serentak -- menghilangkan delay ripple, lebih cepat untuk counter lebar meski butuh lebih banyak gerbang; desain pilihan pada mikrokomputer dan rangkaian timing avionik berkecepatan tinggi.",
 r"Up-counter naik tiap clock, down-counter turun tiap clock; modulo-N (mod-N) counter kembali ke 0 setelah mencapai $N-1$ meski $N\neq2^n$ (contoh: counter mod-10/dekade untuk digit BCD memakai logika reset saat hitungan mencapai 10).",
 r"Kesalahan umum: tertukar SIPO (serial masuk) dengan PISO (serial keluar) -- baca akronimnya huruf demi huruf; menganggap ripple counter 'gratis' padahal delay kumulatifnya adalah batas kecepatan nyata; lupa bahwa counter mod-N butuh logika reset/decode tambahan di luar toggle biasa.",
 r"Soal: sebutkan satu perbedaan antara logika kombinasional dan sekuensial, beserta satu contoh rangkaian masing-masing.",
 r"Solusi: kombinasional -- output hanya bergantung input saat ini (contoh: full adder); sekuensial -- output bergantung input saat ini dan status tersimpan (contoh: counter 4-bit).",
 r"Soal: gambarkan/deskripsikan shift register SIPO 3-bit yang menerima urutan bit serial $1,0,1$ (satu bit per clock, bit tertua lebih dulu).",
 r"Solusi: mulai $Q_2Q_1Q_0=000$; clock 1 (in=1): $100$; clock 2 (in=0): $010$; clock 3 (in=1): $101$; setelah 3 clock register menyimpan $101_2$, tersedia paralel pada $Q_2Q_1Q_0$.",
 r"Soal: berikan urutan hitungan counter ripple (biner) 3-bit untuk 5 pulsa clock, dimulai dari 000.",
 r"Solusi: $000\to001\to010\to011\to100\to101$ (setelah 5 pulsa); tiap tahap toggle saat tahap sebelumnya turun dari 1 ke 0, carry merambat ke atas.",
 r"Soal: counter mod-6 harus menghitung $0,1,2,3,4,5,0,1,\dots$ menggunakan 3 flip-flop. Logika tambahan apa yang dibutuhkan di luar counter biner 3-bit biasa?",
 r"Solusi: counter 3-bit biasa menghitung 0--7; untuk memaksa reset di 6, tambahkan decoder (gerbang AND) yang mendeteksi status $110_2$ (6) dan secara asinkron me-reset semua flip-flop ke $000$, sehingga urutan melewati 6 dan 7 lalu mulai lagi dari 0.",
]

# Meeting 13 -- Analog-to-Digital Conversion (ADC)
RINGKASAN[13] = [
 r"Sensor (airspeed, altitude, temperature, strain gauge) menghasilkan tegangan analog kontinu, sedangkan mikrokomputer hanya memproses nilai digital diskret; ADC (Analog-to-Digital Converter) menjembatani keduanya -- setiap instrumen penerbangan digital bergantung pada ADC di suatu titik dalam rantai sinyalnya.",
 r"Sampling mengukur nilai sesaat sinyal analog pada interval waktu tetap sebesar periode sampling $T_s=1/f_s$; kriteria Nyquist mensyaratkan $f_s>2f_{max}$; melanggar Nyquist menyebabkan aliasing -- konten frekuensi tinggi terlipat balik dan muncul sebagai sinyal frekuensi rendah palsu pada output digital.",
 r"Quantization memetakan tiap tegangan sampel ke level diskret terdekat dari $2^n$ level; karena nilai analog kontinu sedangkan level diskret, quantization selalu menimbulkan error kecil (quantization error, hingga $\pm\tfrac12$ LSB); makin banyak bit $n$ berarti makin banyak level dan error makin kecil, dengan konsekuensi waktu konversi dan kompleksitas rangkaian lebih besar.",
 r"ADC $n$-bit memiliki $2^n$ kode output; tegangan tiap langkah kode adalah Step (LSB) $=V_{ref}/2^n$; contoh: 8 bit = 256 level = 19,5 mV/langkah, 10 bit = 1024 level = 4,88 mV/langkah, 12 bit = 4096 level = 1,22 mV/langkah (untuk $V_{ref}=5$V).",
 r"Arsitektur ADC: Flash ADC memakai bank komparator membandingkan input ke $2^n-1$ level referensi sekaligus -- sangat cepat tapi butuh banyak komparator; SAR (Successive Approximation) melakukan pencarian biner satu bit per waktu memakai DAC pada feedback loop -- keseimbangan kecepatan/akurasi/biaya terbaik dan paling umum; dual-slope (integrating) mengintegralkan input lalu referensi dan mengukur waktunya -- lambat tapi sangat akurat dan tahan noise, dipakai pada instrumen presisi.",
 r"Proses konversi SAR: mulai dengan MSB ditebak 1, sisanya 0, lalu bandingkan output DAC dengan input; jika output DAC lebih besar dari input, bit tersebut dihapus, jika tidak tetap diset; lanjut ke bit berikutnya dari MSB ke LSB -- konversi SAR $n$-bit membutuhkan tepat $n$ langkah perbandingan.",
 r"Di avionik: air data computer mendigitalkan sensor tekanan pitot-static lewat ADC; sensor parameter mesin (EGT, tekanan oli, RPM) mengumpankan kanal ADC untuk tampilan EICAS; banyak kanal sensor analog sering di-multiplex secara bergantian ke satu ADC untuk menghemat biaya.",
 r"Kesalahan umum: lupa bahwa laju Nyquist adalah pertidaksamaan ketat ($f_s>2f_{max}$, bukan $\geq$; sistem nyata memakai margin ekstra), tertukar antara resolusi (jumlah bit/level) dengan akurasi (kedekatan ke nilai sebenarnya), serta salah satuan step size -- selalu bagi $V_{ref}$ dengan $2^n$, bukan $2^n-1$, sesuai konvensi di sini.",
 r"Soal: hitung step size ADC 10-bit dengan $V_{ref}=3,3$V.",
 r"Solusi: Step $=V_{ref}/2^n=3,3/1024\approx3,22$ mV per langkah kode.",
 r"Soal: tentukan laju sampling minimum untuk sinyal dengan komponen frekuensi tertinggi 4 kHz, dan jelaskan yang terjadi jika sampling lebih lambat.",
 r"Solusi: minimum $f_s>2\times4\text{ kHz}=8$ kHz (Nyquist); sampling lebih lambat dari 8 kHz menyebabkan aliasing -- konten frekuensi tinggi terlipat balik dan terbaca sebagai frekuensi rendah palsu pada sinyal digital.",
 r"Soal: ADC 8-bit dengan $V_{ref}=5$V membaca kode $102_{10}$. Berapa tegangan analog yang direpresentasikan?",
 r"Solusi: Step $=5/256\approx19,53$ mV; Tegangan $\approx102\times19,53\text{ mV}\approx1,99$ V.",
 r"Soal: ADC SAR mengonversi sampel 12-bit. Berapa langkah perbandingan yang dibutuhkan satu konversi, dan mengapa SAR sering lebih dipilih dibanding flash ADC untuk desain umum?",
 r"Solusi: konversi SAR 12-bit membutuhkan tepat 12 langkah perbandingan (satu bit terselesaikan per langkah); SAR hanya butuh 1 komparator dan 1 DAC berapa pun resolusinya, dibanding flash ADC yang butuh $2^{12}-1=4095$ komparator -- jauh lebih murah dan hemat daya untuk resolusi yang sama, dengan konsekuensi lebih lambat dibanding flash.",
]
