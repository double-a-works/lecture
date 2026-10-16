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

## Quickstart

### 1. Install OpenClaw

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Follow the onboarding wizard (model provider, API key, Gateway config). See
[OpenClaw getting started](https://docs.openclaw.ai/start/getting-started)
for details. Verify it's running:

```bash
openclaw gateway status
```

### 2. Drop this repo into your workspace

```bash
cd ~/.openclaw/workspace   # or your configured workspace path
git clone https://github.com/double-a-works/lecture.git .
```

(If your workspace already has files, clone elsewhere and copy over what you
need instead of cloning into it directly.)

### 3. Install pipeline dependencies

The build scripts are plain Python 3, plus:

- A LaTeX distribution with `pdflatex` on `PATH` (e.g. `texlive-full` on
  Debian/Ubuntu, or a smaller TeX Live install with the `beamer` and
  `circuitikz` packages).
- `openpyxl` for the Excel-reading scripts:

```bash
pip install openpyxl
```

### 4. Try one build end-to-end

Each `build_*.py` reads from its matching `content_*.py`/`data_*.py` and
shells out to `pdflatex` to produce a PDF. For example:

```bash
cd course-content-pipeline
python3 build_slides.py
```

Check the script's output path for the resulting PDF. If it fails, it's
almost always a missing LaTeX package (`beamer`, `circuitikz`) or a missing
`icon`/`images` asset — the templates use `\IfFileExists` guards so missing
images won't break the build, but missing LaTeX *packages* will.

### 5. Adapt it

Once you see a build succeed, start replacing `content_*.py`/`data_*.py`
with your own course material (see "Using this" above).

## License

MIT — use, adapt, and share freely.
