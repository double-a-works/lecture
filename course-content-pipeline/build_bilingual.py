#!/usr/bin/env python3
"""Build + compile lecture_bilingual.pdf for meetings 1-4 of all 4 courses.
Never touches lecture.tex/lecture.pdf. Run sequentially, one deck at a time."""
import sys
from build_slides_bilingual import build_deck_bilingual, compile_bilingual

import content_logic, content_micro, content_ns1, content_data
import ringkasan_logic, ringkasan_micro, ringkasan_ns1, ringkasan_data

COURSES = [
 (content_logic, ringkasan_logic),
 (content_micro, ringkasan_micro),
 (content_ns1, ringkasan_ns1),
 (content_data, ringkasan_data),
]

def build_one(c, r, meeting_no):
    title, subclo, indicators, slides, summary, assignments = c.M[meeting_no]
    rk = r.RINGKASAN[meeting_no]
    tex = build_deck_bilingual(c.COURSE, c.SUBJECT, c.SUBTITLE, c.REF, c.CLO,
                                meeting_no, title, subclo, indicators, slides, rk,
                                summary, assignments)
    return compile_bilingual(c.COURSE, meeting_no, tex)

if __name__ == "__main__":
    only = sys.argv[1:] if len(sys.argv) > 1 else None  # e.g. "Digital_Technic_Logic:1"
    results = []
    for c, r in COURSES:
        for n in [1, 2, 3, 4]:
            key = f"{c.COURSE}:{n}"
            if only and key not in only:
                continue
            res = build_one(c, r, n)
            results.append(res)
            status = "OK" if res["ok"] else "FAIL"
            print(f"[{status}] {res['course']} meeting {res['meeting']}: {res['size_kb']} KB "
                  f"errors={res['errors']}")
    n_ok = sum(1 for r in results if r["ok"])
    print(f"\n{n_ok}/{len(results)} decks compiled cleanly.")
