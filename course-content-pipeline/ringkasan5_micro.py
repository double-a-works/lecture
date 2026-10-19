#!/usr/bin/env python3
"""ID ringkasan strings, one per TOPICAL slide, in document order, for
Digital_Technic_Micro meeting 17 (Final Review, real content extracted from
the deployed lecture.tex via extract_slides.py / splice_bilingual.py)."""

RINGKASAN = {}

# Meeting 17 -- Final Review
RINGKASAN[17] = [
 r"Cakupan pertemuan 10--16 untuk ujian akhir: IC (skala integrasi SSI--VLSI, keluarga logika TTL/CMOS), karakteristik elektris, pewaktuan, kemasan, dan cara membaca datasheet, serta display (LED, seven-segment, dot-matrix, LCD) beserta cara antarmukanya.",
 r"Rantai pemilihan IC: (1) identifikasi fungsi logika yang dibutuhkan dan perkirakan skala integrasinya; (2) pilih keluarga logika (TTL/CMOS) yang kompatibel dengan sisa desain; (3) verifikasi karakteristik elektris ($V_{IH}/V_{IL}/V_{OH}/V_{OL}$, arus, pewaktuan) terhadap datasheet; (4) pilih kemasan yang sesuai metode perakitan dan jumlah pin.",
 r"Rumus display: resistor seri LED $R=(V_{supply}-V_{LED})/I_{LED}$; refresh multiplex harus melebihi sekitar 50--60 Hz per digit/baris agar tidak berkedip; common-anode menyalakan segmen dengan LOW, common-cathode dengan HIGH.",
 r"Konsep antarmuka: paralel -- lebih banyak pin, lebih cepat per transfer; serial (SPI/I2C) -- lebih sedikit pin, bit demi bit; IC decoder/driver (mis.\ BCD-ke-7-segment) mengalihkan tugas translasi dari perangkat lunak CPU; fan-out dan kecocokan level logika harus diperiksa setiap kali dua chip beda keluarga dihubungkan langsung.",
 r"Contoh integrasi desain lengkap: pilih IC decoder BCD-ke-7-segment CMOS untuk daya statis rendah (Pertemuan 10--11); periksa datasheet-nya -- rentang suplai, $V_{OH}/V_{OL}$, arus penggerak output terhadap kebutuhan arus segmen display (Pertemuan 12--13); hitung resistor seri LED tiap segmen dari $V_{supply}$, $V_{LED}$, dan target $I_{LED}$ (Pertemuan 14); tentukan pengkabelan common-anode atau common-cathode agar sesuai polaritas output decoder.",
 r"Kesalahan lintas-topik yang umum: memilih chip berdasarkan fungsi logikanya tapi lupa memeriksa kecocokan arus/tegangan; melupakan perhitungan resistor LED saat berpindah dari teori ke rangkaian nyata; salah memasangkan pengkabelan common-anode/common-cathode dengan polaritas output driver; meremehkan laju refresh multiplex sehingga tampilan berkedip terlihat.",
 r"Strategi ujian akhir: justifikasi setiap pilihan komponen dengan angka datasheet spesifik, bukan sekadar \"seharusnya berfungsi\"; lacak level logika dengan cermat saat soal mencampur komponen TTL dan CMOS; tampilkan rumus resistor LED dan alasan refresh rate secara eksplisit -- nilai parsial diberikan untuk langkah kerja yang terlihat; gambar diagram blok terlebih dahulu untuk soal antarmuka multi-tahap.",
 r"Soal: pilih dan justifikasi keluarga IC decoder (TTL atau CMOS) untuk desain display seven-segment bertenaga baterai, hemat daya.",
 r"Solusi: CMOS adalah pilihan lebih baik -- konsumsi daya statisnya yang sangat rendah langsung memperpanjang umur baterai dibanding TTL yang menarik arus terus-menerus bahkan saat idle -- faktor penentu setiap kali anggaran daya menjadi perhatian.",
 r"Soal: hitung resistor seri untuk segmen display seven-segment common-cathode, dengan $V_{supply}=5$V, $V_{LED}=2{,}1$V, dan target $I_{LED}=12$mA. Sebutkan juga laju refresh yang masuk akal jika 4 digit dimultiplex.",
 r"Solusi: $R=(5-2{,}1)/0{,}012\approx242\,\Omega$ (nilai standar terdekat $\approx240\,\Omega$ atau $270\,\Omega$). Agar 4 digit multiplex tampak bebas kedip pada $\geq$60 Hz per digit, siklus penuh 4-digit harus berulang pada $\geq4\times60=240$ Hz, yaitu tiap digit menyala paling lama sekitar $1/240\text{s}\approx4{,}2$ms per siklus.",
 r"Soal: gambarkan/jelaskan diagram blok antarmuka mikrokomputer-ke-display untuk tampilan seven-segment multiplex 4-digit.",
 r"Solusi: Mikrokomputer $\to$ (bus paralel atau serial) $\to$ decoder BCD-ke-7-segment $\to$ resistor pembatas arus $\to$ segmen display 7-segment; secara terpisah, mikrokomputer $\to$ jalur pemilih digit $\to$ driver transistor $\to$ common anode/cathode tiap digit, disinkronkan dengan output pola segmen.",
 r"Soal: sebuah desain memakai decoder TTL ($V_{OH,min}=2{,}4$V) untuk menggerakkan pengendali multiplex berbasis CMOS ($V_{IH,min}=3{,}5$V), dan display berkedip tidak menentu hanya pada sebagian posisi digit. Diagnosis penyebab yang paling mungkin.",
 r"Solusi: output HIGH terjamin decoder TTL ($2{,}4$V) berada di bawah ambang input HIGH yang dibutuhkan pengendali CMOS ($3{,}5$V) -- ketidakcocokan antarmuka dari Pertemuan 11. Tergantung margin tegangan dan derau, sebagian transisi mungkin terbaca benar dan sebagian tidak, menghasilkan kedipan yang tidak konsisten dan bergantung posisi, bukan kegagalan total yang konsisten. Solusi: tambahkan resistor pull-up atau buffer level-shifting yang tepat.",
]
