#!/usr/bin/env python3
"""Extract (title, body) slide pairs directly from a deployed lecture.tex,
using brace-depth matching (not naive regex) so tikzpicture/tabular content
with nested braces is captured correctly."""
import re

NON_TOPICAL_TITLES = {
    "", "Course Learning Outcomes (CLO)", "Sub-CLO for This Meeting",
    "Summary of This Meeting", "Assignments / Exercises", "Closing",
}

def extract_all_slides(path):
    text = open(path).read()
    doc = text[text.index("\\begin{document}"):]
    slides = []
    for m in re.finditer(r"\\BeginContentSlide\{(.*?)\}\n", doc):
        title = m.group(1)
        sc_idx = doc.index("\\SlideContent{", m.end())
        start = sc_idx + len("\\SlideContent{")
        depth = 1
        i = start
        while depth > 0:
            if doc[i] == "{":
                depth += 1
            elif doc[i] == "}":
                depth -= 1
            i += 1
        body = doc[start:i - 1]
        if body.startswith("\n"):
            body = body[1:]
        if body.endswith("\n"):
            body = body[:-1]
        slides.append((title, body))
    return slides

def extract_topical_slides(path):
    return [(t, b) for (t, b) in extract_all_slides(path) if t not in NON_TOPICAL_TITLES]

if __name__ == "__main__":
    import sys
    for p in sys.argv[1:]:
        all_s = extract_all_slides(p)
        topical = extract_topical_slides(p)
        print(f"{p}: {len(all_s)} total slides, {len(topical)} topical")
        for t, b in topical:
            print("  -", t)
