#!/usr/bin/env python3
"""ID ringkasan strings, one per TOPICAL slide, in document order, for
Digital_Technic_Logic meeting 17 (Final Review, real content extracted from
the deployed lecture.tex via extract_slides.py / splice_bilingual.py)."""

RINGKASAN = {}

# Meeting 17 -- Final Review
RINGKASAN[17] = [
 r"Cakupan pertemuan 10--16 untuk ujian akhir: flip-flop (SR, D, JK, T -- tabel kebenaran, persamaan karakteristik/eksitasi), rangkaian sekuensial (shift register, pencacah ripple dan sinkron), ADC (sampling, kuantisasi, resolusi, konversi SAR), DAC (binary-weighted, R-2R, resolusi, settling time), serta terminologi komputer dan arsitektur mikrokomputer (CPU, bus, siklus fetch-execute).",
 r"Tabel next-state flip-flop: SR $\to S+\overline{R}Q$ (dengan $SR=0$); D $\to D$; JK $\to J\overline{Q}+\overline{K}Q$; T $\to T\oplus Q$; rangkaian sekuensial menggabungkan flip-flop dengan clock untuk menambahkan memori pada desain.",
 r"Rumus ADC/DAC: step size $=V_{ref}/2^n$; output DAC $V_{out}=V_{ref}\cdot D/2^n$; sampling Nyquist $f_s>2f_{max}$ agar sinyal tidak mengalami aliasing.",
 r"Arsitektur Von Neumann: memori/bus bersama untuk kode dan data; siklus Fetch $\to$ Decode $\to$ Execute berulang tiap instruksi; bus data, alamat, dan kendali menghubungkan CPU, memori, dan I/O.",
 r"Contoh integrasi rantai kendali avionik lengkap: Sensor menghasilkan sinyal analog (mis.\ transduser tekanan) $\to$ ADC mencuplik dan mengkuantisasi menjadi kata digital $\to$ Mikrokomputer (CPU+memori+register, dijaga clock oleh flip-flop) mengambil, menerjemahkan, dan menjalankan instruksi hukum kendali $\to$ DAC mengubah perintah digital kembali menjadi tegangan analog $\to$ Aktuator (mis.\ servo) merespons sinyal analog tersebut.",
 r"Kesalahan lintas-topik yang umum: tertukar arah ADC (analog$\to$digital) dengan DAC (digital$\to$analog); lupa bahwa next-state flip-flop bergantung pada \emph{tepi clock}, bukan sekadar level input; mencampur lebar bus alamat (ruang alamat) dengan lebar bus data (ukuran word).",
 r"Strategi ujian akhir: gambar diagram blok untuk menyusun jawaban bertahap (sensor$\to$ADC$\to\dots$); lacak lebar bit dengan cermat di setiap perhitungan ADC/DAC; nyatakan next-state flip-flop langsung dari persamaan karakteristik -- lebih cepat daripada membangun ulang tabel kebenaran penuh saat waktu terbatas; alokasikan waktu merata karena soal terintegrasi bernilai lebih tinggi namun tidak proporsional lebih panjang.",
 r"Soal: gambarkan rantai digital sensor-ke-aktuator dan beri label tiap tahap (5 blok).",
 r"Solusi: Sensor $\to$ ADC $\to$ Mikrokomputer (CPU+memori+register) $\to$ DAC $\to$ Aktuator; tiap panah mewakili konversi sinyal atau transfer bus; siklus fetch-execute mikrokomputer memproses nilai sensor terdigitasi antara ADC dan DAC.",
 r"Soal: hitung step size ADC dan output DAC yang bersesuaian untuk sistem 8-bit dengan $V_{ref}=5$V dan kode $01100100_2$.",
 r"Solusi: Step size $=5/256\approx19{,}53$mV. $01100100_2=100_{10}$. $V_{out}=5\times100/256\approx1{,}95$V.",
 r"Soal: flip-flop JK dengan $J=1,K=1$ di-clock 3 kali mulai dari $Q=0$. Berapa nilai $Q$ setelah tiap tepi clock?",
 r"Solusi: $J=K=1$ berarti toggle tiap tepi: $Q_0=0\to Q_1=1\to Q_2=0\to Q_3=1$.",
 r"Soal: mikrokomputer dengan bus alamat 16-bit membaca sensor lewat ADC 10-bit, menghitung hukum kendali, lalu keluar lewat DAC 8-bit. Identifikasi satu risiko ketidakcocokan lebar bit dan cara mengatasinya.",
 r"Solusi: ADC menghasilkan nilai 10-bit tetapi DAC hanya menerima 8 bit -- menulis langsung kode ADC ke DAC akan memotong 2 bit resolusi. Atasi dengan menskalakan/membulatkan nilai 10-bit menjadi 8 bit di perangkat lunak sebelum output, atau memilih DAC dengan resolusi setara atau lebih tinggi dari ADC.",
]
