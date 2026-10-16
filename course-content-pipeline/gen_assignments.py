#!/usr/bin/env python3
"""Generate assignment.tex + assignment.pdf for each teaching meeting of a course,
from the shared ~/courses/_templates/assignment.tex template."""
import os
import re
import subprocess
import sys

COURSES_DIR = os.path.expanduser("~/courses")
TEMPLATE_PATH = os.path.join(COURSES_DIR, "_templates", "assignment.tex")

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    TEMPLATE = f.read()

OLD_DEFAULTS = """\\Course{Course Name}
\\CourseCode{CODE000}
\\MeetingNo{0}
\\AssignmentNo{00}
\\TopicTitle{Topic Title}
\\SubCPMKRef{Sub-CPMK X}
\\DueNote{Submit before the next meeting.}"""

OLD_TASKS = """\\begin{tasks}
\\task \\pts{20} Replace with a foundational-level task tied to today's Sub-CPMK.

\\task \\pts{25} Replace with an application-level task.

\\task \\pts{25} Replace with an analysis-level task.

\\task \\pts{30} Replace with an analysis/troubleshooting or challenge-level task.
\\end{tasks}"""

DUE_NOTE = "Kumpulkan dalam bentuk PDF sebelum pertemuan berikutnya dimulai."


def render(course_name, course_code, meeting_no, assignment_no, topic, subcpmk, tasks):
    defaults = (
        f"\\Course{{{course_name}}}\n"
        f"\\CourseCode{{{course_code}}}\n"
        f"\\MeetingNo{{{meeting_no}}}\n"
        f"\\AssignmentNo{{{assignment_no}}}\n"
        f"\\TopicTitle{{{topic}}}\n"
        f"\\SubCPMKRef{{{subcpmk}}}\n"
        f"\\DueNote{{{DUE_NOTE}}}"
    )
    task_lines = ["\\begin{tasks}"]
    for pts, text in tasks:
        task_lines.append(f"\\task \\pts{{{pts}}} {text}\n")
    task_lines.append("\\end{tasks}")
    tasks_block = "\n".join(task_lines)

    tex = TEMPLATE.replace(OLD_DEFAULTS, defaults)
    if tex == TEMPLATE:
        raise RuntimeError("defaults block not found/replaced")
    tex2 = tex.replace(OLD_TASKS, tasks_block)
    if tex2 == tex:
        raise RuntimeError("tasks block not found/replaced")
    return tex2


def build(course_dir_name, meeting_no, tex_content):
    out_dir = os.path.join(COURSES_DIR, course_dir_name, "lectures", f"meeting{meeting_no}")
    os.makedirs(out_dir, exist_ok=True)
    tex_path = os.path.join(out_dir, "assignment.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)

    for _ in range(2):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "assignment.tex"],
            cwd=out_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    pdf_path = os.path.join(out_dir, "assignment.pdf")
    ok = result.returncode == 0 and os.path.isfile(pdf_path)
    if not ok:
        print(f"FAILED: {course_dir_name} meeting{meeting_no}")
        print(result.stdout.decode("utf-8", errors="replace")[-3000:])
    else:
        print(f"OK: {course_dir_name} meeting{meeting_no}")
    return ok


def build_course(course_dir_name, course_name, course_code, meetings):
    """meetings: list of (meeting_no, assignment_no, topic, subcpmk, tasks)"""
    results = {}
    for meeting_no, assignment_no, topic, subcpmk, tasks in meetings:
        tex = render(course_name, course_code, meeting_no, assignment_no, topic, subcpmk, tasks)
        results[meeting_no] = build(course_dir_name, meeting_no, tex)
    return results
