# 🚀 LLM Security Labs — Crash-Test Speed Run

**Time to complete all 4 labs + project:** ~2-3 hours (excluding API wait times)  
**Prerequisites:** Python 3.11+, Node.js 22+ LTS, Gemini API key

---

## ⚡ One-Time Global Setup

```bash
# Clone the course repo (or use your existing copy)
cd ~/projects
git clone https://github.com/btajini/llm-course.git
cd llm-course

# Install dependencies (single venv for all labs)
make install
source .venv/bin/activate

# Configure API key
cp .env.example .env
# Edit .env and add: GEMINI_API_KEY=AIzaSy...your-key-here...
```

---

## 🧪 Lab 1 — Threat Modeling & Secure Prompting

**Estimated time:** 15 minutes

```bash
# Navigate (from repo root)
cd labs/lab1

# Run baseline (uses root .env and .venv)
python -m src.app
# → Creates reports/baseline.json

# Run tests (from repo root)
cd ../..
make w01-day
# → All tests should pass

# Quick validation
cat labs/lab1/reports/baseline.json | head -50
```

**✅ Success:** `reports/baseline.json` has valid JSON with `llm_risks` and `findings`

**📤 Deliverables:**
- `reports/baseline.json`
- 2-page threat model (your analysis)

---

## 🔍 Lab 2 — Secure Code Review Prompts

**Estimated time:** 45-60 minutes (mostly API wait time)

```bash
# Navigate (from repo root)
cd labs/lab2

# Node.js + promptfoo
nvm use 22 || nvm install 22
npm install -g promptfoo@latest

# Run evaluation (Gemini free tier - slow but free)
python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 \
  --delay 180

# Merge results
python merge_batch_results.py

# View report
npx promptfoo view reports/merged_results.json

# Generate metrics
python tools/metrics.py reports/merged_results.json reports/metrics.csv

# Run unit tests
python -m unittest discover tests
```

**⚡ Fast alternative (costs ~$0.02):**
```bash
# Add to .env: OPENROUTER_API_KEY=sk-or-...
python run_batches_simple.py \
  --config promptfooconfig_openrouter.yaml \
  --batch-size 10 \
  --delay 10
```

**✅ Success:** `reports/metrics.csv` shows precision/recall/F1 scores

**📤 Deliverables:**
- `reports/lab2_report.html`
- `reports/merged_results.json`
- `reports/metrics.csv`
- 1-page FP/FN analysis

---

## 🛡️ Lab 3 — Config & IaC Security

**Estimated time:** 20 minutes

```bash
# Navigate (from repo root)
cd labs/lab3

# Baseline scans (venv already active from setup)
python scripts/run_checkov.py
python scripts/run_semgrep.py

# Check findings count
grep -c '"result": "FAILED"' reports/checkov.json
python -c "import json; d=json.load(open('reports/semgrep.json')); print(f'{len(d.get(\"results\",[]))} findings')"

# Apply fixes (edit these files):
# - terraform/main.tf (S3 acl, security group CIDR)
# - k8s/deployment.yaml (privileged: false)
# - docker/Dockerfile (pin version, non-root user)

# Re-scan after fixes
python scripts/run_checkov.py
python scripts/run_semgrep.py

# Run tests (from repo root)
cd ../..
make w03-day
```

**✅ Success:** Re-scan shows fewer failed checks than baseline

**📤 Deliverables:**
- `reports/checkov.json` (before and after)
- `reports/semgrep.json` (before and after)
- Fix evidence table

---

## 🔴 Lab 4 — Guardrails & Red Team

**Estimated time:** 30 minutes

```bash
# Navigate (from repo root)
cd labs/lab4

# Run unguarded attacks (no protection)
PYTHONPATH=. python src/run_suite.py --mode unguarded --limit 10 --delay 12

# Run guarded attacks (with guardrails)
PYTHONPATH=. python src/run_suite.py --mode guarded --limit 10 --delay 12

# Calculate metrics
PYTHONPATH=. python src/metrics.py

# Run tests (from repo root)
cd ../..
make w04-day
```

**✅ Success:** `reports/metrics.csv` shows guarded block rate >> unguarded

**📤 Deliverables:**
- `reports/unguarded.json`
- `reports/guarded.json`
- `reports/metrics.csv`
- Attack analysis brief

---

## 🎓 Final Project — Secure RAG or Safe Agent

**Estimated time:** 45-60 minutes

```bash
# Navigate (from repo root)
cd project

# Test RAG track
python -m src.app --track rag --question "What is LLM01?"

# Test Agent track
python -m src.app --track agent --question "Add 12 and 30; cite the doc id"

# Run evaluation
npx promptfoo eval -c promptfooconfig.yaml \
  -o reports/report.html \
  -o reports/results.json

# Generate metrics
python tools/metrics.py reports/results.json reports/metrics.csv

# Run all unit tests (from repo root)
cd ..
make project-test
```

**✅ Success:** 
- JSON validity ≥ 95%
- Safety rate ≥ 85%
- Citation accuracy ≥ 80% (RAG track)

**📤 Deliverables:**
- `logs.jsonl` (replay log)
- `reports/report.html`
- `reports/results.json`
- `reports/metrics.csv`
- 3-5 page report

---

## 🏃 Full Speed Run (Copy-Paste Block)

```bash
# Clone and setup (one time)
cd ~/projects
git clone https://github.com/btajini/llm-course.git
cd llm-course
make install
source .venv/bin/activate
cp .env.example .env
# Add your GEMINI_API_KEY in .env

# Run all tests
make all  # Runs w01-day through w04-day + project-test

# Or run each lab individually:
make w01-day       # Lab 1: Threat Modeling
make w02-day       # Lab 2: Secure Code Review
make w03-day       # Lab 3: IaC Security
make w04-day       # Lab 4: Guardrails
make project-test  # Final Project
```

---

## 🔧 Makefile Targets (Alternative)

From repo root:

```bash
make help      # Show all targets
make venv      # Create venv only
make install   # Create venv + install deps
make clean     # Remove venv and caches
make test      # Run all tests
make all       # Run all daily workflows
```

---

## ⚠️ Troubleshooting Quick Fixes

| Issue | Fix |
|-------|-----|
| `EBADENGINE` npm error | `nvm use 22` |
| `429 Rate limit` | Increase `--delay` or use OpenRouter |
| `ModuleNotFoundError` | `source .venv/bin/activate` |
| `GEMINI_API_KEY not set` | Check `.env` file at repo root |
| Tests fail on import | Run from repo root with `make wXX-day` |
| JSON parse error | Check API response in `reports/` |

---

## ✅ Final Checklist

- [ ] Lab 1: `baseline.json` + threat model
- [ ] Lab 2: `metrics.csv` + HTML report + analysis
- [ ] Lab 3: Before/after scan JSONs + fix evidence
- [ ] Lab 4: Unguarded vs guarded + metrics
- [ ] Project: Both tracks working + report

**Total artifacts:** ~15 files across all labs

---

*Speed run complete. Now go secure some LLMs.* 🔒
