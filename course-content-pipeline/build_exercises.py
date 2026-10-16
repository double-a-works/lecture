#!/usr/bin/env python3
"""Build bilingual practice-exercise PDFs into <course>/lectures/meeting<N>/exercise/.
Separate from assignment.tex/lecture.tex -- new content, not touching existing files."""
import os, re, subprocess

COURSES_ROOT = "/home/openclaw/courses"
LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"

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

\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\definecolor{headergray}{gray}{0.80}
\definecolor{lblgray}{gray}{0.94}
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}p{#1}}
\newcommand{\lb}[1]{\cellcolor{lblgray}\bfseries #1}

\newcommand{\kiranalogo}{%
  \IfFileExists{_assets/icon/logo_politeknik_kirana.png}
    {\includegraphics[width=2.6cm,height=1.35cm,keepaspectratio]{_assets/icon/logo_politeknik_kirana.png}}
    {\framebox[2.6cm][c]{\rule[-0.65cm]{0pt}{1.35cm}\scriptsize LOGO}}}
"""


def problem_block(idx, level, en, id_, sol_en, sol_id):
    return (
        r"\item \textbf{[" + level + r"]}\\"
        r"\textbf{EN:} " + en + r"\\"
        r"\textbf{ID:} " + id_ + r"\\[2mm]"
        r"\textit{Solution / Penyelesaian:}\\"
        r"\textbf{EN:} " + sol_en + r"\\"
        r"\textbf{ID:} " + sol_id
    )


def build_exercise_tex(course_name, course_code, meeting_no, topic, subcpmk_text, cpmk_text, problems):
    body = "\n".join(problem_block(i + 1, *p) for i, p in enumerate(problems))
    tex = PREAMBLE + r"""
\begin{document}
\begin{tabular}{|C{2.7cm}|L{9.8cm}|L{3.5cm}|}
\hline
\multirow{4}{*}{\kiranalogo} & \multirow{4}{*}{\begin{minipage}{9.6cm}\centering
  {\large\bfseries LATIHAN BILINGUAL / BILINGUAL PRACTICE EXERCISE}\\[1mm]
  {\small PROGRAM STUDI TEKNIK REKAYASA AERONAUTIKA -- POLITEKNIK KIRANA}
\end{minipage}} & \lb{Mata Kuliah / Course} \\ \cline{3-3}
 & & """ + course_name + r""" \\ \cline{3-3}
 & & \lb{Kode / SKS} \\ \cline{3-3}
 & & """ + course_code + r""" / 3 \\ \hline
\end{tabular}

\vspace{3mm}
\begin{tabular}{|L{3.4cm}|L{12.6cm}|}
\hline
\lb{Pertemuan / Meeting} & """ + str(meeting_no) + r""" \\ \hline
\lb{Topik / Topic} & """ + topic + r""" \\ \hline
\lb{Sub-CPMK} & """ + subcpmk_text + r""" \\ \hline
\lb{Capaian / Outcome} & """ + cpmk_text + r""" \\ \hline
\end{tabular}

\vspace{4mm}
\textbf{Petunjuk / Instructions:}
\begin{itemize}[nosep]
\item Ini adalah latihan mandiri bilingual (bukan tugas terstruktur) -- kerjakan untuk melatih pemahaman materi pertemuan ini.
\item This is a self-study bilingual practice sheet (not a graded assignment) -- use it to reinforce this meeting's material.
\item Solusi disertakan langsung di bawah setiap soal untuk pembelajaran mandiri. / Solutions are included directly below each problem for self-study.
\end{itemize}

\vspace{2mm}
\textbf{Soal / Problems:}
\begin{enumerate}[label=\textbf{\arabic*.}, leftmargin=*, itemsep=8pt]
""" + body + r"""
\end{enumerate}

\vfill
\hrule
\vspace{1mm}
{\small Dosen Pengampu: """ + LECTURER + r""" \hfill Politeknik Kirana}

\end{document}
"""
    return tex


def compile_exercise(course, meeting_no, tex):
    d = f"{COURSES_ROOT}/{course}/lectures/meeting{meeting_no}/exercise"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/exercise.tex", "w") as f:
        f.write(tex)
    link = f"{d}/_assets"
    if not os.path.islink(link):
        os.symlink("../../../../_assets", link)
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "exercise.tex"],
                        cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pdf = f"{d}/exercise.pdf"
    lp = f"{d}/exercise.log"
    errs = []
    if os.path.exists(lp):
        txt = open(lp, errors="ignore").read()
        errs = re.findall(r"^! .*", txt, re.M)
    ok = os.path.exists(pdf) and os.path.getsize(pdf) > 0 and not errs
    size = os.path.getsize(pdf) if os.path.exists(pdf) else 0
    return {"course": course, "meeting": meeting_no, "ok": ok, "size_kb": size // 1024, "errors": errs[:3]}
