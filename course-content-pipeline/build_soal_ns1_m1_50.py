#!/usr/bin/env python3
"""50-soal latihan drill sheet for Natural_Science_1 meeting 1
(Arithmetic & Scientific Calculator). Saved as a separate file
(soal_latihan_50.tex) next to the existing 3-soal exercise.tex,
so it does not overwrite it."""
import os, re, subprocess

COURSE = "Natural_Science_1"
COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Urutan Operasi Hitung (BODMAS)", [
        (r"$15 + 6 \times (8-3) \div 2$", r"$30$"),
        (r"$(12-4)\times 3 + 7^2$", r"$73$"),
        (r"$20 \div 4 + 3\times(5-2)$", r"$14$"),
        (r"$2\times(3+4)^2 - 10$", r"$88$"),
        (r"$45 \div (9-4) + 6\times 2$", r"$21$"),
        (r"$(7+3)\times(6-2)\div 4$", r"$10$"),
        (r"$8^2 \div 4 + 3\times(10-7)$", r"$25$"),
        (r"$100 - 4\times(5+3)\div 2$", r"$84$"),
    ]),
    ("B. Pecahan", [
        (r"$\dfrac{3}{4}+\dfrac{2}{5}$", r"$\dfrac{23}{20} = 1\dfrac{3}{20}$"),
        (r"$\dfrac{7}{8}-\dfrac{1}{3}$", r"$\dfrac{13}{24}$"),
        (r"$\dfrac{2}{3}\times\dfrac{5}{6}$", r"$\dfrac{5}{9}$"),
        (r"$\dfrac{4}{5}\div\dfrac{2}{15}$", r"$6$"),
        (r"$1\dfrac{1}{2}+2\dfrac{2}{3}$", r"$4\dfrac{1}{6}$"),
        (r"$\dfrac{5}{6}-\dfrac{1}{4}+\dfrac{1}{3}$", r"$\dfrac{11}{12}$"),
        (r"$3\dfrac{1}{4}\times\dfrac{2}{5}$", r"$1\dfrac{3}{10}$"),
        (r"$\dfrac{7}{10}\div 1\dfrac{2}{5}$", r"$\dfrac{1}{2}$"),
    ]),
    ("C. Rasio dan Proporsi", [
        (r"Sederhanakan rasio $48:36$.", r"$4:3$"),
        (r"Skala peta $1:50000$. Jarak di peta $3.6$ cm, berapa jarak sebenarnya (dalam km)?", r"$1.8$ km"),
        (r"Bagi $450$ dengan rasio $2:3:4$. Tentukan masing-masing bagian.", r"$100, 150, 200$"),
        (r"$8$ teknisi menyelesaikan pekerjaan dalam $15$ hari. Berapa hari jika dikerjakan $12$ teknisi?", r"$10$ hari"),
        (r"Campuran oli:bahan bakar $= 3:7$. Jika total campuran $20$ L, berapa liter oli?", r"$6$ L"),
        (r"Selesaikan proporsi $\dfrac{x}{5}=\dfrac{12}{20}$.", r"$x=3$"),
    ]),
    ("D. Persentase", [
        (r"Tentukan $35\%$ dari $240$.", r"$84$"),
        (r"Tangki bahan bakar berkapasitas $180$ L berisi $45$ L. Berapa persen isi tangki?", r"$25\%$"),
        (r"Harga naik dari Rp150.000 menjadi Rp180.000. Berapa persen kenaikannya?", r"$20\%$"),
        (r"Dari $250$ komponen yang diperiksa, $4$ gagal. Berapa persen tingkat kegagalannya?", r"$1.6\%$"),
        (r"Ubah $0.0625$ menjadi persen.", r"$6.25\%$"),
        (r"Jika $15\%$ dari suatu bilangan adalah $45$, tentukan bilangan tersebut.", r"$300$"),
    ]),
    ("E. Pangkat, Indeks, dan Akar", [
        (r"Hitung $3^4$.", r"$81$"),
        (r"Hitung $2^{-3}$.", r"$\dfrac{1}{8}=0.125$"),
        (r"Sederhanakan $x^5 \times x^3$.", r"$x^8$"),
        (r"Sederhanakan $(x^2)^4 \div x^3$.", r"$x^5$"),
        (r"Hitung $\sqrt{144}$.", r"$12$"),
        (r"Hitung $\sqrt[3]{125}$.", r"$5$"),
        (r"Hitung $27^{2/3}$.", r"$9$"),
        (r"Sederhanakan $(2^3\times 2^2)\div 2^4$.", r"$2$"),
    ]),
    ("F. Notasi Ilmiah", [
        (r"Tulis $0.000456$ dalam notasi ilmiah.", r"$4.56\times10^{-4}$"),
        (r"Tulis $5{,}230{,}000$ dalam notasi ilmiah.", r"$5.23\times10^{6}$"),
        (r"Hitung $(3\times10^{4})\times(2\times10^{-2})$.", r"$6\times10^{2}$"),
        (r"Hitung $(6\times10^{-3})\div(2\times10^{5})$.", r"$3\times10^{-8}$"),
        (r"Hitung $(4.2\times10^{3})+(3.1\times10^{2})$.", r"$4.51\times10^{3}$"),
        (r"Ubah $2.5\times10^{-5}$ ke bentuk desimal.", r"$0.000025$"),
        (r"Galat pembacaan altimeter pesawat adalah $3.4\times10^{-4}$ m. Nyatakan dalam bentuk desimal.", r"$0.00034$ m"),
        (r"Hitung $(1.5\times10^{6})\times(4\times10^{-3})$, nyatakan dalam notasi ilmiah.", r"$6\times10^{3}$"),
    ]),
    ("G. Angka Penting", [
        (r"Berapa banyak angka penting pada $0.004050$?", r"$4$ angka penting"),
        (r"Bulatkan $23.4567$ menjadi $3$ angka penting.", r"$23.5$"),
        (r"Bulatkan $1{,}250{,}000$ menjadi $2$ angka penting.", r"$1.3\times10^{6}$"),
        (r"Hitung $12.34+5.1$ dengan aturan angka penting yang benar.", r"$17.4$"),
        (r"Hitung $2.3\times1.45$ dengan aturan angka penting yang benar.", r"$3.3$"),
        (r"Berapa banyak angka penting pada $1.020\times10^{3}$?", r"$4$ angka penting"),
    ]),
]

EXAMPLES = [
    (r"$18 + 12 \div (6-2) \times 3$", [
        r"Selesaikan dalam kurung dahulu: $6-2=4$.",
        r"Bagi: $12 \div 4 = 3$.",
        r"Kali: $3 \times 3 = 9$.",
        r"Tambah: $18+9=27$.",
    ], r"$27$"),
    (r"$\dfrac{2}{3}+\dfrac{1}{4}$", [
        r"Cari KPK penyebut: KPK$(3,4)=12$.",
        r"Samakan penyebut: $\dfrac{2}{3}=\dfrac{8}{12}$ dan $\dfrac{1}{4}=\dfrac{3}{12}$.",
        r"Jumlahkan pembilang: $\dfrac{8}{12}+\dfrac{3}{12}=\dfrac{11}{12}$.",
    ], r"$\dfrac{11}{12}$"),
    (r"Sederhanakan rasio $24:36$.", [
        r"Cari FPB dari $24$ dan $36$: FPB $=12$.",
        r"Bagi kedua sisi rasio dengan FPB: $24\div12=2$ dan $36\div12=3$.",
    ], r"$2:3$"),
    (r"Tentukan $20\%$ dari $150$.", [
        r"Ubah persen ke pecahan: $20\%=\dfrac{20}{100}$.",
        r"Kalikan dengan nilai yang diketahui: $\dfrac{20}{100}\times150=\dfrac{3000}{100}$.",
    ], r"$30$"),
    (r"Hitung $2^5$.", [
        r"Kalikan $2$ sebanyak $5$ kali: $2\times2\times2\times2\times2$.",
        r"$2\times2=4$, lalu $4\times2=8$, lalu $8\times2=16$, lalu $16\times2=32$.",
    ], r"$32$"),
    (r"Tulis $0.00032$ dalam notasi ilmiah.", [
        r"Geser titik desimal sampai tersisa satu digit bukan nol di depan koma: $3.2$.",
        r"Hitung jumlah pergeseran titik: bergeser $4$ tempat ke kanan, sehingga eksponen $=-4$.",
    ], r"$3.2\times10^{-4}$"),
    (r"Berapa banyak angka penting pada $0.00520$?", [
        r"Nol di depan (sebelum angka bukan nol pertama) tidak dihitung sebagai angka penting.",
        r"Angka penting dimulai dari digit $5$: yaitu $5$, $2$, dan $0$ -- nol di akhir pada bilangan desimal ikut dihitung.",
    ], r"$3$ angka penting"),
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
\lb{Pertemuan} & 1 \\ \hline
\lb{Topik} & Mathematics: Arithmetic \& Scientific Calculator \\ \hline
\lb{Sub-CPMK} & Mampu melakukan operasi aritmatika dan mengoperasikan kalkulator ilmiah secara akurat. \\ \hline
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
    d = f"{COURSES_ROOT}/{COURSE}/lectures/meeting1/exercise"
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
