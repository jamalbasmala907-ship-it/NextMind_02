# Project Task Board (TODO): Fuel&Go — Assignment 02 Report

| Field | Value |
| --- | --- |
| **Project** | Fuel&Go Smart Fueling & EV Charging Platform (Assignment 02 Report) |
| **Team** | NextMind |
| **Partners** | Maria Mnasra, Basmala Jamal |
| **TODO & PLAN Owner** | Maria Mnasra (Planning, Task Governance & Active Report Production Lead for GitHub Sharing) |
| **PRD Specification Owner** | Basmala Jamal (Requirements & Scope Boundary Owner; Pulls Shared Work to Review/Revise & Prepare `README.md`) |
| **Active Human Work Agreement** | Maria leads report production & prepares GitHub sharing; Basmala pulls, reviews/revises, and prepares `README.md` (no new content claimed as Basmala-approved prior to her review) |
| **Joint Decision Authority** | Maria Mnasra & Basmala Jamal (Scope, Final Visual Design, Final Report & Submission Sign-Off) |
| **Governing Plan** | [PLAN.md](PLAN.md) (v1.1.0) |
| **Authoritative Specification** | [PRD.md](PRD.md) (v1.2.0-draft — File/version verified; content approval pending) |
| **Target Document Length** | Strictly 25 English Pages (Exact target; counting boundary resolved via lecturer instructions) |
| **Status Vocabulary** | `TODO`, `IN PROGRESS`, `BLOCKED`, `DONE` |

---

## Next Three Actionable Tasks

```
+----------------------------------------------------------------------------------------------------+
| 1. [TASK-P4-05 / TASK-P7-01] Partner Review, Git Sharing & README Authoring                        |
|    Owner: Maria Mnasra (Final Check & Git Commit/Push Authorization), then Basmala Jamal           |
|    Action: Inspect verified 25-page main.pdf (PASS in qa/redteam/redteam_audit_main.md; 0 open     |
|            defects; 15/15 closed). Authorize Git commit/push so Basmala can pull, review/revise,   |
|            and author README.md (no Basmala approval claimed prior to her review pass).             |
+----------------------------------------------------------------------------------------------------+
| 2. [TASK-P1-01 / TASK-P5-03 / Q-04..05..10] Resolve Open Scope, Visual & NFR Decisions             |
|    Owner: Maria Mnasra & Basmala Jamal (Joint; Basmala review/approval pending on new content)     |
|    Action: Maria accepted visual_preview.pdf as working design (nextmind-pdr.cls v0.3.2); Basmala  |
|            to review working design (Q-04), Ch. 1–3 draft, proposed FR-06a/FR-06b split & Slide 40 |
|            AI Assistant / EXT-01..05 scope (Q-05), Q-02/Q-03 framing, and Q-10 NFR targets.        |
+----------------------------------------------------------------------------------------------------+
| 3. [TASK-P2-01] Resolve 25-Page Counting Boundary via Lecturer Clarification (Q-01)                |
|    Owner: Maria Mnasra & Basmala Jamal (Joint)                                                     |
|    Action: All 3 local assignment PDFs were inspected (docs/RESEARCH_NOTES.md Sec. 2) and do NOT   |
|            resolve whether front/back matter count toward 25 English pages. Obtain lecturer        |
|            clarification (Option A vs. Option B) and verify Israel CBS primary URL if needed.      |
+----------------------------------------------------------------------------------------------------+
```

---

## Phase 0: Project Setup, Governance & Infrastructure Baseline (Historical Milestones)

> **Historical Milestone Note**: Tasks marked `DONE` below record verified milestone completions achieved during setup. They serve as an authentic historical record and do **not** constitute proof that background agent sessions or mesh processes currently remain live. Retrievable relative paths are recorded where available; unextracted runtime logs are noted as requiring persistent archiving.

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P0-01** | Save verbatim user prompts sequentially to preserve authentic provenance | Master / Maria | None | `DONE` | Prompts preserved verbatim at retrievable relative paths: `prompts/001-team-setup.txt` through `prompts/017-complete-report.txt` (plus Basmala's `prompts/prompt_01_revise_prd.md`, `prompts/prompt_02_targeted_prd_corrections.md`). |
| **TASK-P0-02** | Define role-specific SKILL.md instruction files for all five agents | Maria & Basmala | None | `DONE` | Verified non-empty role skills at retrievable relative paths: `agents/master/SKILL.md`, `agents/research/SKILL.md`, `agents/design/SKILL.md`, `agents/detector/SKILL.md`, `agents/fixer/SKILL.md`. |
| **TASK-P0-03** | Launch agymesh hub and 5 agent sessions; verify via genuine health check | Master / Maria | `TASK-P0-02` | `DONE` | Historical launch milestone: Mesh hub port 9877 and 5 sessions verified live during setup; real `ping-all` returned 4 genuine `PONG`s. *(Runtime logs recorded in tool transcripts; session evidence still needs archiving into `agents/logs/`)*. |
| **TASK-P0-04** | Verify and anchor authoritative Assignment 02 PRD specification file | Basmala Jamal | None | `DONE` | File integrity milestone: Tracked specification verified at `PRD.md` (`v1.2.0-draft`, identical in content to ignored local copy `PRD (1).md`). *(Content approval tracked in TASK-P1-01)*. |
| **TASK-P0-05** | Author Project Execution Plan (PLAN.md) incorporating minimal corrections and preserve baseline backup | Maria Mnasra | `TASK-P0-04` | `DONE` | Active plan and baseline backup at retrievable relative paths: `PLAN.md` (v1.1.0) and `backups/PLAN.original.md`. |
| **TASK-P0-06** | Author initial Project Task Board (TODO.md) and preserve baseline backup | Maria Mnasra | `TASK-P0-05` | `DONE` | Active task board and baseline backup at retrievable relative paths: `TODO.md` and `backups/TODO.original.md`. |

---

## Phase 1: Source Verification, Scope Alignment & Decision Resolution

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P1-01** | Final PRD Content Approval & Scope Resolution: Review original Fuel&Go course materials (`materials/fuel-and-go/`) with Basmala and Maria to evaluate each disputed extension feature individually (`EXT-01` C-store, `EXT-02` loyalty, `EXT-03` fleet, `EXT-04` corporate invoicing, `EXT-05` operator portal / `Q-05`); resolve based on source evidence rather than automatic exclusion, and approve content baseline | Basmala Jamal (supported by Maria) | `TASK-P1-03`, `TASK-P0-04` | `TODO` | Written partner sign-off evaluating each extension against sources and confirming core/roadmap boundaries; documented in `docs/decisions/DEC-05-scope-resolution.md`. |
| **TASK-P1-02** | Resolve intended report audience (`Q-03`): course grader vs. optional secondary technical/business panel | Maria Mnasra & Basmala Jamal | None | `TODO` | Approved audience profile determining Executive Summary depth and technical tone; documented in `docs/decisions/DEC-03-audience.md`. |
| **TASK-P1-03** | Verify available assignment materials in `materials/assignment02/` and original Fuel&Go materials in `materials/fuel-and-go/`; catalog reading limitations and provenance (`Q-06`) | Research (verified by Maria) | None | `DONE` | Verified requirements checklist with exact PDF page references and limitation log in `docs/REQUIREMENTS_CHECKLIST.md`. |
| **TASK-P1-04** | Confirm report framing and working title (*"Preliminary Design Report"* / `Q-02`) against course guidelines | Maria Mnasra & Basmala Jamal | `TASK-P1-03` | `TODO` | Written confirmation of document title, cover formatting, and running headers in `docs/decisions/DEC-02-title-framing.md`. |

---

## Phase 2: Report Outline, 25-Page Budget Approval & Early Git Setup

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P2-01** | Resolve 25-page counting boundary interpretation (`Q-01`) directly from official lecturer instructions (`materials/assignment02/`) or formal lecturer clarification (confirming whether front/back matter count toward 25 pages), avoiding arbitrary team assumptions | Maria Mnasra & Basmala Jamal | `TASK-P1-03` | `TODO` | Written decision citing lecturer instruction page or formal inquiry response documented in `docs/decisions/DEC-01-page-budget.md`. |
| **TASK-P2-02** | Review and finalize proposed report outline & 25-page budget (`docs/REPORT_OUTLINE.md`) based on verified `Q-01` boundary without artificial 1-page references compression | Maria Mnasra & Basmala Jamal | `TASK-P1-01`, `TASK-P2-01` | `IN PROGRESS` | Provisional 25.0-page outline, audience framing, scope map, and visual brief drafted in `docs/REPORT_OUTLINE.md`; awaiting partner review, chapter-owner assignment (`Q-09`), and `Q-01` confirmation. |
| **TASK-P2-03** | Early Git Setup & Checkpoint 1 (Verified Baseline): Local Git repository on `main`, `.gitignore` active (excluding `agy-multi-agent-mesh/`, `.mesh/`, `PRD (1).md`, and build outputs), remote `origin` (`NextMind_02.git`) connected, and initial attributable commits from both Basmala and Maria pushed | Maria Mnasra & Basmala Jamal | None (Completed early) | `DONE` | Verified clean `main` synced with `origin/main` at `4b1d1f9` (commits from both partners; `.gitignore` active; no force-push). *Note: Repository visibility/grader access & course material permissions (`Q-07`) remain pending confirmation.* |

---

## Phase 3: Academic Research, Standards & Data Provenance (Decoupled Stream)

*Note: Academic research and data cataloging may proceed independently in parallel without waiting for outline budget sign-off or visual styling.*

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P3-01** | Verify authoritative editions and roles of candidate domain standards & regulations: charging-management/roaming APIs (e.g., OCPI), charger-to-management (OCPP), vehicle-to-charger (ISO 15118), forecourt gateways (IFSF), PCI DSS, OWASP, WCAG AA, and target-jurisdiction privacy laws | Research | None | `DONE` | Verified candidate standards & regulatory register documented in `docs/RESEARCH_NOTES.md` (Sec. 4–6, disclosing paywalled ISO/IFSF limits) and `bib/references.bib`; independently audited `PASS` by Detector (`qa/defects.json`, `qa/incidents/INC-DEF-001..004.md`). |
| **TASK-P3-02** | Survey academic and industrial literature on dual-energy forecourt architecture, dynamic EV load management, and payment settlement | Research | None | `IN PROGRESS` | `bib/references.bib` expanded to 27 verified entries (+4 Ch. 4–6 official docs: `flutter2025docs`, `postgis2025docs`, `rabbitmq2025docs`, `redis2025docs`, plus verbatim WCAG 2.2 SC checks in `docs/RESEARCH_NOTES.md` Sec. 9). Ch. 1–3 entries Detector `PASS`; 4 new Ch. 4–6 entries await Detector audit in `draft_ch1_6`. Additional Ch. 7–9 papers may be added as needed. |
| **TASK-P3-03** | Collect, verify, and catalog empirical quantitative datasets (forecourt throughput, EV charging curves, telemetry packet sizes, payment latencies) | Research | `TASK-P3-01` | `IN PROGRESS` | Initial verified market summary saved in `data/ev_market_summary_verified.csv` & `data/README.md` (Detector `PASS`; Israel rows explicitly tagged `PENDING_PRIMARY_SOURCE_URL`; raw multi-year CSVs pending). |
| **TASK-P3-04** | Checkpoint 2 (Research Gate): Commit verified bibliography and data provenance register to Git with joint partner review | Maria Mnasra & Basmala Jamal | `TASK-P2-03`, `TASK-P3-02`, `TASK-P3-03` | `TODO` | Attributable Git commit on `main` recording verified research artifacts and provenance tags. |

---

## Phase 4: Content Drafting & Citation Assembly (Aligned with PRD Outline)

> **Outline Governance Note**: Drafting tasks and chapter filenames below are aligned with the PRD Section 3.3 proposed outline. **Final chapter structure, titles, and file organization require explicit approval by Maria Mnasra and Basmala Jamal (`TASK-P4-05`).** Text drafting operates under a single-writer lock held by Research; chapters are authored in modular LaTeX files.

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P4-01** | Draft Front Matter: Cover Page (`front/cover.tex`), Document Control & Executive Summary (`front/executive_summary.tex`), and Table of Contents (`main.tex`, navigation only; acronyms placed in appendices) | Fixer / Design (led by Maria; Basmala review pending) | `TASK-P1-01`, `TASK-P1-02` | `DONE` | `front/cover.tex` and `front/executive_summary.tex` drafted, integrated into `main.tex`, and verified `PASS` by Detector (`qa/redteam/redteam_audit_main.md`). *Basmala review pending.* |
| **TASK-P4-02** | Draft Sections 1–3: Introduction, Business Motivation & Scope Boundaries (`sections/sec01_intro.tex`), Market Context, Business Model, Users & Stakeholders (`sections/sec02_users_stakeholders.tex`), and System Requirements Specification (`sections/sec03_requirements.tex`) | Research & Design (led by Maria; Basmala review pending) | `TASK-P3-01` | `DONE` | Verified in `draft_ch1_3.pdf` (preserved untouched) and integrated with Fig. 2 placement fix into final 25-page `main.pdf` (Detector `PASS`). *Basmala review pending.* |
| **TASK-P4-03** | Draft Sections 4–6: Preliminary System Architecture & Tech Trade-Offs (`sections/sec04_architecture.tex`), Data Model & External Integration Boundaries (`sections/sec05_data_protocols.tex`), and UX/UI Preliminary Flows, Visual Identity & Accessibility (`sections/sec06_ux_ui.tex`) | Research, Design & Fixer (led by Maria; Basmala review pending) | `TASK-P4-02`, `TASK-P3-01`, `TASK-P3-03` | `DONE` | Drafted, corrected across A1–A6 (reproducible weighted matrix scores + `[Assumption]` disclosure, durable idempotency + operator limits, aligned state names + bay-reservation lock, excluded bandwidth overheads, ambiguous auth-timeout -> `RECONCILING`), integrated into `draft_ch1_6.pdf` (preserved) and final 25-page `main.pdf` (Detector `PASS`). *Basmala review pending.* |
| **TASK-P4-04** | Draft Sections 7–9 & Back Matter: Security, Physical Safety, Privacy & Compliance (`sections/sec07_security_safety.tex`), Planned Product Verification vs. Actual Report QA (`sections/sec08_verification_qa.tex`), Product Delivery Plan, Risks, Roadmap & Conclusions (`sections/sec09_plan_conclusions.tex`), and Appendices (`back/appendices.tex`, incl. reproducibility, provenance legend & acronyms) | Fixer & Design (from verified `bib/references.bib` & `docs/RESEARCH_NOTES.md`; Basmala review pending) | `TASK-P4-03` | `DONE` | `sections/sec07_security_safety.tex`, `sec08_verification_qa.tex`, `sec09_plan_conclusions.tex`, and `back/appendices.tex` drafted, integrated into 25-page `main.pdf`, and verified `PASS` by Detector (`qa/redteam/redteam_audit_main.md`). *Basmala review pending.* |
| **TASK-P4-05** | Checkpoint 4 (Drafting Gate & Chapter Structure Sign-Off): Partner editorial review of drafted content; formal partner sign-off on final chapter structure and filenames; commit chapter drafts to Git | Maria Mnasra & Basmala Jamal | `TASK-P2-03`, `TASK-P4-04` | `TODO` | Editorial sign-off note in `docs/reviews/editorial_signoff.md` approving chapter structure and attributable Git commit on `main`. |

---

## Phase 5: Visual Sample Approval, LaTeX Production & Reproducible Python Graphs

*Strict Sequence: 1. Toolchain & Visual sample -> 2. Partner approval -> 3. Styling finalization, diagrams, plots & master integration.*

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P5-01** | Local Toolchain Verification: Validate local LuaLaTeX (`--disable-installer -halt-on-error`), fonts, and `pdftoppm` rendering in clean shell | Design (supported by Maria) | None (Decoupled stream) | `DONE` | Verified offline LuaHBTeX 1.24.0 + `pdftoppm` build & embedded fonts (`Calibri`, `Georgia`, `Consolas`); `lastpage.sty` absent in MiKTeX (deferred); logged in `docs/toolchain_verification.log`. *(Biber/Python plot test remains before Phase 5 plot build)*. |
| **TASK-P5-02** | Representative Visual Sample & 3-Page Editorial Preview (Step 1): Author visual preview derived from the confirmed Fuel&Go presentation visual brief (`docs/REPORT_OUTLINE.md`, Sec. 5) with enriched semantic palette, bespoke TikZ illustrations, and non-hyphenated headings | Design | `TASK-P5-01` | `DONE` | Baseline v0.1 preserved in `backups/`; redesigned 3-page `visual_preview.pdf` (237,781 bytes) from `visual_preview.tex`, backward-compatible provisional `nextmind-pdr.cls` v0.2, and `figures/{cover_illustration,journey_process,arch_integration_preview}.tex`; color + grayscale PNGs independently verified `PASS` by Detector after Fixer closed `DEF-005` (`qa/incidents/INC-DEF-005.md`; 0 open defects). |
| **TASK-P5-03** | Partner Visual Design Sign-Off (Step 2 / `Q-04`): Review visual sample prototype and approve document design system | Maria Mnasra (accepted working design) & Basmala Jamal (review pending) | `TASK-P5-02` | `IN PROGRESS` | Maria accepted `visual_preview.pdf` direction as the working report design with enlarged labels and conceptual-interface wording applied in `nextmind-pdr.cls` Working v0.3.2 (prior previews preserved untouched). **Separate Basmala review/approval remains pending** prior to final `docs/decisions/DEC-04-visual-design.md` sign-off. |
| **TASK-P5-04** | Document Class Finalization (Step 3a): Finalize custom `nextmind-pdr.cls` encapsulating approved typography, geometry, headers, callouts, and page budget hooks | Design / Fixer | `TASK-P5-03` | `IN PROGRESS` | Working class `nextmind-pdr.cls` updated to **Working v0.3.3** (`\FloatBarrier` + `\needspace` in `\fgchapter` closing `DEF-011` & `DEF-014`; backward-compatible with `visual_preview.tex` and `visual_sample.tex`); final freeze awaits Basmala visual sign-off (`Q-04`). |
| **TASK-P5-05** | Vector Diagram Authoring (Step 3b): Author TikZ architectural diagrams, dual-energy state machines, and sequence flows | Design / Fixer | `TASK-P5-03`, `TASK-P4-03` | `DONE` | All 6 TikZ vector diagrams completed and independently verified `PASS` by Detector: `figures/use_case_diagram.tex`, `arch_multilayer.tex`, `session_fsm.tex` (`DEF-012` closed), `sequence_auth_settlement.tex`, `ux_journey_flow.tex`, and `safety_trust_boundary.tex` (`DEF-013` closed). |
| **TASK-P5-06** | Reproducible Python Plotting Pipeline (Step 3c): Develop Python 3.12 plotting scripts with pinned `requirements.txt` generating vector PDFs with mandatory 4-category provenance labels | Design | `TASK-P3-03`, `TASK-P5-01` | `DONE` | `scripts/plots/fig2_1_market_context.py` -> `figures/fig2_1_market_context.pdf` and `scripts/plots/fig5_2_telemetry_sizing.py` -> `figures/fig5_2_telemetry_sizing.pdf` registered in `scripts/generate_figures.py` (exit 0) and verified `PASS` by Detector. Decorative Fig. 8.1 intentionally omitted per `docs/REPORT_OUTLINE.md`. |
| **TASK-P5-07** | Master Document Integration (Step 3d): Assemble `main.tex` orchestrating modular chapter files, TikZ figures, Python vector plots, and IEEE references | Design / Fixer | `TASK-P4-04`, `TASK-P5-04`, `TASK-P5-05`, `TASK-P5-06` | `DONE` | `main.tex` assembled and compiled to exact **25-page** `main.pdf` (`838,144` bytes; prior partial drafts `draft_ch1_3.*` and `draft_ch1_6.*` preserved untouched). |
| **TASK-P5-08** | Checkpoint 3 (Design Gate): Commit visual engine (`.cls`), TikZ figures, plotting scripts, and master LaTeX harness to Git | Maria Mnasra & Basmala Jamal | `TASK-P2-03`, `TASK-P5-07` | `TODO` | Attributable Git commit on `main` recording the production layout harness. |

---

## Phase 6: Compilation, Independent QA Review, Incident Remediation & Retesting

> **Defect Remediation & Retest Lifecycle**:
> 1. Detector performs read-only red-team audits and logs defect tickets in `qa/defects/`.
> 2. **Fixer** investigates, fixes root causes in CLS/LaTeX/Python, and authors Sections 1–4 of incident records (What happened, Why it happened, Why earlier checks missed it, What changed).
> 3. **Detector alone** records independent retest results (Section 5: method, raw evidence, `PASS`/`FAIL`).
> 4. **Repeated fix/retest cycles** are explicitly permitted and executed iteratively until zero open defects remain.

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P6-01** | Deterministic Full Build Execution: Run clean production LuaLaTeX + Biber compilation. Build execution assigned to **Design**, coordinated and verified by **Master** | Design (coordinated by Master) | `TASK-P5-07` | `DONE` | Clean 4-pass `lualatex -> biber -> lualatex -> lualatex` build of `main.tex` -> `main.pdf` (**exact 25 pages**, `838,144` bytes; 0 LaTeX/Biber/Missing-char errors, 0 `??`/`[?]`, max overfull `1.60pt`, 27/27 IEEE refs incl. RTL Hebrew). |
| **TASK-P6-02** | Independent Red-Team QA Audit (Detector): Conduct dual-track audit (Product Design Verification vs. Report Quality Assurance, verifying exact 25-page target per verified `Q-01`, zero fabrication, and provenance tags) | Detector (read-only audit) | `TASK-P6-01` | `DONE` | Full-report audit + 25-page PNG inspection logged in `qa/redteam/redteam_audit_main.md`; 5 visual/layout defects logged as `DEF-011`–`DEF-015` in `qa/defects.json` and `qa/DEFECTS.md` (0 factual/citation/fabrication defects). |
| **TASK-P6-03** | Root-Cause Defect Remediation & Incident Logging (Fixer): Resolve all identified defects across CLS, LaTeX, and Python; author Sections 1–4 of mandatory 5-part incident records | Fixer / Design | `TASK-P6-02` | `DONE` | `DEF-011`–`DEF-015` remediated across `nextmind-pdr.cls` (v0.3.3), `figures/session_fsm.tex`, `figures/safety_trust_boundary.tex`, and `main.tex`; 5-part incident records logged in `qa/incidents/INC-DEF-011.md`–`INC-DEF-015.md`. |
| **TASK-P6-04** | Independent Defect Retesting & Verification (Detector): Re-audit all remediated items without modifying files; record Section 5 (`PASS`/`FAIL` and raw retest evidence) in incident records | Detector alone | `TASK-P6-03` | `DONE` | Detector independently retested and closed `DEF-011`–`DEF-015` (`PASS`, 0 regressions, **0 open defects** across 15/15 total defects) in `qa/incidents/INC-DEF-011..015.md`, `qa/DEFECTS.md`, `qa/defects.json`, and `qa/redteam/redteam_audit_main.md` Sec. 6. |
| **TASK-P6-05** | Checkpoint 5 (QA Gate): Commit QA audit reports, incident records, and retest evidence to Git | Maria Mnasra & Basmala Jamal | `TASK-P2-03`, `TASK-P6-04` | `TODO` | Attributable Git commit on `main` capturing complete verification and defect-resolution history. |

---

## Phase 7: Repository Documentation, Submission Checks & Release

> **Distinct Moodle Submission Deliverables**:
> - **Personal Moodle Submission-Form PDF**: Partner-specific declaration or submission-form PDF required by course instructions (to be uploaded to Moodle if mandated).
> - **Portal Submission Confirmation**: Formal confirmation of submission from the Moodle portal, archived in whatever format Moodle actually provides (e.g., timestamped screenshot, exported web confirmation page, text log, or confirmation email/PDF); **do not assume Moodle generates a downloadable receipt PDF**.

| Task ID | Action | Owner | Dependencies | Status | Completion Criterion & Evidence Path |
| --- | --- | --- | --- | :---: | --- |
| **TASK-P7-01** | Author Project Documentation (`README.md`): Team attribution, reproducible build guide, data provenance system, multi-agent evidence summary, and figures showcase | Basmala Jamal (primary author after pulling shared work; joint final sign-off with Maria) | `TASK-P6-04` | `TODO` | Comprehensive `README.md` at root prepared by Basmala upon reviewing shared work and jointly approved by both partners. |
| **TASK-P7-02** | Multi-Agent Evidence & Prompt Archive Verification: Audit completeness of verbatim prompts (`prompts/`), authentic agent message journals, and incident records | Master (verified by Maria & Basmala) | `TASK-P6-04` | `TODO` | Complete, authentic audit trail verified in `prompts/`, `agents/messages/`, and `qa/incidents/` (zero fabrication). |
| **TASK-P7-03** | Final Git Packaging, Clean-Up & Release Tagging (Checkpoint 6): Confirm `.gitignore` strictly excludes `agy-multi-agent-mesh/` and build artifacts, push `main`, and tag release | Maria Mnasra & Basmala Jamal | `TASK-P7-01`, `TASK-P7-02` | `TODO` | Clean repository status, all partner commits pushed to `https://github.com/jamalbasmala907-ship-it/NextMind_02.git`, release tag `v1.0.0`. |
| **TASK-P7-04** | Maria Mnasra Personal Moodle Submission: Verify exact portal requirements; prepare required personal Moodle submission-form PDF; submit GitHub URL and partner details; archive submission confirmation in whatever format Moodle provides (screenshot, export, or PDF) | Maria Mnasra | `TASK-P7-03` | `TODO` | Archived personal submission-form PDF in `submissions/maria_moodle_form.pdf` and portal confirmation record in `submissions/maria_moodle_confirmation.*`. |
| **TASK-P7-05** | Basmala Jamal Personal Moodle Submission: Verify exact portal requirements; prepare required personal Moodle submission-form PDF; submit GitHub URL and partner details; archive submission confirmation in whatever format Moodle provides (screenshot, export, or PDF) | Basmala Jamal | `TASK-P7-03` | `TODO` | Archived personal submission-form PDF in `submissions/basmala_moodle_form.pdf` and portal confirmation record in `submissions/basmala_moodle_confirmation.*`. |

---

## Open Decisions Cross-Reference Register

The following open decisions from [PLAN.md](PLAN.md) Section 9 are tracked directly against their governing tasks:

| Decision ID | Summary | Governing Task | Responsible Owner(s) | Impact / Resolution Path |
| --- | --- | --- | --- | --- |
| **Q-01** | 25-Page Boundary Interpretation | `TASK-P2-01` | Maria Mnasra & Basmala Jamal | Resolved from lecturer instruction text or inquiry, not arbitrary team choice. |
| **Q-02** | Report Framing & Course Title Verification | `TASK-P1-04` | Maria Mnasra & Basmala Jamal | Governs document cover title and running headers. |
| **Q-03** | Intended Report Audience Scope | `TASK-P1-02` | Maria Mnasra & Basmala Jamal | Shapes Executive Summary depth and technical tone. |
| **Q-04** | Visual Design System Approval (Presentation-Based Direction) | `TASK-P5-02`, `TASK-P5-03` | Maria Mnasra (accepted working design) & Basmala Jamal (review pending) | Maria accepted `visual_preview.pdf` as working design (`nextmind-pdr.cls` v0.3.1 with enlarged labels & conceptual-interface wording); separate Basmala review/approval remains pending before final class lock. |
| **Q-05** | Disputed Scope Extensions (`EXT-01..05`) & AI Assistant Conflict | `TASK-P1-01` | Basmala Jamal (supported by Maria) | Slide audit completed (`docs/RESEARCH_NOTES.md` Sec. 7); `EXT-01`, VAT invoicing, standalone operator dashboard, and Slide 3/40 AI Digital Assistant remain quarantined pending partner ruling. |
| **Q-06** | Lecturer Instruction Filename / Page Provenance | `TASK-P1-03` | Research & Maria Mnasra | Verifies requirements checklist against course PDFs. |
| **Q-07** | GitHub Access Permissions & Material IP | `TASK-P7-03` *(Open check after `TASK-P2-03`)* | Maria Mnasra & Basmala Jamal | Baseline Git setup done; confirm repo visibility/grader access & copyright compliance. |
| **Q-08** | Exact Moodle Submission Requirements | `TASK-P7-04`, `TASK-P7-05` | Maria Mnasra & Basmala Jamal | Distinguishes required submission-form PDF from portal confirmation. |
| **Q-09** | Detailed Partner Work Breakdown | `TASK-P4-05`, `TASK-P7-01` | Maria Mnasra & Basmala Jamal | Updated agreement (2026-11-27): Maria leads report production for GitHub sharing; Basmala pulls, reviews/revises, and prepares `README.md` (preserving prior contributions and `PRD.md` ownership). |
| **Q-10** | Numerical Target Rationales (`NFR-01a..04`) | `TASK-P4-03` | Basmala Jamal (with Research) | Supplies rigorous engineering justification for NFRs. |

---
*Document author: Maria Mnasra (Task Governance Owner) & Team NextMind.*  
*Anchored specification: `PRD.md` (v1.2.0-draft — File/version verified; content approval pending).*  
*Governing execution plan: `PLAN.md` (v1.1.0).*
