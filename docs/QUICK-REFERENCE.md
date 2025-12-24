# LLM Cybersecurity Labs — Quick Reference

> One-page command reference for all 4 labs and the final project.  
> Run these in order. Replace `<your-key>` with your actual Gemini API key.

---

## Common Setup (All Labs)

```bash
# Clone the repo (or unzip the bundle)
git clone https://github.com/btajini/<repo>.git
cd llm-course

# Verify you have Node 20+ and Python 3.9+
node --version    # should be v20.x or higher
python --version  # should be 3.9+
```

---

## Lab 1: Threat Modeling & Secure Prompting

```bash
cd starter-labs/llm-sec-lab1-starter/llm-sec-lab1

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GEMINI_API_KEY=<your-key>

# Run tests
python -m unittest discover tests

# Generate baseline report
python -m src.app
# Output: reports/baseline.json

# From repo root
make w01-day
```

**Deliverables**: `reports/baseline.json`, 2-page threat model PDF

---

## Lab 2: Secure Code Review Prompts + Eval

```bash
cd starter-labs/llm-sec-lab2-starter/llm-sec-lab2

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GEMINI_API_KEY=<your-key>

# Install promptfoo (requires Node 20+)
npm install -g promptfoo@latest

# Run tests
python -m unittest discover tests

# Option 1: Custom provider (no API cost, testing only)
npx promptfoo eval -c promptfooconfig_custom.yaml \
  -o reports/lab2_results.json \
  -o reports/lab2_report.html

# Option 2: Gemini Free Tier (slow but free)
source .env
python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 --delay 180
python merge_batch_results.py

# Calculate metrics
python tools/metrics.py reports/merged_results.json reports/metrics.csv

# View dashboard
npx promptfoo view reports/merged_results.json

# From repo root
make w02-day
```

**Deliverables**: `reports/merged_results.json`, `reports/lab2_report.html`, `reports/metrics.csv`, 1-page brief

---

## Lab 3: Config & IaC Security

```bash
cd starter-labs/llm-sec-lab3-starter/llm-sec-lab3

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GEMINI_API_KEY=<your-key>

# Run tests
python -m unittest discover tests

# Baseline scans
python scripts/run_checkov.py
python scripts/run_semgrep.py
# Outputs: reports/checkov.json, reports/semgrep.json

# After fixing issues
python scripts/run_checkov.py --after
python scripts/run_semgrep.py --after
# Outputs: reports/checkov_after.json, reports/semgrep_after.json

# From repo root
make w03-day
```

**Deliverables**: Before/after reports, LLM triage notes, MicroK8s observations (optional)

---

## Lab 4: Guardrails + Automated Red Team

```bash
cd starter-labs/llm-sec-lab4-starter/llm-sec-lab4

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GEMINI_API_KEY=<your-key>

# Run tests
python -m unittest discover tests

# Run unguarded baseline
python src/run_suite.py --mode unguarded --limit 50
# Output: reports/unguarded.json

# Run guarded comparison
python src/run_suite.py --mode guarded --limit 50
# Output: reports/guarded.json

# Calculate metrics
python src/metrics.py reports/unguarded.json reports/guarded.json reports/metrics.csv
# Output: reports/metrics.csv

# From repo root
make w04-day
```

**Deliverables**: `reports/unguarded.json`, `reports/guarded.json`, `reports/metrics.csv`, policy write-up

---

## Final Project: Secure RAG or Safe Agent

```bash
cd starter-project/llm-sec-final-project-starter

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GEMINI_API_KEY=<your-key>

# Run tests
python -m unittest discover tests

# Run your chosen track
python -m src.app --track rag     # Secure RAG
python -m src.app --track agent   # Safe Agent
# Output: logs/logs.jsonl

# Run promptfoo evaluation
npx promptfoo eval -c promptfooconfig.yaml \
  -o reports/results.json \
  -o reports/report.html

# Calculate metrics
python tools/metrics.py reports/results.json reports/metrics.csv

# From repo root
make project-test
```

**Deliverables**: `logs/logs.jsonl`, `reports/results.json`, `reports/report.html`, `reports/metrics.csv`, 3-5 page report

---

## Troubleshooting Cheat Sheet

| Issue | Quick Fix |
|-------|-----------|
| `429 Rate Limit` | Increase `--delay` to 240+ or use OpenRouter |
| `503 Server Error` | Retry; batch runner has automatic fallback |
| `API Key not found` | Check `.env` file, ensure `source .env` was run |
| `EBADENGINE` (Node) | Use `nvm use 20` before running promptfoo |
| `ModuleNotFoundError` | Activate venv: `source .venv/bin/activate` |
| Test failures | Run `pip install -r requirements.txt` again |

---

## Daily Workflow Summary

```bash
# Each day, from repo root:
make w01-day       # Lab 1: unit tests + model comparison reminder
make w02-day       # Lab 2: metrics tests + promptfoo reminder
make w03-day       # Lab 3: scanner tests + baseline/after reminder
make w04-day       # Lab 4: guardrails tests + suite reminder
make project-test  # Project: full tests + eval gates reminder
```

---

## Key Artifacts by Lab

| Lab | Must-Have Outputs |
|-----|-------------------|
| 1 | `reports/baseline.json`, threat model PDF |
| 2 | `reports/merged_results.json`, `metrics.csv`, HTML report, 1-page brief |
| 3 | `reports/checkov.json`, `semgrep.json`, triage notes |
| 4 | `reports/unguarded.json`, `guarded.json`, `metrics.csv` |
| Project | `logs/logs.jsonl`, `reports/results.json`, `metrics.csv`, 3-5 page report |

---

*Generated from course materials. Keep your API keys private. Happy hacking (ethically)!*
