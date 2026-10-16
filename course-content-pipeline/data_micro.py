# Digital_Technic_Micro (AV0302DT) assignment data
MICRO = [
(1, 1, "Mikrokomputer Dasar: Arsitektur Umum", "Sub-CPMK 1",
 [(20, "Gambarkan diagram blok dasar mikrokomputer yang menunjukkan CPU, memori, unit I/O, dan bus "
       "penghubung antarblok."),
  (25, "Jelaskan fungsi umum masing-masing blok utama mikrokomputer (CPU, memori, unit I/O) dalam "
       "memproses data."),
  (25, "Jelaskan aliran data (data flow) dari sensor avionik masuk ke mikrokomputer, diproses, hingga "
       "hasilnya dikirim ke aktuator, dikaitkan dengan blok-blok arsitektur yang telah digambarkan."),
  (30, "Sebuah sistem avionik sederhana harus membaca dua sensor (tekanan dan suhu) serta mengendalikan "
       "satu aktuator. Rancang diagram blok arsitektur mikrokomputer yang sesuai untuk sistem tersebut, "
       "lengkap dengan jalur bus dan unit I/O yang diperlukan, serta jelaskan alasan setiap pilihan "
       "blok."),
 ]),
(2, 2, "CPU, ALU, dan Register", "Sub-CPMK 1",
 [(20, "Jelaskan fungsi utama CPU, ALU, dan register dalam sistem mikrokomputer."),
  (25, "Jelaskan perbedaan register general-purpose dan register khusus (mis. program counter, "
       "instruction register, accumulator)."),
  (25, "ALU menerima dua operand dari register $R1=00000110_2$ dan $R2=00000011_2$ untuk operasi "
       "penjumlahan. Jelaskan alur data dari register menuju ALU hingga hasil disimpan kembali, dan "
       "hitung hasil penjumlahannya."),
  (30, "Rancang diagram alur (data path) sederhana yang menunjukkan bagaimana CPU mengambil dua nilai dari "
       "register, mengirimkannya ke ALU untuk dijumlahkan, dan menyimpan hasilnya kembali ke sebuah "
       "register tujuan. Jelaskan peran unit kendali (control unit) dalam mengatur alur tersebut."),
 ]),
(3, 3, "Bus Sistem \\& Siklus Fetch--Execute", "Sub-CPMK 2",
 [(20, "Jelaskan fungsi bus alamat, bus data, dan bus kendali pada sistem mikrokomputer."),
  (25, "Jelaskan tahapan siklus fetch-execute (fetch instruksi, decode, execute) secara berurutan."),
  (25, "Sebuah bus alamat memiliki lebar 12-bit. Hitung jumlah maksimum lokasi memori yang dapat "
       "dialamati oleh CPU tersebut."),
  (30, "Sebuah instruksi \"tambahkan nilai dari alamat memori $200_{16}$ ke akumulator\" akan dieksekusi "
       "CPU. Jelaskan langkah demi langkah siklus fetch-execute untuk instruksi ini, termasuk sinyal apa "
       "yang aktif pada bus alamat, bus data, dan bus kendali di setiap tahap."),
 ]),
(4, 4, "Praktikum: Simulasi Arsitektur Mikrokomputer", "Sub-CPMK 2",
 [(20, "Telusuri (trace) siklus fetch-execute untuk satu instruksi sederhana \"muat nilai dari memori ke "
       "register A\" pada arsitektur mikrokomputer generik, tuliskan urutan langkahnya."),
  (25, "Menggunakan simulator/diagram arsitektur generik, jelaskan perubahan nilai program counter (PC) "
       "sebelum dan sesudah instruksi pada Soal 1 dieksekusi."),
  (25, "Telusuri siklus fetch-execute untuk instruksi percabangan (branch/jump) ke alamat $100_{16}$, "
       "jelaskan bagaimana nilai PC diperbarui secara berbeda dibanding instruksi sekuensial biasa."),
  (30, "Buat studi kasus telusuran (trace table) untuk program sederhana 3 instruksi berurutan (mis. LOAD, "
       "ADD, STORE) yang beroperasi pada dua nilai data di memori. Tunjukkan nilai PC, isi register, dan "
       "aktivitas bus pada setiap siklus fetch-execute dari instruksi pertama hingga selesai."),
 ]),
(5, 5, "Perangkat Memori: Klasifikasi (RAM/ROM)", "Sub-CPMK 3",
 [(20, "Jelaskan perbedaan mendasar antara memori volatil dan non-volatil, beri contoh masing-masing."),
  (25, "Klasifikasikan RAM dan ROM berdasarkan sifat volatilitas dan kemampuan tulis-baca (read/write) "
       "dalam sebuah tabel perbandingan."),
  (25, "Jelaskan mengapa program firmware kritis avionik (mis. boot loader) harus disimpan pada memori "
       "non-volatil, bukan RAM, dengan menghubungkan pada sifat volatilitas."),
  (30, "Sebuah sistem avionik memerlukan tiga jenis penyimpanan: (a) program boot permanen, (b) data "
       "konfigurasi yang jarang diubah tetapi harus tetap tersimpan saat daya mati, (c) data kerja "
       "sementara selama operasi. Tentukan jenis memori (RAM/ROM/turunannya) yang paling sesuai untuk "
       "masing-masing kebutuhan dan jelaskan alasannya."),
 ]),
(6, 6, "Jenis RAM dan ROM serta Karakteristiknya", "Sub-CPMK 3",
 [(20, "Jelaskan perbedaan RAM statis (SRAM) dan RAM dinamis (DRAM)."),
  (25, "Jelaskan perbedaan ROM, PROM, EPROM, EEPROM, dan Flash dalam hal kemampuan pemrograman ulang "
       "(reprogrammable) dan metode penghapusannya."),
  (25, "Jelaskan mengapa DRAM memerlukan proses refresh berkala sedangkan SRAM tidak, dan jelaskan "
       "dampaknya terhadap kompleksitas rangkaian pendukung masing-masing."),
  (30, "Sebuah perangkat avionik portabel membutuhkan memori yang dapat diprogram ulang di lapangan tanpa "
       "alat khusus (bukan di pabrik), namun tetap menyimpan data saat daya dimatikan. Tentukan jenis "
       "memori non-volatil yang paling sesuai (di antara PROM, EPROM, EEPROM, Flash) dan jelaskan "
       "alasannya berdasarkan karakteristik penghapusan dan penulisan ulangnya."),
 ]),
(7, 7, "Organisasi \\& Pengalamatan Memori (Memory Map)", "Sub-CPMK 4",
 [(20, "Sebuah memori memiliki kapasitas $4096$ word dengan lebar data 8-bit. Hitung jumlah bit alamat "
       "(address lines) minimum yang dibutuhkan untuk mengalamati seluruh memori tersebut."),
  (25, "Jelaskan konsep memory map dan bagaimana ruang alamat CPU dapat dibagi antara ROM, RAM, dan "
       "perangkat I/O."),
  (25, "Sebuah CPU memiliki bus alamat 16-bit. Jika ROM dialokasikan pada alamat $0000_{16}$ hingga "
       "$3FFF_{16}$, hitung kapasitas ROM tersebut dalam KB."),
  (30, "Rancang sebuah memory map untuk sistem mikrokomputer avionik dengan bus alamat 16-bit yang harus "
       "mengalokasikan: ROM boot $16\\,\\text{KB}$, RAM kerja $32\\,\\text{KB}$, dan register I/O sensor "
       "$1\\,\\text{KB}$, sisanya tidak digunakan. Tentukan rentang alamat heksadesimal untuk setiap "
       "blok tersebut dan tunjukkan perhitungannya."),
 ]),
(8, 8, "Review \\& Latihan: Mikrokomputer \\& Memori", "Sub-CPMK 1--4",
 [(20, "Jelaskan kembali fungsi CPU, ALU, register, dan bus dalam satu paragraf ringkas."),
  (25, "Sebuah bus alamat memiliki lebar 14-bit. Hitung kapasitas memori maksimum yang dapat dialamati "
       "dalam KB."),
  (25, "Jelaskan siklus fetch-execute untuk instruksi \"simpan nilai akumulator ke alamat memori "
       "$500_{16}$\", termasuk peran bus data dan bus kendali."),
  (30, "Soal gabungan pra-UTS: Sebuah sistem mikrokomputer memiliki ROM $8\\,\\text{KB}$ pada alamat awal "
       "$0000_{16}$ dan RAM $16\\,\\text{KB}$ setelahnya. (a) Tentukan rentang alamat ROM dan RAM, "
       "(b) jelaskan siklus fetch-execute untuk mengambil instruksi pertama dari ROM saat sistem baru "
       "dinyalakan (reset), (c) jelaskan mengapa program counter (PC) harus diinisialisasi ke alamat awal "
       "ROM saat reset."),
 ]),
(10, 9, "Rangkaian Terintegrasi (IC): Konsep \\& Klasifikasi", "Sub-CPMK 5",
 [(20, "Jelaskan pengertian rangkaian terintegrasi (IC) dan keuntungannya dibanding rangkaian diskret."),
  (25, "Sebutkan dan jelaskan singkat klasifikasi IC berdasarkan skala integrasi: SSI, MSI, LSI, dan "
       "VLSI."),
  (25, "Jelaskan perbedaan IC analog dan IC digital, beri masing-masing satu contoh aplikasinya pada "
       "sistem avionik."),
  (30, "Sebuah komponen avionik menggunakan IC mikrokontroler tunggal yang menggantikan ratusan komponen "
       "diskret pada generasi sebelumnya. Jelaskan skala integrasi yang paling sesuai untuk mikrokontroler "
       "tersebut (SSI/MSI/LSI/VLSI) dan jelaskan dampaknya terhadap keandalan, berat, dan konsumsi daya "
       "sistem avionik."),
 ]),
(11, 10, "Skala Integrasi, Keluarga Logika \\& Karakteristik Listrik IC", "Sub-CPMK 6",
 [(20, "Jelaskan perbedaan keluarga logika TTL dan CMOS dalam hal level tegangan operasi dan konsumsi "
       "daya."),
  (25, "Jelaskan mengapa IC CMOS umumnya lebih hemat daya dibanding TTL, dan mengapa hal ini penting untuk "
       "sistem avionik bertenaga baterai/terbatas."),
  (25, "Jelaskan pengaruh kemasan IC (package, mis. DIP vs SMD) terhadap kepadatan rangkaian dan disipasi "
       "panas suatu sistem digital."),
  (30, "Sebuah rangkaian digital avionik akan mencampur komponen keluarga TTL dan CMOS. Jelaskan potensi "
       "masalah kompatibilitas level tegangan logika (logic level) antara kedua keluarga tersebut, dan "
       "usulkan solusi rangkaian antarmuka (interface) yang umum digunakan untuk mengatasi masalah "
       "tersebut."),
 ]),
(12, 11, "Displays: LED, Seven-Segment \\& LCD/Dot-Matrix", "Sub-CPMK 7",
 [(20, "Jelaskan prinsip kerja dasar LED sebagai indikator dan seven-segment display sebagai penampil "
       "angka."),
  (25, "Buat tabel pola segmen (a--g) yang harus menyala untuk menampilkan angka $0$--$9$ pada seven-segment "
       "display common-cathode."),
  (25, "Jelaskan perbedaan prinsip kerja LCD dan LED/seven-segment, khususnya terkait sumber cahaya "
       "(emisif vs non-emisif) dan konsumsi dayanya."),
  (30, "Sebuah panel indikator kokpit menampilkan ketinggian pesawat dalam 4 digit angka. Bandingkan "
       "penggunaan 4 buah seven-segment display dengan 1 modul LCD dot-matrix untuk kebutuhan ini, "
       "ditinjau dari konsumsi daya, keterbacaan pada siang/malam hari, dan kompleksitas antarmuka "
       "mikrokomputer."),
 ]),
(13, 12, "Praktikum: Antarmuka Display dengan Mikrokomputer", "Sub-CPMK 7",
 [(20, "Jelaskan fungsi IC decoder BCD-to-seven-segment dalam menghubungkan mikrokomputer dengan display "
       "seven-segment."),
  (25, "Gambarkan diagram blok antarmuka sederhana antara register keluaran mikrokomputer, IC decoder, dan "
       "seven-segment display."),
  (25, "Jelaskan teknik multiplexing pada penggunaan beberapa seven-segment display sekaligus (mis. 4 "
       "digit) agar dapat dikendalikan dengan jumlah pin mikrokomputer yang terbatas."),
  (30, "Rancang skema antarmuka untuk menampilkan nilai desimal 2 digit ($00$--$99$) dari sebuah register "
       "mikrokomputer 8-bit BCD ke dua buah seven-segment display menggunakan teknik multiplexing. "
       "Jelaskan alur sinyal dari register hingga tampil di display, termasuk peran decoder dan sinyal "
       "select multiplexing."),
 ]),
(14, 13, "Multiplexer, De-multiplexer \\& Piranti Tristate", "Sub-CPMK 8",
 [(20, "Jelaskan fungsi multiplexer (MUX) dan de-multiplexer (DEMUX) dalam pengarahan sinyal digital."),
  (25, "Sebuah multiplexer 4-ke-1 memiliki input data $D_0,D_1,D_2,D_3$ dan dua saluran select $S_1S_0$. "
       "Buat tabel kebenaran yang menunjukkan input mana yang diteruskan ke output untuk setiap kombinasi "
       "select."),
  (25, "Jelaskan konsep piranti tristate (three-state) dan mengapa piranti ini diperlukan agar beberapa "
       "perangkat dapat berbagi (share) satu bus data yang sama tanpa konflik sinyal."),
  (30, "Rancang skema penggunaan MUX 8-ke-1 untuk membaca 8 sensor avionik secara bergantian oleh satu "
       "jalur ADC, serta jelaskan bagaimana piranti tristate digunakan pada bus data agar keluaran dari "
       "beberapa modul sensor lain tidak saling bertabrakan (bus contention) saat tidak sedang dipilih."),
 ]),
(15, 14, "Mikroprosesor: Arsitektur, Register \\& Siklus Instruksi", "Sub-CPMK 10",
 [(20, "Jelaskan blok penyusun utama mikroprosesor: register, ALU, dan unit kendali (control unit)."),
  (25, "Jelaskan fungsi register program counter (PC), instruction register (IR), dan accumulator (ACC) "
       "pada mikroprosesor."),
  (25, "Jelaskan tahapan siklus instruksi mikroprosesor: fetch, decode, execute, dan (bila ada) "
       "write-back, dengan menyebutkan register yang terlibat pada setiap tahap."),
  (30, "Sebuah mikroprosesor menjalankan instruksi \"ACC $\\leftarrow$ ACC + M[$300_{16}$]\". Jelaskan "
       "secara rinci siklus instruksi lengkap (fetch-decode-execute) untuk instruksi tersebut, termasuk "
       "peran PC, IR, ALU, dan accumulator pada setiap tahap, serta bagaimana nilai PC berubah setelah "
       "instruksi selesai."),
 ]),
(16, 15, "Mikroprosesor: Mode Pengalamatan \\& Aplikasi Avionik", "Sub-CPMK 11",
 [(20, "Jelaskan perbedaan mode pengalamatan immediate dan direct pada instruksi mikroprosesor."),
  (25, "Jelaskan perbedaan mode pengalamatan indirect dan indexed, beri contoh instruksi sederhana untuk "
       "masing-masing mode."),
  (25, "Sebuah instruksi \"LOAD A, \\#25\" menggunakan mode pengalamatan immediate, sedangkan \"LOAD A, "
       "$300_{16}$\" menggunakan mode direct. Jelaskan perbedaan hasil eksekusi kedua instruksi tersebut."),
  (30, "Sebuah LRU (Line Replaceable Unit) avionik memproses larik (array) data sensor menggunakan mode "
       "pengalamatan indexed, di mana alamat dasar (base address) $200_{16}$ ditambah nilai register "
       "index yang bertambah pada setiap iterasi. Jelaskan bagaimana mode pengalamatan indexed ini "
       "memudahkan pemrosesan larik data dibanding jika hanya menggunakan mode direct, serta jelaskan "
       "alamat efektif yang diakses pada 3 iterasi pertama jika register index dimulai dari $0$ dan "
       "bertambah $1$ setiap iterasi."),
 ]),
(17, 16, "Review \\& Latihan Terpadu (Pra-UAS)", "Sub-CPMK 5--11",
 [(20, "Jelaskan perbedaan IC keluarga TTL dan CMOS, serta perbedaan LED dan LCD sebagai perangkat "
       "tampilan."),
  (25, "Jelaskan fungsi multiplexer dalam mengarahkan beberapa sinyal sensor ke satu ADC, dan jelaskan "
       "peran piranti tristate saat beberapa modul berbagi bus data yang sama."),
  (25, "Jelaskan siklus instruksi mikroprosesor (fetch-decode-execute) untuk sebuah instruksi yang "
       "menggunakan mode pengalamatan direct."),
  (30, "Soal terpadu lintas topik: Sebuah sistem avionik membaca 4 sensor melalui MUX 4-ke-1 menuju satu "
       "ADC, hasilnya diproses oleh mikroprosesor menggunakan mode pengalamatan indexed untuk menyimpan "
       "hasil ke larik memori, lalu hasil akhirnya ditampilkan pada seven-segment display melalui decoder "
       "BCD. Jelaskan alur data lengkap sistem ini dari sensor hingga display, serta jelaskan peran "
       "piranti tristate jika bus data yang sama juga digunakan oleh modul I/O lain."),
 ]),
]
