#!/usr/bin/env python3
"""50-soal latihan drill sheet for Natural_Science_1 meeting 2
(Matematika: Aljabar), mirroring build_soal_ns1_m1_50.py, including
worked examples before each section's questions. Saved as a separate
file (soal_latihan_50.tex) next to the existing exercise.tex."""
import os, re, subprocess

COURSE = "Natural_Science_1"
COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Suku Sejenis dan Hukum Distributif", [
        (r"Sederhanakan $3x+5x$.", r"$8x$"),
        (r"Sederhanakan $7y-2y+4y$.", r"$9y$"),
        (r"Sederhanakan $4a+3b-2a+5b$.", r"$2a+8b$"),
        (r"Jabarkan $3(x+4)$.", r"$3x+12$"),
        (r"Jabarkan $-2(x-5)$.", r"$-2x+10$"),
        (r"Sederhanakan $5(x+2)-3x$.", r"$2x+10$"),
        (r"Sederhanakan $2(3x-1)+4(x+2)$.", r"$10x+6$"),
    ]),
    ("B. Hukum Eksponen dalam Aljabar", [
        (r"Sederhanakan $x^3 \times x^5$.", r"$x^8$"),
        (r"Sederhanakan $y^7 \div y^2$.", r"$y^5$"),
        (r"Sederhanakan $(x^2)^4$.", r"$x^8$"),
        (r"Sederhanakan $(2x^3)^2$.", r"$4x^6$"),
        (r"Sederhanakan $x^0$ (untuk $x\neq0$).", r"$1$"),
        (r"Sederhanakan $x^{-2}$.", r"$\dfrac{1}{x^2}$"),
        (r"Sederhanakan $\dfrac{x^5 y^2}{x^2 y}$.", r"$x^3y$"),
    ]),
    ("C. Menjabarkan Dua Kurung (Ekspansi)", [
        (r"Jabarkan $(x+2)(x+3)$.", r"$x^2+5x+6$"),
        (r"Jabarkan $(x-4)(x+1)$.", r"$x^2-3x-4$"),
        (r"Jabarkan $(2x+1)(x-3)$.", r"$2x^2-5x-3$"),
        (r"Jabarkan $(x+5)^2$.", r"$x^2+10x+25$"),
        (r"Jabarkan $(x-3)^2$.", r"$x^2-6x+9$"),
        (r"Jabarkan $(x+4)(x-4)$.", r"$x^2-16$"),
        (r"Jabarkan $(3x-2)(2x+5)$.", r"$6x^2+11x-10$"),
    ]),
    ("D. Memfaktorkan Ekspresi", [
        (r"Faktorkan $4x+8$.", r"$4(x+2)$"),
        (r"Faktorkan $x^2+7x+12$.", r"$(x+3)(x+4)$"),
        (r"Faktorkan $x^2-9$.", r"$(x+3)(x-3)$"),
        (r"Faktorkan $x^2-5x+6$.", r"$(x-2)(x-3)$"),
        (r"Faktorkan $2x^2+6x$.", r"$2x(x+3)$"),
        (r"Faktorkan $x^2-x-6$.", r"$(x-3)(x+2)$"),
        (r"Faktorkan $9x^2-25$.", r"$(3x+5)(3x-5)$"),
    ]),
    ("E. Menyelesaikan Persamaan Linear", [
        (r"Selesaikan $x+7=12$.", r"$x=5$"),
        (r"Selesaikan $3x=15$.", r"$x=5$"),
        (r"Selesaikan $2x-5=9$.", r"$x=7$"),
        (r"Selesaikan $4x+3=2x+11$.", r"$x=4$"),
        (r"Selesaikan $3(x+2)=18$.", r"$x=4$"),
        (r"Selesaikan $2(x-1)+5=x+8$.", r"$x=5$"),
        (r"Selesaikan $\dfrac{x}{3}+2=5$.", r"$x=9$"),
        (r"Selesaikan $\dfrac{x+1}{2}=\dfrac{x-1}{3}$.", r"$x=-5$"),
    ]),
    ("F. Menyelesaikan Persamaan Kuadrat dengan Pemfaktoran", [
        (r"Selesaikan $x^2-5x+6=0$.", r"$x=2$ atau $x=3$"),
        (r"Selesaikan $x^2-9=0$.", r"$x=3$ atau $x=-3$"),
        (r"Selesaikan $x^2+3x-10=0$.", r"$x=-5$ atau $x=2$"),
        (r"Selesaikan $x^2-7x+12=0$.", r"$x=3$ atau $x=4$"),
        (r"Selesaikan $x^2+x-6=0$.", r"$x=-3$ atau $x=2$"),
        (r"Selesaikan $2x^2-8=0$.", r"$x=2$ atau $x=-2$"),
        (r"Selesaikan $x^2-4x=0$.", r"$x=0$ atau $x=4$"),
    ]),
    ("G. Rumus Kuadrat dan Diskriminan", [
        (r"Hitung diskriminan dari $x^2+5x+6=0$.", r"$D=1$"),
        (r"Hitung diskriminan dari $2x^2+3x-5=0$.", r"$D=49$"),
        (r"Tentukan jenis akar jika $D>0$.", r"Dua akar real berbeda"),
        (r"Tentukan jenis akar jika $D=0$.", r"Satu akar real (kembar)"),
        (r"Tentukan jenis akar jika $D<0$.", r"Tidak ada akar real"),
        (r"Gunakan rumus kuadrat untuk menyelesaikan $x^2-3x-4=0$.", r"$x=4$ atau $x=-1$"),
        (r"Gunakan rumus kuadrat untuk menyelesaikan $2x^2+5x+2=0$.", r"$x=-0.5$ atau $x=-2$"),
    ]),
]

EXAMPLES = [
    (r"Sederhanakan $4x+7-2x+3$.", [
        r"Kelompokkan suku sejenis: suku $x$ ($4x$ dan $-2x$) dan konstanta ($7$ dan $3$).",
        r"Jumlahkan suku $x$: $4x-2x=2x$.",
        r"Jumlahkan konstanta: $7+3=10$.",
    ], r"$2x+10$"),
    (r"Sederhanakan $(3x^2)^3 \div x^4$.", [
        r"Pangkatkan setiap faktor dalam kurung: $(3x^2)^3=3^3x^{2\times3}=27x^6$.",
        r"Bagi dengan $x^4$ menggunakan hukum eksponen $x^a\div x^b=x^{a-b}$: $27x^6\div x^4=27x^{6-4}$.",
    ], r"$27x^2$"),
    (r"Jabarkan $(x+6)(x-2)$.", [
        r"Kalikan tiap suku pada kurung pertama dengan tiap suku pada kurung kedua (metode FOIL): $x\times x+x\times(-2)+6\times x+6\times(-2)$.",
        r"Hitung tiap hasil kali: $x^2-2x+6x-12$.",
        r"Gabungkan suku sejenis: $-2x+6x=4x$.",
    ], r"$x^2+4x-12$"),
    (r"Faktorkan $x^2+5x+6$.", [
        r"Cari dua bilangan yang hasil kalinya $6$ dan jumlahnya $5$: yaitu $2$ dan $3$.",
        r"Tulis dalam bentuk faktor: $(x+2)(x+3)$.",
    ], r"$(x+2)(x+3)$"),
    (r"Selesaikan $2(x+3)-4=x+5$.", [
        r"Jabarkan kurung: $2x+6-4=x+5$.",
        r"Sederhanakan ruas kiri: $2x+2=x+5$.",
        r"Pindahkan variabel ke satu ruas: $2x-x=5-2$, sehingga $x=3$.",
    ], r"$x=3$"),
    (r"Selesaikan $x^2-x-6=0$ dengan pemfaktoran.", [
        r"Cari dua bilangan yang hasil kalinya $-6$ dan jumlahnya $-1$: yaitu $-3$ dan $2$.",
        r"Tulis dalam bentuk faktor: $(x-3)(x+2)=0$.",
        r"Setiap faktor dapat bernilai nol: $x-3=0$ atau $x+2=0$.",
    ], r"$x=3$ atau $x=-2$"),
    (r"Gunakan rumus kuadrat untuk menyelesaikan $x^2+2x-3=0$.", [
        r"Identifikasi koefisien: $a=1$, $b=2$, $c=-3$.",
        r"Hitung diskriminan: $D=b^2-4ac=2^2-4(1)(-3)=4+12=16$.",
        r"Substitusikan ke rumus kuadrat: $x=\dfrac{-b\pm\sqrt{D}}{2a}=\dfrac{-2\pm\sqrt{16}}{2}=\dfrac{-2\pm4}{2}$.",
    ], r"$x=1$ atau $x=-3$"),
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
\lb{Topik} & Mathematics: Aljabar \\ \hline
\lb{Sub-CPMK} & Mampu memanipulasi persamaan aljabar linear dan kuadrat serta menyederhanakan ekspresi. \\ \hline
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
