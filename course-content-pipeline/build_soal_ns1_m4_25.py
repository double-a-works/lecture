#!/usr/bin/env python3
"""25-soal latihan drill sheet for Natural_Science_1 meeting 4
(Matematika: Trigonometri) -- trimmed version of build_soal_ns1_m4_50.py,
keeping the first N items per section (25 total), with worked examples
before each section's questions. Saved as soal_latihan_25.tex."""
import os, re, subprocess

COURSE = "Natural_Science_1"
COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Rasio Trigonometri Dasar (SOH-CAH-TOA)", [
        (r"Segitiga siku-siku memiliki sisi depan $3$\,cm dan sisi miring $5$\,cm. Tentukan $\sin\theta$.", r"$\dfrac{3}{5}=0{,}6$"),
        (r"Segitiga siku-siku memiliki sisi samping $4$\,cm dan sisi miring $5$\,cm. Tentukan $\cos\theta$.", r"$\dfrac{4}{5}=0{,}8$"),
        (r"Segitiga siku-siku memiliki sisi depan $3$\,cm dan sisi samping $4$\,cm. Tentukan $\tan\theta$.", r"$\dfrac{3}{4}=0{,}75$"),
        (r"Diketahui $\sin\theta=0{,}6$ dan sisi miring $=10$\,cm. Berapa panjang sisi depan?", r"$6$\,cm"),
    ]),
    ("B. Konversi Derajat ke Radian", [
        (r"Ubah $30^\circ$ menjadi radian.", r"$\dfrac{\pi}{6}$"),
        (r"Ubah $45^\circ$ menjadi radian.", r"$\dfrac{\pi}{4}$"),
        (r"Ubah $90^\circ$ menjadi radian.", r"$\dfrac{\pi}{2}$"),
    ]),
    ("C. Nilai Trigonometri Sudut Istimewa", [
        (r"Tentukan $\sin 30^\circ$.", r"$\dfrac{1}{2}$"),
        (r"Tentukan $\cos 30^\circ$.", r"$\dfrac{\sqrt{3}}{2}$"),
        (r"Tentukan $\tan 45^\circ$.", r"$1$"),
        (r"Tentukan $\sin 60^\circ$.", r"$\dfrac{\sqrt{3}}{2}$"),
    ]),
    ("D. Identitas Trigonometri Dasar", [
        (r"Jika $\sin\theta=0{,}6$ ($\theta$ lancip), tentukan $\cos\theta$ menggunakan $\sin^2\theta+\cos^2\theta=1$.", r"$0{,}8$"),
        (r"Jika $\cos\theta=\dfrac{5}{13}$ ($\theta$ lancip), tentukan $\sin\theta$.", r"$\dfrac{12}{13}$"),
        (r"Sederhanakan $\dfrac{\sin\theta}{\cos\theta}$.", r"$\tan\theta$"),
    ]),
    ("E. Lingkaran Satuan (Unit Circle)", [
        (r"Titik pada lingkaran satuan bersudut $0^\circ$ berkoordinat berapa?", r"$(1,0)$"),
        (r"Titik pada lingkaran satuan bersudut $90^\circ$ berkoordinat berapa?", r"$(0,1)$"),
        (r"Titik pada lingkaran satuan bersudut $45^\circ$ berkoordinat berapa?", r"$\left(\dfrac{\sqrt{2}}{2},\dfrac{\sqrt{2}}{2}\right)$"),
    ]),
    ("F. Menyelesaikan Segitiga Siku-siku", [
        (r"Segitiga siku-siku memiliki sudut $30^\circ$ dan sisi miring $10$\,cm. Carilah sisi di depan sudut tersebut.", r"$5$\,cm"),
        (r"Segitiga siku-siku memiliki sudut $60^\circ$ dan sisi miring $8$\,cm. Carilah sisi di samping sudut tersebut.", r"$4$\,cm"),
        (r"Segitiga siku-siku memiliki sisi depan $6$\,cm dan sudut $30^\circ$ di hadapannya. Carilah sisi miring.", r"$12$\,cm"),
        (r"Segitiga siku-siku memiliki sisi depan $5$\,cm dan sisi samping $5$\,cm. Carilah besar sudutnya (selain $90^\circ$).", r"$45^\circ$ pada kedua sudut lancip"),
    ]),
    ("G. Aplikasi Trigonometri dalam Teknik", [
        (r"Dari jarak $50$\,m, sudut elevasi puncak menara adalah $30^\circ$. Berapa tinggi menara?", r"$\dfrac{50}{\sqrt3}\approx28{,}87$\,m"),
        (r"Seorang pengamat di ketinggian $100$\,m melihat sebuah objek dengan sudut depresi $45^\circ$. Berapa jarak horizontal ke objek?", r"$100$\,m"),
        (r"Sebuah tangga sepanjang $6$\,m disandarkan ke dinding membentuk sudut $60^\circ$ terhadap lantai. Berapa tinggi tangga mencapai dinding?", r"$3\sqrt3\approx5{,}20$\,m"),
        (r"Sebuah kapal berlayar sejauh $20$\,km dengan arah bearing $60^\circ$ dari titik keberangkatan. Berapa jarak komponen ke arah timur dari titik keberangkatan?", r"$20\sin60^\circ=10\sqrt3\approx17{,}32$\,km"),
    ]),
]

EXAMPLES = [
    (r"Segitiga siku-siku memiliki sisi depan $6$\,cm dan sisi miring $10$\,cm. Tentukan $\sin\theta$ dan $\cos\theta$.", [
        r"Cari sisi samping dengan Pythagoras: $\sqrt{10^2-6^2}=\sqrt{64}=8$\,cm.",
        r"$\sin\theta=\dfrac{\text{depan}}{\text{miring}}=\dfrac{6}{10}=0{,}6$.",
        r"$\cos\theta=\dfrac{\text{samping}}{\text{miring}}=\dfrac{8}{10}=0{,}8$.",
    ], r"$\sin\theta=0{,}6$, $\cos\theta=0{,}8$"),
    (r"Ubah $120^\circ$ menjadi radian.", [
        r"Gunakan rumus radian $=$ derajat $\times \dfrac{\pi}{180}$.",
        r"Radian $=120\times\dfrac{\pi}{180}=\dfrac{2\pi}{3}$.",
    ], r"$\dfrac{2\pi}{3}$"),
    (r"Tentukan nilai $\tan 30^\circ$.", [
        r"Gunakan $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$.",
        r"$\tan30^\circ=\dfrac{1/2}{\sqrt3/2}=\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}\approx0{,}577$.",
    ], r"$\dfrac{\sqrt3}{3}\approx0{,}577$"),
    (r"Jika $\cos\theta=0{,}6$ ($\theta$ lancip), tentukan $\sin\theta$ menggunakan identitas Pythagoras.", [
        r"$\sin^2\theta=1-\cos^2\theta=1-0{,}36=0{,}64$.",
        r"$\sin\theta=\sqrt{0{,}64}=0{,}8$.",
    ], r"$0{,}8$"),
    (r"Tentukan koordinat titik pada lingkaran satuan bersudut $30^\circ$.", [
        r"Koordinat $x=\cos30^\circ=\dfrac{\sqrt3}{2}$.",
        r"Koordinat $y=\sin30^\circ=\dfrac{1}{2}$.",
    ], r"$\left(\dfrac{\sqrt3}{2},\dfrac{1}{2}\right)$"),
    (r"Segitiga siku-siku memiliki sudut $30^\circ$ dan sisi miring $12$\,cm. Carilah sisi di depan sudut tersebut.", [
        r"Sisi depan $=$ sisi miring $\times\sin\theta$.",
        r"Sisi depan $=12\times\sin30^\circ=12\times0{,}5=6$\,cm.",
    ], r"$6$\,cm"),
    (r"Dari jarak $40$\,m, sudut elevasi puncak sebuah tiang pemancar adalah $30^\circ$. Berapa tinggi tiang?", [
        r"$\tan\theta=\dfrac{\text{tinggi}}{\text{jarak}}$, sehingga tinggi $=$ jarak $\times\tan\theta$.",
        r"Tinggi $=40\times\tan30^\circ=40\times\dfrac{\sqrt3}{3}\approx23{,}09$\,m.",
    ], r"$\approx23{,}09$\,m"),
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


HEADER = r"""\begin{tabular}{|C{2.7cm}|L{9.8cm}|L{3.5cm}|}
\hline
\multirow{4}{*}{\kiranalogo} & \multirow{4}{*}{\begin{minipage}{9.6cm}\centering
  {\large\bfseries %TITLE% (25 NOMOR)}\\[1mm]
  {\small PROGRAM STUDI TEKNIK REKAYASA AERONAUTIKA -- POLITEKNIK KIRANA}
\end{minipage}} & \lb{Mata Kuliah / Course} \\ \cline{3-3}
 & & """ + COURSE_NAME + r""" \\ \cline{3-3}
 & & \lb{Kode / SKS} \\ \cline{3-3}
 & & """ + COURSE_CODE + r""" / 3 \\ \hline
\end{tabular}

\vspace{3mm}
\begin{tabular}{|L{3.4cm}|L{12.6cm}|}
\hline
\lb{Pertemuan} & 4 \\ \hline
\lb{Topik} & Mathematics: Trigonometri \\ \hline
\lb{Sub-CPMK} & Mampu memformulasikan parameter ruang dan sudut menggunakan prinsip geometri dan trigonometri. \\ \hline
\lb{Capaian} & CPMK-2 (CPL-1) \\ \hline
\end{tabular}

\vspace{4mm}
"""

FOOTER = r"""\vfill
\hrule
\vspace{1mm}
{\small Dosen Pengampu: """ + LECTURER + r""" \hfill Politeknik Kirana}

\end{document}
"""


def build_soal_tex():
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

    tex = PREAMBLE + r"""
\begin{document}
""" + HEADER.replace("%TITLE%", "SOAL LATIHAN") + r"""
\textbf{Petunjuk:}
\begin{itemize}[nosep]
\item Latihan mandiri -- kerjakan tanpa melihat kunci jawaban terlebih dahulu.
\item Kunci jawaban disediakan pada berkas terpisah.
\end{itemize}

\vspace{2mm}
""" + q_body + "\n" + FOOTER
    return tex


def build_kunci_tex():
    k_body = r"\begin{multicols}{3}" + "\n" + r"\begin{enumerate}[label=\textbf{\arabic*.},leftmargin=*,itemsep=2pt]" + "\n"
    for title, items in SECTIONS:
        for _, a in items:
            k_body += r"\item " + a + "\n"
    k_body += r"\end{enumerate}" + "\n" + r"\end{multicols}" + "\n"

    tex = PREAMBLE + r"""
\begin{document}
""" + HEADER.replace("%TITLE%", "KUNCI JAWABAN") + r"""
\vspace{2mm}
""" + k_body + "\n" + FOOTER
    return tex


def compile_tex(tex, fname):
    d = f"{COURSES_ROOT}/{COURSE}/lectures/meeting4/exercise"
    os.makedirs(d, exist_ok=True)
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
    r1 = compile_tex(build_soal_tex(), "soal_latihan_25")
    r2 = compile_tex(build_kunci_tex(), "kunci_jawaban_25")
    print("SOAL:", r1)
    print("KUNCI:", r2)
