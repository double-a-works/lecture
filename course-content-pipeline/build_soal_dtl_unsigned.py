#!/usr/bin/env python3
"""20-soal latihan drill sheet for Digital_Technic_Logic (unsigned number
systems: decimal<->binary, binary<->octal, binary<->hex, octal/hex<->decimal,
range of unsigned numbers), mirroring build_soal_ns1_m3_20.py, including
worked examples before each section's questions. Covers Meeting 1-2 material
(all unsigned). Saved as soal_latihan_unsigned.tex in meeting2/exercise."""
import os, re, subprocess

COURSE = "Digital_Technic_Logic"
COURSE_NAME = "Digital Technic: Digital Logic Fundamentals and Introduction to Microcomputers"
COURSE_CODE = "AV0301DT"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Desimal ke Biner (Metode Pembagian)", [
        (r"Konversikan $37_{10}$ ke biner.", r"$100101_2$"),
        (r"Konversikan $100_{10}$ ke biner.", r"$1100100_2$"),
    ]),
    ("B. Biner ke Desimal (Bobot Posisi)", [
        (r"Konversikan $110101_2$ ke desimal.", r"$53_{10}$"),
        (r"Konversikan $11001010_2$ ke desimal.", r"$202_{10}$"),
    ]),
    ("C. Pecahan Desimal ke Biner", [
        (r"Konversikan $0.75_{10}$ ke biner (4 digit pecahan).", r"$0.1100_2$"),
        (r"Konversikan $0.3125_{10}$ ke biner.", r"$0.0101_2$"),
    ]),
    ("D. Biner ke Oktal (Kelompok 3 Bit)", [
        (r"Konversikan $11001101_2$ ke oktal.", r"$315_8$"),
        (r"Konversikan $101110_2$ ke oktal.", r"$56_8$"),
    ]),
    ("E. Biner ke Heksadesimal (Kelompok 4 Bit)", [
        (r"Konversikan $11001101_2$ ke heksadesimal.", r"$CD_{16}$"),
        (r"Konversikan $101110_2$ ke heksadesimal.", r"$2E_{16}$"),
    ]),
    ("F. Oktal/Hex ke Desimal", [
        (r"Konversikan $254_8$ ke desimal.", r"$172_{10}$"),
        (r"Konversikan $9A_{16}$ ke desimal.", r"$154_{10}$"),
        (r"Konversikan $B7_{16}$ ke desimal.", r"$183_{10}$"),
    ]),
    ("G. Desimal ke Heksadesimal (Pembagian 16)", [
        (r"Konversikan $500_{10}$ ke heksadesimal menggunakan metode pembagian.", r"$1F4_{16}$"),
        (r"Konversikan $91_{10}$ ke heksadesimal.", r"$5B_{16}$"),
    ]),
    ("H. Rentang Bilangan Unsigned n-bit", [
        (r"Berapa rentang nilai bilangan unsigned 6-bit?", r"$0$ sampai $63$"),
        (r"Berapa rentang nilai bilangan unsigned 10-bit?", r"$0$ sampai $1023$"),
    ]),
]

EXAMPLES = [
    (r"Konversikan $58_{10}$ ke biner.", [
        r"Bagi berulang dengan 2 dan catat sisanya: $58\div2=29$ sisa $0$; $29\div2=14$ sisa $1$; $14\div2=7$ sisa $0$; $7\div2=3$ sisa $1$; $3\div2=1$ sisa $1$; $1\div2=0$ sisa $1$.",
        r"Baca sisa dari bawah ke atas: $111010$.",
    ], r"$111010_2$"),
    (r"Konversikan $101101_2$ ke desimal.", [
        r"Jumlahkan (digit $\times$ bobot posisi): $1(32)+0(16)+1(8)+1(4)+0(2)+1(1)$.",
        r"$=32+8+4+1=45$.",
    ], r"$45_{10}$"),
    (r"Konversikan $0.625_{10}$ ke biner.", [
        r"Kalikan berulang dengan 2, catat bagian bulatnya: $0.625\times2=1.25\to1$; $0.25\times2=0.5\to0$; $0.5\times2=1.0\to1$.",
        r"Baca bagian bulat dari atas ke bawah: $0.101$.",
    ], r"$0.101_2$"),
    (r"Konversikan $10110101_2$ ke oktal.", [
        r"Kelompokkan per 3 bit dari kanan, tambahkan nol di depan jika perlu: $010\ 110\ 101$.",
        r"Baca setiap kelompok sebagai digit oktal: $2\,6\,5$.",
    ], r"$265_8$"),
    (r"Konversikan $10110101_2$ ke heksadesimal.", [
        r"Kelompokkan per 4 bit dari kanan: $1011\ 0101$.",
        r"Baca setiap nibble sebagai digit hex: $B\,5$.",
    ], r"$B5_{16}$"),
    (r"Konversikan $176_8$ ke desimal.", [
        r"Jumlahkan (digit $\times$ bobot basis-8): $1\times8^2+7\times8^1+6\times8^0$.",
        r"$=64+56+6=126$.",
    ], r"$126_{10}$"),
    (r"Konversikan $350_{10}$ ke heksadesimal.", [
        r"Bagi berulang dengan 16: $350\div16=21$ sisa $14=E$; $21\div16=1$ sisa $5$; $1\div16=0$ sisa $1$.",
        r"Baca sisa dari bawah ke atas: $15E$.",
    ], r"$15E_{16}$"),
    (r"Berapa rentang nilai bilangan unsigned 8-bit?", [
        r"Bilangan unsigned n-bit berkisar dari $0$ hingga $2^n-1$.",
        r"Untuk $n=8$: $2^8-1=255$.",
    ], r"$0$ sampai $255$"),
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

    k_body = r"\begin{multicols}{3}" + "\n" + r"\begin{enumerate}[label=\textbf{\arabic*.},leftmargin=*,itemsep=2pt]" + "\n"
    for title, items in SECTIONS:
        for _, a in items:
            k_body += r"\item " + a + "\n"
    k_body += r"\end{enumerate}" + "\n" + r"\end{multicols}" + "\n"

    tex = PREAMBLE + r"""
\begin{document}
\begin{tabular}{|C{2.7cm}|L{9.8cm}|L{3.5cm}|}
\hline
\multirow{4}{*}{\kiranalogo} & \multirow{4}{*}{\begin{minipage}{9.6cm}\centering
  {\large\bfseries SOAL LATIHAN (20 NOMOR)}\\[1mm]
  {\small PROGRAM STUDI TEKNIK REKAYASA AERONAUTIKA -- POLITEKNIK KIRANA}
\end{minipage}} & \lb{Mata Kuliah / Course} \\ \cline{3-3}
 & & """ + COURSE_NAME + r""" \\ \cline{3-3}
 & & \lb{Kode / SKS} \\ \cline{3-3}
 & & """ + COURSE_CODE + r""" / 3 \\ \hline
\end{tabular}

\vspace{3mm}
\begin{tabular}{|L{3.4cm}|L{12.6cm}|}
\hline
\lb{Pertemuan} & 1--2 \\ \hline
\lb{Topik} & Sistem Bilangan Unsigned: Desimal, Biner, Oktal, Heksadesimal \\ \hline
\lb{Sub-CPMK} & Mampu mengkonversi bilangan unsigned antar sistem desimal, biner, oktal, dan heksadesimal secara tepat. \\ \hline
\lb{Capaian} & CPMK-1 (CPL-1) \\ \hline
\end{tabular}

\vspace{4mm}
\textbf{Petunjuk:}
\begin{itemize}[nosep]
\item Latihan mandiri -- kerjakan tanpa melihat kunci jawaban terlebih dahulu.
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
    fname = "soal_latihan_unsigned"
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
