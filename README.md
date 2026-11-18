# Assignment 8 — Optimize Anything (Emergency Starter Submission)

This repository is an **emergency, reproducible starter package**, not a claim that every compulsory requirement has been fully completed. It contains small runnable demonstrations and an honest status register. Complete the marked environment-specific work before representing those tracks as finished.

## Chapter 6 syllabus coverage
- Continuous optimization: `tracks/track_a_continuous.py`
- Discrete optimization: `tracks/track_b_discrete.py`
- Submodular functions: `tracks/track_d_parallel.py`
- Load balancing: `tracks/track_d_parallel.py`
- Data locality: `tracks/track_j_software.py`
- Synchronization/communication: `tracks/track_d_parallel.py`
- Strategy selection: `tracks/track_e_main_case.py`

The assignment PDF additionally requires all Tracks A–J, including quantum and systems work. See `REPORT.md` and `STATUS.md`.

## Setup
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_all.py
```

Some tracks use only the Python standard library. Quantum track is a small classical state-vector-style educational simulation, **not a quantum hardware run**.

## Repository map
- `tracks/`: small demonstrations for the ten tracks
- `results/`: generated console output (populate by running scripts)
- `prompts/`: AI-use log template; replace/add actual exports and screenshots
- `report/REPORT.md`: report draft and explicit limitations
- `STATUS.md`: honest completion checklist

## Reproducibility
Fixed random seeds are used where applicable. Record your machine, Python version, run date and actual output in the report. Do not claim speedups based on a single noisy run.

## Academic integrity
AI assistance must be disclosed. This package includes an AI-use template, not fabricated chat exports or commit history. Add your real prompts, responses, screenshots, tool/model versions and at least three genuine error/fix cases. Explain every submitted component in the viva.
