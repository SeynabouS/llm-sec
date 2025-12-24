# Lab 4 — Guardrails + Automated Red Team

**Author**: Badr TAJINI | LLM Cybersecurity | ECE 2025/2026

---

Lab 4 is where everything shifts from "can we detect problems?" to "can we keep an automated system from hurting itself even when someone is actively trying to trick it?" The starter gives students two versions of the same evaluation suite: one with no guardrails (unguarded) and one that wraps every prompt and response with policies, regex filters, and structured schemas (guarded). Their mission is to run both versions, compare the outcomes, and then iterate until the guarded run either blocks or clearly labels every malicious attempt.

The setup follows the familiar ritual. Students clone or unzip the lab, create a virtual environment, install requirements, and drop their Gemini API key into the environment file. The README explains what "guardrails" mean in this context: input rules that block instruction overrides, output scanning for secrets or unsafe content, and schema checks that force the model to return JSON.

The red team is where students meet the adversary. The lab ships with a curated set of adversarial prompts lifted from real jailbreak challenges—things like "Ignore all prior instructions" or "Summarize the secret training data." Students run the unguarded suite to see how the raw model behaves: most of the time it leaks, hallucinates, or simply follows the attacker's instructions. That unguarded output file becomes the baseline showing just how bad things can get without protection.

Applying guardrails is the next step. Students run the same attacks through the guardrails module, which checks inputs with regex to deny typical jailbreak phrases, cleans outputs, enforces JSON structure, and logs every decision. They tweak those guard rules, maybe add heuristics for new attack patterns, until the model either refuses or clearly labels the output as unsafe. The logs and guarded output file give them evidence of what changed.

Measuring the impact is what makes the lab persuasive. A metrics script generates side-by-side statistics: refusal rate, unsafe completions, latency, and more. The deliverables expect a concise narrative: "Without guardrails we saw X percent secret leaks; with guardrails we blocked Y percent and any remaining outputs were flagged as unsafe."

The automation keeps everyone disciplined. A Make target runs the lab's unit tests every session and prints reminders of the two key commands. GitHub Actions mirrors that flow, running the tests in the lab directory so regressions get caught immediately.

In short, Lab 4 shows that secure LLMs aren't just about better prompts; they rely on layered guardrails, logging, and metrics. Students learn to treat the model like any other untrusted component: you wrap it, monitor it, and prove with data that the guardrails are doing their job. They finish with a concrete portfolio piece—before-and-after reports plus a metrics CSV—that demonstrates they can operationalize safety decisions, not just theorize about them.

---

## How This Translates to Industry Roles

**Financial-Services Chatbot Guardianship**

Think of the chatbot as a new employee in a bank branch. You would never put them in front of customers without checking how they answer trick questions about passwords or transfers. A bank wants to let customers ask a wealth-advisor chatbot about investments. Regulators demand proof the chatbot will not leak account data or obey dangerous instructions. The security team runs the Lab 4 suite and pastes the unguarded-versus-guarded block-rate chart into their model-risk memo.

The same CSV you generate in this lab becomes a story: "Without guardrails, the bot leaked X percent of secrets; with guardrails, that dropped to Y percent." People who sign off on risk need exactly this kind of before-and-after picture.

**SOC Automation Engineer**

Imagine a security team as firefighters. They do practice drills not only to fight fires but to test that alarms and hoses still work after upgrades. Security Operations Centers now run "LLM purple-team" scripts every week. They replay their top 50 internal attack prompts and watch a small dashboard built from the Lab 4 metrics. If block rates fall after a model update, the on-call engineer is paged to roll back or tighten policies.

Your habit of logging why each prompt was blocked or not makes upgrades safer. It's the difference between "we hope nothing broke" and "we can prove the new version is at least as safe as the old one."
