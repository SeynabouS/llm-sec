Lab 2 — Secure Code Review Prompts + Eval (Promptfoo + Gemini)
=======================================================
> Author : Badr TAJINI - LLM Cybersecurity - ECE 2025/2026

**Goal.** Compare a naïve vs a secure-review prompt on 30 seeded code snippets. Produce JSON-only outputs and compute Precision/Recall/F1.

## Quick start
1) **Prereqs**: Node.js 22+ LTS, Python 3.11+ (3.11-3.13 supported), a Gemini API key (free via Google AI Studio).
2) **Install**:
```bash
# From repo root (llm-course/)
make install                           # Creates .venv at repo root
source .venv/bin/activate
cp .env.example .env                   # put your Gemini key here
npm i -g promptfoo@latest              # or: npx promptfoo@latest eval
cd labs/lab2
```
3) **Run eval**:
```bash
# HTML + JSON outputs
promptfoo eval -c promptfooconfig.yaml -o reports/lab2_report.html -o reports/lab2_results.json
```
4) **Score metrics**:
```bash
python tools/metrics.py reports/lab2_results.json reports/metrics.csv
```

## Files
- `prompts/baseline_prompt.txt` — naïve code-review prompt.
- `prompts/secure_review_prompt.txt` — schema-validated, security-focused prompt.
- `_generated/tests.yaml` — 30 tests with embedded code and ground-truth labels.
- `promptfooconfig.yaml` — providers, prompts, assertions, and tests config.
- `tools/metrics.py` — computes precision, recall, F1 for each prompt.
- `snippets/` — the raw code snippets used to build tests.

## Provider setup
Use a `.env` file:
```
GEMINI_API_KEY=PUT_YOUR_KEY_HERE
# or GOOGLE_API_KEY=...
MODEL_ID=google:gemini-2.5-flash
```
Per promptfoo docs, both `GEMINI_API_KEY` or `GOOGLE_API_KEY` are accepted for the Google provider.

## What you submit
- `reports/lab2_report.html` + `reports/metrics.csv`
- A 1‑page brief describing FP/FN patterns and at least 3 improvements to your prompt.

## References
- Google provider for promptfoo (API key env vars and model ids)
- Promptfoo getting started, outputs, JSON assertions, and custom JS assertions
- Gemini API quickstart and structured output best practices

See the course handout for the exact links.
