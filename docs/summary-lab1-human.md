# Lab 1 — Threat Modeling & Secure Prompting

**Author**: Badr TAJINI | LLM Cybersecurity | ECE 2025/2026

---

Lab 1 serves as the gateway from treating LLMs as a novelty to approaching them with the discipline of a security engineer. Students begin by setting up the secure starter project, wiring their Gemini API key, and running both command-line and notebook baselines across several Gemini model tiers. The experience teaches them to document refusals, validate JSON schema output, and archive how each model behaves differently—whether it's the quick Flash variant, the lighter Flash-Lite, or the more deliberate Pro tier. By forcing notebook evidence capture and warm-up exercises with tools like Gandalf and RedArena, the lab ensures students don't just run code; they think about attacks and defenses from minute one.

The deliverables tell the story of what students actually learn. They produce baseline JSON files that capture model responses, comparison notes that explain why one tier refused a prompt while another did not, schema-compliant transcripts that prove the output met validation rules, and a two-page threat model that ties everything together. The underlying lesson is simple but often overlooked: prompt engineering only counts when the evidence is repeatable and auditable by another security engineer. If you can't hand someone your artifacts and have them reproduce your findings, you haven't proven anything.

---

## How This Translates to Industry Roles

**Product Security Prompt Engineer (2025 Copilot Launch)**

Think of a coding copilot as a new pilot flying passengers for the first time. No airline would let them take off without many test flights in a simulator. The same logic applies to companies shipping internal coding assistants. Before launch, the product security team runs something very similar to Lab 1 every night: a fixed list of jailbreak prompts, secret-stealing questions, and strange instruction chains. They keep the attacks consistent so they can compare model versions fairly and catch regressions before customers see them.

The JSON transcripts and model-comparison notes function like a flight log. When you tell risk and compliance teams, "We tested three Gemini tiers, here are the refusal rates, here are the dangerous prompts we blocked," they have something concrete to trust. Without that log, they simply say no to the launch because they have no evidence to evaluate.

**Managed Red-Team for LLM Platforms**

Imagine hiring a "friendly hacker" to test your house locks. They write a report saying, "This lock opens with a hairpin; this one is strong." Consulting firms now offer LLM Red Team services that work the same way. They copy the Lab 1 pipeline, plug in the client's chatbot, and run a full round of attacks. The result is a clear document explaining which prompts leaked secrets, which ones were blocked, and which parts of the policy need to change.

Customers in 2025 don't want vague answers like "we think the model is safe." They want the same kind of artifacts you produce in this lab: before and after JSON, a written threat model, and screenshots from tools like Gandalf or RedArena showing where the model still fails. Your ability to produce these materials is what makes you employable in this space.
