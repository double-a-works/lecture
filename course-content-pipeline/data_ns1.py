# NS1 (AV0102BM) assignment data: (meeting_no, assignment_no, topic, subcpmk, tasks[(pts,text)])
NS1 = [
(1, 1, "Matematika: Aritmatika \\& Penggunaan Kalkulator", "Sub-CPMK 1",
 [(20, "Hitung tanpa kalkulator, tunjukkan langkah: (a) $\\frac{3}{4} + \\frac{2}{5}$, "
       "(b) $18 : 24$ dinyatakan sebagai persentase, (c) $150$ dikurangi $12\\%$ dari $150$."),
  (25, "Sebuah resistor memiliki toleransi $\\pm5\\%$ dari nilai nominal $220\\,\\Omega$. Tentukan rentang "
       "nilai resistansi minimum dan maksimum yang masih dianggap sesuai spesifikasi."),
  (25, "Gunakan kalkulator saintifik untuk menghitung $\\sqrt{2\\times10^{5}} \\div (3.2\\times10^{-2})$. "
       "Tuliskan hasil dengan 3 angka penting dan jelaskan urutan tombol yang digunakan."),
  (30, "Sebuah pesawat membawa bahan bakar sebanyak $2400$ liter. Jika $35\\%$ digunakan pada fase lepas landas "
       "dan sisanya dibagi rata untuk 3 fase penerbangan berikutnya, hitung volume bahan bakar (liter) yang "
       "tersedia untuk masing-masing fase tersebut."),
 ]),
(2, 2, "Matematika: Aljabar", "Sub-CPMK 1",
 [(20, "Sederhanakan ekspresi aljabar berikut: (a) $3x + 5 - (x - 2)$, (b) $\\dfrac{2x^2 - 8}{x-2}$."),
  (25, "Selesaikan persamaan linear $4(x-3) = 2x + 6$ dan tunjukkan setiap langkah manipulasi persamaannya."),
  (25, "Selesaikan persamaan kuadrat $x^2 - 5x + 6 = 0$ menggunakan pemfaktoran, kemudian verifikasi hasilnya "
       "menggunakan rumus $abc$."),
  (30, "Tegangan total pada suatu rangkaian dinyatakan sebagai $V = IR + I^2r$, dengan $r=2\\,\\Omega$ adalah "
       "resistansi dalam. Jika $V=24\\,\\text{V}$ dan $R=10\\,\\Omega$, susun persamaan kuadrat dalam $I$ dan "
       "tentukan nilai $I$ yang bermakna secara fisis."),
 ]),
(3, 3, "Matematika: Geometri", "Sub-CPMK 2",
 [(20, "Hitung luas permukaan dan volume sebuah tangki bahan bakar berbentuk silinder dengan jari-jari "
       "$0.6\\,\\text{m}$ dan tinggi $2\\,\\text{m}$."),
  (25, "Sebuah panel sayap berbentuk trapesium memiliki sisi sejajar $1.2\\,\\text{m}$ dan $0.8\\,\\text{m}$ "
       "dengan tinggi $2.5\\,\\text{m}$. Hitung luas panel tersebut."),
  (25, "Sebuah komponen berbentuk kerucut terpancung (frustum) memiliki jari-jari alas $0.3\\,\\text{m}$, "
       "jari-jari atas $0.15\\,\\text{m}$, dan tinggi $0.4\\,\\text{m}$. Hitung volumenya."),
  (30, "Sebuah hanggar berbentuk gabungan balok dan setengah silinder (atap lengkung) memiliki panjang "
       "$20\\,\\text{m}$, lebar $10\\,\\text{m}$, tinggi dinding $4\\,\\text{m}$, dan jari-jari atap "
       "$5\\,\\text{m}$. Hitung total volume ruang di dalam hanggar."),
 ]),
(4, 4, "Matematika: Trigonometri", "Sub-CPMK 2",
 [(20, "Diketahui segitiga siku-siku dengan sudut $37^\\circ$ dan sisi miring $10\\,\\text{m}$. Hitung "
       "panjang sisi depan dan sisi samping sudut tersebut."),
  (25, "Sebuah pesawat menanjak dengan sudut elevasi $8^\\circ$ terhadap horizontal. Jika jarak tempuh "
       "mendatar adalah $5000\\,\\text{m}$, hitung ketinggian yang telah dicapai pesawat."),
  (25, "Buktikan identitas trigonometri $\\dfrac{1-\\cos^2\\theta}{\\sin\\theta} = \\sin\\theta$ dan jelaskan "
       "setiap langkah penyederhanaannya."),
  (30, "Dua stasiun radar A dan B berjarak $12\\,\\text{km}$. Dari A, sebuah pesawat teramati pada sudut elevasi "
       "$30^\\circ$, dan dari B pada sudut elevasi $45^\\circ$ (kedua stasiun dan pesawat segaris vertikal). "
       "Tentukan ketinggian pesawat menggunakan aturan segitiga yang sesuai."),
 ]),
(5, 5, "Matematika: Logaritma", "Sub-CPMK 3",
 [(20, "Hitung nilai (a) $\\log_{10} 1000$, (b) $\\ln e^{3}$, (c) $\\log_2 32$."),
  (25, "Sederhanakan $\\log_{10} 50 + \\log_{10} 2$ menjadi satu logaritma tunggal, lalu hitung nilainya."),
  (25, "Rasio daya sinyal keluaran terhadap masukan suatu penguat (amplifier) avionik adalah $P_{out}/P_{in}=250$. "
       "Hitung penguatan dalam desibel menggunakan $dB = 10\\log_{10}(P_{out}/P_{in})$."),
  (30, "Sinyal suatu instrumen meluruh menurut $A(t) = A_0 e^{-kt}$. Jika amplitudo berkurang menjadi "
       "setengahnya ($A_0/2$) setelah $t=4$ detik, tentukan nilai konstanta peluruhan $k$ menggunakan "
       "logaritma natural."),
 ]),
(6, 6, "Matematika: Diferensial (Circuit)", "Sub-CPMK 4",
 [(20, "Tentukan turunan pertama dari $f(t) = 3t^2 + 5t - 7$ dan $g(t) = \\sin(2t)$."),
  (25, "Muatan pada suatu kapasitor dinyatakan $q(t) = 4t^3 - 2t$ (coulomb). Tentukan ekspresi arus "
       "$i(t) = dq/dt$ dan hitung nilainya pada $t=2$ detik."),
  (25, "Tegangan pada suatu induktor adalah $v(t) = L\\,di/dt$. Jika arus $i(t) = 5\\sin(100t)$ ampere dan "
       "$L=0.2\\,\\text{H}$, tentukan ekspresi $v(t)$."),
  (30, "Daya sesaat pada suatu rangkaian dinyatakan $P(t) = 100t - 5t^2$ (watt) untuk $0\\le t\\le 20$ detik. "
       "Gunakan turunan untuk menentukan waktu $t$ saat daya maksimum tercapai, dan hitung nilai daya "
       "maksimum tersebut."),
 ]),
(7, 7, "Matematika: Integral (Circuit)", "Sub-CPMK 4",
 [(20, "Tentukan integral tak tentu dari $f(t) = 6t^2 - 4t + 1$."),
  (25, "Arus pada suatu kapasitor adalah $i(t) = 3t^2$ (ampere). Tentukan muatan total $q$ yang terkumpul "
       "dari $t=0$ hingga $t=4$ detik menggunakan $q=\\int i\\,dt$."),
  (25, "Tegangan pada suatu rangkaian RC dinyatakan $v(t)=10e^{-0.5t}$. Hitung luas area di bawah kurva "
       "$v(t)$ (energi relatif) dari $t=0$ hingga $t=2$ detik."),
  (30, "Daya rata-rata suatu sinyal periodik dengan periode $T=2\\pi/\\omega$ dihitung dari "
       "$P_{avg} = \\frac{1}{T}\\int_0^T p(t)\\,dt$, dengan $p(t) = 50\\sin^2(\\omega t)$. Tunjukkan langkah "
       "integrasi untuk membuktikan $P_{avg} = 25$ watt (gunakan identitas $\\sin^2\\theta = \\frac{1-\\cos2\\theta}{2}$)."),
 ]),
(8, 8, "Review \\& Latihan: Matematika Terapan", "Sub-CPMK 1--4",
 [(20, "Sederhanakan $\\dfrac{x^2-9}{x+3}$ kemudian evaluasi pada $x=5$."),
  (25, "Sebuah kabel penyangga membentuk sudut $60^\\circ$ terhadap tanah dan panjangnya $8\\,\\text{m}$. "
       "Hitung ketinggian titik pengikat kabel di menara menggunakan trigonometri."),
  (25, "Suatu sinyal memiliki penguatan daya $P_{out}/P_{in} = 400$. Hitung penguatan dalam dB, lalu, jika "
       "$i(t)=2t^2$ ampere adalah arus pengisian kapasitor, tentukan $q(t)=\\int i\\,dt$ dari $t=0$ ke $t=3$."),
  (30, "Soal gabungan: Sebuah tangki silinder berjari-jari $0.5\\,\\text{m}$ dan tinggi $3\\,\\text{m}$ diisi "
       "dengan laju $dV/dt = 0.2\\,\\text{m}^3/\\text{menit}$. (a) Hitung volume total tangki, (b) tentukan "
       "waktu yang diperlukan untuk mengisi penuh tangki, (c) nyatakan waktu tersebut sebagai persentase "
       "dari 1 jam kerja."),
 ]),
(10, 9, "Kimia: Elemen Kimia", "Sub-CPMK 5",
 [(20, "Jelaskan perbedaan utama sifat unsur logam, non-logam, dan semikonduktor pada tabel periodik."),
  (25, "Klasifikasikan unsur berikut sebagai logam, non-logam, atau semikonduktor, dan berikan alasannya: "
       "Aluminium (Al), Silikon (Si), Belerang (S), Tembaga (Cu)."),
  (25, "Jelaskan mengapa silikon dan germanium banyak digunakan sebagai bahan semikonduktor pada komponen "
       "elektronik avionik, dikaitkan dengan posisinya pada tabel periodik."),
  (30, "Sebuah komponen struktur pesawat menggunakan paduan aluminium karena ringan namun kuat. Jelaskan sifat "
       "kimia unsur logam yang mendukung karakteristik tersebut, serta identifikasi golongan dan periode "
       "Aluminium pada tabel periodik."),
 ]),
(11, 10, "Kimia: Struktur Atom dan Molekul", "Sub-CPMK 5",
 [(20, "Tuliskan konfigurasi elektron untuk atom Natrium (Na, Z=11) dan Klorin (Cl, Z=17)."),
  (25, "Jelaskan perbedaan ikatan ion dan ikatan kovalen, masing-masing disertai satu contoh senyawa."),
  (25, "Berdasarkan konfigurasi elektron pada Soal 1, jelaskan jenis ikatan yang terbentuk antara Na dan Cl "
       "pada pembentukan NaCl serta gambarkan proses transfer elektronnya."),
  (30, "Sebuah kabel konduktor menggunakan tembaga (Cu) karena ikatan logamnya memungkinkan elektron "
       "bergerak bebas. Jelaskan model ikatan logam tersebut dan hubungkan dengan sifat konduktivitas "
       "listrik yang tinggi pada tembaga."),
 ]),
(12, 11, "Kimia: Struktur Kristal", "Sub-CPMK 5",
 [(20, "Sebutkan dan jelaskan tiga jenis struktur kristal logam yang umum (BCC, FCC, HCP)."),
  (25, "Jelaskan bagaimana susunan atom pada struktur kristal FCC memberikan sifat keuletan (ductility) "
       "yang lebih tinggi dibanding struktur BCC."),
  (25, "Hitung jumlah atom efektif per sel satuan untuk struktur kristal FCC (face-centered cubic), tunjukkan "
       "cara perhitungannya (kontribusi atom sudut dan atom pada sisi)."),
  (30, "Sebuah komponen landing gear membutuhkan material dengan kombinasi kekuatan tinggi dan ketahanan "
       "terhadap deformasi. Jelaskan bagaimana pemilihan struktur kristal material logam memengaruhi "
       "keputusan desain tersebut."),
 ]),
(13, 12, "Kimia: Koloid", "Sub-CPMK 6",
 [(20, "Jelaskan definisi sistem koloid dan sebutkan tiga contoh koloid dalam kehidupan sehari-hari."),
  (25, "Bedakan karakteristik fisik antara larutan sejati, koloid, dan suspensi berdasarkan ukuran partikel "
       "dan kestabilannya."),
  (25, "Jelaskan efek Tyndall pada sistem koloid dan bagaimana fenomena ini digunakan untuk membedakan "
       "koloid dari larutan sejati."),
  (30, "Cairan hidrolik pada sistem pesawat dapat terkontaminasi membentuk emulsi (koloid air-minyak). "
       "Jelaskan dampak kontaminasi ini terhadap performa sistem hidrolik dan usulkan satu metode "
       "sederhana untuk mendeteksi keberadaan koloid tersebut."),
 ]),
(14, 13, "Kimia: Larutan (Solution) dan Pelarut (Solvents)", "Sub-CPMK 6",
 [(20, "Hitung konsentrasi molaritas larutan yang dibuat dari $0.5$ mol NaCl dilarutkan dalam $2$ liter air."),
  (25, "Jelaskan konsep kelarutan (solubility) dan faktor-faktor yang memengaruhinya (suhu, tekanan, "
       "polaritas pelarut)."),
  (25, "Suatu larutan pembersih avionik menggunakan pelarut organik nonpolar. Jelaskan mengapa pelarut "
       "tersebut tidak efektif untuk melarutkan kontaminan garam (senyawa ionik), dikaitkan dengan prinsip "
       "\"like dissolves like\"."),
  (30, "Sebanyak $200\\,\\text{mL}$ larutan dengan konsentrasi $2\\,\\text{M}$ akan diencerkan menjadi "
       "$0.5\\,\\text{M}$. Hitung volume air yang harus ditambahkan menggunakan rumus pengenceran "
       "$M_1V_1=M_2V_2$."),
 ]),
(15, 14, "Material: Kekerasan (Hardness) dan Kelenturan (Ductility)", "Sub-CPMK 7",
 [(20, "Jelaskan definisi kekerasan (hardness) dan kelenturan (ductility) suatu material, serta hubungan "
       "keduanya secara umum (mengapa material sangat keras sering kali kurang ulet)."),
  (25, "Sebutkan dan jelaskan singkat dua metode pengujian kekerasan material yang umum digunakan pada "
       "industri (mis. Brinell, Rockwell, atau Vickers)."),
  (25, "Dua material diuji tarik: Material A patah setelah mengalami perpanjangan $2\\%$, Material B patah "
       "setelah perpanjangan $15\\%$. Tentukan mana yang lebih ulet (ductile) dan jelaskan implikasinya "
       "untuk pemilihan material komponen yang menahan beban kejut."),
  (30, "Sebuah baut pengikat struktur pesawat harus dipilih antara material bertitik keras tinggi namun getas "
       "(brittle) dan material dengan kekerasan sedang namun ulet. Jelaskan pertimbangan teknik yang "
       "mendasari pemilihan material yang lebih aman untuk aplikasi tersebut."),
 ]),
(16, 15, "Review \\& Latihan: Kimia dan Material", "Sub-CPMK 5--7",
 [(20, "Jelaskan perbedaan struktur atom logam dan non-logam serta pengaruhnya pada sifat konduktivitas."),
  (25, "Suatu larutan garam ($0.2$ mol dalam $500\\,\\text{mL}$) dicampur dengan sedikit minyak sehingga "
       "membentuk emulsi. Jelaskan jenis campuran yang terbentuk dan hitung konsentrasi molar larutan "
       "garam sebelum pencampuran."),
  (25, "Sebuah paduan logam baru diuji dan menunjukkan struktur kristal FCC dengan kekerasan sedang. "
       "Prediksikan karakteristik keuletannya dan jelaskan alasan ilmiahnya."),
  (30, "Soal terpadu: Jelaskan alur pemilihan material untuk badan pesawat mulai dari (a) identifikasi unsur "
       "penyusun paduan, (b) struktur kristal yang terbentuk, hingga (c) sifat mekanik (hardness/ductility) "
       "yang dihasilkan, serta kaitkan dengan kebutuhan desain ringan dan kuat."),
 ]),
(17, 16, "Review \\& Latihan Terpadu (Pra-UAS)", "Sub-CPMK 1--7",
 [(20, "Hitung $\\log_{10}(2.5\\times10^{3})$ dan sederhanakan $\\dfrac{x^2-16}{x-4}$."),
  (25, "Sebuah menara kontrol setinggi $30\\,\\text{m}$ diamati dari jarak $40\\,\\text{m}$. Hitung sudut "
       "elevasi pengamatan menggunakan trigonometri, lalu hitung volume material solid menara jika "
       "berbentuk silinder berjari-jari $2\\,\\text{m}$."),
  (25, "Arus pengisian kapasitor $i(t)=4t$ ampere. Tentukan muatan pada $t=3$ detik menggunakan integral, "
       "kemudian jelaskan bagaimana konsep turunan digunakan untuk memverifikasi hasil tersebut."),
  (30, "Soal terpadu lintas topik: Sebuah sensor kimia pada pesawat mendeteksi larutan dengan konsentrasi "
       "$0.8\\,\\text{M}$ dalam volume $150\\,\\text{mL}$. (a) Hitung jumlah mol zat terlarut, (b) jika "
       "larutan tersebut kontak dengan komponen logam berstruktur kristal FCC, jelaskan potensi dampak "
       "korosinya terhadap sifat ductility material tersebut."),
 ]),
]
