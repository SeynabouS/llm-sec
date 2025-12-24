# Lab 2 — Secure Code Review Prompts + Evaluation

**Author**: Badr TAJINI | LLM Cybersecurity | ECE 2025/2026

---

Lab 2 shifts the focus from "can the model refuse bad input?" to "can it help you triage piles of insecure code quickly without hallucinating fixes?" Students inherit a starter project that already connects promptfoo, an evaluation harness, to a set of code-review questions. Their job is to become the human in the loop who keeps the LLM honest. They craft prompts, filters, and refusal policies that make Gemini act like a conscientious security reviewer rather than a guessy autocomplete.

The daily routine is straightforward. Students set up the lab the same way as Lab 1: clone or unzip the private repo, create a virtual environment, install dependencies, copy the environment template, and paste in their Gemini API key. The README then walks them through running the daily guard check, which executes unit tests for the metrics tool and generates reports. Those reports come in two forms: an HTML dashboard for eyeballing results and a JSON log that feeds into the metrics calculator.

Promptfoo is the heart of this lab. Instead of randomly poking at the model, students define a suite of "evidence cards"—code snippets with known vulnerabilities, false positives, and injection attempts. The starter includes some seed tests, but learners are expected to expand them. After each evaluation run, they condense the JSON into CSV metrics covering precision, recall, and refusal rates. The unit tests ensure those CSV calculations don't silently regress by mocking promptfoo output and confirming the metrics file still reports the right columns.

The non-technical takeaway is that Lab 2 is an exercise in consistent, auditable code review. Students learn to ask, "How do I prove to a stakeholder that the LLM isn't inventing CVEs?" The answer lies in process: tuning templates to enforce JSON responses that cite CWE or OWASP entries, tightening the schema or adding refusal instructions when Gemini starts hallucinating patch commands, and comparing report artifacts across iterations to argue whether guardrails actually improved. Every promptfoo run produces an HTML report, JSON results, and a metrics CSV. Students compare these across iterations to build their case.

The deliverables force students to tell a story. They owe an HTML report, JSON results, a metrics CSV, and a one-page brief describing false positives, false negatives, and how they improved their prompts. This keeps them focused on narrative, not just raw numbers.

---

## How This Translates to Industry Roles

**DevSecOps Engineer Triaging CI/CD Scan Debt**

Picture a doctor's waiting room with hundreds of patients. If the doctor sees them in random order, some urgent cases wait too long while minor issues get all the attention. That's what unfiltered scanner output looks like. Most companies have thousands of unresolved static-analysis alerts piling up in GitHub. A DevSecOps engineer plugs the Lab 2 promptfoo config into their pipeline so every pull request generates a small HTML dashboard: "Here are the 5 findings that look real and serious; here are the noisy ones."

The metrics CSV becomes part of sprint planning. Product managers finally see which findings are high-confidence "patients" and which are low-priority noise. Instead of arguing about the tool, teams discuss facts.

**Managed Services Provider Delivering Secure Code Reviews**

Think of an MSP as a mechanic for software. Companies drop off their codebase and expect a clear checklist explaining what's broken and what's fine. Consulting firms now sell LLM-assisted code review. During onboarding, they drop in the Lab 2 tests, tune prompts for the client's main languages, and run promptfoo. The deliverable is an HTML report plus a CSV of metrics showing how often the model agreed with the ground truth.

Clients judge these firms on clarity and honesty. The precision and recall you compute is what lets a consultant say, "This AI helps us find 80% of the real issues with a low false-alarm rate. We still have humans check the rest." Your lab work is a practice version of that conversation.
