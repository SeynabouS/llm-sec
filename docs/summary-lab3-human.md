# Lab 3 — Config & IaC Security

**Author**: Badr TAJINI | LLM Cybersecurity | ECE 2025/2026

---

Lab 3 puts an LLM on top of traditional scanners so it feels like you have a diligent security analyst helping you triage mountains of findings. Instead of poking at prompts one at a time, students run real tools—Checkov for infrastructure-as-code and Semgrep for application code—to produce JSON reports that can be overwhelming in raw form. The starter shows them how to automate those scans, capture "before" versus "after" states, and then use Gemini to highlight what truly matters.

The workflow starts the same way as earlier labs: clone or unzip, set up the virtual environment, install dependencies, configure the environment file with your Gemini key. The README also includes an optional section on installing MicroK8s, a lightweight Kubernetes distribution for students who want to deploy a tiny cluster locally and mimic real cloud infrastructure. That section is explicitly optional because not everyone has the resources or time, but it adds valuable realism for those who pursue it.

The baseline scans are the foundation of this lab. Two helper scripts run Checkov and Semgrep twice each: once against the unmodified sample code to establish a baseline, and once after students apply fixes or policy changes. Each run saves JSON summaries in the reports directory so you can compare how many issues were found before and after your mitigation. This before-and-after comparison is central to the lab's message: security isn't about running a tool once; it's about measuring improvement over time.

LLM-assisted triage is where things get interesting. The JSON from Checkov and Semgrep can be unwieldy, so the starter includes routines that feed the key findings into Gemini along with context that nudges it toward good behavior. The model learns to cite policies, explain severity, and suggest mitigations only when confident. Students tune these prompts so the model flags obvious false positives, groups related issues, and writes plain-language summaries that developers can actually act on without drowning in raw scanner output.

For students who want extra realism, the optional MicroK8s loop lets them spin up a local cluster, deploy the vulnerable IaC, re-run Checkov against a live environment, and see whether their mitigations hold up. It's framed as a stretch goal; the core grading happens even if everything runs on plain files.

The deliverables include before-and-after reports, LLM-generated triage notes, optional MicroK8s observations, and a short narrative explaining what changed, why certain findings were real or false positives, and how Gemini helped prioritize. Students also document lessons learned so they can explain, non-technically, what the LLM contributed versus what the scanners already told them.

In plain language, Lab 3 teaches that classic static tools are powerful but noisy, and an LLM—if guided carefully—can act like the first-level analyst who sifts through the noise. Students leave with the confidence to run Checkov and Semgrep on new repos, feed the results into a templated LLM workflow, and produce concise security summaries backed by raw scanner evidence.

---

## How This Translates to Industry Roles

**Cloud Security Architect Validating Landing Zones**

Imagine checking a new house before your family moves in. You walk through each room with a checklist: do the windows lock? Is the smoke detector working? Is the front door solid? Lab 3 applies that same idea to cloud accounts and configuration files. An enterprise stands up a new AWS landing zone, and before any production workload goes in, the architect runs Checkov plus Semgrep, dumps the JSON into the Lab 3 script, and shares the LLM summary with executives. The report says, "These 7 controls failed, here is the exact file and line, here is the impact in simple words."

The before-and-after JSON helps leaders decide whether they're comfortable moving in or need to delay the migration. The MicroK8s practice is like testing the fire alarms in a model house before touching the real building.

**Platform Engineering "Security Champions"**

Think of platform engineers as the city planners of a tech company. They don't own every house, but they maintain the roads, electricity, and water. Platform teams manage shared Kubernetes clusters for many product teams. Every night they run the Lab 3 scripts and post a short Slack digest: "We found 3 serious misconfigurations across all teams, here is what they mean, here is where to fix them." Each item links back to the raw JSON for verification.

Your ability to turn long scanner output into a friendly daily message—one that developers can actually act on—is what separates effective security champions from teams that just forward raw tool logs.
