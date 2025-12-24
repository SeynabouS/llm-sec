Lab 2 Student Runbook — Secure Code Review Prompts + Eval
=======================================================
> Author : Badr TAJINI - LLM Cybersecurity - ECE 2025/2026

Goal: compare a naïve code-review prompt vs a security-hardened prompt on 30 seeded snippets using **promptfoo** + **Gemini**, then score precision/recall/F1.

---

## Table of Contents

1. [Prerequisites](#0-prerequisites)
2. [Getting the Starter](#1-getting-the-starter)
3. [Configure Environment](#2-configure-environment)
4. [Run Evaluation (3 Options)](#3-run-the-evaluation)
5. [Analyze Results](#4-analyze-results)
6. [Score Metrics](#5-score-metrics)
7. [Troubleshooting](#6-troubleshooting)
8. [Deliverables](#deliverables-checklist)

---

## 0. Prerequisites (do these before class)

- **Python 3.11+** installed locally (3.11-3.13 supported)
- **Node.js 22+ LTS** — For promptfoo eval
- A Google **Gemini API key** from [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Basic terminal and Git familiarity

Optional but recommended:

- Visual Studio Code or another editor with Jupyter support.
- A GitHub account if you plan to push lab artifacts to a remote repo.
- GitHub CLI (`gh`) for pushing from command line.
- OpenRouter API key for faster evaluations.

---

## 1. Getting the starter

### Option A — Clone the course repository

```bash
git clone https://github.com/btajini/llm-course.git
cd llm-course
```

### Option B — Professor shares a ZIP archive

```bash
unzip llm-course.zip -d ~/projects
cd ~/projects/llm-course

git init
git branch -m main
git add .
git commit -m "Initial commit"
```

Publish to GitHub:

- **GitHub CLI (recommended)**
  ```bash
  gh auth login
  gh repo create <your-username>/llm-course --private --source=. --remote=origin --push
  ```
- **Manual git**
  ```bash
  git remote add origin https://github.com/<your-username>/llm-course.git
  git push -u origin main
  ```

`.gitignore` already excludes `.env` and notes, so only the starter is tracked.

---

## 2. Configure environment

The course uses a **single shared venv** at the repository root:

```bash
# From repo root (llm-course/)
make install                    # Creates .venv and installs all dependencies
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1

# Configure API key (at repo root)
cp .env.example .env            # Add GEMINI_API_KEY and (optional) OPENROUTER_API_KEY

# Node.js 22+ + promptfoo (skip if already installed)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # load nvm
nvm install 22
nvm use 22
npm install -g promptfoo@latest

# Navigate to Lab 2
cd labs/lab2
```

If you prefer not to install globally, run `npx promptfoo@latest eval ...` **after** `nvm use 22`. Older Node (v18) will fail with EBADENGINE/better-sqlite3 errors.

---

## 3. Run the evaluation

### Understanding Deterministic vs Probabilistic Evaluation

| Type | Meaning | Example |
|------|---------|---------|
| **Deterministic** | Same input → **always** same output | Custom provider: rule-based pattern matching. Run 100 times, get 100 identical results. |
| **Probabilistic** | Same input → **variable** output | Real LLMs (Gemini, OpenRouter): temperature, sampling, model state cause variance. Run 100 times, get slightly different results each time. |

**Why this matters:**
- Use **Custom (deterministic)** to validate your setup and CI pipelines — 100% reproducible
- Use **Gemini/OpenRouter (probabilistic)** to test real-world performance — expect some variance in results
- Document differences in your brief to show you understand LLM behavior

### OpenRouter Free Tier: Important Pricing Note

> **Source**: [OpenRouter FAQ - Free Tier Options](https://openrouter.ai/docs/faq#what-free-tier-options-exist)

| Status | Rate Limit | Notes |
|--------|------------|-------|
| **New user (no purchase)** | 50 requests/day total | Very limited, for testing only |
| **After buying $10 credits** | 1000 requests/day on free models | Sufficient for this course |

⚠️ **Recommendation**: Purchase $10 credits once to unlock 1000 req/day. The credits themselves last forever and free models don't consume them — you just need the purchase to unlock higher limits.

---

### Option 1: Gemini Free Tier (Recommended)

**Best for**: Students using Google AI Studio free tier

```bash
source .env

python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 \
  --delay 180
```

**What this does**:
- Splits 30 tests into 15 batches (2 tests each)
- Waits 180 seconds between batches (avoids rate limits)
- Auto-switches to fallback models if Google servers are overloaded
- Takes ~47 minutes total

**After completion**, merge and view results:

```bash
python merge_batch_results.py
npx promptfoo view reports/merged_results.json
```

### Option 2: OpenRouter (Fastest)

**Best for**: Speed and reliability (small cost ~$0.02)

```bash
# Add OPENROUTER_API_KEY to your .env first!
source .env

python run_batches_simple.py \
  --config promptfooconfig_openrouter.yaml \
  --batch-size 10 \
  --delay 10
```

Takes ~4 minutes with no rate limit issues.

### Option 3: Custom Deterministic (Testing)

**Best for**: Testing the evaluation pipeline without API costs

```bash
npx promptfoo eval \
  -c promptfooconfig_custom.yaml \
  -o reports/lab2_results.json \
  -o reports/lab2_report.html
```

Uses rule-based detection (not a real LLM), but validates your setup works.

---

## 4. Analyze results

### Comprehensive Analysis

```bash
python tools/analyze_results.py
```

Shows:
- Per-batch pass/fail status
- Overall success rate (aim for >85%)
- Error breakdown (429, 503, JSON, accuracy)
- Fix recommendations

### Detailed Failure Analysis

```bash
python tools/analyze_results.py --failures-only
```

Shows each failed test with:
- Code snippet and expected result
- Model's actual output
- Root cause analysis
- Suggested fixes

### Raw Output Inspection

```bash
python tools/analyze_results.py --raw 10    # Check batch 10
```

Useful for debugging JSON format issues.

---

## 5. Score metrics

```bash
python tools/metrics.py reports/merged_results.json reports/metrics.csv
```

`reports/metrics.csv` lists TP/FP/TN/FN plus precision/recall/F1 for the secure prompt.

---

## 6. Troubleshooting

### Error 429: Rate Limit

**Cause**: Too many requests to Google AI Studio (free tier: 15 RPM)

**Fix**:
```bash
# Increase delay between batches
python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 \
  --delay 240    # 4 minutes instead of 3

# Or use OpenRouter (no rate limits)
python run_batches_simple.py \
  --config promptfooconfig_openrouter.yaml \
  --batch-size 10 \
  --delay 10
```

### Error 503: Model Overloaded

**Cause**: Google servers are overloaded (not your fault!)

**Fix**: The batch runner automatically tries fallback models:
1. `google:gemini-2.0-flash-lite`
2. `google:gemini-1.5-flash`
3. `google:gemini-2.5-pro`

If all fail, use OpenRouter instead.

### JSON Parse Errors

**Cause**: Model returned malformed JSON

**Fix**:
```bash
# Check the raw output
python tools/analyze_results.py --raw <batch_number>

# Retry specific batch
python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 \
  --delay 180 \
  --start <batch_number> \
  --end <batch_number>
```

### Accuracy Errors (Wrong Classification)

**Cause**: Model said "safe" when code was vulnerable (or vice versa)

**This is expected!** It shows the prompt's limitations. Document these in your brief.

### Start Fresh

```bash
python tools/cleanup.py --force
```

Removes all batch results for a clean slate.

---

## 7. Run automated checks

The starter ships with regression tests for `tools/metrics.py`.

```bash
python -m unittest discover tests
# or, from repo root
make w02-day
```

`make w02-day` mirrors the GitHub Actions workflow (`.github/workflows/lab2-tests.yml`).

---

## 8. Publish updates

```bash
git status -sb          # look for lines starting with 'M '
git add <path>          # stage modified files you want synced
git commit -m "Describe your change"
git push                # upload to your private repo
```

Keep the repo private to protect your API keys and lab answers.

---

## DELIVERABLES CHECKLIST — What You Must Submit

### ⚠️ IMPORTANT: Track Your Prompt Improvements!

This lab is about improving prompts. You need to show WHAT you changed and WHY it helped.

### Files to Create:

| File | Description | When to Create |
|------|-------------|----------------|
| `reports/merged_results.json` | Combined evaluation results | After running all batches |
| `reports/lab2_report.html` | Interactive dashboard | Generated by promptfoo |
| `reports/metrics.csv` | Precision/recall/F1 scores | After running metrics.py |

### Document to Write:

**1-Page Analysis Brief** (`reports/brief.md` or PDF) must include:

| Section | What to Write |
|---------|---------------|
| **1. Evaluation Summary** | How many tests? What overall precision/recall? |
| **2. False Positives** | Which safe code was flagged as vulnerable? Why did the prompt fail? |
| **3. False Negatives** | Which vulnerable code was missed? What CWE categories? |
| **4. Prompt Improvements** | What changes did you make to the prompts? Show before/after examples |
| **5. Limitations** | What can't the LLM reliably detect even with good prompts? |

### Prompt Improvement Evidence:

In your brief, show specific examples:

```markdown
## Prompt Improvement Example

### BEFORE (naive prompt):
"Review this code for security issues"

### AFTER (improved prompt):  
"Act as a security auditor. Analyze this code for vulnerabilities.
Return JSON with: {vulnerable: boolean, cwe: string, evidence: string, line: number}"

### Result:
- False positives reduced from 8 to 3
- Precision improved from 0.65 to 0.82
```

### Before Submitting, Verify:

```bash
# From repo root:
make w02-day

# Check your reports folder:
ls reports/
# Should show: merged_results.json, lab2_report.html, metrics.csv

# Verify metrics.csv has scores:
cat reports/metrics.csv
```

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `promptfooconfig_gemini_free_tier.yaml` | Gemini Free Tier config |
| `promptfooconfig_openrouter.yaml` | OpenRouter config (fastest) |
| `promptfooconfig_custom.yaml` | Deterministic testing |
| `run_batches_simple.py` | Batch runner with smart error handling |
| `merge_batch_results.py` | Combine batch results |
| `tools/analyze_results.py` | Observability & analysis |
| `tools/cleanup.py` | Clean up for fresh run |
| `tools/metrics.py` | Calculate precision/recall/F1 |

---

## Quick Command Reference

```bash
# Full workflow
source .env
python tools/cleanup.py --force                           # Clean previous run
python run_batches_simple.py \
  --config promptfooconfig_gemini_free_tier.yaml \
  --batch-size 2 --delay 180                              # Run evaluation
python tools/analyze_results.py                           # Check results
python merge_batch_results.py                             # Merge batches
python tools/metrics.py reports/merged_results.json \
  reports/metrics.csv                                     # Calculate metrics
npx promptfoo view reports/merged_results.json            # View dashboard
```

---

Happy triaging!
