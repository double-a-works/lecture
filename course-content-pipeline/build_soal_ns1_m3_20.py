#!/usr/bin/env python3
"""20-soal latihan drill sheet for Natural_Science_1 meeting 3
(Matematika: Geometri), mirroring build_soal_ns1_m2_50.py, including
worked examples before each section's questions. Saved as a separate
file (soal_latihan_20.tex) next to the existing exercise.tex."""
import os, re, subprocess

COURSE = "Natural_Science_1"
COURSE_NAME = "Natural Science 1: Applied Mathematics and Chemistry"
COURSE_CODE = "AV0102BM"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"
COURSES_ROOT = "/home/openclaw/courses"

SECTIONS = [
    ("A. Sudut: Komplementer dan Suplementer", [
        (r"Dua sudut saling berpelengkap (komplementer) dan salah satunya $35^\circ$. Berapa sudut lainnya?", r"$55^\circ$"),
        (r"Dua sudut saling berpenyiku (suplementer) dan salah satunya $110^\circ$. Berapa sudut lainnya?", r"$70^\circ$"),
    ]),
    ("B. Segitiga: Jumlah Sudut", [
        (r"Sebuah segitiga memiliki sudut $45^\circ$ dan $60^\circ$. Berapa besar sudut ketiga?", r"$75^\circ$"),
        (r"Segitiga sama kaki memiliki sudut puncak $40^\circ$. Berapa besar masing-masing sudut alasnya?", r"$70^\circ$"),
    ]),
    ("C. Luas dan Keliling Bangun Datar", [
        (r"Hitung luas dan keliling persegi panjang $12$\,m $\times$ $7$\,m.", r"Luas $=84$\,m$^2$, Keliling $=38$\,m"),
        (r"Hitung luas segitiga dengan alas $14$\,cm dan tinggi $9$\,cm.", r"$63$\,cm$^2$"),
        (r"Hitung luas jajar genjang dengan alas $10$\,cm dan tinggi $6$\,cm.", r"$60$\,cm$^2$"),
        (r"Hitung luas trapesium dengan sisi sejajar $8$\,cm dan $12$\,cm, tinggi $5$\,cm.", r"$50$\,cm$^2$"),
    ]),
    ("D. Lingkaran: Keliling, Luas, Panjang Busur", [
        (r"Hitung keliling lingkaran dengan $r=7$\,cm.", r"$14\pi\approx43{,}98$\,cm"),
        (r"Hitung luas lingkaran dengan $r=10$\,cm.", r"$100\pi\approx314{,}16$\,cm$^2$"),
        (r"Hitung panjang busur bersudut $90^\circ$ pada lingkaran dengan $r=8$\,cm.", r"$4\pi\approx12{,}57$\,cm"),
    ]),
    ("E. Bangun Datar Gabungan", [
        (r"Braket berbentuk L adalah persegi panjang $12$\,cm$\times9$\,cm dengan lekukan $5$\,cm$\times4$\,cm dipotong dari satu sudut. Hitung luasnya.", r"$88$\,cm$^2$"),
        (r"Sebuah persegi panjang $10$\,cm$\times6$\,cm memiliki ujung setengah lingkaran berradius $3$\,cm. Hitung luas totalnya.", r"$\approx74{,}14$\,cm$^2$"),
    ]),
    ("F. Bangun Ruang: Volume dan Luas Permukaan", [
        (r"Hitung volume balok berukuran $5$\,m$\times4$\,m$\times3$\,m.", r"$60$\,m$^3$"),
        (r"Hitung volume tabung dengan $r=4$\,cm dan $h=10$\,cm.", r"$160\pi\approx502{,}65$\,cm$^3$"),
        (r"Hitung volume bola dengan $r=6$\,cm.", r"$288\pi\approx904{,}78$\,cm$^3$"),
        (r"Sebuah kerucut memiliki $r=5$\,cm dan $h=12$\,cm. Hitung volume dan luas permukaannya.", r"$V=100\pi\approx314{,}16$\,cm$^3$; $S=90\pi\approx282{,}74$\,cm$^2$"),
    ]),
    ("G. Teorema Pythagoras", [
        (r"Segitiga siku-siku memiliki sisi siku-siku $6$\,cm dan $8$\,cm. Carilah sisi miringnya.", r"$10$\,cm"),
        (r"Segitiga siku-siku memiliki sisi miring $13$\,cm dan salah satu sisi siku-siku $5$\,cm. Carilah sisi siku-siku lainnya.", r"$12$\,cm"),
    ]),
    ("H. Diagonal Ruang Balok", [
        (r"Sebuah peti berukuran $2$\,m$\times3$\,m$\times6$\,m. Carilah diagonal ruangnya.", r"$7$\,m"),
    ]),
]

EXAMPLES = [
    (r"Dua sudut suplementer dan salah satunya $65^\circ$. Carilah sudut lainnya.", [
        r"Sudut suplementer berjumlah $180^\circ$.",
        r"Sudut lainnya $=180^\circ-65^\circ=115^\circ$.",
    ], r"$115^\circ$"),
    (r"Sebuah segitiga memiliki sudut $50^\circ$ dan $70^\circ$. Carilah sudut ketiga.", [
        r"Jumlah sudut dalam segitiga selalu $180^\circ$.",
        r"Sudut ketiga $=180^\circ-50^\circ-70^\circ=60^\circ$.",
    ], r"$60^\circ$"),
    (r"Sebuah panel persegi panjang berukuran $8$\,m$\times5$\,m. Carilah luas dan kelilingnya.", [
        r"Luas $=l\times w=8\times5=40$\,m$^2$.",
        r"Keliling $=2(l+w)=2(8+5)=26$\,m.",
    ], r"Luas $=40$\,m$^2$, Keliling $=26$\,m"),
    (r"Sebuah lubang inspeksi berbentuk lingkaran dengan $r=6$\,cm. Carilah keliling dan luasnya.", [
        r"Keliling $=2\pi r=2\pi(6)=12\pi\approx37{,}70$\,cm.",
        r"Luas $=\pi r^2=\pi(6)^2=36\pi\approx113{,}10$\,cm$^2$.",
    ], r"Keliling $\approx37{,}70$\,cm, Luas $\approx113{,}10$\,cm$^2$"),
    (r"Sebuah braket berbentuk L adalah persegi panjang $10$\,cm$\times8$\,cm dengan lekukan $4$\,cm$\times3$\,cm dipotong dari satu sudut. Carilah luasnya.", [
        r"Luas persegi panjang besar $=10\times8=80$\,cm$^2$.",
        r"Luas lekukan $=4\times3=12$\,cm$^2$.",
        r"Luas bentuk L $=80-12=68$\,cm$^2$.",
    ], r"$68$\,cm$^2$"),
    (r"Sebuah saluran bahan bakar berbentuk tabung dengan $r=3$\,cm dan panjang $h=8$\,cm. Carilah volume dan luas permukaannya.", [
        r"Volume $=\pi r^2h=\pi(3)^2(8)=72\pi\approx226{,}19$\,cm$^3$.",
        r"Luas permukaan $=2\pi r(r+h)=2\pi(3)(3+8)=66\pi\approx207{,}35$\,cm$^2$.",
    ], r"$V\approx226{,}19$\,cm$^3$, $S\approx207{,}35$\,cm$^2$"),
    (r"Segitiga siku-siku memiliki sisi siku-siku $3$\,cm dan $4$\,cm. Carilah sisi miringnya.", [
        r"Gunakan teorema Pythagoras: $c=\sqrt{a^2+b^2}$.",
        r"$c=\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5$\,cm.",
    ], r"$5$\,cm"),
    (r"Sebuah peti berukuran $3$\,m$\times4$\,m$\times12$\,m. Carilah diagonal ruangnya.", [
        r"Diagonal ruang $d=\sqrt{l^2+w^2+h^2}$.",
        r"$d=\sqrt{3^2+4^2+12^2}=\sqrt{9+16+144}=\sqrt{169}=13$\,m.",
    ], r"$13$\,m"),
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
\lb{Pertemuan} & 3 \\ \hline
\lb{Topik} & Mathematics: Geometri \\ \hline
\lb{Sub-CPMK} & Mampu merumuskan parameter ruang menggunakan geometri: luas, keliling, volume, luas permukaan, dan teorema Pythagoras. \\ \hline
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
    d = f"{COURSES_ROOT}/{COURSE}/lectures/meeting3/exercise"
    os.makedirs(d, exist_ok=True)
    fname = "soal_latihan_20"
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
