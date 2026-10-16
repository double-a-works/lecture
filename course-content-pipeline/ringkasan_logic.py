#!/usr/bin/env python3
"""Indonesian ringkasan (ID summary) strings for Digital_Technic_Logic, meetings 1-4.
Each list is positionally ordered to match content_logic.py M[n][3] (the slides list)."""

RINGKASAN = {
1: [
 r"Komputer avionik merepresentasikan besaran fisik seperti ketinggian dan kecepatan sebagai sinyal digital (hanya 0 dan 1); insinyur harus mampu mengonversi nilai desimal yang mudah dipahami manusia ke bentuk biner, oktal, dan heksadesimal yang digunakan mesin.",
 r"Setiap sistem bilangan memiliki basis (radix) $r$ dan bobot posisi $r^i$; nilai desimal dihitung dengan menjumlahkan setiap digit dikali bobot posisinya, seperti pada contoh $1011_2 = 11_{10}$.",
 r"Istilah dasar: bit adalah satu digit biner, nibble adalah 4 bit, byte adalah 8 bit; MSB adalah bit paling kiri (paling signifikan) dan LSB adalah bit paling kanan.",
 r"Konversi desimal ke biner dilakukan dengan membagi berulang dengan 2 dan mencatat sisa baginya; hasil biner dibaca dari sisa terakhir ke sisa pertama (dari bawah ke atas).",
 r"Contoh: $45_{10}$ dibagi berulang dengan 2 menghasilkan sisa $1,0,1,1,0,1$; dibaca dari bawah ke atas menjadi $101101_2$, terverifikasi dengan menjumlahkan bobot bit bernilai 1.",
 r"Dengan metode yang sama, $178_{10}$ dikonversi menjadi $10110010_2$ melalui delapan langkah pembagian berulang dengan 2.",
 r"Bagian pecahan desimal dikonversi ke biner dengan mengalikan berulang dengan 2 dan mencatat bagian bulat sebagai bit berikutnya; bit dibaca dari atas ke bawah, berkebalikan dengan metode pembagian.",
 r"Contoh: $0.625_{10}$ dikalikan berulang dengan 2 menghasilkan bit $1,0,1$; dibaca dari atas ke bawah menjadi $0.101_2$.",
 r"Konversi biner ke desimal dilakukan dengan menjumlahkan bobot setiap bit bernilai 1, termasuk pangkat negatif dua untuk bagian pecahan setelah titik biner.",
 r"Kesalahan umum: salah arah pembacaan sisa bagi (harus dari bawah ke atas) atau bit hasil kali (harus dari atas ke bawah), serta lupa bahwa sebagian pecahan desimal tidak pernah berakhir dalam biner sehingga harus dibulatkan.",
 r"Latihan kelas: mengonversi $67_{10}$ dan $0.8125_{10}$ ke biner, serta mengonversi $101110.011_2$ ke desimal, untuk melatih kedua arah konversi.",
],
2: [
 r"String biner yang panjang sulit dibaca manusia; oktal dan heksadesimal mengelompokkan bit menjadi digit yang lebih ringkas, dan heksadesimal adalah standar untuk alamat memori dan bus data avionik.",
 r"Oktal (basis 8) memetakan setiap digit ke 3 bit biner; heksadesimal (basis 16, digit 0--9 dan A--F) memetakan setiap digit ke 4 bit (satu nibble).",
 r"Biner dikonversi ke oktal dengan mengelompokkan bit menjadi 3 dari titik radiks, menambahkan nol di ujung bila perlu, lalu setiap kelompok dikonversi langsung ke digit oktal.",
 r"Sama seperti oktal, namun biner dikelompokkan menjadi 4 bit untuk mendapatkan setiap digit heksadesimal.",
 r"Contoh: $10111011_2$ menghasilkan $273_8$ (kelompok 3 bit) dan $BB_{16}$ (kelompok 4 bit).",
 r"Nilai oktal dan heksadesimal dikonversi ke desimal dengan rumus jumlah berbobot yang sama, menggunakan basis masing-masing (8 atau 16); keduanya harus menghasilkan nilai desimal yang sama.",
 r"Setiap digit heksadesimal diperluas menjadi nibble 4-bit, lalu dijumlahkan berbobot untuk mendapatkan $759_{10}$.",
 r"Algoritma pembagian berulang juga berlaku untuk basis 16, dengan sisa 10--15 dituliskan sebagai huruf A--F.",
 r"Algoritma perkalian berulang juga berlaku untuk konversi pecahan ke basis apa pun, termasuk heksadesimal.",
 r"Kesalahan umum: lupa menambahkan nol pembatas sebelum pengelompokan, tertukar ukuran kelompok oktal (3 bit) dan heksadesimal (4 bit), serta salah membaca huruf A--F sebagai angka desimal.",
 r"Latihan: mengonversi $11001010_2$ ke oktal dan heksadesimal, $1F4_{16}$ ke biner dan desimal, serta $0.75_{10}$ ke heksadesimal.",
],
3: [
 r"Tiga cara merepresentasikan bilangan bertanda n-bit: sign-magnitude (bit MSB sebagai tanda), komplemen satu (NOT semua bit), dan komplemen dua (komplemen satu ditambah satu) yang menjadi standar modern.",
 r"Untuk menegasikan bilangan: balik semua bit lalu tambahkan 1; MSB tetap menunjukkan tanda dan operasi aritmatika tidak memerlukan kasus khusus.",
 r"Rentang bilangan bertanda komplemen dua n-bit adalah $-2^{n-1}$ hingga $+2^{n-1}-1$; hanya komplemen dua yang memiliki representasi nol tunggal.",
],
4: [
 r"Penjumlahan biner dilakukan bit demi bit dengan carry, mengikuti aturan $0+0=0$, $1+0=1$, dan $1+1=10$ (menghasilkan carry).",
 r"Pengurangan $A-B$ dilakukan dengan menjumlahkan $A$ dengan komplemen dua dari $B$, lalu membuang carry keluar terakhir.",
 r"Overflow bertanda terjadi bila dua operan bertanda sama menghasilkan tanda hasil yang berlawanan; carry-out tidak sama dengan overflow pada aritmatika bertanda.",
],
}
