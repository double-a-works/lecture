#!/usr/bin/env python3
"""Indonesian ringkasan (ID summary) strings for Digital_Technic_Micro, meetings 1-4.
Each list is positionally ordered to match content_micro.py M[n][3] (the slides list)."""

RINGKASAN = {
1: [
 r"Setiap unit avionik (flight management computer, autopilot, indikator mesin) dibangun di atas inti mikrokomputer; memahami arsitekturnya penting untuk troubleshooting dan perawatan peralatan avionik yang aman.",
 r"Mikrokomputer mengintegrasikan CPU, memori, dan I/O yang terhubung melalui bus; CPU mengeksekusi instruksi, memori menyimpan program dan data, I/O menjadi antarmuka ke dunia luar.",
 r"CPU mengambil, mendekode, dan mengeksekusi instruksi; memori menyimpan program dan data; I/O menjadi antarmuka ke sensor dan aktuator; ketiganya hanya berfungsi bila terhubung dan terkoordinasi lewat bus.",
 r"Bus alamat membawa lokasi yang ingin diakses CPU, bus data membawa nilai yang dibaca/ditulis, dan bus kendali membawa sinyal pewaktuan dan perintah seperti baca/tulis dan interrupt.",
 r"Diagram blok menunjukkan CPU, memori, dan I/O saling terhubung melalui bus sistem bersama yang membawa jalur alamat, data, dan kendali ke setiap blok.",
 r"Arsitektur Von Neumann menggunakan satu memori dan bus bersama untuk instruksi dan data (lebih sederhana); arsitektur Harvard memisahkan keduanya sehingga fetch instruksi dan akses data bisa berlangsung bersamaan (lebih cepat).",
 r"Mikroprosesor adalah chip CPU saja; mikrokontroler menggabungkan CPU, memori, dan I/O dalam satu chip; mikrokomputer adalah sistem komputasi lengkap dengan papan memori/I-O eksternal.",
 r"Flight Management Computer, EICAS, dan komputer autopilot semuanya secara internal mengikuti model CPU-memori-I/O yang sama seperti dibahas pada pertemuan ini.",
 r"Input berupa saklar dan sensor, output berupa layar dan aktuator; perangkat I/O terhubung melalui rangkaian antarmuka (buffer, ADC/DAC, driver), bukan langsung ke pin CPU.",
 r"Kesalahan umum: menyamakan mikroprosesor (chip) dengan mikrokomputer (sistem lengkap), mengira mikrokontroler perlu memori eksternal, dan melupakan bahwa I/O butuh rangkaian antarmuka.",
 r"Diskusi kelas: mengidentifikasi CPU/memori/I-O pada smartphone, memilih arsitektur yang cocok untuk komputer autopilot, dan menyebutkan contoh LRU avionik beserta perangkat I/O-nya.",
],
2: [
 r"CPU terdiri dari Control Unit (CU) yang mendekode dan mengurutkan operasi, ALU yang melakukan aritmatika dan logika, serta register sebagai penyimpanan cepat di dalam chip.",
 r"CU mengambil instruksi berikutnya dari memori, mendekodenya untuk menentukan operasi dan operan, lalu menghasilkan sinyal kendali untuk ALU, register, dan bus; CU sendiri tidak menghitung nilai, hanya mengatur unit lain.",
 r"ALU menghitung operan dari register: operasi aritmatika (tambah, kurang) dan logika (AND, OR, NOT, XOR), serta menetapkan flag status zero, carry, sign, dan overflow.",
 r"Contoh: $5_{10}+3_{10}$ pada register 4-bit menghasilkan $1000_2=8_{10}$ tanpa carry keluar bit 3, sehingga flag Carry dan Zero bernilai 0.",
 r"Flag Zero aktif jika hasil ALU nol, Carry aktif jika ada carry/borrow di luar bit paling signifikan, Sign menyalin bit paling signifikan, dan Overflow aktif jika hasil bertanda melebihi rentang; flag ini memungkinkan percabangan bersyarat.",
 r"Register kunci meliputi PC (alamat instruksi berikutnya), IR (instruksi saat ini), ACC (hasil ALU), SP (stack pointer), MAR/MDR (alamat/data memori), dan Flags (status Z,C,S,V).",
 r"Register tujuan khusus (PC, IR, SP, Flags) masing-masing memiliki peran tetap dalam siklus fetch-execute, sedangkan register tujuan umum bebas dipakai programmer/compiler; lebih banyak register tujuan umum mengurangi trafik ke memori utama yang lebih lambat.",
 r"Register 8-bit menyimpan $0$--$255$ (tak bertanda); ukuran word memengaruhi rentang bilangan, ukuran alamat, dan kapasitas memori yang bisa diakses langsung oleh CPU.",
 r"Siklus fetch-decode-execute: PC menunjuk instruksi lalu dimuat ke IR dan PC bertambah (fetch); CU mengenali operasi ADD (decode); ALU menjumlahkan operan ke ACC dan flag diperbarui (execute).",
 r"Kesalahan umum: menyamakan akumulator (menyimpan nilai) dengan program counter (menyimpan alamat), lupa flag hanya mencerminkan operasi ALU terakhir, dan mengira overflow sama dengan carry padahal keduanya mengukur hal berbeda (bertanda vs tak bertanda).",
 r"Latihan: menjumlahkan $9_{10}$ dan $7_{10}$ pada register 4-bit dan memeriksa flag Carry, menjelaskan fungsi PC/IR/ACC, dan alasan CPU membutuhkan register tujuan umum maupun khusus.",
],
3: [
 r"Bus data membawa instruksi/data selebar word, bus alamat memilih lokasi (n jalur mengalamatkan $2^n$ sel), dan bus kendali membawa sinyal baca/tulis, clock, dan interrupt.",
 r"Siklus berulang: PC dikirim ke bus alamat untuk membaca instruksi ke IR, CU mendekodenya, lalu ALU/register mengeksekusinya sambil PC bertambah.",
 r"Semakin lebar bus alamat, semakin besar memori yang dapat dialamati; misalnya 16 jalur mengalamatkan 64 KB, 32 jalur mengalamatkan 4 GB.",
],
4: [
 r"Menggunakan simulator CPU, mahasiswa mengamati bagaimana instruksi memindahkan data melalui register, ALU, dan memori lewat bus sistem.",
 r"Program singkat LOAD-ADD-STORE: LOAD mengambil operan ke ACC, ADD menjumlahkan lewat ALU, STORE menulis hasil ke memori, sambil mengamati perubahan PC, IR, dan ACC di setiap langkah.",
 r"Yang dicatat: nilai PC sebelum/sesudah setiap instruksi, perubahan ACC dan flag, serta isi bus alamat/data saat fetch dan execute, untuk dibandingkan dengan teori fetch-execute.",
],
}
