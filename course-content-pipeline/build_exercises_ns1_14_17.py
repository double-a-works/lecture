#!/usr/bin/env python3
"""Bilingual practice-exercise PDFs for Natural_Science_1 meetings 14-17,
in lectures/meeting<N>/exercise/, following exercise_content.py's NS1 pattern
(course code AV0102BM). CPMK-5 covers the solutions/materials chemistry
block per the course's 2026-09-14 CPL mapping (all NS1 CPMK -> CPL-1)."""
from build_exercises import build_exercise_tex, compile_exercise

COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"

MEETINGS = {
    14: {
        "topic": "Chemistry: Solutions and Solvents",
        "subcpmk": "Mampu mengkarakterisasi larutan, pelarut, dan konsentrasi.",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Compute the molarity of a solution containing 0.8 mol of solute in 1.6 L of solution.",
             r"Hitung molaritas larutan yang mengandung 0,8 mol solut dalam 1,6 L larutan.",
             r"$M=0.8/1.6=0.5$ mol/L.",
             r"$M=0{,}8/1{,}6=0{,}5$ mol/L."),
            ("Application",
             r"12 g of salt is dissolved to make 240 g of solution total. Find the mass percent concentration, then determine how many grams of salt would be needed to make 600 g of solution at the same concentration.",
             r"12 g garam dilarutkan hingga total larutan 240 g. Cari konsentrasi persen massa, lalu tentukan berapa gram garam dibutuhkan untuk membuat 600 g larutan pada konsentrasi yang sama.",
             r"Mass percent $=12/240\times100\%=5\%$. For 600 g at 5\%: $0.05\times600=30$ g of salt.",
             r"Persen massa $=12/240\times100\%=5\%$. Untuk 600 g pada 5\%: $0{,}05\times600=30$ g garam."),
            ("Analytical",
             r"A technician needs to dilute a 5 M stock solution down to 0.5 M to make 2 L of working solution. Compute the volume of stock solution required, and explain (using the polarity/solubility factors from this meeting) why this dilution works reliably for an ionic solute in water but would not work the same way for a non-polar solute in water.",
             r"Seorang teknisi harus mengencerkan larutan stok 5 M menjadi 0,5 M untuk membuat 2 L larutan kerja. Hitung volume larutan stok yang dibutuhkan, dan jelaskan (memakai faktor polaritas/kelarutan dari pertemuan ini) mengapa pengenceran ini bekerja andal untuk solut ionik dalam air tetapi tidak akan bekerja sama untuk solut non-polar dalam air.",
             r"$M_1V_1=M_2V_2 \Rightarrow (5)V_1=(0.5)(2) \Rightarrow V_1=0.2$ L. This dilution works reliably for an ionic solute because water (a polar solvent) fully dissolves ionic/polar solutes at essentially any concentration below saturation (\"like dissolves like\"), so simply adding solvent proportionally lowers concentration. A non-polar solute would not dissolve appreciably in water in the first place, so there would be no true solution to dilute -- the stock solution itself could not exist as a stable homogeneous mixture.",
             r"$M_1V_1=M_2V_2\Rightarrow(5)V_1=(0{,}5)(2)\Rightarrow V_1=0{,}2$ L. Pengenceran ini bekerja andal untuk solut ionik karena air (pelarut polar) sepenuhnya melarutkan solut ionik/polar pada hampir semua konsentrasi di bawah titik jenuh (\"like dissolves like\"), sehingga menambah pelarut secara proporsional menurunkan konsentrasi. Solut non-polar tidak akan larut signifikan dalam air sejak awal, sehingga tidak ada larutan sejati untuk diencerkan -- larutan stok itu sendiri tidak bisa ada sebagai campuran homogen yang stabil."),
        ],
    },
    15: {
        "topic": "Chemistry: Hardness of Materials",
        "subcpmk": "Mampu mengevaluasi properti mekanis material rekayasa (kekerasan).",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"Name the three hardness testing methods covered this meeting and one distinguishing feature of each.",
             r"Sebutkan tiga metode uji kekerasan yang dibahas pertemuan ini dan satu ciri pembeda masing-masing.",
             r"Brinell -- steel/carbide ball indenter, measures indent diameter. Rockwell -- reads indenter depth under load directly on a dial. Vickers -- diamond pyramid indenter, precise for thin or very hard samples.",
             r"Brinell -- indenter bola baja/karbida, mengukur diameter indentasi. Rockwell -- membaca kedalaman indenter di bawah beban langsung pada dial. Vickers -- indenter piramida intan, presisi untuk sampel tipis atau sangat keras."),
            ("Application",
             r"Two aircraft skin candidate materials are tested: Material A shows a small, shallow indent under a standard hardness test; Material B shows a large, deep indent. Which material is harder, and what does this suggest about their relative wear resistance?",
             r"Dua material kandidat kulit pesawat diuji: Material A menunjukkan indentasi kecil dan dangkal pada uji kekerasan standar; Material B menunjukkan indentasi besar dan dalam. Material mana yang lebih keras, dan apa yang ini menunjukkan tentang ketahanan aus relatif keduanya?",
             r"Material A is harder -- a smaller, shallower indent means it resisted surface indentation more strongly. Harder materials generally resist wear (scratching, abrasion) better, so Material A would be expected to have better wear resistance than Material B.",
             r"Material A lebih keras -- indentasi yang lebih kecil dan dangkal berarti ia lebih kuat menahan indentasi permukaan. Material yang lebih keras umumnya lebih tahan aus (goresan, abrasi), sehingga Material A diperkirakan memiliki ketahanan aus lebih baik dibanding Material B."),
            ("Analytical",
             r"A designer increases the hardness of a landing-gear component via heat treatment to improve wear resistance. Explain the trade-off this likely introduces (referencing the hardness-ductility-brittleness relationship from this meeting), and why this trade-off matters specifically for a landing-gear part that experiences repeated impact loading.",
             r"Seorang perancang meningkatkan kekerasan komponen landing gear lewat perlakuan panas untuk memperbaiki ketahanan aus. Jelaskan trade-off yang kemungkinan ditimbulkan (merujuk hubungan kekerasan-duktilitas-kegetasan dari pertemuan ini), dan mengapa trade-off ini penting khususnya untuk bagian landing gear yang mengalami beban benturan berulang.",
             r"Increasing hardness via heat treatment generally reduces ductility and increases brittleness -- the material resists indentation and wear better, but becomes less able to deform plastically to absorb impact energy, fracturing more easily under sudden loads instead. This matters critically for a landing-gear component because it repeatedly absorbs high-impact loads on touchdown; if hardened too far, it gains wear resistance but risks brittle fracture under the very impact loading it must survive, so the heat treatment must be balanced rather than maximized.",
             r"Menaikkan kekerasan lewat perlakuan panas umumnya menurunkan duktilitas dan meningkatkan kegetasan -- material lebih tahan indentasi dan aus, tapi menjadi kurang mampu berdeformasi plastis untuk menyerap energi benturan, sehingga lebih mudah patah di bawah beban mendadak. Ini krusial untuk komponen landing gear karena berulang kali menyerap beban benturan tinggi saat mendarat; jika terlalu dikeraskan, ia mendapat ketahanan aus tapi berisiko patah getas di bawah beban benturan yang justru harus ia tahan, sehingga perlakuan panas harus diseimbangkan, bukan dimaksimalkan."),
        ],
    },
    16: {
        "topic": "Chemistry: Ductility of Materials",
        "subcpmk": "Mampu mengevaluasi properti mekanis material rekayasa (duktilitas).",
        "cpmk": "CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"A metal sample 150 mm long is stretched to 159 mm before it fractures. Compute its \% elongation.",
             r"Sampel logam sepanjang 150 mm diregangkan hingga 159 mm sebelum patah. Hitung \% elongasinya.",
             r"\% elongation $=(159-150)/150\times100\%=6\%$.",
             r"\% elongasi $=(159-150)/150\times100\%=6\%$."),
            ("Application",
             r"During a tensile test, Sample P shows 2\% elongation before fracture and Sample Q shows 18\% elongation before fracture. Classify each sample as ductile or brittle, and state which would be preferred for a part that must bend slightly under load without cracking.",
             r"Selama uji tarik, Sampel P menunjukkan elongasi 2\% sebelum patah dan Sampel Q menunjukkan elongasi 18\% sebelum patah. Klasifikasikan tiap sampel sebagai duktil atau getas, dan sebutkan mana yang lebih disukai untuk bagian yang harus sedikit menekuk di bawah beban tanpa retak.",
             r"Sample P (2\% elongation) is brittle; Sample Q (18\% elongation) is ductile. Sample Q would be preferred for a part that must bend slightly under load without cracking, since its high ductility lets it deform plastically instead of fracturing.",
             r"Sampel P (elongasi 2\%) adalah getas; Sampel Q (elongasi 18\%) adalah duktil. Sampel Q lebih disukai untuk bagian yang harus sedikit menekuk di bawah beban tanpa retak, karena duktilitasnya yang tinggi memungkinkannya berdeformasi plastis alih-alih patah."),
            ("Analytical",
             r"A fuselage skin panel must survive both a sudden bird-strike impact and continuous cyclic pressurization/depressurization over the aircraft's life. Explain why a highly ductile aluminium alloy is generally chosen over a harder but more brittle alternative for this role, connecting your answer to the tensile-test concepts (\% elongation, plastic deformation) from this meeting.",
             r"Panel kulit fuselage harus bertahan dari benturan burung mendadak sekaligus tekanan/depresurisasi siklik terus-menerus sepanjang usia pesawat. Jelaskan mengapa paduan aluminium yang sangat duktil umumnya dipilih dibanding alternatif yang lebih keras tapi lebih getas untuk peran ini, hubungkan jawaban Anda dengan konsep uji tarik (\% elongasi, deformasi plastis) dari pertemuan ini.",
             r"A ductile aluminium alloy can absorb a sudden bird-strike impact by deforming plastically (a measurable \% elongation) rather than fracturing outright, and its ability to yield slightly under repeated cyclic stress from pressurization cycles reduces the risk of brittle crack initiation over time. A harder, more brittle alternative would resist scratching/wear better but would be far more likely to crack or shatter under either the sudden impact or the repeated cyclic loading, since it lacks the plastic-deformation margin that ductility provides -- making ductility, not hardness, the priority property for this structural role.",
             r"Paduan aluminium yang duktil bisa menyerap benturan burung mendadak dengan berdeformasi plastis (elongasi \% yang terukur) alih-alih langsung patah, dan kemampuannya menekuk sedikit di bawah tegangan siklik berulang dari siklus pressurisasi mengurangi risiko munculnya retak getas seiring waktu. Alternatif yang lebih keras dan getas akan lebih tahan goresan/aus tapi jauh lebih mungkin retak atau pecah di bawah benturan mendadak maupun beban siklik berulang, karena tidak memiliki margin deformasi plastis yang diberikan duktilitas -- menjadikan duktilitas, bukan kekerasan, sebagai properti prioritas untuk peran struktural ini."),
        ],
    },
    17: {
        "topic": "Chemistry Review \\& Problem Solving",
        "subcpmk": "Mampu mengintegrasikan konsep kimia dan material (Pertemuan 10--16) untuk persiapan UAS.",
        "cpmk": "CPMK-3, CPMK-4, CPMK-5 (CPL-1)",
        "problems": [
            ("Foundational",
             r"List the six chemistry/materials topic areas covered by Meetings 10--15 that feed into this final review.",
             r"Sebutkan enam area topik kimia/material dari Pertemuan 10--15 yang menjadi bahan review akhir ini.",
             r"Elements/periodic table (M10), atomic/molecular bonding (M11), crystal structure (M12), colloids/mixtures (M13), solutions/concentration (M14), hardness/ductility (M15).",
             r"Unsur/tabel periodik (P10), ikatan atom/molekul (P11), struktur kristal (P12), koloid/campuran (P13), larutan/konsentrasi (P14), kekerasan/duktilitas (P15)."),
            ("Application",
             r"A 3 M stock solution is diluted from 400 mL to 1.2 L. Find the new molarity, then classify the resulting mixture as a true solution or colloid if the solute particles are approximately 0.3 nm in size.",
             r"Larutan stok 3 M diencerkan dari 400 mL menjadi 1,2 L. Cari molaritas baru, lalu klasifikasikan campuran hasil sebagai larutan sejati atau koloid jika partikel solutnya berukuran sekitar 0,3 nm.",
             r"$M_1V_1=M_2V_2 \Rightarrow (3)(0.4)=M_2(1.2) \Rightarrow M_2=1$ M. At 0.3 nm, the particles are far below the 1--1000 nm colloidal range, so this is a true solution, not a colloid.",
             r"$M_1V_1=M_2V_2\Rightarrow(3)(0{,}4)=M_2(1{,}2)\Rightarrow M_2=1$ M. Pada 0,3 nm, partikel jauh di bawah rentang koloid 1--1000 nm, sehingga ini adalah larutan sejati, bukan koloid."),
            ("Analytical",
             r"Two candidate alloys for a wing spar are compared: Alloy X has metallic bonding with an FCC crystal structure and 15\% elongation; Alloy Y has metallic bonding with a BCC crystal structure and 4\% elongation. Using the bonding-structure-property-application chain emphasized in this review, recommend which alloy is better suited for the spar and justify each link in the chain.",
             r"Dua paduan kandidat untuk spar sayap dibandingkan: Paduan X berikatan logam dengan struktur kristal FCC dan elongasi 15\%; Paduan Y berikatan logam dengan struktur kristal BCC dan elongasi 4\%. Memakai rantai ikatan-struktur-properti-aplikasi yang ditekankan dalam review ini, rekomendasikan paduan mana yang lebih cocok untuk spar dan justifikasi tiap mata rantai.",
             r"\textbf{Bonding:} both are metallically bonded (delocalized electrons), giving both good electrical/thermal conductivity, so bonding alone does not differentiate them here. \textbf{Structure:} Alloy X's FCC structure has more close-packed slip systems than Alloy Y's BCC structure, generally enabling easier plastic deformation. \textbf{Property:} this is confirmed by the tensile-test data -- Alloy X's 15\% elongation indicates good ductility versus Alloy Y's 4\% (closer to brittle behaviour). \textbf{Application:} a wing spar experiences significant cyclic and impact loading in flight, so \textbf{Alloy X is the better choice} -- its FCC structure and high ductility let it absorb stress by deforming rather than cracking, which is safety-critical for a primary structural member.",
             r"\textbf{Ikatan:} keduanya berikatan logam (elektron terdelokalisasi), memberi keduanya konduktivitas listrik/termal yang baik, sehingga ikatan saja tidak membedakan keduanya di sini. \textbf{Struktur:} struktur FCC Paduan X memiliki lebih banyak sistem slip rapat dibanding struktur BCC Paduan Y, umumnya memungkinkan deformasi plastis lebih mudah. \textbf{Properti:} ini dikonfirmasi oleh data uji tarik -- elongasi 15\% Paduan X menunjukkan duktilitas baik dibanding 4\% Paduan Y (lebih mendekati perilaku getas). \textbf{Aplikasi:} spar sayap mengalami beban siklik dan benturan signifikan saat terbang, sehingga \textbf{Paduan X adalah pilihan lebih baik} -- struktur FCC dan duktilitas tingginya memungkinkannya menyerap tegangan dengan berdeformasi alih-alih retak, yang kritis bagi keselamatan untuk anggota struktural utama."),
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
        res = compile_exercise("Natural_Science_1", n, tex)
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']} exercise: {res['size_kb']} KB errors={res['errors']}")
