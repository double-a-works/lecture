# Kona — OpenClaw Course-Content Agent

This is the working setup of **Kona**, a personal assistant built on
[OpenClaw](https://github.com/openclaw/openclaw) that helps run a
polytechnic lecturer's teaching workload: generating course materials,
exercises, slide decks, and keeping class attendance/scheduling automations
in sync with the campus portal (SIAKAD).

It's shared so others can learn the pattern and adapt it to their own
courses, agent, or LMS.

## What's here

- **`AGENTS.md` / `SOUL.md` / `USER.md` / `IDENTITY.md`** — the agent's
  persona and workspace instructions (OpenClaw's standard agent config
  files). `USER.md` and `IDENTITY.md` are left as unfilled templates —
  fill them in with your own preferences/persona.
- **`course-content-pipeline/`** — Python scripts that generate lecture
  slides, exercise sets, and summaries ("ringkasan") for real courses
  (Digital Technic Logic/Micro/Data, Natural Science 1/2, Aircraft
  Familiarization) from structured content/data modules. Each
  `content_*.py` / `data_*.py` pair holds the source material; the
  `build_*.py` / `ringkasan_*.py` scripts render it into LaTeX/PDF
  output using a shared template system (not included here — see
  OpenClaw docs on workspace templates).
- **`automation-scripts/`** — browser-automation helpers (via Chrome
  DevTools Protocol) that auto-close forgotten class sessions and manage
  assignment entries on the campus portal, so attendance records don't
  go stale if a class is forgotten to be closed manually.

## What's intentionally left out

Student grades, rosters, exam answer keys, personal notes, and any
institution-specific data were stripped before publishing. This repo is
the *mechanism*, not the data.

## Using this

1. Set up [OpenClaw](https://github.com/openclaw/openclaw) in your own
   workspace.
2. Drop in your own `AGENTS.md`/`SOUL.md`/`USER.md` (or adapt these).
3. Write your own `content_*.py`/`data_*.py` modules for your course
   material, and adapt the `build_*.py` scripts to your document
   templates.
4. Point `automation-scripts/` at your own portal if it exposes a
   similar browser-automatable workflow — the CDP connection details
   (`cdp_ws.py`, `cdp_helpers.py`) are generic.

## License

MIT — use, adapt, and share freely.
