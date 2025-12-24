# LLM Cybersecurity Course — Student Guide

> **Author:** Prof. Badr TAJINI — ECE 2025/2026

---

## START HERE — Read This First!

Welcome to the LLM Cybersecurity course. This page explains **how to navigate** the course materials. If you're confused, come back here.

---

## Understanding the README Files

**There are multiple README files. Each has a different purpose:**

| File | Location | Purpose | Who Should Read |
|------|----------|---------|-----------------|
| **This README** | `/README.md` | Course overview, structure, grading | Everyone (start here) |
| **README-student.md** | Inside each lab folder | **Step-by-step instructions for that lab** | You, when working on that lab |
| **README.md** | Inside each lab folder | Technical reference, architecture details | You, if you need deeper understanding |

### IMPORTANT: Always Read README-student.md First!

When you start a lab, go to its folder and open `README-student.md`. That's your **step-by-step guide**.

```
Example for Lab 1:
  labs/lab1/README-student.md  ← READ THIS
  labs/lab1/README.md          ← Reference only
```

---

## Course Structure

```
llm-course/
├── README.md                    ← YOU ARE HERE (course overview)
├── requirements.txt             ← Unified dependencies for all labs
├── .env.example                 ← Copy to .env and add your API key
├── Makefile                     ← Run "make w01-day" etc. to test your work
├── .venv/                       ← Single virtual environment (created by make venv)
├── docs/                        ← Additional guides and summaries
│   ├── CRASH-TEST-SPEEDRUN.md   ← Quick commands for all labs
│   ├── QUICK-REFERENCE.md       ← Command cheat sheet
│   └── ...
├── labs/                        ← THE 4 LABS
│   ├── lab1/                    ← Lab 1: Threat Modeling
│   ├── lab2/                    ← Lab 2: Secure Code Review
│   ├── lab3/                    ← Lab 3: Config & IaC Security
│   └── lab4/                    ← Lab 4: Guardrails & Red Team
└── project/                     ← FINAL PROJECT
```

---

## The Golden Rule: BEFORE → AFTER → COMPARE

**Every lab follows this pattern. Memorize it:**

```
┌─────────────────────────────────────────────────────────────────┐
│  1. CAPTURE BEFORE STATE                                        │
│     → Run the baseline                                          │
│     → Save output with "_before" or "baseline" name             │
│                                                                 │
│  2. MAKE YOUR IMPROVEMENTS                                      │
│     → Edit prompts, policies, code                              │
│     → Apply what you learned                                    │
│                                                                 │
│  3. CAPTURE AFTER STATE                                         │
│     → Run again                                                 │
│     → Save output with "_after" or "final" name                 │
│                                                                 │
│  4. WRITE ANALYSIS                                              │
│     → Compare before vs after                                   │
│     → Explain what improved and why                             │
└─────────────────────────────────────────────────────────────────┘
```

**If you don't save the BEFORE state, you can't prove you improved anything!**

---

## Lab Overview

| Lab | Topic | Key Deliverables | Makefile Target |
|-----|-------|------------------|-----------------|
| **Lab 1** | Threat Modeling & Secure Prompting | `baseline_before.json`, `baseline_after.json`, threat model PDF | `make w01-day` |
| **Lab 2** | Secure Code Review Prompts | `metrics.csv`, HTML report, 1-page analysis | `make w02-day` |
| **Lab 3** | Config & IaC Security | `checkov.json` → `checkov_after.json`, fix evidence | `make w03-day` |
| **Lab 4** | Guardrails & Red Team | `unguarded.json`, `guarded.json`, metrics comparison | `make w04-day` |
| **Project** | Secure RAG or Safe Agent | Full app, evaluation suite, 3-5 page report | `make project-test` |

---

## How to Start Each Lab

### Step 1: Navigate to the lab folder
```bash
cd labs/lab1  # For Lab 1
```

### Step 2: Open README-student.md
```bash
# Read it in VS Code, or:
cat README-student.md
```

### Step 3: Follow the instructions exactly
The README-student.md tells you:
- How to set up the environment
- What commands to run
- What files to create
- What to submit

### Step 4: Validate your work
```bash
# From the repo root:
make w01-day   # For Lab 1
make w02-day   # For Lab 2
# etc.
```

---

## Environment Setup (One Time)

### Prerequisites
- **Python 3.11+** — Check: `python --version` (3.11-3.13 supported)
- **Node.js 22+ LTS** — For promptfoo (Labs 2, Project). Check: `node --version`
- **Git** — For version control
- **Gemini API Key** — From [Google AI Studio](https://aistudio.google.com/apikey)

### Quick Setup (From Repository Root)
```bash
# 1. Clone and enter the repository
git clone <your-repo-url>
cd llm-course

# 2. Create virtual environment and install dependencies
make install    # Creates .venv and installs all packages

# 3. Configure API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 4. Activate the environment
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
```

### Manual Setup (If make doesn't work)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Grading Structure

| Component | Weight | Description |
|-----------|--------|-------------|
| **Lab 1** | 12.5% | Threat modeling + secure prompting |
| **Lab 2** | 12.5% | Secure code review evaluation |
| **Lab 3** | 12.5% | IaC scanning + LLM triage |
| **Lab 4** | 12.5% | Guardrails + red team metrics |
| **Final Project** | 50% | Complete secure application + report |

### What Gets Graded

For **every** lab, you need:
1. ✅ **Before/After evidence** — Proving your improvements worked
2. ✅ **Technical artifacts** — JSON outputs, metrics CSV, etc.
3. ✅ **Written analysis** — Explaining what you did and why

---

## Makefile Commands Reference

Run these from the **repository root** (not inside lab folders):

```bash
make w01-day       # Run Lab 1 tests + show model comparison artifacts
make w02-day       # Run Lab 2 metrics tests
make w03-day       # Run Lab 3 Checkov/Semgrep tests
make w04-day       # Run Lab 4 guardrails tests
make project-test  # Run Final Project tests
```

These commands validate your work. **Run them before submitting.**

---

## Free Resources

| Resource | Purpose | Link |
|----------|---------|------|
| **Gemini API** | LLM for all labs | [Google AI Studio](https://ai.google.dev/) |
| **Gandalf** | Jailbreak practice (Lab 1) | [gandalf.lakera.ai](https://gandalf.lakera.ai/) |
| **RedArena** | Red team challenges (Lab 1) | [redarena.ai](https://redarena.ai/) |
| **promptfoo** | LLM evaluation | [promptfoo.dev](https://www.promptfoo.dev/) |
| **Checkov** | IaC scanning (Lab 3) | [checkov.io](https://www.checkov.io/) |
| **Semgrep** | Code scanning (Lab 3) | [semgrep.dev](https://semgrep.dev/) |
| **OWASP LLM Top 10** | Risk framework | [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| **MITRE ATLAS** | AI threat taxonomy | [atlas.mitre.org](https://atlas.mitre.org/) |

---

## Common Questions

### "Which README do I read?"
→ **README-student.md** in the lab folder. That's your guide.

### "What do I submit?"
→ Check the **Deliverables Checklist** at the bottom of each README-student.md.

### "How do I know if I'm done?"
→ Run `make wXX-day` (e.g., `make w01-day` for Lab 1). All tests should pass.

### "I'm getting API errors"
→ Check your `.env` file has the correct `GEMINI_API_KEY`. Use `source .env` before running.

### "The JSON is malformed"
→ The model sometimes wraps JSON in markdown. The starter code handles this. If it still fails, reduce temperature or simplify your prompt.

---

## Quick Links

| Lab | README-student Location |
|-----|------------------------|
| Lab 1 | `labs/lab1/README-student.md` |
| Lab 2 | `labs/lab2/README-student.md` |
| Lab 3 | `labs/lab3/README-student.md` |
| Lab 4 | `labs/lab4/README-student.md` |
| Project | `project/README-student.md` |

---

## Additional Documentation

For more details, see the `docs/` folder:

### Recommended Reading for Students

| Document | Purpose | Priority |
|----------|---------|----------|
| **`docs/summary-lab*-human.md`** | Human-friendly lab summaries (one per lab) | ⭐ High |
| **`docs/STUDENT-CAREER-GUIDE.md`** | How this course impacts your career | ⭐ High |
| **`docs/llm-course-mindmap.html`** | Visual overview of the course | ⭐ High |
| **`docs/QUICK-REFERENCE.md`** | Command cheat sheet for all labs | Medium |
| **`docs/CRASH-TEST-SPEEDRUN.md`** | Fast-path commands for testing | Medium |
| **`docs/COURSE-SUMMARY-SHAREABLE.txt`** | Plain text course summary (shareable) | Optional |

---

## Safety & Ethics

- **Never use real secrets** — Use placeholder API keys and test data
- **Treat model output as untrusted** — Always validate and sanitize
- **Don't run exploit code** — Use simulated targets only
- **Keep your work private** — Don't share API keys or solutions

---

**Questions?** Ask your professor or teaching assistant. Good luck! 
