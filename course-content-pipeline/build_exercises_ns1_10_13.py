#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Natural_Science_1 meetings 10-13,
in lectures/meeting<N>/exercise/ (separate from exercises/ assignment PDFs)."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"

MEETINGS = {
    10: {
        "topic": "Chemical Elements",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Name the three broad classes into which elements on the periodic table are grouped, and state one distinguishing physical property of each.",
             r"Sebutkan tiga golongan besar yang membagi unsur pada tabel periodik, dan sebutkan satu sifat fisik pembeda dari masing-masing.",
             r"\textbf{Metals} -- good electrical/thermal conductors, malleable, lustrous. \textbf{Non-metals} -- poor conductors (mostly insulators), brittle if solid. \textbf{Metalloids/semiconductors} -- intermediate electrical conductivity that can be controlled (e.g.\ by doping or temperature), between metals and non-metals.",
             r"\textbf{Logam} -- konduktor listrik/panas yang baik, dapat ditempa, berkilau. \textbf{Non-logam} -- konduktor buruk (kebanyakan insulator), rapuh jika padat. \textbf{Metaloid/semikonduktor} -- konduktivitas listrik menengah yang dapat dikendalikan (mis.\ lewat doping atau suhu), di antara logam dan non-logam."),
            ("Application",
             r"An aircraft skin panel is made from an aluminum alloy, while a microprocessor chip inside the avionics bay is built on silicon. Classify aluminum and silicon by element class, and justify each classification using one property relevant to its aerospace use.",
             r"Panel kulit pesawat dibuat dari paduan aluminium, sedangkan chip mikroprosesor di dalam ruang avionik dibangun di atas silikon. Klasifikasikan aluminium dan silikon berdasarkan golongan unsur, dan justifikasi masing-masing klasifikasi menggunakan satu sifat yang relevan dengan penggunaan aerospace-nya.",
             r"\textbf{Aluminum} is a \textbf{metal} -- its high strength-to-weight ratio combined with ductility (formability into skin panels) and good corrosion resistance (protective oxide layer) make it suitable for airframe structure. \textbf{Silicon} is a \textbf{metalloid/semiconductor} -- its electrical conductivity can be precisely controlled by doping, which is exactly the property required to build transistors and integrated circuits for avionics computers.",
             r"\textbf{Aluminium} adalah \textbf{logam} -- rasio kekuatan-terhadap-berat yang tinggi dikombinasikan dengan keuletan (dapat dibentuk menjadi panel kulit) dan ketahanan korosi yang baik (lapisan oksida pelindung) membuatnya cocok untuk struktur airframe. \textbf{Silikon} adalah \textbf{metaloid/semikonduktor} -- konduktivitas listriknya dapat dikendalikan secara presisi lewat doping, yang justru merupakan sifat yang dibutuhkan untuk membangun transistor dan integrated circuit bagi komputer avionik."),
            ("Analytical",
             r"Titanium alloys are chosen over aluminum alloys for hot-section engine components (e.g.\ compressor disks) despite titanium being denser and more expensive. Using periodic-table trends in melting point and metallic bonding strength, explain why titanium is the better choice for this specific application.",
             r"Paduan titanium dipilih dibanding paduan aluminium untuk komponen mesin bagian panas (mis.\ compressor disk) meskipun titanium lebih padat dan lebih mahal. Dengan menggunakan tren tabel periodik pada titik leleh dan kekuatan ikatan logam, jelaskan mengapa titanium adalah pilihan lebih baik untuk aplikasi spesifik ini.",
             r"Titanium sits further along the transition-metal series with stronger metallic bonding (more delocalized valence electrons contributing to the electron sea) than aluminum, a main-group metal. This gives titanium a much higher melting point ($\approx1668^\circ$C vs.\ aluminum's $\approx660^\circ$C) and it retains useful strength at high temperature, whereas aluminum alloys soften and lose strength well below typical hot-section operating temperatures. Even though titanium is denser and costlier, only its bonding-derived high-temperature strength makes it survive the engine's hot section, so the trade-off favors titanium there while aluminum remains preferred for the cooler airframe/skin.",
             r"Titanium berada lebih jauh dalam deret logam transisi dengan ikatan logam yang lebih kuat (lebih banyak elektron valensi terdelokalisasi menyumbang ke lautan elektron) dibanding aluminium, logam golongan utama. Hal ini memberi titanium titik leleh yang jauh lebih tinggi ($\approx1668^\circ$C vs.\ aluminium $\approx660^\circ$C) dan tetap mempertahankan kekuatan bergunanya pada suhu tinggi, sedangkan paduan aluminium melunak dan kehilangan kekuatan jauh di bawah suhu operasi khas bagian panas mesin. Meskipun titanium lebih padat dan lebih mahal, hanya kekuatan suhu tinggi yang berasal dari ikatannya yang membuatnya mampu bertahan di bagian panas mesin, sehingga trade-off tersebut menguntungkan titanium di sana sementara aluminium tetap dipilih untuk airframe/kulit yang lebih dingin."),
        ],
    },
    11: {
        "topic": "Structure of Atom \\& Molecule",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Define atomic number and mass number, and state what determines an atom's identity as a particular element.",
             r"Definisikan nomor atom dan nomor massa, dan sebutkan apa yang menentukan identitas suatu atom sebagai unsur tertentu.",
             r"\textbf{Atomic number ($Z$)} = number of protons in the nucleus. \textbf{Mass number ($A$)} = number of protons + neutrons. An atom's identity as a specific element is determined \textbf{solely by its atomic number} (proton count) -- atoms of the same element can have different mass numbers (isotopes) but never a different atomic number.",
             r"\textbf{Nomor atom ($Z$)} = jumlah proton dalam inti. \textbf{Nomor massa ($A$)} = jumlah proton + neutron. Identitas suatu atom sebagai unsur tertentu ditentukan \textbf{semata-mata oleh nomor atomnya} (jumlah proton) -- atom dari unsur yang sama dapat memiliki nomor massa berbeda (isotop) tetapi tidak pernah nomor atom yang berbeda."),
            ("Application",
             r"Sodium (electronegativity $\approx0.9$) reacts with chlorine (electronegativity $\approx3.0$). Predict the type of bond formed and briefly explain the electron-transfer/sharing mechanism.",
             r"Natrium (elektronegativitas $\approx0{,}9$) bereaksi dengan klorin (elektronegativitas $\approx3{,}0$). Prediksikan jenis ikatan yang terbentuk dan jelaskan secara singkat mekanisme transfer/pemakaian bersama elektronnya.",
             r"The electronegativity difference is large ($\approx2.1$), so an \textbf{ionic bond} forms: sodium transfers its single valence electron to chlorine, becoming $\text{Na}^+$, while chlorine gains that electron to complete its outer shell, becoming $\text{Cl}^-$; the resulting oppositely-charged ions attract electrostatically.",
             r"Selisih elektronegativitas besar ($\approx2{,}1$), sehingga terbentuk \textbf{ikatan ionik}: natrium mentransfer satu elektron valensinya ke klorin, menjadi $\text{Na}^+$, sementara klorin menerima elektron tersebut untuk melengkapi kulit terluarnya, menjadi $\text{Cl}^-$; ion-ion berlawanan muatan yang dihasilkan saling tarik-menarik secara elektrostatik."),
            ("Analytical",
             r"An aircraft uses aluminum skin panels fastened with steel bolts, and moisture is present at the joint in service. Using the concept of electron transfer between dissimilar metals, explain the electrochemical mechanism that causes galvanic corrosion at this joint, and identify which metal is preferentially attacked.",
             r"Sebuah pesawat menggunakan panel kulit aluminium yang disambung dengan baut baja, dan kelembapan hadir pada sambungan tersebut saat beroperasi. Dengan menggunakan konsep transfer elektron antar logam berbeda, jelaskan mekanisme elektrokimia yang menyebabkan korosi galvanik pada sambungan ini, dan identifikasi logam mana yang diserang secara preferensial.",
             r"When two dissimilar metals are in electrical contact with an electrolyte (here, moisture) bridging them, the more reactive (less noble) metal readily loses electrons -- oxidizes -- and those electrons flow through the metal-to-metal contact to the less reactive metal, where reduction reactions consume them. Aluminum is more reactive (more readily gives up electrons) than steel, so \textbf{aluminum is preferentially attacked} (corroded/oxidized) while acting as the sacrificial anode, and the steel bolt is relatively protected (acts as the cathode) -- this is exactly why insulating barriers or compatible fastener materials are required at aluminum-steel joints in aircraft structure.",
             r"Ketika dua logam berbeda berada dalam kontak listrik dengan elektrolit (di sini, kelembapan) yang menjembataninya, logam yang lebih reaktif (kurang mulia) dengan mudah kehilangan elektron -- teroksidasi -- dan elektron tersebut mengalir lewat kontak logam-ke-logam menuju logam yang kurang reaktif, di mana reaksi reduksi mengonsumsinya. Aluminium lebih reaktif (lebih mudah melepas elektron) dibanding baja, sehingga \textbf{aluminium diserang secara preferensial} (terkorosi/teroksidasi) sambil berperan sebagai anode korban, dan baut baja relatif terlindungi (berperan sebagai katode) -- inilah tepatnya mengapa penghalang isolasi atau material pengencang yang kompatibel dibutuhkan pada sambungan aluminium-baja di struktur pesawat."),
        ],
    },
    12: {
        "topic": "Crystals",
        "subcpmk": "Sub-CPMK 5",
        "cpmk": "CPMK-4 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Define a crystal lattice and a unit cell, and name the two most common cubic unit-cell structures found in metals.",
             r"Definisikan kisi kristal dan unit cell, dan sebutkan dua struktur unit cell kubik yang paling umum ditemukan pada logam.",
             r"A \textbf{crystal lattice} is the regular, repeating three-dimensional arrangement of atoms/ions throughout a crystalline solid. A \textbf{unit cell} is the smallest repeating group of atoms that, when translated in all directions, reproduces the entire lattice. The two most common cubic structures in metals are \textbf{body-centered cubic (BCC)} and \textbf{face-centered cubic (FCC)}.",
             r"\textbf{Kisi kristal} adalah susunan tiga dimensi atom/ion yang teratur dan berulang di seluruh padatan kristalin. \textbf{Unit cell} adalah kelompok atom terkecil yang berulang, yang jika ditranslasikan ke segala arah, mereproduksi seluruh kisi. Dua struktur kubik paling umum pada logam adalah \textbf{body-centered cubic (BCC)} dan \textbf{face-centered cubic (FCC)}."),
            ("Application",
             r"Aluminum crystallizes in a face-centered cubic (FCC) structure, which has a higher atomic packing factor ($\approx0.74$) than body-centered cubic ($\approx0.68$). State one mechanical-property consequence of this closer packing that is relevant to choosing aluminum for aircraft skin.",
             r"Aluminium mengkristal dalam struktur face-centered cubic (FCC), yang memiliki faktor pengemasan atom lebih tinggi ($\approx0{,}74$) dibanding body-centered cubic ($\approx0{,}68$). Sebutkan satu konsekuensi sifat mekanik dari pengemasan yang lebih rapat ini yang relevan untuk pemilihan aluminium sebagai kulit pesawat.",
             r"FCC structures have more closely-packed slip planes with more available slip systems, which generally gives FCC metals like aluminum \textbf{higher ductility} (better ability to be rolled/formed into thin sheet without cracking) compared to less densely packed structures -- directly useful for manufacturing formable aircraft skin panels.",
             r"Struktur FCC memiliki bidang slip yang lebih rapat dengan lebih banyak sistem slip yang tersedia, yang umumnya memberikan logam FCC seperti aluminium \textbf{keuletan (ductility) lebih tinggi} (kemampuan lebih baik untuk digulung/dibentuk menjadi lembaran tipis tanpa retak) dibanding struktur yang kurang rapat -- langsung berguna untuk memproduksi panel kulit pesawat yang dapat dibentuk."),
            ("Analytical",
             r"Two batches of the same aluminum alloy have identical chemical composition, but batch A has small, uniform crystal grains while batch B has large, irregular grains from slower cooling during manufacture. Explain, in terms of crystal defects (grain boundaries) and dislocation motion, why batch A is expected to exhibit better fatigue resistance for a wing-skin application.",
             r"Dua batch paduan aluminium yang sama memiliki komposisi kimia identik, tetapi batch A memiliki butir kristal kecil dan seragam sedangkan batch B memiliki butir besar dan tidak beraturan akibat pendinginan yang lebih lambat saat manufaktur. Jelaskan, dari segi cacat kristal (batas butir) dan pergerakan dislokasi, mengapa batch A diperkirakan menunjukkan ketahanan fatik yang lebih baik untuk aplikasi kulit sayap.",
             r"Grain boundaries are crystal defects that impede the motion of dislocations (the microscopic mechanism of plastic deformation), because a dislocation moving through one grain's lattice orientation cannot easily continue into a neighboring grain with a different orientation. A fine-grained structure (batch A) has \textbf{more grain boundary area per unit volume}, so dislocations are blocked more frequently and cyclic plastic deformation (the root cause of fatigue crack initiation) is suppressed more effectively than in the coarse-grained batch B, where dislocations can travel further within large grains before being stopped, promoting easier fatigue crack initiation and growth -- so batch A is preferred for a fatigue-critical wing skin.",
             r"Batas butir adalah cacat kristal yang menghambat pergerakan dislokasi (mekanisme mikroskopis deformasi plastis), karena dislokasi yang bergerak melalui orientasi kisi satu butir tidak dapat dengan mudah berlanjut ke butir tetangga dengan orientasi berbeda. Struktur berbutir halus (batch A) memiliki \textbf{luas batas butir per satuan volume yang lebih besar}, sehingga dislokasi lebih sering terhambat dan deformasi plastis siklik (penyebab utama inisiasi retak fatik) lebih efektif ditekan dibanding pada batch B yang berbutir kasar, di mana dislokasi dapat bergerak lebih jauh di dalam butir besar sebelum terhenti, mempermudah inisiasi dan perambatan retak fatik -- sehingga batch A lebih disukai untuk kulit sayap yang kritis terhadap fatik."),
        ],
    },
    13: {
        "topic": "Colloids",
        "subcpmk": "Sub-CPMK 6",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Define a colloid in terms of dispersed-particle size, and state how this size range distinguishes a colloid from both a true solution and a suspension.",
             r"Definisikan koloid dari segi ukuran partikel terdispersi, dan sebutkan bagaimana rentang ukuran ini membedakan koloid dari larutan sejati maupun suspensi.",
             r"A \textbf{colloid} has dispersed particles roughly \textbf{1--1000\,nm} in size. This is \textbf{larger} than the dissolved ions/molecules of a true solution ($<1$\,nm, which never settle and pass through filters/membranes) but \textbf{smaller} than the particles of a suspension ($>1000$\,nm, which settle out over time and are easily filtered).",
             r"\textbf{Koloid} memiliki partikel terdispersi berukuran kira-kira \textbf{1--1000\,nm}. Ukuran ini \textbf{lebih besar} dari ion/molekul terlarut pada larutan sejati ($<1$\,nm, yang tidak pernah mengendap dan dapat melewati filter/membran) tetapi \textbf{lebih kecil} dari partikel suspensi ($>1000$\,nm, yang mengendap seiring waktu dan mudah disaring)."),
            ("Application",
             r"Classify each of the following as the colloid type sol, emulsion, or aerosol, and briefly justify each: (a) aircraft de-icing fluid concentrate suspended as fine droplets while being sprayed into the air; (b) a paint consisting of solid pigment particles dispersed in a liquid binder.",
             r"Klasifikasikan masing-masing berikut sebagai jenis koloid sol, emulsi, atau aerosol, dan justifikasi secara singkat: (a) konsentrat cairan de-icing pesawat yang tersuspensi sebagai tetesan halus saat disemprotkan ke udara; (b) cat yang terdiri dari partikel pigmen padat terdispersi dalam pengikat cair.",
             r"(a) \textbf{Aerosol} -- liquid droplets dispersed in a gas (air) as the dispersion medium. (b) \textbf{Sol} -- solid particles (pigment) dispersed in a liquid dispersion medium (binder).",
             r"(a) \textbf{Aerosol} -- tetesan cairan terdispersi dalam gas (udara) sebagai medium dispersi. (b) \textbf{Sol} -- partikel padat (pigmen) terdispersi dalam medium dispersi cair (pengikat)."),
            ("Analytical",
             r"A fuel-quality inspector shines a narrow beam of light through two clear samples drawn from an aircraft fuel tank: sample A stays perfectly invisible with no visible beam path, while sample B shows a clearly visible, scattered light path through the liquid (both otherwise look clear to the naked eye). Using the Tyndall effect, explain what this test reveals about each sample, and what sample B's result most likely indicates about fuel contamination.",
             r"Seorang inspektur kualitas bahan bakar menyorotkan berkas cahaya sempit melalui dua sampel bening yang diambil dari tangki bahan bakar pesawat: sampel A tetap sepenuhnya tidak terlihat tanpa jejak berkas yang tampak, sedangkan sampel B menunjukkan jejak cahaya yang tersebar dan jelas terlihat melalui cairan tersebut (keduanya tampak bening bagi mata telanjang). Dengan menggunakan efek Tyndall, jelaskan apa yang diungkapkan uji ini tentang masing-masing sampel, dan apa yang paling mungkin ditunjukkan hasil sampel B mengenai kontaminasi bahan bakar.",
             r"The Tyndall effect is the scattering of light by dispersed particles in the colloidal size range (1--1000\,nm); a true solution's dissolved molecules are too small to scatter visible light, so the beam passes through invisibly. \textbf{Sample A} shows no visible beam path, indicating it is a \textbf{true solution} (no colloidal-sized particles present) -- consistent with clean, properly dissolved fuel. \textbf{Sample B} shows a clearly visible scattered beam, indicating the presence of \textbf{colloidal-sized particles} -- for aviation fuel this most likely indicates a \textbf{water-in-fuel emulsion or fine particulate/microbial contamination}, both of which are colloidal in scale and invisible to the naked eye but detectable by the Tyndall effect, making this a valuable fuel-quality screening test even when a sample looks visually clear.",
             r"Efek Tyndall adalah penghamburan cahaya oleh partikel terdispersi dalam rentang ukuran koloid (1--1000\,nm); molekul terlarut pada larutan sejati terlalu kecil untuk menghamburkan cahaya tampak, sehingga berkas cahaya lewat tanpa terlihat. \textbf{Sampel A} tidak menunjukkan jejak berkas yang terlihat, menandakan sampel tersebut adalah \textbf{larutan sejati} (tidak ada partikel berukuran koloid) -- sesuai dengan bahan bakar yang bersih dan terlarut dengan benar. \textbf{Sampel B} menunjukkan berkas cahaya yang tersebar dan jelas terlihat, menandakan keberadaan \textbf{partikel berukuran koloid} -- untuk bahan bakar penerbangan hal ini paling mungkin menandakan \textbf{emulsi air-dalam-bahan bakar atau kontaminasi partikulat/mikroba halus}, keduanya berskala koloid dan tidak terlihat mata telanjang tetapi terdeteksi oleh efek Tyndall, menjadikan ini uji penyaringan kualitas bahan bakar yang berharga meskipun sampel tampak bening secara visual."),
        ],
    },
}

if __name__ == "__main__":
    results = []
    for n, m in MEETINGS.items():
        tex = build_exercise_tex(COURSE_NAME, COURSE_CODE, n, m["topic"], m["subcpmk"], m["cpmk"], m["problems"])
        res = compile_exercise("Natural_Science_1", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
