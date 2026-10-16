#!/usr/bin/env python3
"""Build lecture_bilingual.pdf for Digital_Technic_Micro meetings 10-13,
using the splice_bilingual pattern (splice ID ringkasan into deployed
lecture.tex, byte-identical elsewhere)."""
from splice_bilingual import compile_bilingual
from ringkasan_micro_10_13 import RINGKASAN

if __name__ == "__main__":
    results = []
    for n in [10, 11, 12, 13]:
        res = compile_bilingual("Digital_Technic_Micro", n, RINGKASAN[n])
        results.append(res)
        status = "OK" if res["ok"] else "FAIL"
        print(f"[{status}] meeting {res['meeting']}: {res['size_kb']} KB errors={res['errors']}")
