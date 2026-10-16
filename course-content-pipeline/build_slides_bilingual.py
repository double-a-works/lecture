#!/usr/bin/env python3
"""Bilingual (EN main text + ID ringkasan box) lecture_bilingual.pdf builder.
Reuses chrome (cover/titlecard/profile/etc.) verbatim from build_slides.py -- do
not change the DO-NOT-CHANGE cover/campus-logo tikz blocks.
"""
import os, re, subprocess
from build_slides import (PREAMBLE, cover, titlecard, PROFILE, PCS2T,
                           clo_slide, subclo_slide, summary_slide, assignments_slide, CLOSING)


def content_slide_bilingual(title, body, ringkasan):
    ringkasan_block = (
        r"\vspace{0.3cm}\hrule\vspace{0.2cm}"
        r"\footnotesize\textit{Ringkasan (ID): " + ringkasan + r"}"
    )
    full_body = body + "\n" + ringkasan_block
    return "\n\\BeginContentSlide{" + title + "}\n\\SlideContent{\n" + full_body + "\n}\n\\EndContentSlide\n"


def build_deck_bilingual(course, subject, subtitle, ref, clo, meeting_no, meeting_title,
                          subclo, indicators, slides, ringkasan_list, summary, assignments):
    if len(ringkasan_list) != len(slides):
        raise ValueError(
            f"{course} meeting {meeting_no}: {len(slides)} slides but "
            f"{len(ringkasan_list)} ringkasan entries -- must match 1:1")
    meeting_line = f"Meeting {meeting_no} -- {meeting_title}"
    preamble = PREAMBLE.replace("SUBJECT : DIGITAL TECHNIC", "SUBJECT : " + subject)
    parts = [preamble, cover(subject, subtitle),
             titlecard(subject, subtitle, meeting_line, ref),
             PROFILE, PCS2T, clo_slide(clo),
             subclo_slide(subclo, indicators)]
    for (t, b), rk in zip(slides, ringkasan_list):
        parts.append(content_slide_bilingual(t, b, rk))
    parts.append(summary_slide(summary))
    parts.append(assignments_slide(assignments))
    parts.append(CLOSING)
    parts.append("\n\\end{document}\n")
    tex = "\n".join(parts)
    tex = re.sub(r"\\hline(?=[A-Za-z])", r"\\hline ", tex)
    return tex


def compile_bilingual(course, meeting_no, tex, courses_root="/home/openclaw/courses"):
    d = f"{courses_root}/{course}/lectures/meeting{meeting_no}"
    pdf = f"{d}/lecture_bilingual.pdf"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/lecture_bilingual.tex", "w") as f:
        f.write(tex)
    link = f"{d}/_assets"
    if not os.path.islink(link):
        os.symlink("../../../_assets", link)
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "lecture_bilingual.tex"],
                        cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lp = f"{d}/lecture_bilingual.log"
    errs = []
    if os.path.exists(lp):
        txt = open(lp, errors="ignore").read()
        errs = re.findall(r"^! .*", txt, re.M)
    ok = os.path.exists(pdf) and os.path.getsize(pdf) > 0 and not errs
    size = os.path.getsize(pdf) if os.path.exists(pdf) else 0
    return {"course": course, "meeting": meeting_no, "ok": ok, "size_kb": size // 1024, "errors": errs[:3]}


if __name__ == "__main__":
    print("This module is driven by build_bilingual.py")
