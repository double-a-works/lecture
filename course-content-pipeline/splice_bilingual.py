#!/usr/bin/env python3
"""Build lecture_bilingual.tex by splicing a Ringkasan (ID) box into every
TOPICAL slide of the real, deployed lecture.tex -- byte-identical everywhere
else. This guarantees the bilingual deck has the same content as the actual
English original (not a stale python data module)."""
import os, re, subprocess
from extract_slides import NON_TOPICAL_TITLES


def find_slide_spans(text):
    spans = []
    for m in re.finditer(r"\\BeginContentSlide\{(.*?)\}\n", text):
        title = m.group(1)
        sc_idx = text.index("\\SlideContent{", m.end())
        start = sc_idx + len("\\SlideContent{")
        depth = 1
        i = start
        while depth > 0:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        body_end = i - 1  # offset of the matching closing brace
        spans.append({"title": title, "body_end": body_end})
    return spans


def topical_spans(text):
    return [s for s in find_slide_spans(text) if s["title"] not in NON_TOPICAL_TITLES]


def splice(src_path, ringkasan_list):
    text = open(src_path).read()
    spans = topical_spans(text)
    if len(spans) != len(ringkasan_list):
        raise ValueError(
            f"{src_path}: {len(spans)} topical slides but {len(ringkasan_list)} ringkasan entries")
    out = []
    pos = 0
    for s, rk in zip(spans, ringkasan_list):
        out.append(text[pos:s["body_end"]])
        block = ("\n\\vspace{0.3cm}\\hrule\\vspace{0.2cm}"
                  "\\footnotesize\\textit{Ringkasan (ID): " + rk + "}\n")
        out.append(block)
        pos = s["body_end"]
    out.append(text[pos:])
    return "".join(out)


def compile_bilingual(course, meeting_no, ringkasan_list, courses_root="/home/openclaw/courses"):
    d = f"{courses_root}/{course}/lectures/meeting{meeting_no}"
    src = f"{d}/lecture.tex"
    tex = splice(src, ringkasan_list)
    with open(f"{d}/lecture_bilingual.tex", "w") as f:
        f.write(tex)
    pdf = f"{d}/lecture_bilingual.pdf"
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
