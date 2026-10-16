# Digital_Technic_Logic (AV0301DT) assignment data
LOGIC = [
(1, 1, "Sistem Bilangan: Konversi Desimal--Biner", "Sub-CPMK 1",
 [(20, "Konversikan bilangan desimal $89_{10}$ ke biner dan bilangan biner $101101_2$ ke desimal."),
  (25, "Sebuah register avionik 8-bit menyimpan nilai $01011010_2$. Tentukan nilai desimalnya dan jelaskan "
       "makna posisi setiap bit (bobot tempat)."),
  (25, "Konversikan $173_{10}$ ke biner menggunakan metode pembagian berulang (successive division), "
       "tunjukkan setiap langkah sisa pembagiannya."),
  (30, "Sebuah sensor memberikan pembacaan dalam rentang $0$--$255$ (8-bit unsigned). Jika pembacaan saat "
       "ini adalah $01110011_2$, (a) tentukan nilai desimalnya, (b) tentukan nilai biner yang mewakili "
       "$75\\%$ dari skala penuh sensor tersebut."),
 ]),
(2, 2, "Konversi Oktal dan Heksadesimal", "Sub-CPMK 2",
 [(20, "Konversikan $250_{10}$ ke oktal dan ke heksadesimal."),
  (25, "Konversikan bilangan heksadesimal $2F_{16}$ langsung ke biner dan ke oktal (tunjukkan langkah "
       "melalui representasi biner)."),
  (25, "Sebuah alamat memori dinyatakan sebagai $3A7_{16}$. Tentukan nilai desimal dan biner (12-bit) dari "
       "alamat tersebut."),
  (30, "Sebuah word data 16-bit adalah $1010110011110000_2$. (a) Kelompokkan menjadi 4-bit lalu konversikan "
       "ke heksadesimal, (b) kelompokkan menjadi 3-bit dari kanan lalu konversikan ke oktal, (c) jelaskan "
       "mengapa heksadesimal lebih umum digunakan untuk data 16/32-bit dibanding oktal."),
 ]),
(3, 3, "Bilangan Bertanda (Signed Numbers)", "Sub-CPMK 2",
 [(20, "Nyatakan $-45_{10}$ dalam format sign-magnitude 8-bit dan dalam komplemen dua (two's complement) 8-bit."),
  (25, "Diberikan bilangan komplemen dua 8-bit $11010110_2$, tentukan nilai desimal bertandanya."),
  (25, "Jelaskan kelemahan format sign-magnitude dibanding komplemen dua untuk operasi aritmatika digital, "
       "beri contoh kasus $+0$ dan $-0$."),
  (30, "Sebuah sensor suhu menghasilkan pembacaan bertanda 8-bit dalam komplemen dua. Jika register bernilai "
       "$11110001_2$, (a) tentukan suhu terukur dalam desimal, (b) jika suhu tersebut naik $10$ derajat, "
       "tentukan representasi biner register yang baru."),
 ]),
(4, 4, "Perhitungan Digital (Aritmatika Biner)", "Sub-CPMK 3",
 [(20, "Jumlahkan $01011_2 + 00111_2$ dan tunjukkan proses carry pada setiap kolom."),
  (25, "Kurangkan $01001_2 - 00110_2$ menggunakan metode komplemen dua (bentuk komplemen dari pengurang, "
       "lalu jumlahkan)."),
  (25, "Dua register 8-bit menyimpan $01110010_2$ dan $00101101_2$ (keduanya unsigned). Jumlahkan keduanya "
       "dan tentukan apakah terjadi overflow pada register 8-bit tersebut."),
  (30, "Dua bilangan bertanda 8-bit dalam komplemen dua, $01111000_2$ dan $01100100_2$, dijumlahkan. "
       "(a) Hitung hasil penjumlahannya, (b) tentukan apakah terjadi kondisi overflow pada bilangan "
       "bertanda tersebut, dan jelaskan bagaimana overflow terdeteksi dari bit carry."),
 ]),
(5, 5, "Gerbang Logika \\& Aljabar Boolean", "Sub-CPMK 4",
 [(20, "Buat tabel kebenaran untuk gerbang AND, OR, dan XOR dengan dua input $A$ dan $B$."),
  (25, "Tuliskan ekspresi Boolean dan tabel kebenaran untuk fungsi $F = \\overline{A}\\,B + A\\,\\overline{B}$, "
       "lalu identifikasi gerbang logika dasar yang setara dengan fungsi ini."),
  (25, "Sederhanakan ekspresi Boolean $F = A\\,B + A\\,\\overline{B}$ menggunakan hukum aljabar Boolean, "
       "tunjukkan setiap langkah penyederhanaan dan hukum yang digunakan."),
  (30, "Sebuah sistem peringatan pesawat menyala ($F=1$) jika roda pendaratan belum turun ($A=1$) DAN "
       "(ketinggian rendah ($B=1$) ATAU kecepatan rendah ($C=1$)). (a) Tuliskan ekspresi Boolean $F$, "
       "(b) buat tabel kebenarannya, (c) gambarkan rangkaian gerbang logika yang mengimplementasikannya."),
 ]),
(6, 6, "Rangkaian Logika Kombinasional", "Sub-CPMK 4",
 [(20, "Buat peta Karnaugh (K-map) untuk fungsi 3-variabel $F(A,B,C) = \\sum m(1,3,5,7)$."),
  (25, "Sederhanakan fungsi Boolean $F = A\\overline{B}C + AB\\overline{C} + ABC + A\\overline{B}\\,\\overline{C}$ "
       "menggunakan peta Karnaugh, tunjukkan pengelompokan (grouping) yang digunakan."),
  (25, "Rancang rangkaian logika kombinasional minimum untuk fungsi 4-variabel "
       "$F(A,B,C,D)=\\sum m(0,2,5,7,8,10,13,15)$ menggunakan K-map 4-variabel."),
  (30, "Sebuah sistem interlock pintu kargo pesawat harus mengunci ($F=1$) jika: pintu tertutup ($A$) DAN "
       "(tekanan kabin normal ($B$) ATAU mode darat ($C$)) DAN BUKAN kondisi darurat ($\\overline{D}$). "
       "(a) Tuliskan ekspresi Boolean-nya, (b) sederhanakan menggunakan K-map jika berlaku, (c) gambarkan "
       "rangkaian gerbang hasil penyederhanaan."),
 ]),
(7, 7, "Review \\& Latihan: Sistem Bilangan \\& Logika Kombinasional", "Sub-CPMK 1--4",
 [(20, "Konversikan $2D_{16}$ ke biner dan ke desimal."),
  (25, "Nyatakan $-27_{10}$ dalam komplemen dua 8-bit, lalu jumlahkan hasilnya dengan $+15_{10}$ (dalam "
       "komplemen dua 8-bit juga) dan verifikasi hasil akhirnya dalam desimal."),
  (25, "Sederhanakan ekspresi Boolean $F = \\overline{A}\\,\\overline{B}\\,C + \\overline{A}\\,B\\,C + A\\,B\\,C$ "
       "menggunakan aljabar Boolean atau K-map."),
  (30, "Soal gabungan: Sebuah register 8-bit unsigned berisi hasil konversi dari $3F_{16}$. (a) Tentukan "
       "nilai biner dan desimalnya, (b) rancang rangkaian logika sederhana yang menghasilkan output $1$ "
       "jika nilai register tersebut lebih besar dari $50_{10}$ hanya dengan memeriksa 2 bit "
       "paling signifikan (jelaskan penalarannya)."),
 ]),
(8, 8, "Review \\& Latihan Terpadu (Pra-UTS)", "Sub-CPMK 1--4",
 [(20, "Konversikan $150_{10}$ ke biner, oktal, dan heksadesimal."),
  (25, "Kurangkan $01010101_2 - 00011011_2$ menggunakan metode komplemen dua."),
  (25, "Sederhanakan fungsi Boolean $F(A,B,C)=\\sum m(0,1,2,3,6)$ menggunakan peta Karnaugh."),
  (30, "Soal persiapan UTS: Sebuah word 8-bit komplemen dua bernilai $10011100_2$. (a) Tentukan nilai "
       "desimal bertandanya, (b) konversikan nilai magnitudonya ke heksadesimal, (c) rancang gerbang "
       "logika yang mendeteksi bit tanda (sign bit) bernilai negatif pada register tersebut."),
 ]),
(10, 9, "Flip-Flop: Terminologi \\& Jenis (SR, D)", "Sub-CPMK 5",
 [(20, "Jelaskan perbedaan latch dan flip-flop, serta jelaskan fungsi sinyal clock pada flip-flop."),
  (25, "Buat tabel kebenaran (tabel karakteristik) untuk flip-flop SR, termasuk kondisi terlarang "
       "(forbidden state) dan jelaskan mengapa kondisi tersebut dihindari."),
  (25, "Gambarkan diagram pewaktuan (timing diagram) untuk flip-flop D dengan input $D$ dan sinyal clock "
       "yang diberikan, tunjukkan kapan output $Q$ berubah."),
  (30, "Sebuah sistem penyimpan status \"landing gear locked\" menggunakan flip-flop D. Jelaskan mengapa "
       "flip-flop D lebih sesuai dibanding latch SR untuk aplikasi ini, dan gambarkan rangkaian sederhana "
       "flip-flop D yang dibangun dari flip-flop SR dan gerbang logika tambahan."),
 ]),
(11, 10, "Flip-Flop: Operasi (JK, T) \\& Aplikasi", "Sub-CPMK 5",
 [(20, "Buat tabel karakteristik untuk flip-flop JK dan jelaskan bagaimana flip-flop JK mengatasi kondisi "
       "terlarang pada flip-flop SR."),
  (25, "Jelaskan cara kerja flip-flop T (toggle) dan buat tabel karakteristiknya."),
  (25, "Rangkaian flip-flop JK dengan $J=K=1$ menerima 4 pulsa clock berurutan, dengan kondisi awal $Q=0$. "
       "Gambarkan diagram pewaktuan output $Q$ untuk keempat pulsa clock tersebut."),
  (30, "Rancang rangkaian pencacah (counter) 2-bit sederhana menggunakan 2 flip-flop JK yang dikonfigurasi "
       "sebagai flip-flop T (toggle mode). Gambarkan diagram rangkaian dan buat tabel status pencacahannya "
       "dari $00$ hingga $11$ lalu kembali ke $00$."),
 ]),
(12, 11, "Rangkaian Logika Sekuensial", "Sub-CPMK 5",
 [(20, "Jelaskan perbedaan mendasar antara rangkaian logika kombinasional dan rangkaian logika sekuensial."),
  (25, "Jelaskan fungsi register geser (shift register) dan sebutkan satu aplikasinya pada sistem digital "
       "avionik."),
  (25, "Sebuah shift register 4-bit menyimpan $0110_2$. Gambarkan isi register setelah 2 kali pergeseran "
       "ke kanan (shift right) dengan input serial $1$ pada setiap pergeseran."),
  (30, "Rancang diagram blok pencacah biner (binary counter) 3-bit menggunakan flip-flop JK yang tersambung "
       "secara berurutan (ripple counter). Jelaskan urutan status yang dihasilkan dari $000$ hingga $111$ "
       "dan jelaskan keterbatasan ripple counter terkait waktu tunda (propagation delay)."),
 ]),
(13, 12, "Konversi Data: ADC", "Sub-CPMK 6",
 [(20, "Jelaskan tahapan dasar proses konversi analog ke digital (sampling, quantization, encoding)."),
  (25, "Sebuah ADC 8-bit memiliki tegangan referensi $5\\,\\text{V}$. Hitung resolusi tegangan (langkah "
       "kuantisasi terkecil) yang dapat dideteksi oleh ADC tersebut."),
  (25, "Jelaskan konsep frekuensi Nyquist dan mengapa frekuensi sampling harus lebih besar dari dua kali "
       "frekuensi sinyal analog tertinggi yang akan dikonversi."),
  (30, "Sebuah sensor ketinggian pesawat menghasilkan sinyal analog $0$--$10\\,\\text{V}$ yang mewakili "
       "ketinggian $0$--$40000\\,\\text{ft}$. Jika digunakan ADC 10-bit, (a) hitung resolusi tegangan, "
       "(b) hitung resolusi ketinggian (ft) yang setara, (c) jika ADC membaca kode digital $512_{10}$, "
       "tentukan perkiraan ketinggian yang terbaca."),
 ]),
(14, 13, "Konversi Data: DAC", "Sub-CPMK 6",
 [(20, "Jelaskan prinsip kerja dasar DAC (digital ke analog) dan sebutkan satu metode implementasinya "
       "(mis. R-2R ladder atau binary weighted resistor)."),
  (25, "Sebuah DAC 8-bit dengan tegangan referensi $5\\,\\text{V}$ menerima input digital $10000000_2$. "
       "Hitung tegangan analog keluaran yang dihasilkan."),
  (25, "Jelaskan mengapa DAC menghasilkan keluaran berbentuk tangga (staircase) dan bagaimana filter "
       "low-pass digunakan untuk menghaluskan sinyal keluaran tersebut."),
  (30, "Sebuah sistem kendali autopilot mengonversi perintah digital 8-bit menjadi sinyal tegangan analog "
       "untuk aktuator, dengan referensi $10\\,\\text{V}$. (a) Hitung resolusi tegangan DAC tersebut, "
       "(b) jika aktuator memerlukan tegangan $7.5\\,\\text{V}$, tentukan kode digital input terdekat yang "
       "harus dikirim, (c) hitung kesalahan (error) tegangan akibat pembulatan kode digital tersebut."),
 ]),
(15, 14, "Terminologi Terkait Komputer", "Sub-CPMK 7",
 [(20, "Jelaskan pengertian bit, byte, dan word, serta hubungan ukuran (dalam bit) di antara ketiganya."),
  (25, "Jelaskan fungsi bus alamat (address bus), bus data (data bus), dan bus kendali (control bus) pada "
       "sistem komputer."),
  (25, "Jelaskan perbedaan CPU, ALU, dan memori (memory) dalam arsitektur komputer sederhana, serta "
       "hubungan kerja di antara ketiganya."),
  (30, "Sebuah sistem komputer avionik memiliki bus alamat 16-bit. (a) Hitung jumlah maksimum lokasi memori "
       "yang dapat dialamati, (b) jika setiap word data adalah 8-bit (1 byte), hitung total kapasitas "
       "memori maksimum dalam KB, (c) jelaskan mengapa lebar bus alamat membatasi kapasitas memori "
       "sistem."),
 ]),
(16, 15, "Pengantar Arsitektur Mikrokomputer", "Sub-CPMK 7",
 [(20, "Gambarkan diagram blok dasar arsitektur mikrokomputer yang menunjukkan CPU, memori, unit I/O, dan "
       "bus penghubung."),
  (25, "Jelaskan siklus fetch-execute secara singkat: bagaimana instruksi diambil dari memori dan "
       "dieksekusi oleh CPU."),
  (25, "Jelaskan perbedaan memori RAM dan ROM dalam konteks arsitektur mikrokomputer, dan jelaskan mengapa "
       "program boot avionik biasanya disimpan di ROM/Flash, bukan RAM."),
  (30, "Sebuah sistem mikrokomputer avionik sederhana harus membaca data sensor, memprosesnya, dan mengirim "
       "perintah ke aktuator. Gambarkan diagram blok arsitektur mikrokomputer yang sesuai untuk tugas "
       "tersebut (termasuk unit I/O sensor dan aktuator) dan jelaskan alur data pada setiap tahap siklus "
       "fetch-execute yang relevan."),
 ]),
(17, 16, "Review \\& Latihan Terpadu (Pra-UAS)", "Sub-CPMK 5--7",
 [(20, "Jelaskan perbedaan flip-flop D dan flip-flop T, serta satu aplikasi umum masing-masing."),
  (25, "Sebuah ADC 8-bit dengan referensi $5\\,\\text{V}$ membaca sinyal sensor tekanan kabin. Hitung "
       "resolusi tegangannya, lalu jelaskan bagaimana hasil digital tersebut dapat dikirim melalui bus "
       "data ke CPU untuk diproses."),
  (25, "Rancang pencacah (counter) 3-bit menggunakan flip-flop JK yang menghitung mundur (down-counter) "
       "dari $111$ ke $000$, tunjukkan tabel status pencacahannya."),
  (30, "Soal terpadu lintas topik: Sebuah sistem avionik membaca sensor analog melalui ADC 10-bit, "
       "menyimpan hasilnya sementara pada register (flip-flop D), lalu meneruskannya ke CPU melalui bus "
       "data 10-bit sebelum akhirnya dikonversi kembali menjadi sinyal analog melalui DAC untuk indikator "
       "kokpit. Jelaskan alur data lengkap sistem ini dan peran masing-masing komponen (ADC, "
       "register/flip-flop, bus, DAC) dalam siklus tersebut."),
 ]),
]
