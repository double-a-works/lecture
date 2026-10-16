#!/usr/bin/env python3
"""Build lecture_bilingual.pdf for Digital_Technic_Micro meetings 14-16,
using the splice_bilingual pattern (splice ID ringkasan into deployed
lecture.tex, byte-identical elsewhere)."""
import sys
from splice_bilingual import compile_bilingual
from ringkasan_micro_14_16 import RINGKASAN

if __name__ == "__main__":
    meetings = [int(x) for x in sys.argv[1:]] or [14, 15, 16]
    results = []
    for n in meetings:
        res = compile_bilingual("Digital_Technic_Micro", n, RINGKASAN[n])
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']}: {res['size_kb']} KB errors={res['errors']}")
