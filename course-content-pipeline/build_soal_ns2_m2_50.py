#!/usr/bin/env python3
"""50-soal latihan drill sheet for Natural_Science_2 meeting 2
(Mechanics: Gaya dan Hukum Newton), mirroring the NS1 meeting-1
50-soal sheet (build_soal_ns1_m1_50.py), including worked examples
before each section's questions."""
import os, re, subprocess

COURSE = "Natural_Science_2"
COURSE_NAME = "Natural Science 2: Applied Physics"
COURSE_CODE = "AV0103BM"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Besaran Gaya, Massa, dan Percepatan (Satuan SI)", [
        (r"Nyatakan satuan SI untuk gaya.", r"Newton (N) $=$ kg$\cdot$m/s$^2$"),
        (r"Konversi $3.2$ kN menjadi N.", r"$3200$ N"),
        (r"Konversi $750$ g menjadi kg.", r"$0.75$ kg"),
        (r"Nyatakan gaya $45$ N dalam kN.", r"$0.045$ kN"),
        (r"Jabarkan satuan dasar dari $1$ N.", r"$1$ kg$\cdot$m/s$^2$"),
        (r"Konversi massa $2.3$ ton menjadi kg.", r"$2300$ kg"),
        (r"Gaya dorong mesin pesawat $12{,}000$ N. Nyatakan dalam kN.", r"$12$ kN"),
        (r"Konversi percepatan $5$ m/s$^2$ menjadi cm/s$^2$.", r"$500$ cm/s$^2$"),
    ]),
    ("B. Hukum Newton I (Kelembaman)", [
        (r"Balok diam ditarik dua gaya berlawanan arah masing-masing $15$ N. Tentukan resultan gayanya.", r"$0$ N (setimbang)"),
        (r"Jika resultan gaya pada benda sama dengan nol, apa yang terjadi pada kecepatan benda?", r"Tetap (konstan), tidak berubah"),
        (r"Benda bergerak lurus beraturan (GLB) memiliki percepatan sebesar ...", r"$0$ m/s$^2$"),
        (r"Gaya $20$ N ke kanan dan $20$ N ke kiri bekerja pada benda. Tentukan keadaan gerak benda.", r"Setimbang -- diam atau bergerak dengan kecepatan tetap"),
        (r"Kotak ditarik gaya $30$ N ke kanan dan gaya gesek $30$ N ke kiri. Hitung percepatan kotak.", r"$0$ m/s$^2$"),
        (r"Mengapa penumpang pesawat terdorong ke depan saat pesawat direm mendadak?", r"Karena kelembaman (inersia) tubuh mempertahankan keadaan geraknya"),
        (r"Benda bermassa $10$ kg diam di lantai (hanya gaya berat dan gaya normal). Tentukan resultan gaya vertikal.", r"$0$ N"),
        (r"Jika gaya total pada benda tidak nol, benda akan mengalami ...", r"Percepatan (kecepatannya berubah)"),
    ]),
    ("C. Hukum Newton II ($F=m\\cdot a$)", [
        (r"Benda bermassa $5$ kg diberi gaya $20$ N. Hitung percepatannya.", r"$a=4$ m/s$^2$"),
        (r"Benda bermassa $2$ kg mengalami percepatan $6$ m/s$^2$. Hitung gaya yang bekerja.", r"$F=12$ N"),
        (r"Gaya $50$ N menghasilkan percepatan $2.5$ m/s$^2$ pada suatu benda. Hitung massa benda.", r"$m=20$ kg"),
        (r"Mobil bermassa $1000$ kg dipercepat $2$ m/s$^2$ dari diam (abaikan gesekan). Hitung gaya mesin yang dibutuhkan.", r"$F=2000$ N"),
        (r"Dua gaya segaris searah $10$ N dan $15$ N bekerja pada benda bermassa $5$ kg. Hitung percepatan benda.", r"$a=5$ m/s$^2$"),
        (r"Benda bermassa $8$ kg, awalnya diam, mendapat gaya $40$ N selama $3$ s. Hitung kecepatan akhirnya.", r"$v=15$ m/s"),
    ]),
    ("D. Hukum Newton III (Aksi-Reaksi)", [
        (r"Tangan mendorong tembok dengan gaya $50$ N. Berapa besar gaya reaksi tembok terhadap tangan?", r"$50$ N, berlawanan arah"),
        (r"Roket terdorong maju karena gas panas disemburkan ke belakang. Sebutkan pasangan gaya aksi-reaksinya.", r"Aksi: roket mendorong gas ke belakang; reaksi: gas mendorong roket ke depan, sama besar berlawanan arah"),
        (r"Buku diletakkan di atas meja. Gaya reaksi pasangan dari gaya berat buku pada meja adalah ...", r"Gaya normal meja pada buku, sama besar berlawanan arah"),
        (r"Gaya aksi $80$ N bekerja antara dua benda yang bertumbukan. Berapa besar gaya reaksinya?", r"$80$ N"),
        (r"Apakah pasangan gaya aksi-reaksi bekerja pada benda yang sama atau benda yang berbeda?", r"Benda yang berbeda"),
        (r"Perenang mendorong air ke belakang dengan gaya $120$ N agar bergerak maju. Berapa gaya dorong air terhadap perenang?", r"$120$ N ke arah depan"),
    ]),
    ("E. Gaya Berat ($W=m\\cdot g$, $g=10$ m/s$^2$)", [
        (r"Hitung berat benda bermassa $5$ kg.", r"$W=50$ N"),
        (r"Berat suatu benda $150$ N. Hitung massanya.", r"$m=15$ kg"),
        (r"Astronot bermassa $70$ kg berada di bulan ($g_{bulan}=1.6$ m/s$^2$). Hitung beratnya di bulan.", r"$W=112$ N"),
        (r"Berat benda di Bumi $300$ N. Hitung massanya.", r"$m=30$ kg"),
        (r"Kotak bermassa $12$ kg diangkat dengan kecepatan tetap. Hitung gaya angkat minimum yang dibutuhkan.", r"$F=120$ N"),
        (r"Hitung berat benda bermassa $2.5$ kg.", r"$W=25$ N"),
        (r"Dua benda identik bermassa $4$ kg digabung. Hitung total berat gabungan.", r"$W=80$ N"),
        (r"Hitung massa benda yang beratnya $980$ N jika $g=9.8$ m/s$^2$.", r"$m=100$ kg"),
    ]),
    ("F. Gaya Gesek ($f=\\mu N$)", [
        (r"Benda bermassa $10$ kg ($g=10$) di lantai datar, $\mu=0.3$. Hitung gaya gesek maksimum.", r"$f=30$ N"),
        (r"Balok bermassa $5$ kg ditarik gaya $20$ N, gaya gesek $8$ N. Hitung percepatan balok.", r"$a=2.4$ m/s$^2$"),
        (r"Koefisien gesek statis $0.4$, gaya normal $50$ N. Hitung gaya gesek maksimum sebelum benda bergerak.", r"$f=20$ N"),
        (r"Benda bermassa $4$ kg ($g=10$), $\mu=0.25$. Hitung gaya geseknya.", r"$f=10$ N"),
        (r"Mobil mainan bermassa $2$ kg ditarik gaya $15$ N, gaya gesek $5$ N. Hitung percepatannya.", r"$a=5$ m/s$^2$"),
        (r"Mengapa gaya gesek berguna saat roda pesawat mendarat?", r"Menghasilkan gaya hambat untuk memperlambat laju pesawat"),
        (r"Koefisien gesek kinetis $0.2$, gaya normal $60$ N. Hitung gaya gesek kinetis.", r"$f=12$ N"),
        (r"Benda bermassa $6$ kg ($g=10$), $\mu=0.5$, ditarik gaya horizontal $40$ N. Hitung percepatan benda.", r"$a\approx1.67$ m/s$^2$"),
    ]),
    ("G. Resultan Gaya dan Percepatan pada Sistem", [
        (r"Dua gaya segaris searah $30$ N dan $20$ N bekerja pada benda bermassa $10$ kg. Hitung percepatan benda.", r"$a=5$ m/s$^2$"),
        (r"Dua gaya berlawanan arah $40$ N dan $25$ N bekerja pada benda bermassa $5$ kg. Hitung percepatan benda.", r"$a=3$ m/s$^2$"),
        (r"Benda bermassa $8$ kg ditarik gaya $50$ N, gaya gesek $10$ N melawan arah gerak. Hitung percepatan benda.", r"$a=5$ m/s$^2$"),
        (r"Tiga gaya segaris: $10$ N dan $15$ N searah, $5$ N berlawanan arah, pada benda bermassa $4$ kg. Hitung percepatannya.", r"$a=5$ m/s$^2$"),
        (r"Balok bermassa $15$ kg ditarik dua gaya berlawanan arah, masing-masing $60$ N. Hitung percepatan balok.", r"$a=0$ m/s$^2$"),
        (r"Benda A ($6$ kg) ditarik gaya $36$ N, terhubung tali dengan benda B ($3$ kg) di belakangnya (gesekan diabaikan). Hitung percepatan sistem.", r"$a=4$ m/s$^2$"),
    ]),
]

EXAMPLES = [
    (r"Konversi $4.8$ kN menjadi N.", [
        r"Ingat hubungan satuan: $1$ kN $= 1000$ N.",
        r"Kalikan nilai dengan faktor konversi: $4.8 \times 1000$.",
    ], r"$4800$ N"),
    (r"Balok ditarik gaya $25$ N ke kanan dan $25$ N ke kiri secara bersamaan pada bidang datar. Tentukan resultan gaya dan keadaan gerak balok.", [
        r"Jumlahkan gaya dengan memperhatikan arah: ke kanan $(+25$ N$)$ dan ke kiri $(-25$ N$)$.",
        r"Resultan $=25+(-25)=0$ N.",
        r"Karena resultan gaya nol, menurut Hukum Newton I balok tetap diam atau bergerak lurus beraturan.",
    ], r"Resultan $=0$ N; balok dalam keadaan setimbang"),
    (r"Balok bermassa $4$ kg didorong dengan gaya $12$ N pada permukaan licin (tanpa gesekan). Hitung percepatan balok.", [
        r"Gunakan Hukum Newton II: $F=m\times a$, sehingga $a=F/m$.",
        r"Substitusi nilai: $a=12/4$.",
    ], r"$a=3$ m/s$^2$"),
    (r"Seseorang mendorong dinding dengan gaya $60$ N. Tentukan besar dan arah gaya reaksi dinding terhadap tangan orang tersebut.", [
        r"Menurut Hukum Newton III, gaya aksi menghasilkan gaya reaksi yang sama besar namun berlawanan arah.",
        r"Gaya aksi $=60$ N (tangan mendorong dinding), sehingga gaya reaksi dinding terhadap tangan $=60$ N berlawanan arah.",
    ], r"$60$ N, berlawanan arah dengan gaya dorong"),
    (r"Peti bermassa $8$ kg berada di permukaan Bumi ($g=10$ m/s$^2$). Hitung berat peti tersebut.", [
        r"Gunakan rumus berat: $W=m\times g$.",
        r"Substitusi nilai: $W=8\times10$.",
    ], r"$W=80$ N"),
    (r"Balok bermassa $5$ kg ($g=10$ m/s$^2$) berada di lantai datar dengan koefisien gesek $\mu=0.2$. Hitung gaya gesek yang bekerja pada balok.", [
        r"Hitung gaya normal: $N=m\times g=5\times10=50$ N.",
        r"Hitung gaya gesek: $f=\mu\times N=0.2\times50$.",
    ], r"$f=10$ N"),
    (r"Dua gaya segaris bekerja pada benda bermassa $6$ kg: gaya $50$ N ke kanan dan gaya gesek $20$ N ke kiri. Hitung percepatan benda tersebut.", [
        r"Hitung resultan gaya: $F_{net}=50-20=30$ N.",
        r"Gunakan Hukum Newton II: $a=F_{net}/m=30/6$.",
    ], r"$a=5$ m/s$^2$"),
]

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.2cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{graphicx}
\usepackage{array,multirow,ragged2e}
\usepackage[table]{xcolor}
\usepackage{enumitem}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage{multicol}

\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\definecolor{lblgray}{gray}{0.94}
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
\newcommand{\lb}[1]{\cellcolor{lblgray}\bfseries #1}

\newcommand{\kiranalogo}{%
  \IfFileExists{_assets/icon/logo_politeknik_kirana.png}
    {\includegraphics[width=2.6cm,height=1.35cm,keepaspectratio]{_assets/icon/logo_politeknik_kirana.png}}
    {\framebox[2.6cm][c]{\rule[-0.65cm]{0pt}{1.35cm}\scriptsize LOGO}}}
"""


def build_tex():
    qnum = 0
    q_body = ""
    for (title, items), (ex_q, ex_steps, ex_ans) in zip(SECTIONS, EXAMPLES):
        q_body += r"\textbf{" + title + r"}\\[1mm]" + "\n"
        ex_steps_tex = "\n".join(r"\item " + s for s in ex_steps)
        q_body += (
            r"\noindent\colorbox{lblgray}{\begin{minipage}{0.96\linewidth}\vspace{1mm}"
            + r"\textbf{Contoh:} " + ex_q + r"\\[1mm]"
            + r"\textit{Penyelesaian:}"
            + r"\begin{enumerate}[label=Langkah \arabic*:,leftmargin=*,itemsep=1pt]"
            + ex_steps_tex
            + r"\end{enumerate}"
            + r"\textbf{Jawaban:} " + ex_ans
            + r"\vspace{1mm}\end{minipage}}" + "\n\\vspace{3mm}\n\n"
        )
        q_body += r"\begin{enumerate}[label=\textbf{\arabic*.},leftmargin=*,itemsep=4pt,start=" + str(qnum + 1) + r"]" + "\n"
        for q, _ in items:
            qnum += 1
            q_body += r"\item " + q + "\n"
        q_body += r"\end{enumerate}" + "\n\\vspace{2mm}\n"

    knum = 0
    k_body = r"\begin{multicols}{3}" + "\n" + r"\begin{enumerate}[label=\textbf{\arabic*.},leftmargin=*,itemsep=2pt]" + "\n"
    for title, items in SECTIONS:
        for _, a in items:
            knum += 1
            k_body += r"\item " + a + "\n"
    k_body += r"\end{enumerate}" + "\n" + r"\end{multicols}" + "\n"

    tex = PREAMBLE + r"""
\begin{document}
\begin{tabular}{|C{2.7cm}|L{9.8cm}|L{3.5cm}|}
\hline
\multirow{4}{*}{\kiranalogo} & \multirow{4}{*}{\begin{minipage}{9.6cm}\centering
  {\large\bfseries SOAL LATIHAN (50 NOMOR)}\\[1mm]
  {\small PROGRAM STUDI TEKNIK REKAYASA AERONAUTIKA -- POLITEKNIK KIRANA}
\end{minipage}} & \lb{Mata Kuliah / Course} \\ \cline{3-3}
 & & """ + COURSE_NAME + r""" \\ \cline{3-3}
 & & \lb{Kode / SKS} \\ \cline{3-3}
 & & """ + COURSE_CODE + r""" / 3 \\ \hline
\end{tabular}

\vspace{3mm}
\begin{tabular}{|L{3.4cm}|L{12.6cm}|}
\hline
\lb{Pertemuan} & 2 \\ \hline
\lb{Topik} & Physics: Mekanika -- Gaya dan Hukum Newton \\ \hline
\lb{Sub-CPMK} & Mampu menerapkan Hukum Newton (I, II, III) untuk menganalisis gaya, berat, dan gaya gesek pada benda. \\ \hline
\lb{Capaian} & CPMK-1 (CPL-1) \\ \hline
\end{tabular}

\vspace{4mm}
\textbf{Petunjuk:}
\begin{itemize}[nosep]
\item Latihan mandiri -- kerjakan tanpa melihat kunci jawaban terlebih dahulu.
\item Gunakan $g=10$ m/s$^2$ kecuali dinyatakan lain pada soal.
\item Kunci jawaban tersedia di halaman terakhir untuk mengecek hasil pekerjaan sendiri.
\end{itemize}

\vspace{2mm}
""" + q_body + r"""
\clearpage
\textbf{\large Kunci Jawaban}
\vspace{2mm}

""" + k_body + r"""
\vfill
\hrule
\vspace{1mm}
{\small Dosen Pengampu: """ + LECTURER + r""" \hfill Politeknik Kirana}

\end{document}
"""
    return tex


def compile_tex(tex):
    d = f"{COURSES_ROOT}/{COURSE}/lectures/meeting2/exercise"
    os.makedirs(d, exist_ok=True)
    fname = "soal_latihan_50"
    with open(f"{d}/{fname}.tex", "w") as f:
        f.write(tex)
    link = f"{d}/_assets"
    if not os.path.islink(link):
        os.symlink("../../../../_assets", link)
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{fname}.tex"],
                        cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pdf = f"{d}/{fname}.pdf"
    lp = f"{d}/{fname}.log"
    errs = []
    if os.path.exists(lp):
        txt = open(lp, errors="ignore").read()
        errs = re.findall(r"^! .*", txt, re.M)
    ok = os.path.exists(pdf) and os.path.getsize(pdf) > 0 and not errs
    size = os.path.getsize(pdf) if os.path.exists(pdf) else 0
    return {"ok": ok, "size_kb": size // 1024, "errors": errs[:5], "pdf": pdf}


if __name__ == "__main__":
    tex = build_tex()
    result = compile_tex(tex)
    print(result)
