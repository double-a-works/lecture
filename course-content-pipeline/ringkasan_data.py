#!/usr/bin/env python3
"""Indonesian ringkasan (ID summary) strings for Digital_Technic_Data, meetings 1-4.
Each list is positionally ordered to match content_data.py M[n][3] (the slides list)."""

RINGKASAN = {
1: [
 r"Encoding mengubah aliran data biner menjadi sinyal fisik (level tegangan terhadap waktu); membantu sinkronisasi clock penerima, mengurangi bias DC, dan meningkatkan imunitas derau, dengan trade-off bandwidth dan kompleksitas.",
 r"Pada NRZ, level sinyal tetap TINGGI untuk bit 1 dan RENDAH untuk bit 0 sepanjang periode bit; sederhana dan hemat bandwidth, tetapi sulit untuk pemulihan clock pada rangkaian bit identik yang panjang.",
 r"Pada RZ, sinyal kembali ke level nol/netral di tengah setiap periode bit, bahkan untuk bit identik berurutan; menjamin transisi di setiap bit sehingga memudahkan pemulihan clock, namun membutuhkan bandwidth sekitar dua kali lipat NRZ.",
 r"Perbandingan: NRZ memiliki bandwidth lebih rendah dan lebih sederhana tetapi pemulihan clock lebih sulit; RZ membutuhkan bandwidth lebih tinggi dan lebih kompleks tetapi pemulihan clock lebih mudah.",
],
2: [
 r"NRZ kesulitan pemulihan clock pada rangkaian bit identik yang panjang, RZ mengatasinya dengan biaya bandwidth; encoding Manchester menjamin transisi di tengah setiap bit tanpa biaya bandwidth tambahan seperti RZ.",
 r"Setiap bit direpresentasikan oleh transisi di tengah periode bit: bit 1 adalah transisi RENDAH-ke-TINGGI, bit 0 adalah kebalikannya; pemulihan clock sangat baik dan digunakan pada Ethernet klasik.",
 r"Nilai bit ditentukan oleh ada/tidaknya transisi di awal periode bit (bukan arah transisi tengah bit); lebih tahan terhadap pembalikan polaritas kabel, digunakan pada jaringan Token Ring.",
 r"Manchester mengkodekan bit lewat arah transisi, Differential Manchester lewat ada/tidaknya transisi; keduanya menjamin pemulihan clock, tetapi hanya Differential Manchester yang tahan terhadap pembalikan polaritas.",
],
3: [
 r"Pertemuan 1: encoding mengubah data biner menjadi sinyal fisik (NRZ vs RZ). Pertemuan 2: Manchester dan Differential Manchester menjamin pemulihan clock. Hari ini: bagaimana penerima memulihkan bit asli dari sinyal yang diterima (decoding).",
 r"Decoding adalah proses di penerima yang mengubah sinyal fisik yang diterima kembali menjadi aliran data biner asli; merupakan kebalikan dari encoding dan penerima harus mengetahui skema encoding yang dipakai pengirim.",
 r"Alur decoding: sinyal jalur diterima, clock recovery mengekstrak informasi pewaktuan, lalu sampling/decision membaca level atau transisi pada saat yang tepat untuk menentukan nilai bit.",
 r"Aturan decoding NRZ: sampel level sinyal di tengah setiap periode bit (TINGGI=1, RENDAH=0); kelemahan utamanya adalah tidak ada informasi self-clocking sehingga rangkaian bit identik yang panjang menyebabkan drift clock.",
 r"Karena sinyal RZ selalu kembali ke nol, penerima mendeteksi ada/tidaknya pulsa dalam jendela bit (ada pulsa=1, tidak ada=0); setiap periode bit mengandung transisi sehingga clock dapat disinkronkan ulang lebih mudah dibanding NRZ.",
 r"Contoh: sampel tengah setiap sel menghasilkan urutan TINGGI,RENDAH,RENDAH,TINGGI,RENDAH,TINGGI,TINGGI, yang didekode menjadi bit $1001011$.",
 r"Aturan decoding Manchester: periksa arah transisi di tengah setiap sel bit (RENDAH ke TINGGI=1, TINGGI ke RENDAH=0); karena setiap sel menjamin transisi tengah, penerima dapat terus mensinkronkan ulang clock-nya (self-clocking).",
 r"Aturan decoding Differential Manchester: periksa ada/tidaknya transisi di awal sel bit (transisi tengah diabaikan, hanya untuk clocking); ada transisi di awal=0, tidak ada=1, sehingga tahan terhadap pembalikan polaritas jalur.",
 r"Contoh: membaca arah transisi tengah-sel pada 8 sel menghasilkan urutan RENDAH-TINGGI dan TINGGI-RENDAH berselang-seling, yang didekode menjadi bit $10101010$.",
 r"Penyebab kesalahan decoding di dunia nyata: jitter (pergeseran waktu transisi), noise (lonjakan tegangan yang disalahartikan sebagai transisi), bias DC/redaman sinyal, dan drift clock terutama pada kode non-self-clocking seperti NRZ murni.",
 r"Perangkat keras penerima memulihkan clock menggunakan Phase-Locked Loop (PLL) yang mengunci fase osilator internal ke transisi sinyal masuk; kode self-clocking (RZ, Manchester) memberi referensi pewaktuan di setiap bit sehingga PLL tetap terkunci dengan andal.",
 r"Perbandingan aturan keputusan (level vs kehadiran pulsa vs arah transisi), kemampuan self-clocking, dan kerentanan masing-masing skema (rangkaian panjang, biaya bandwidth, atau derau pada tepi sinyal).",
 r"Latihan: mendekode gelombang NRZ 6-bit, menentukan nilai bit dari transisi Manchester TINGGI-ke-RENDAH, dan menjelaskan mengapa Differential Manchester tidak peduli polaritas kabel.",
 r"ARINC 429 menggunakan gelombang mirip RZ bipolar, MIL-STD-1553 menggunakan Manchester II karena tahan terhadap variasi panjang kabel dan pewaktuan; chip transceiver bus mengintegrasikan clock recovery dan logika keputusan dalam perangkat keras berkecepatan tinggi.",
],
4: [
 r"Pertemuan 1-2: skema encoding mengubah bit menjadi sinyal fisik. Pertemuan 3: decoding memulihkan bit di penerima, tetapi noise, jitter, dan drift tetap bisa menyebabkan bit salah dibaca. Hari ini: bagaimana penerima mengetahui data yang didekode benar (deteksi kesalahan).",
 r"Tidak ada kanal transmisi yang sempurna; derau listrik, interferensi elektromagnetik (EMI), dan crosstalk dapat membalik bit, terutama di avionik yang dekat dengan mesin dan radar sebagai sumber EMI kuat; karena itu ditambahkan bit redundan untuk deteksi kesalahan.",
 r"Pengirim menghitung bit cek tambahan dari data menggunakan aturan tertentu; penerima menghitung ulang aturan yang sama pada data yang diterima dan membandingkannya -- ketidakcocokan menandakan terjadi kesalahan.",
 r"Parity check menambahkan satu bit agar jumlah total bit 1 mengikuti aturan tetap (genap atau ganjil); murah dan cepat, tetapi hanya andal mendeteksi jumlah kesalahan bit yang ganjil.",
 r"Contoh: data $1011000$ memiliki 3 bit 1 (ganjil), sehingga bit parity $P=1$ ditambahkan agar totalnya genap, menghasilkan codeword $10110001$.",
 r"Checksum membagi data menjadi blok tetap, menjumlahkannya secara aritmatika, dan mengirim hasil jumlah beserta data; mendeteksi lebih banyak pola kesalahan daripada satu bit parity, tetapi kesalahan yang saling meniadakan tetap bisa lolos.",
 r"Contoh: tiga blok 4-bit $1101,1011,0110$ dijumlahkan secara biner menjadi $11110$; jika melebihi ukuran blok, carry-nya dilingkarkan kembali (wrap-around), sama seperti prinsip checksum Internet.",
 r"CRC memperlakukan bit data sebagai polinomial dan membaginya (aritmatika XOR modulo-2) dengan polinomial generator tetap; sisa pembagian menjadi bit cek CRC, dan sisa nol pada penerima berarti tidak ada kesalahan terdeteksi.",
 r"Contoh: pesan $M=1101$ dengan generator $G=1011$ (derajat 3, tambah 3 bit nol) dibagi modulo-2 menghasilkan sisa $001$, sehingga codeword yang dikirim adalah $1101001$.",
 r"Kasus tanpa kesalahan: pembagian ulang menghasilkan sisa $000$ (codeword diterima). Kasus satu bit berubah: pembagian ulang menghasilkan sisa $010\neq000$, sehingga kesalahan terdeteksi.",
 r"Parity memiliki overhead terkecil (1 bit) tetapi deteksi terlemah; checksum overhead satu blok dengan deteksi sedang; CRC overhead tetap (misalnya 8/16/32 bit) dengan deteksi terkuat namun komputasi lebih berat.",
 r"Deteksi kesalahan hanya memberi tahu penerima bahwa terjadi kesalahan (sehingga bisa meminta transmisi ulang), sedangkan koreksi kesalahan (misalnya kode Hamming) memungkinkan penerima memperbaikinya langsung; sistem avionik umumnya memilih deteksi-saja demi keamanan.",
 r"Latihan: menghitung bit parity ganjil untuk data $1001100$, menentukan tindakan penerima saat checksum tidak cocok, dan menjelaskan mengapa CRC lebih andal daripada parity untuk kesalahan 2-bit.",
 r"ARINC 429 menyertakan bit parity, MIL-STD-1553 menambahkan parity per word plus pemeriksaan protokol, dan ARINC 664/AFDX modern menggunakan CRC seperti Ethernet standar; deteksi kesalahan wajib karena komputer penerbangan tidak boleh diam-diam menerima data sensor yang rusak.",
],
}
