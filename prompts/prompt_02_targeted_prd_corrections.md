Work inside: "C:\Users\jamal\OneDrive - Bar-Ilan University - Students\Desktop\NextMind-ex02"
Do NOT write chapters, create PLAN.md/TODO.md/README.md, launch agents, run builds, or install software.

Apply one targeted correction pass to `PRD.md` (v1.1.0-draft):

1. Save this exact prompt to `prompts/` as the next numbered file, and back up `PRD.md` to `backups/PRD.v1.1.0-draft.bak.md`.
2. Edit `PRD.md` in place (preserve existing valid content, update revision history, check for contradictions):
   - **Deliverables:** List `PRD.md` (Basmala Jamal: requirements), `PLAN.md` (Maria Mnasra: phases, dependencies, owners, quality gates), `TODO.md` (Maria Mnasra: tasks, owners, status, evidence), and `README.md` (joint: overview, both authors, build/reproduction steps, screenshots, figures, real agent evidence).
   - **Ownership & Handoffs:** Basmala owns `PRD.md`; Maria owns `PLAN.md` & `TODO.md`; both approve major decisions. `Master` coordinates without replacing human ownership. `Research` researches & drafts content; `Design` handles LaTeX, layout, diagrams, and reproducible graphs. Define handoffs to prevent simultaneous edits.
   - **Scope Provenance:** Keep fueling & EV charging as core. Check disputed features against original Fuel&Go slides/PRD; cite slide/section or mark `"Unverified — pending source review"`. Never invent citations.
   - **Requirements vs. Team Choices:** Label the 5-agent setup and incident format as team workflow choices unless explicitly required by lecturer files (cite actual filenames/pages only; do not scan unrelated personal folders).
   - **Honest Status:** Replace premature `"Implemented / Tested"` with `"Planned — verification pending"` unless evidence exists; separate artifact type from completion status.
   - **Utility Setup:** Allow `agy-multi-agent-mesh/` locally without moving/modifying it, exclude it via `.gitignore`, and document the external dependency.
   - **25-Page Target:** Keep strictly at 25 English pages. Keep front/back matter inclusion unresolved; if 25 body pages are required, excluded parts are additional. Allow section rebalancing without forcing references/appendices into 1 page or hard-coding `"Page X of 25"`.
   - **Targets:** Replace arbitrary numbers with `"TBD — requires rationale and team approval"` + verification method; keep justified targets with sources.
   - **Preserve:** IEEE style, pending visual design, both authors, Detector/Fixer review & retesting, incident records, reproducible Python graphs, honest data provenance, real agent evidence, and `"Draft — Pending Team Review"` status.
3. Ensure `.gitignore` excludes `agy-multi-agent-mesh/`, commit all changes to `main`, and push to `https://github.com/jamalbasmala907-ship-it/NextMind_02.git`.

End with ONLY: (1) updated PRD & backup paths, (2) short Hebrew summary of fixes, (3) unresolved source limitations or team decisions. Do not print the full PRD or repeat this prompt.
