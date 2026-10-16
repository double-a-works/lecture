#!/usr/bin/env python3
"""ID ringkasan strings for Natural_Science_1, meetings 14-17, one per
TOPICAL slide in document order, matching extract_slides.topical_spans()
(real content extracted from the deployed lecture.tex)."""

RINGKASAN = {}

# Meeting 14 -- Solutions and Concentration
RINGKASAN[14] = [
 r"Solut (zat terlarut): zat yang dilarutkan, jumlahnya lebih sedikit; Pelarut (solvent): zat yang melarutkan, sering air, jumlahnya lebih banyak; Larutan (solution): campuran homogen (seragam) antara solut dan pelarut.",
 r"Molaritas $M=\dfrac{\text{mol solut}}{\text{liter larutan}}$, satuan mol/L. Contoh: melarutkan 0,5 mol solut dalam 2 L larutan menghasilkan $M=0{,}5/2=0{,}25$ mol/L.",
 r"Persen massa $=\dfrac{\text{massa solut}}{\text{massa larutan}}\times100\%$. Contoh: 10 g garam dilarutkan hingga total larutan 200 g menghasilkan $10/200\times100\%=5\%$ berdasarkan massa.",
 r"Menambahkan pelarut menurunkan konsentrasi sementara jumlah mol solut tetap: $M_1V_1=M_2V_2$. Contoh: mengencerkan 1 L larutan 2 M menjadi 4 L menghasilkan $M_2=(2)(1)/4=0{,}5$ M.",
 r"Suhu: umumnya menaikkan kelarutan padatan dalam cairan, tapi menurunkan kelarutan gas dalam cairan; Tekanan: sangat memengaruhi kelarutan gas (tekanan lebih tinggi, gas lebih banyak larut); Polaritas: \"like dissolves like\" -- pelarut polar (air) melarutkan solut polar/ionik; pelarut non-polar melarutkan solut non-polar.",
 r"Larutan \textbf{jenuh} adalah saat larutan menampung solut maksimum yang bisa larut pada suhu tersebut; menambah solut lagi menyisakan padatan tak larut di dasar. Larutan lewat jenuh (supersaturated) menampung lebih banyak dari titik jenuh tetapi tidak stabil.",
 r"Instruksi latihan di kelas: coba tiap soal dulu sebelum memeriksa solusi di slide berikutnya.",
 r"Soal: hitung molaritas larutan yang mengandung 1,5 mol solut dalam 3 L larutan.",
 r"Solusi: $M=1{,}5\text{ mol}/3\text{ L}=0{,}5$ mol/L.",
 r"Soal: sebuah larutan dibuat dari 25 g gula dilarutkan hingga total larutan 500 g. Cari konsentrasi persen massa.",
 r"Solusi: Persen massa $=25/500\times100\%=5\%$.",
 r"Soal: Anda punya 2 L larutan 3 M. Berapa banyak air harus ditambahkan untuk mengencerkannya menjadi 1 M (asumsikan volume langsung bertambah)?",
 r"Solusi: $M_1V_1=M_2V_2\Rightarrow(3)(2)=(1)V_2\Rightarrow V_2=6$ L total. Air yang ditambahkan $=6-2=4$ L.",
]

# Meeting 15 -- Mechanical Properties of Materials
RINGKASAN[15] = [
 r"Memilih material yang tepat untuk bagian pesawat berarti menyeimbangkan kekuatan, bobot, dan bagaimana material merespons indentasi, pembengkokan, dan peregangan.",
 r"Kekerasan (hardness): ketahanan material terhadap indentasi atau goresan permukaan lokal. Material yang lebih keras lebih tahan aus tapi sering lebih getas.",
 r"Duktilitas (ductility): kemampuan berdeformasi plastis (permanen) sebelum patah -- bisa ditarik menjadi kawat tanpa putus; Kegetasan (brittleness): patah dengan sedikit atau tanpa deformasi plastis -- kebalikan duktilitas; Kelenturan (malleability): mirip duktilitas tapi untuk digulung/ditempa menjadi lembaran.",
 r"Metode pengujian kekerasan: Brinell -- indenter bola baja/karbida, mengukur diameter indentasi; Rockwell -- kedalaman indenter di bawah beban, pembacaan dial langsung; Vickers -- indenter piramida intan, presisi untuk sampel tipis/keras.",
 r"Uji tarik (tensile test): sampel ditarik hingga patah, sementara tegangan (stress) dan regangan (strain) dicatat. \% pemanjangan (elongasi) $=$ pertambahan panjang / panjang awal $\times100\%$, ukuran langsung duktilitas. Kurva tegangan-regangan juga mengungkap kekuatan luluh (yield strength) dan kekuatan tarik maksimum (ultimate strength).",
 r"Trade-off pemilihan material: kulit pesawat -- paduan ringan dan duktil (aluminium) yang bisa menyerap benturan tanpa retak; alat potong, bantalan -- material keras (baja yang dikeraskan, karbida) yang tahan aus; trade-off umum: menaikkan kekerasan (mis.\ lewat perlakuan panas) biasanya menurunkan duktilitas.",
 r"Instruksi latihan di kelas: coba tiap soal dulu sebelum memeriksa solusi di slide berikutnya.",
 r"Soal: sampel logam sepanjang 100 mm diregangkan hingga 108 mm sebelum patah. Hitung \% elongasinya dan komentari duktilitasnya.",
 r"Solusi: \% elongasi $=(108-100)/100\times100\%=8\%$. Elongasi 8\% menunjukkan material yang cukup duktil (material getas biasanya menunjukkan elongasi jauh di bawah 5\%).",
 r"Soal: perancang pesawat harus memilih antara paduan keras-getas dan paduan lebih lunak-duktil untuk panel kulit luar. Mana yang umumnya lebih disukai, dan mengapa?",
 r"Solusi: paduan duktil umumnya lebih disukai untuk panel kulit -- ia bisa menyerap energi benturan dan berdeformasi alih-alih retak di bawah tegangan, dan lebih mudah dibentuk menjadi panel melengkung saat produksi.",
]

# Meeting 16 -- Integration: Chemistry & Materials
RINGKASAN[16] = [
 r"Cakupan Pertemuan 10--15: P10 unsur, nomor atom, organisasi tabel periodik; P11 struktur atom/molekul, ikatan ionik vs kovalen; P12 struktur kristal (BCC/FCC/HCP), hubungan struktur-properti; P13 koloid dan klasifikasi campuran, efek Tyndall; P14 larutan, molaritas, persen massa, pengenceran; P15 kekerasan, duktilitas, dan pemilihan material.",
 r"Ikatan logam (elektron terdelokalisasi, dari P11) dan pengemasan FCC (74\%, dari P12) bersama-sama menjelaskan mengapa aluminium adalah konduktor listrik yang baik sekaligus cukup duktil untuk membentuk panel kulit pesawat (P15) -- menghubungkan ikatan, struktur kristal, dan properti mekanis ke pilihan material nyata.",
 r"Silikon adalah metaloid (P10) dengan kisi kristal kubik-berlian (P12), yang ikatan atomiknya (P11, kovalen) memberinya konduktivitas menengah -- dasar dari elektronika semikonduktor.",
 r"Strategi ujian: hubungkan struktur $\to$ ikatan $\to$ properti $\to$ aplikasi di setiap jawaban; tunjukkan perhitungan konsentrasi langkah demi langkah dengan satuan yang jelas; gunakan satuan yang benar secara konsisten (mol, mol/L, \%).",
 r"Instruksi latihan di kelas: soal terintegrasi ini menggabungkan dua atau lebih topik dari Pertemuan 10--15.",
 r"Soal: klasifikasikan ikatan pada NaCl (P11), lalu jelaskan bagaimana ikatan ini menyebabkan NaCl membentuk kisi kristal teratur (P12) alih-alih padatan amorf.",
 r"Solusi: ikatan NaCl adalah ionik (Na memindahkan elektron ke Cl, membentuk Na$^+$ dan Cl$^-$). Tarikan elektrostatik antar ion bermuatan berlawanan paling kuat saat tiap ion dikelilingi susunan tetangga bermuatan berlawanan yang teratur -- inilah yang mendorong terbentuknya kisi kristal berulang dan teratur, bukan padatan tak beraturan.",
 r"Soal: suspensi koloid 250 mL disiapkan dengan mendispersikan 5 g padatan dalam air. (a) Hitung konsentrasi persen massanya (asumsikan massa larutan $\approx$ 250 g). (b) Apakah campuran ini diperkirakan menunjukkan efek Tyndall? Mengapa?",
 r"Solusi: (a) Persen massa $=5/250\times100\%=2\%$. (b) Ya -- sebagai koloid (partikel 1--1000 nm), ia menghamburkan cahaya dan menunjukkan efek Tyndall, tidak seperti larutan sejati.",
]

# Meeting 17 -- Final Review
RINGKASAN[17] = [
 r"Penekanan pada Pertemuan 10--16 (kimia dan material): unsur, struktur atom/molekul, ikatan, struktur kristal, koloid, larutan, dan properti mekanis -- dengan matematika terapan (P1--P8) sebagai alat pendukung untuk perhitungan.",
 r"Ikatan ionik (transfer elektron) vs ikatan kovalen (berbagi elektron); kisi kristal (BCC/FCC/HCP) menjelaskan densitas, duktilitas, dan perilaku semikonduktor.",
 r"Larutan, koloid, suspensi berbeda berdasarkan ukuran partikel dan pengendapan; Molaritas $M=\text{mol}/\text{L}$, persen massa, dan pengenceran $M_1V_1=M_2V_2$.",
 r"Kekerasan (Brinell/Rockwell/Vickers) vs duktilitas (uji tarik, \% elongasi); pemilihan material selalu menukar satu properti dengan properti lain.",
 r"Hitung konsentrasi larutan yang disiapkan (aljabar + satuan), lalu bernalar tentang bagaimana struktur solut (ikatan, polaritas) memengaruhi kelarutan -- menggabungkan matematika kuantitatif dengan pemahaman kimia.",
 r"Strategi ujian akhir: baca tiap soal untuk mengenali konsep yang diuji sebelum menghitung; tunjukkan pekerjaan kuantitatif langkah demi langkah -- nilai parsial diberikan untuk penalaran yang terlihat; jaga satuan kimia tetap konsisten (mol, mol/L, \%, nm); atur waktu di antara soal matematika dan kimia campuran.",
 r"Instruksi latihan di kelas: soal terintegrasi ini mencerminkan gaya campuran ujian akhir.",
 r"Soal: larutan stok 4 M diencerkan dari 500 mL menjadi 2 L. (a) Cari molaritas baru. (b) Apakah larutan hasil lebih mungkin tetap larutan sejati atau membentuk koloid, jika solutnya adalah ion terlarut kecil (mis.\ Na$^+$)?",
 r"Solusi: (a) $M_1V_1=M_2V_2\Rightarrow(4)(0{,}5)=M_2(2)\Rightarrow M_2=1$ M. (b) Larutan sejati -- ion terlarut berukuran $<1$ nm, jauh lebih kecil dari rentang koloid 1--1000 nm, sehingga tidak pernah membentuk koloid berapa pun pengencerannya.",
 r"Soal: dua sampel logam tak dikenal diuji: Sampel X berstruktur FCC dan \% elongasi tinggi. Sampel Y berstruktur tak teratur (amorf) dan hancur di bawah tegangan. Sampel mana yang akan Anda pilih untuk panel kulit pesawat, dan mengapa?",
 r"Solusi: Sampel X -- struktur FCC dengan \% elongasi tinggi menunjukkan duktilitas baik, artinya bisa menyerap energi benturan dengan berdeformasi alih-alih patah, yang esensial untuk panel kulit struktural. Kegetasan Sampel Y membuatnya tidak cocok.",
]
