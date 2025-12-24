# Final Project — Secure RAG & Safe Agent

**Author**: Badr TAJINI | LLM Cybersecurity | ECE 2025/2026

---

The final project is where students stop working with tidy lab demos and build something that feels like a miniature product. They receive a starter that contains two possible tracks—Secure RAG (retrieval-augmented generation) and Safe Agent—but they must pick one and finish it to a standard that could pass a lightweight security review.

When you open the starter, you see a single directory with both tracks living side by side. There's one entry point that accepts a track argument, so students don't have to maintain two separate repos. Shared guardrails, logging, and schema validation live in a common module. The README spells out the expectations, deliverables, and daily workflow: run unit tests via the Make target, then run promptfoo and metrics.

The Secure RAG track focuses on grounded responses. A small corpus of reference documents lives in the data directory. The model must answer questions strictly using those texts, citing which files back each claim. The pipeline uses TF-IDF retrieval to pick the most relevant snippets, then the model produces a JSON response with an answer, citations, safety flag, and rationale. Guards ensure it labels anything risky as unsafe. Logs are written to a JSONL file for later replay. Students tune the guardrails, expand the corpus, craft better prompts, and run evaluations until the metrics show high citation accuracy and low unsafe answers. They also write a mini report explaining how the system defends against prompt injection and hallucinations.

The Safe Agent track focuses on controlled actions. The agent is only allowed to call two tools: search_corpus to read local documents and calc to perform math. It must finish within three steps and return a JSON payload that includes the step transcript. Students refine how the agent decides when to use a tool, how it handles malicious inputs like "ignore the rules," and how it documents every step for auditing. They might add extra policies, such as rejecting tool requests that don't cite specific questions. Their job is to analyze transcripts, prove the agent never strays outside the allow-list, and document how the guardrails respond to classic jailbreak tactics.

Both tracks share common expectations. Automation parity with earlier labs means the Make target runs the project's unit tests (mocked Gemini calls for RAG, agent, and entrypoint) and prints reminders to run promptfoo plus metrics. GitHub Actions runs the same suite in CI, so instructors see a green badge before merging.

Evidence and metrics are mandatory. Students must run the promptfoo evaluation and then the metrics script to generate an HTML report, JSON results, and a CSV file. Gates enforce minimum JSON validity, safety, and citation rates; students must tune prompts and guards until those thresholds pass on CI.

Every call goes to a JSONL log file, which serves as a replay log for grading. Students include it in their submission to prove exactly how the model behaved. The final deliverables go beyond code: in addition to logs, they submit a 3 to 5 page report covering the threat model, design decisions, evaluation results, OWASP and ATLAS mapping, and the failures and fixes they encountered.

In short, the project takes everything practiced in Labs 1 through 4—prompt hardening, metrics, guardrails, and CI discipline—and rolls it into a single, higher-stakes deliverable. By the end, students can say, "I built, tested, and documented a mini secure LLM system from end to end," whether that system retrieves knowledge safely or acts like a tightly controlled agent.

---

## How This Translates to Industry Roles

**Secure RAG for Policy and Compliance Teams**

Picture a big company with thousands of pages of HR and cloud policies. People are tired of digging through PDFs, so they ask, "Can we have a chatbot that answers policy questions for us?" Fortune 100 companies are rolling out internal copilots that answer HR or cloud-policy questions. They expect the assistant not only to answer but also to say, "This comes from page 12 of the security handbook."

Engineers mirror the Secure RAG track from your project. They index the documents, force the model to return JSON with citations, and set CI gates that fail if the bot stops citing or starts hiding risky answers. When auditors ask, "How do you know the bot didn't invent this rule?", teams literally hand over the promptfoo HTML and the results JSON and metrics CSV you learned to create. What feels like a school exercise here is exactly what unblocks real deployments.

**Safe Agent for SOC Copilots**

Think of the Safe Agent as a junior analyst who is only allowed to follow written playbooks and use a small set of tools, never to improvise on production systems. Security operations centers want a "playbook runner" agent that only calls approved tools—search-corpus for IOCs, calc for simple math—and never exceeds three steps. During audits, they must show every tool invocation: what the agent asked, which tool it used, and what it did with the result.

Your logs and JSON transcript design are the blueprint for that audit trail. The step-by-step transcripts you define are not busywork. They become the story the SOC tells future managers and regulators: "Here is exactly how the bot behaved, here are the guardrails, and here is where humans still review decisions."
