Lab 1 — Threat Model + First Secure Prompts (Gemini + Gandalf/RedArena)
=======================================================
> Author : Seynabou SOUGOU, Maxime XU - LLM Cybersecurity - ECE 2025/2026

Ce README decrit ce que nous avons realise et ou trouver les preuves.

## Ce que nous avons fait
- Capture du baseline avant/apres durcissement des invites.
- Observation d'attaques via Gandalf et RedArena, puis prise de notes.
- Redaction du modele de menace et synthese des risques.

## Artefacts
- `reports/baseline_before.json`, `reports/baseline_after.json`
- `reports/gandalf_notes.md`, `reports/redarena_notes.md`
- Dossier `reports/screenshots/` pour les captures utiles

## 0) Prereqs
- **Python 3.11+** (3.11-3.13 supported)
- A **Gemini API key** from Google AI Studio. Set env var `GEMINI_API_KEY`.
- Basic Git and terminal usage.

## 1) Setup
```bash
# From repo root (llm-course/)
cp .env.example .env              # put your API key in .env
make install                      # Creates .venv at repo root
source .venv/bin/activate         # Windows: .venv\Scripts\activate
cd labs/lab1
python -m src.app                 # runs a baseline over data/prompts_lab1.json
```

## 2) What you will do
1. Obtain a Gemini key, confirm a first call.
2. Play **Gandalf** to observe jailbreak patterns.
3. Map observed tactics to **OWASP LLM Top-10** and **MITRE ATLAS**.
4. Run the baseline pipeline: input → filter → Gemini → **JSON schema** → report.
5. Submit: 2‑page threat model PDF + repo with your notes and baseline results.

## 3) Deliverables
- `reports/gandalf_notes.md`
- `reports/baseline.json` + brief summary in `README.md`
- Threat model (2 pages) as PDF inside `reports/`

## 4) References
- Gemini quickstart & API keys: https://ai.google.dev/gemini-api/docs/quickstart
- OWASP LLM Top‑10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- MITRE ATLAS: https://atlas.mitre.org/
- Gandalf: https://gandalf.lakera.ai/  • RedArena: https://redarena.ai/

## 5) Notes
- Model outputs are **untrusted** until validated. This template enforces **JSON** via Pydantic.
- Keep your API key **out** of Git. `.env` is ignored by default.
