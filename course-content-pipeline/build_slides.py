#!/usr/bin/env python3
"""Generate + compile lecture.pdf decks for the overnight build window.
Idempotent: skips any meeting that already has a non-empty lecture.pdf.
Preamble/chrome are lifted verbatim from _templates/lecture.tex so the
campus logos and DO-NOT-CHANGE cover elements are preserved exactly.
"""
import os, re, subprocess, sys

COURSES = "/home/openclaw/courses"
TEMPLATE = f"{COURSES}/_templates/lecture.tex"

# --- lift the verbatim preamble (everything up to and including \begin{document}) ---
tpl = open(TEMPLATE).read()
PREAMBLE = tpl[: tpl.index("\\begin{document}") + len("\\begin{document}")]

LECTURER = "Anak Agung Maharaja Adhisthanaya Indrawan"

# ---- reusable chrome fragments (parameterized) ----
def cover(subject, subtitle):
    return r"""
\begin{tikzpicture}[remember picture, overlay]
    \fill[white] (current page.south west) rectangle (current page.north east);
    % DO NOT CHANGE COVER !!!
    \node[anchor=south west, inner sep=0pt] at (current page.south west) {%
        \includegraphics[height=6cm]{_assets/icon/Cover2_kiri_bawah.png}};
    \node[anchor=north east, inner sep=0pt] at (current page.north east) {%
        \includegraphics[height=5cm]{_assets/icon/Cover2_kanan_atas.png}};
    \node[anchor=center] at ([yshift=3.0cm] current page.center) {%
        \includegraphics[height=2.5cm]{_assets/icon/Cover1.png}};
    \node[anchor=center] at ([yshift=-0.5cm] current page.center) {%
        \includegraphics[height=4.0cm]{_assets/icon/Cover3.jpg}};
    \node[align=center] at ([yshift=-3.5cm] current page.center) {%
        \Large \bfseries Engineering Technology of\\[0.2cm]
        \Large \bfseries Aeronautics (Avionic)};
\end{tikzpicture}
\newpage
"""

def titlecard(subject, subtitle, meeting_line, ref):
    return r"""
\begin{tikzpicture}[remember picture, overlay]
    \fill[white] (current page.south west) rectangle (current page.north east);
    % DO NOT CHANGE!!! CAMPUS PROFILE AND MAJOR LOGO!!! + SIDE ELEMENTS
    \node[anchor=north west, inner sep=0pt] at ([xshift=0.5cm, yshift=-0.5cm] current page.north west) {%
        \includegraphics[height=1.7cm]{_assets/icon/Cover1.png}};
    \node[anchor=south east, inner sep=0pt] at ([xshift=-0.5cm, yshift=0.5cm] current page.south east) {%
        \includegraphics[height=1.5cm]{_assets/icon/Cover3.jpg}};
    \node[anchor=south west, inner sep=0pt] at (current page.south west) {%
        \includegraphics[height=6cm]{_assets/icon/Cover2_kiri_bawah.png}};
    \node[anchor=north east, inner sep=0pt] at (current page.north east) {%
        \includegraphics[height=5cm]{_assets/icon/Cover2_kanan_atas.png}};
    \node[align=left,text width=14cm] at (current page.center) {
        \Large\bfseries SUBJECT : """ + subject + r"""\\[0.28cm]
        \large """ + subtitle + r"""\\[0.22cm]
        \normalsize """ + meeting_line + r"""\\[0.35cm]
        \small """ + LECTURER + r"""\\[1cm]
        \small ref: """ + ref + r"""
    };
\end{tikzpicture}
\newpage
"""

PROFILE = r"""
\BeginContentSlide{}
\SlideContent{
\begin{minipage}[t]{0.38\textwidth}
\vspace{0pt}
\centering
\includegraphics[height=5.2cm]{_assets/icon/profile.jpg}
\end{minipage}
\hfill
\begin{minipage}[t]{0.58\textwidth}
\vspace{0pt}
\small
\begin{itemize}
    \item """ + LECTURER + r"""
    \item Manado, 23 November 2002
    \item Education
    \begin{itemize}
        \item Bachelor of Electrical Engineering\\
        Sepuluh Nopember Institute of Technology (2021--2025)
        \item Master of Electrical Engineering\\
        Sepuluh Nopember Institute of Technology (2025--2026)
        \item Specialize on Electronics (Renewable Energy, Microelectronics, and Electronic Control System)
    \end{itemize}
\end{itemize}
\end{minipage}
}
\EndContentSlide
"""

PCS2T = r"""
\BeginContentSlide{}
\SlideContent{
    \begin{center}
        \includegraphics[height=4cm]{_assets/icon/PCS2T.png}
    \end{center}
}
\EndContentSlide
"""

def clo_slide(clo_items):
    body = "\n".join(f"\\item {x}" for x in clo_items)
    return r"""
\BeginContentSlide{Course Learning Outcomes (CLO)}
\SlideContent{
After studying this course, students are expected to be able to:
\begin{enumerate}
""" + body + r"""
\end{enumerate}
}
\EndContentSlide
"""

def subclo_slide(subclo, indicators):
    body = "\n".join(f"\\item {x}" for x in indicators)
    return r"""
\BeginContentSlide{Sub-CLO for This Meeting}
\SlideContent{
\textbf{Expected Final Ability:}\\
""" + subclo + r"""

\vspace{0.3cm}
\textbf{Indicators:}
\begin{itemize}
""" + body + r"""
\end{itemize}
}
\EndContentSlide
"""

def content_slide(title, body):
    return "\n\\BeginContentSlide{" + title + "}\n\\SlideContent{\n" + body + "\n}\n\\EndContentSlide\n"

def summary_slide(points):
    body = "\n".join(f"\\item {x}" for x in points)
    return content_slide("Summary of This Meeting", "\\begin{itemize}\n" + body + "\n\\end{itemize}")

def assignments_slide(items):
    body = "\n".join(f"\\item {x}" for x in items)
    return content_slide("Assignments / Exercises",
        "\\begin{enumerate}\n" + body + "\n\\end{enumerate}\n\n\\vspace{0.35cm}\n"
        "\\begin{center}\n\\Large\\bfseries Submit assignments before the next meeting.\n\\end{center}")

CLOSING = r"""
\BeginContentSlide{Closing}
\SlideContent{
\vspace{0.5cm}
\begin{center}
\Large\bfseries Questions? Discussion?

\vspace{0.6cm}
\normalsize\bfseries Happy Studying!
\end{center}
\vfill
\hrule
\vspace{0.15cm}
\textbf{Lecturer:}\\
""" + LECTURER + r"""\\
Aeronautical Engineering Study Program\\
Politeknik Kirana
}
\EndContentSlide
"""

def build_deck(course, subject, subtitle, ref, clo, meeting_no, meeting_title, subclo, indicators, slides, summary, assignments):
    meeting_line = f"Meeting {meeting_no} -- {meeting_title}"
    # the preamble hardcodes the top-right corner label; set it per course
    preamble = PREAMBLE.replace("SUBJECT : DIGITAL TECHNIC", "SUBJECT : " + subject)
    parts = [preamble, cover(subject, subtitle),
             titlecard(subject, subtitle, meeting_line, ref),
             PROFILE, PCS2T, clo_slide(clo),
             subclo_slide(subclo, indicators)]
    for (t, b) in slides:
        parts.append(content_slide(t, b))
    parts.append(summary_slide(summary))
    parts.append(assignments_slide(assignments))
    parts.append(CLOSING)
    parts.append("\n\\end{document}\n")
    tex = "\n".join(parts)
    # guard: \hline (or \\) directly abutting a letter becomes an undefined control seq
    tex = re.sub(r"\\hline(?=[A-Za-z])", r"\\hline ", tex)
    return tex

def compile_meeting(course, meeting_no, tex):
    d = f"{COURSES}/{course}/lectures/meeting{meeting_no}"
    pdf = f"{d}/lecture.pdf"
    if os.path.exists(pdf) and os.path.getsize(pdf) > 0:
        return ("skip", meeting_no, "already built")
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/lecture.tex", "w") as f:
        f.write(tex)
    link = f"{d}/_assets"
    if not os.path.islink(link):
        os.symlink("../../../_assets", link)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "lecture.tex"],
                           cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if os.path.exists(pdf) and os.path.getsize(pdf) > 0:
        return ("ok", meeting_no, f"{os.path.getsize(pdf)//1024} KB")
    # capture last error
    log = ""
    lp = f"{d}/lecture.log"
    if os.path.exists(lp):
        txt = open(lp, errors="ignore").read()
        m = re.findall(r"^! .*", txt, re.M)
        log = m[-1] if m else "unknown error"
    return ("fail", meeting_no, log)

if __name__ == "__main__":
    print("This module is driven by per-course content files.")
