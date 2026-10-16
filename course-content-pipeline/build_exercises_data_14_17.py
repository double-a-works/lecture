#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Digital_Technic_Data meetings 14-17,
in lectures/meeting<N>/exercise/, following the build_exercises_data_10_13.py
pattern. CPMK/CPL labels follow the 2026-09-14 revised mapping (see MEMORY.md):
CPMK-5 (fiber optics + software management control) -> CPL-1."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Digital Technic: Digital Data Transmission"
COURSE_CODE = "AV0303DT"

MEETINGS = {
    14: {
        "topic": "Transmisi Serat Optik (Fiber Optics)",
        "subcpmk": "Mampu menjelaskan prinsip pemantulan internal total dan komponen sistem transmisi serat optik.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"A fiber has core index $n_1=1.50$ and cladding index $n_2=1.45$. Compute the critical angle $\theta_c$.",
             r"Sebuah serat memiliki indeks core $n_1=1{,}50$ dan indeks cladding $n_2=1{,}45$. Hitung sudut kritis $\theta_c$.",
             r"$\theta_c=\sin^{-1}(n_2/n_1)=\sin^{-1}(1.45/1.50)=\sin^{-1}(0.9667)\approx75.2^\circ$.",
             r"$\theta_c=\sin^{-1}(n_2/n_1)=\sin^{-1}(1{,}45/1{,}50)=\sin^{-1}(0{,}9667)\approx75{,}2^\circ$."),
            ("Application",
             r"A fiber has $n_1=1.46$, $n_2=1.44$. Compute its numerical aperture (NA) and maximum acceptance angle $\theta_{max}$.",
             r"Sebuah serat memiliki $n_1=1{,}46$, $n_2=1{,}44$. Hitung numerical aperture (NA) dan sudut penerimaan maksimum $\theta_{max}$.",
             r"$NA=\sqrt{1.46^2-1.44^2}=\sqrt{2.1316-2.0736}=\sqrt{0.058}\approx0.241$. $\theta_{max}=\sin^{-1}(0.241)\approx13.9^\circ$.",
             r"$NA=\sqrt{1{,}46^2-1{,}44^2}=\sqrt{2{,}1316-2{,}0736}=\sqrt{0{,}058}\approx0{,}241$. $\theta_{max}=\sin^{-1}(0{,}241)\approx13{,}9^\circ$."),
            ("Analytical",
             r"An avionics designer must link two equipment bays 500 meters apart at very high data rate, versus a short 2-meter link inside a single equipment rack. Recommend single-mode or multi-mode fiber for each case, and justify using the modal-dispersion and cost trade-offs from this meeting.",
             r"Seorang perancang avionik harus menghubungkan dua bay peralatan berjarak 500 meter dengan laju data sangat tinggi, dibandingkan tautan pendek 2 meter di dalam satu rak peralatan. Rekomendasikan serat single-mode atau multi-mode untuk masing-masing kasus, dan justifikasi memakai trade-off dispersi modal dan biaya dari pertemuan ini.",
             r"\textbf{500m high-speed link:} single-mode fiber -- no modal dispersion means the signal stays clean over the long distance at high bandwidth, which is exactly what the long backbone link needs, despite the higher cost of laser sources and tighter alignment. \textbf{2m rack-internal link:} multi-mode fiber -- the distance is far too short for modal dispersion to matter, so the cheaper LED sources and looser alignment tolerances of MMF are the more cost-effective choice.",
             r"\textbf{Tautan 500m berkecepatan tinggi:} serat single-mode -- tanpa dispersi modal, sinyal tetap bersih pada jarak jauh dengan bandwidth tinggi, persis kebutuhan tautan backbone panjang, meski biaya sumber laser dan toleransi keselarasan lebih ketat. \textbf{Tautan 2m dalam rak:} serat multi-mode -- jarak terlalu pendek untuk dispersi modal menjadi masalah, sehingga sumber LED yang lebih murah dan toleransi keselarasan MMF yang lebih longgar menjadi pilihan yang lebih hemat biaya."),
        ],
    },
    15: {
        "topic": "Serat Optik: Keunggulan \\& Aplikasi Avionik",
        "subcpmk": "Mampu menjelaskan keunggulan serat optik dan penerapannya pada jaringan data pesawat.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"State two of the four advantages of fiber optics over copper covered this meeting.",
             r"Sebutkan dua dari empat keunggulan serat optik dibanding tembaga yang dibahas pertemuan ini.",
             r"Any two of: EMI immunity, weight savings, higher bandwidth, and better tap resistance (security).",
             r"Sebutkan dua dari: kekebalan EMI, penghematan bobot, bandwidth lebih tinggi, dan ketahanan sadap lebih baik (keamanan)."),
            ("Application",
             r"A cable route runs directly alongside a high-power AC generator bus. Which fiber advantage is most directly relevant, and why would copper be the worse choice here?",
             r"Jalur kabel berjalan tepat di samping bus generator AC berdaya tinggi. Keunggulan serat mana yang paling relevan, dan mengapa tembaga menjadi pilihan lebih buruk di sini?",
             r"EMI immunity is most relevant. Copper wiring near a high-power AC bus would act like an antenna, picking up induced interference that corrupts the digital signal, while the fiber's light-based signal is completely unaffected by the nearby electromagnetic field.",
             r"Kekebalan EMI paling relevan. Kabel tembaga dekat bus AC berdaya tinggi akan bertindak seperti antena, menangkap interferensi terinduksi yang merusak sinyal digital, sementara sinyal serat berbasis cahaya sama sekali tidak terpengaruh medan elektromagnetik terdekat."),
            ("Analytical",
             r"A technician must splice a damaged fiber run inside an aircraft equipment bay during a time-limited maintenance window, and the route includes a tight bend around a structural member. Identify the two maintenance risks most relevant here (from splicing and bend radius) and the correct action for each.",
             r"Seorang teknisi harus menyambung jalur serat yang rusak di dalam bay peralatan pesawat selama jendela perawatan terbatas waktu, dan rute tersebut mencakup tikungan ketat di sekitar elemen struktural. Identifikasi dua risiko perawatan paling relevan di sini (dari splicing dan radius bengkok) dan tindakan yang benar untuk masing-masing.",
             r"\textbf{Splicing risk:} a rushed or misaligned splice (fusion or mechanical) introduces excess signal loss -- the correct action is to use a fusion splice for the lowest, most reliable loss and verify alignment before finalizing, even under time pressure. \textbf{Bend radius risk:} routing the fiber tighter than its minimum bend radius around the structural member causes bend loss (and possible microcracking) -- the correct action is to route the cable with a gentler curve or use a bend-tolerant fiber rated for the tighter radius, never force it past the specified minimum.",
             r"\textbf{Risiko splicing:} sambungan yang terburu-buru atau tidak sejajar (fusion atau mekanis) menghasilkan rugi sinyal berlebih -- tindakan benar adalah memakai fusion splice untuk rugi paling rendah dan andal serta memverifikasi keselarasan sebelum menyelesaikannya, meski di bawah tekanan waktu. \textbf{Risiko radius bengkok:} merutekan serat lebih ketat dari radius bengkok minimumnya di sekitar elemen struktural menyebabkan rugi bengkokan (dan potensi retak mikro) -- tindakan benar adalah merutekan kabel dengan lengkungan lebih landai atau memakai serat tahan-bengkok yang dirancang untuk radius lebih ketat, jangan pernah memaksakannya melebihi minimum yang ditentukan."),
        ],
    },
    16: {
        "topic": "Software Management Control",
        "subcpmk": "Mampu menjelaskan prinsip kendali konfigurasi dan verifikasi perangkat lunak avionik.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"List the five steps of the software management control cycle covered this meeting, in order.",
             r"Sebutkan lima langkah siklus kendali manajemen perangkat lunak yang dibahas pertemuan ini, secara berurutan.",
             r"Identify (part no./version) $\to$ Approve (change control) $\to$ Load (LSAP procedure) $\to$ Verify (checksum/CRC) $\to$ Record (maintenance log).",
             r"Identifikasi (nomor part/versi) $\to$ Persetujuan (kendali perubahan) $\to$ Pemuatan (prosedur LSAP) $\to$ Verifikasi (checksum/CRC) $\to$ Pencatatan (log perawatan)."),
            ("Application",
             r"After loading an LSAP onto an avionics LRU, the readback checksum does not match the expected published value. What is the correct next action, and what must NOT be done?",
             r"Setelah memuat LSAP ke LRU avionik, checksum hasil baca-ulang tidak sesuai dengan nilai terpublikasi yang diharapkan. Apa tindakan yang benar berikutnya, dan apa yang TIDAK boleh dilakukan?",
             r"Correct action: treat the load as failed/incomplete, re-attempt the load from a verified source, and re-check the checksum before proceeding. \textbf{Must not:} return the unit to service on the assumption that it \"probably loaded fine\" -- an unverified load could contain a defect that only appears under a specific flight condition.",
             r"Tindakan benar: perlakukan pemuatan sebagai gagal/tidak lengkap, coba ulang pemuatan dari sumber yang terverifikasi, dan periksa ulang checksum sebelum melanjutkan. \textbf{Tidak boleh:} mengembalikan unit ke layanan dengan asumsi \"kemungkinan sudah termuat dengan baik\" -- pemuatan yang tidak terverifikasi bisa mengandung cacat yang hanya muncul pada kondisi penerbangan tertentu."),
            ("Analytical",
             r"Two avionics functions are being certified: a cockpit display formatting function (DAL C) and a flight-control law function (DAL A). Explain why the flight-control function requires a far more rigorous software management control process than the display formatting function.",
             r"Dua fungsi avionik sedang disertifikasi: fungsi pemformatan display kokpit (DAL C) dan fungsi hukum kendali penerbangan (DAL A). Jelaskan mengapa fungsi kendali penerbangan membutuhkan proses kendali manajemen perangkat lunak yang jauh lebih ketat dibanding fungsi pemformatan display.",
             r"Design Assurance Level reflects failure consequence severity: DAL A means a software defect could cause a catastrophic outcome (loss of aircraft), while DAL C means at most a major (but not catastrophic) consequence. Because an undetected defect in the DAL A flight-control function has far higher safety stakes, DO-178C mandates much more rigorous identification, change control, verification, and traceability for it than for the lower-criticality DAL C display function.",
             r"Design Assurance Level mencerminkan keparahan konsekuensi kegagalan: DAL A berarti cacat perangkat lunak bisa menyebabkan hasil katastrofik (kehilangan pesawat), sementara DAL C berarti konsekuensi paling parah adalah mayor (bukan katastrofik). Karena cacat yang tidak terdeteksi pada fungsi kendali penerbangan DAL A memiliki taruhan keselamatan jauh lebih tinggi, DO-178C mewajibkan identifikasi, kendali perubahan, verifikasi, dan ketertelusuran yang jauh lebih ketat untuknya dibanding fungsi display DAL C yang kekritisannya lebih rendah."),
        ],
    },
    17: {
        "topic": "Review \\& Latihan Terpadu (Pra-UAS)",
        "subcpmk": "Mampu mengintegrasikan CRT, ESD, serat optik, dan kendali manajemen perangkat lunak sebagai persiapan UAS.",
        "cpmk": "CPMK-3 (CPL-1), CPMK-4 (CPL-5), CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"List the four topic blocks covered by the final exam (Meetings 10--16) in this course.",
             r"Sebutkan empat blok topik yang dicakup ujian akhir (Pertemuan 10--16) mata kuliah ini.",
             r"CRT (M10--11), ESD-sensitive device handling (M12--13), fiber optics (M14--15), software management control (M16).",
             r"CRT (P10--11), penanganan perangkat sensitif ESD (P12--13), serat optik (P14--15), kendali manajemen perangkat lunak (P16)."),
            ("Application",
             r"A maintenance report describes an avionics display that flickers intermittently, and separately notes that a software update was recently loaded on the same unit without documented verification. Which of these two facts is more likely the root cause of a flicker artifact, and why?",
             r"Laporan perawatan mendeskripsikan display avionik yang berkedip sebentar-sebentar, dan secara terpisah mencatat bahwa pembaruan perangkat lunak baru-baru ini dimuat pada unit yang sama tanpa verifikasi terdokumentasi. Fakta mana dari keduanya yang lebih mungkin menjadi akar penyebab artefak kedipan, dan mengapa?",
             r"Flicker is a CRT/display-timing artifact (phosphor persistence and refresh rate), not typically a software-load symptom -- an unverified software load is a serious safety/traceability risk, but it is the wrong category of cause for a visual flicker unless the software directly controls refresh timing. The more likely root cause is a CRT/display hardware or refresh-rate issue; the undocumented software load is a separate, independently serious finding that must still be investigated and corrected.",
             r"Kedipan adalah artefak pewaktuan CRT/display (persistensi fosfor dan refresh rate), bukan gejala khas pemuatan perangkat lunak -- pemuatan perangkat lunak tak terverifikasi adalah risiko keselamatan/ketertelusuran serius, tapi merupakan kategori penyebab yang salah untuk kedipan visual kecuali perangkat lunak tersebut langsung mengendalikan pewaktuan refresh. Akar penyebab yang lebih mungkin adalah masalah perangkat keras CRT/display atau refresh rate; pemuatan perangkat lunak tak terdokumentasi adalah temuan terpisah yang tetap serius dan harus tetap diselidiki serta dikoreksi."),
            ("Analytical",
             r"A new cabin data link must run 300 meters through an area with both high EMI (near generators) and tight bend routing (around structural frames), and must also carry a software-controlled display feed that requires DAL C certification. Integrate this meeting's topics: recommend a cable type, note the physical installation constraint to respect, and state what software control step is mandatory before the display feed goes live.",
             r"Tautan data kabin baru harus berjalan 300 meter melewati area dengan EMI tinggi (dekat generator) dan rute tikungan ketat (di sekitar rangka struktural), dan juga harus membawa feed display yang dikendalikan perangkat lunak yang membutuhkan sertifikasi DAL C. Integrasikan topik pertemuan ini: rekomendasikan jenis kabel, catat batasan instalasi fisik yang harus dihormati, dan sebutkan langkah kendali perangkat lunak yang wajib sebelum feed display aktif.",
             r"\textbf{Cable:} fiber optic, since it is immune to the nearby generator EMI and copper would not be. \textbf{Installation constraint:} respect the fiber's minimum bend radius at every tight turn around the structural frames to avoid bend loss or link failure. \textbf{Software step:} the DAL C display-control software must go through the full software management control cycle -- identified part number/version, approved change control, loaded via the LSAP procedure, and verified by checksum/CRC readback -- before the unit is returned to service.",
             r"\textbf{Kabel:} serat optik, karena kebal terhadap EMI generator terdekat sementara tembaga tidak. \textbf{Batasan instalasi:} hormati radius bengkok minimum serat di setiap tikungan ketat di sekitar rangka struktural untuk menghindari rugi bengkokan atau kegagalan tautan. \textbf{Langkah perangkat lunak:} perangkat lunak kendali display DAL C harus melalui siklus kendali manajemen perangkat lunak penuh -- nomor part/versi teridentifikasi, kendali perubahan disetujui, dimuat lewat prosedur LSAP, dan diverifikasi lewat pembacaan checksum/CRC -- sebelum unit dikembalikan ke layanan."),
        ],
    },
}

if __name__ == "__main__":
    import sys
    meetings = [int(x) for x in sys.argv[1:]] or list(MEETINGS.keys())
    results = []
    for n in meetings:
        m = MEETINGS[n]
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Digital_Technic_Data", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
