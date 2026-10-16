#!/usr/bin/env python3
"""Build bilingual practice-exercise PDFs for Digital_Technic_Data meetings
10-13, into lectures/meetingN/exercise/ (separate from exercises/ assignment
folder). Reuses build_exercises.py's template verbatim."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Digital Technic: Digital Data Transmission"
COURSE_CODE = "AV0303DT"

MEETINGS = {
 10: {
  "topic": "Tabung Sinar Katoda (CRT): Struktur \\& Prinsip",
  "subcpmk": "Sub-CPMK 4",
  "cpmk": "CPMK-3 (CPL-3)",
  "problems": [
   ("Foundational",
    r"List the four major functional blocks of a CRT in the order the electron beam passes through them, from emission to the visible spot.",
    r"Sebutkan empat blok fungsional utama CRT sesuai urutan yang dilalui berkas elektron, dari emisi hingga titik cahaya.",
    r"(1) Electron gun (cathode/heater, control grid, focusing \& accelerating anodes), (2) vacuum envelope enclosing the whole path, (3) deflection system, (4) phosphor screen.",
    r"(1) Electron gun (katode/heater, control grid, focusing \& accelerating anode), (2) envelope vakum yang membungkus seluruh jalur, (3) sistem deflection, (4) layar fosfor."),
   ("Application",
    r"A CRT's control-grid voltage is made more negative than before. Explain what happens to the beam current and to screen brightness, and name the phenomenon that occurs if the grid voltage is negative enough.",
    r"Tegangan control grid sebuah CRT dibuat lebih negatif dari sebelumnya. Jelaskan apa yang terjadi pada arus berkas dan kecerahan layar, dan sebutkan fenomena yang terjadi jika tegangan grid cukup negatif.",
    r"More negative grid voltage repels more electrons back toward the cathode, reducing beam current and therefore reducing brightness; if negative enough, the beam is cut off completely (blanking).",
    r"Tegangan grid yang lebih negatif menolak lebih banyak elektron kembali ke katode, sehingga arus berkas berkurang dan kecerahan menurun; jika cukup negatif, berkas terputus sepenuhnya (blanking)."),
   ("Analytical",
    r"A bench CRT (oscilloscope) needs very fast, precise beam positioning, while a large weather-radar CRT display prioritizes robustness over speed. Which deflection method (electrostatic or electromagnetic) is better suited to each, and why?",
    r"CRT osiloskop di bengkel membutuhkan pemosisian berkas yang sangat cepat dan presisi, sedangkan display radar cuaca besar mengutamakan keandalan dibanding kecepatan. Metode deflection mana (elektrostatik atau elektromagnetik) yang lebih cocok untuk masing-masing, dan mengapa?",
    r"The oscilloscope should use electrostatic deflection (parallel plates) because it responds fast enough for precise, high-speed tracing; the radar display typically uses electromagnetic deflection (yoke coils) since it can produce larger deflection angles for a bigger screen, trading some speed for a more compact/robust neck design.",
    r"Osiloskop sebaiknya memakai deflection elektrostatik (pelat paralel) karena responsnya cukup cepat untuk penjejakan presisi dan berkecepatan tinggi; display radar umumnya memakai deflection elektromagnetik (kumparan yoke) karena mampu menghasilkan sudut pembelokan lebih besar untuk layar yang lebih lebar, dengan trade-off kecepatan demi desain leher tabung yang lebih ringkas/tahan."),
  ],
 },
 11: {
  "topic": "CRT: Pembentukan Citra \\& Aplikasi",
  "subcpmk": "Sub-CPMK 4",
  "cpmk": "CPMK-3 (CPL-3)",
  "problems": [
   ("Foundational",
    r"Describe the four steps of raster scanning, in order, that turn a single moving dot into a full image.",
    r"Deskripsikan empat langkah raster scanning secara berurutan yang mengubah satu titik bergerak menjadi gambar penuh.",
    r"(1) Sweep left to right across one line (trace), (2) rapid horizontal retrace back to the left edge, (3) step down one line and repeat, (4) after the last line, rapid vertical retrace to the top-left corner to start the next frame.",
    r"(1) Menyapu dari kiri ke kanan pada satu baris (trace), (2) horizontal retrace cepat kembali ke tepi kiri, (3) turun satu baris dan mengulang, (4) setelah baris terakhir, vertical retrace cepat ke pojok kiri-atas untuk memulai frame berikutnya."),
   ("Application",
    r"A CRT display has a refresh rate that drops well below its normal 60 Hz due to a fault. Describe what a viewer would perceive, and explain the underlying phosphor-related reason.",
    r"Sebuah display CRT mengalami penurunan refresh rate jauh di bawah 60 Hz normalnya akibat gangguan. Deskripsikan apa yang akan dirasakan penonton, dan jelaskan alasan yang berkaitan dengan fosfor.",
    r"The viewer perceives flicker -- the image appears to pulse/blink rather than stay steady -- because the phosphor's glow (persistence) decays noticeably before the next frame refreshes it.",
    r"Penonton merasakan flicker -- gambar tampak berkedip/berdenyut, bukan stabil -- karena cahaya fosfor (persistence) meluruh cukup jauh sebelum frame berikutnya menyegarkannya kembali."),
   ("Analytical",
    r"In a color CRT, the shadow mask becomes slightly misaligned (poor convergence) after a hard landing shock during ground testing. Explain the visible symptom on screen and why it happens, tracing the fault back to how the shadow mask normally works.",
    r"Pada CRT berwarna, shadow mask sedikit bergeser (convergence buruk) setelah guncangan pendaratan keras saat uji darat. Jelaskan gejala yang tampak di layar dan mengapa hal itu terjadi, kaitkan dengan cara kerja normal shadow mask.",
    r"Normally each mask hole lets only the correct-color gun strike its matching phosphor dot; if misaligned, beams strike the wrong-color dots, so the display shows color fringing/inaccurate colors, especially visible at the edges of bright shapes.",
    r"Normalnya setiap lubang mask hanya meloloskan gun warna yang sesuai ke titik fosfor pasangannya; jika bergeser, berkas menumbuk titik warna yang salah, sehingga layar menampilkan color fringing/warna tidak akurat, terutama terlihat di tepi bentuk yang terang."),
  ],
 },
 12: {
  "topic": "Piranti Peka Muatan Elektrostatik (ESD)",
  "subcpmk": "Sub-CPMK 5",
  "cpmk": "CPMK-4 (CPL-4)",
  "problems": [
   ("Foundational",
    r"Define electrostatic discharge (ESD) and name two types of components that are especially ESD-sensitive.",
    r"Definisikan electrostatic discharge (ESD) dan sebutkan dua jenis komponen yang sangat peka terhadap ESD.",
    r"ESD is the sudden, uncontrolled flow of charge between two objects at different electrostatic potentials, triggered by contact or a strong field. CMOS ICs (very thin gate-oxide layers) and MOSFETs (insulated gate punctured by small voltage spikes) are especially ESD-sensitive.",
    r"ESD adalah aliran muatan mendadak dan tak terkendali antara dua benda berpotensial elektrostatik berbeda, dipicu kontak atau medan kuat. IC CMOS (lapisan gate-oxide sangat tipis) dan MOSFET (gerbang berinsulasi yang bisa tertembus lonjakan tegangan kecil) sangat peka ESD."),
   ("Application",
    r"A technician slides a spare circuit card out of its foam packaging on a dry day. Identify the charge-generation mechanism at work and explain why dry air makes it worse.",
    r"Seorang teknisi menggeser kartu sirkuit cadangan keluar dari kemasan busanya pada hari yang kering. Identifikasi mekanisme pembangkitan muatan yang terjadi dan jelaskan mengapa udara kering memperparahnya.",
    r"This is the triboelectric effect -- friction/contact between the card and foam transfers electrons between the two surfaces. Dry air lacks the conductive moisture path that would otherwise continuously bleed off small static charges, so charge accumulates to much higher levels before discharging.",
    r"Ini adalah efek triboelektrik -- gesekan/kontak antara kartu dan busa memindahkan elektron antar permukaan. Udara kering tidak memiliki jalur konduktif dari kelembapan yang biasanya membuang muatan statis kecil secara terus-menerus, sehingga muatan menumpuk jauh lebih tinggi sebelum terjadi discharge."),
   ("Analytical",
    r"An avionics LRU containing a CMOS microprocessor is touched briefly by an ungrounded technician, receives a small ESD event well below the human sensory threshold, and later passes its post-installation functional test. Explain why this scenario is more dangerous in aviation than an ESD event that destroys the part outright, and name the failure mode involved.",
    r"Sebuah LRU avionik berisi mikroprosesor CMOS tersentuh sesaat oleh teknisi yang tidak ter-ground, menerima kejadian ESD kecil jauh di bawah ambang rasa manusia, dan kemudian lolos uji fungsional pasca-pemasangan. Jelaskan mengapa skenario ini lebih berbahaya dalam penerbangan dibanding kejadian ESD yang langsung merusak komponen total, dan sebutkan mode kegagalan yang terlibat.",
    r"This is a latent defect: the part is only partially weakened, so it passes initial testing and is returned to service, but the degraded structure can fail unpredictably later -- potentially in flight -- unlike a catastrophic failure which is caught immediately because the part simply does not work.",
    r"Ini adalah cacat laten: komponen hanya melemah sebagian sehingga lolos uji awal dan dikembalikan ke layanan, namun strukturnya yang terdegradasi bisa gagal tak terduga kemudian -- berpotensi saat terbang -- berbeda dengan kegagalan katastrofik yang langsung terdeteksi karena komponen langsung tidak berfungsi."),
  ],
 },
 13: {
  "topic": "Prosedur Penanganan \\& Proteksi ESD",
  "subcpmk": "Sub-CPMK 5",
  "cpmk": "CPMK-4 (CPL-4)",
  "problems": [
   ("Foundational",
    r"Explain why a wrist strap's grounding cord includes a current-limiting resistor instead of connecting the technician directly to ground with a bare wire.",
    r"Jelaskan mengapa kabel grounding wrist strap menyertakan resistor pembatas arus, bukan menghubungkan teknisi langsung ke ground dengan kawat telanjang.",
    r"The resistor (typically around 1 M-ohm) limits current to a safe level if the technician accidentally contacts a live circuit, protecting them from electrical shock, while still allowing static charge to bleed off slowly and safely.",
    r"Resistor (biasanya sekitar 1 M-ohm) membatasi arus ke tingkat aman jika teknisi tidak sengaja menyentuh rangkaian bertegangan, melindungi dari sengatan listrik, sambil tetap membiarkan muatan statis terbuang perlahan dan aman."),
   ("Application",
    r"A technician wears a correctly connected wrist strap but stands on an ordinary carpeted floor while working. Is this technician fully ESD-protected? Justify your answer.",
    r"Seorang teknisi memakai wrist strap yang tersambung dengan benar namun berdiri di lantai berkarpet biasa saat bekerja. Apakah teknisi ini sudah terlindungi ESD sepenuhnya? Jelaskan alasannya.",
    r"No -- the wrist strap only grounds the hands. Ordinary carpet is a strong static generator and is not grounded, so the technician's body can still build up charge through the feet, and an ungrounded floor undermines the overall EPA.",
    r"Tidak -- wrist strap hanya men-ground tangan. Karpet biasa adalah penghasil statis yang kuat dan tidak di-ground, sehingga tubuh teknisi tetap bisa membangun muatan lewat kaki, dan lantai yang tidak di-ground merusak keseluruhan EPA."),
   ("Analytical",
    r"A plastic connector cover (an insulator) on an avionics test bench becomes charged during handling. Explain why a grounded work-surface mat alone cannot discharge it, and describe the mechanism by which an ionizer solves this problem.",
    r"Penutup konektor plastik (isolator) di meja uji avionik menjadi bermuatan saat ditangani. Jelaskan mengapa mat kerja yang di-ground saja tidak dapat membuang muatannya, dan deskripsikan mekanisme ionizer mengatasi masalah ini.",
    r"A grounded mat can only drain charge from conductive objects touching it; an insulator's surface charge has no conductive path to flow through. An ionizer generates a balanced cloud of positive and negative air ions near the surface, and the charged insulator attracts ions of the opposite polarity from the air, neutralizing it without needing a conductive path.",
    r"Mat yang di-ground hanya dapat membuang muatan dari benda konduktif yang menyentuhnya; muatan pada permukaan isolator tidak memiliki jalur konduktif untuk mengalir. Ionizer menghasilkan awan ion positif dan negatif seimbang di dekat permukaan, dan permukaan isolator yang bermuatan menarik ion berpolaritas berlawanan dari udara, menetralkannya tanpa memerlukan jalur konduktif."),
  ],
 },
}

if __name__ == "__main__":
    results = []
    for n, m in MEETINGS.items():
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Digital_Technic_Data", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {n}: {res['size_kb']} KB errors={res['errors']}")
