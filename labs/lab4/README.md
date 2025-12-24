Lab 4 — Guardrails + Red Team Suite (Before/After Block‑Rate)
=======================================================
> Author : Seynabou SOUGOU, Maxime XU - LLM Cybersecurity - ECE 2025/2026

**Goal.** Add a minimal guardrails layer to an LLM app and measure protection using an automated red‑team prompt set.
Run the same attacks **with** and **without** guardrails and report the delta.

## Ce que nous avons fait
- Execution des attaques en mode unguarded puis guarded.
- Ajout de regles de guardrails et comparaison avant/apres.
- Redaction de l'analyse avec exemples bloques.

## Artefacts
- `reports/unguarded.json`, `reports/guarded_initial.json`, `reports/guarded_final.json`
- `reports/metrics_initial.csv`, `reports/metrics_final.csv`
- `reports/analysis.md`

## Deliverables
- `reports/unguarded.json` and `reports/guarded.json`
- `reports/metrics.csv` with block rate and unsafe‑pass rate
- 1‑page report with examples and policy rationale

## Quick start
```bash
# From repo root (llm-course/)
make install                      # Creates .venv at repo root
source .venv/bin/activate
cp .env.example .env              # add GEMINI_API_KEY
cd labs/lab4
python src/run_suite.py --mode unguarded --limit 50
python src/run_suite.py --mode guarded --limit 50
python src/metrics.py reports/unguarded.json reports/guarded.json reports/metrics.csv
```
