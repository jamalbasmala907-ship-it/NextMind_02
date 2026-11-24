# Product Requirements Document (PRD): Fuel&Go — Assignment 02 Report

| Field | Value |
| --- | --- |
| **Project Name** | Fuel&Go (Core: Smart Fueling & EV Charging Platform) |
| **Deliverable** | Assignment 02 Engineering Report (Working Framing: *Preliminary Design Report* — Pending Verification) |
| **Team** | NextMind |
| **Team Partners** | Maria Mnasra, Basmala Jamal |
| **PRD Owner** | Basmala Jamal (Requirements Owner; Joint Major-Decision Approval with Maria Mnasra) |
| **Document Language** | English (en-US) |
| **Target & Acceptance Length** | Strictly 25 English Pages (Exact; front/back matter inclusion unresolved — see `Q-01`) |
| **Typesetting Engine** | LuaLaTeX + Biber (`biblatex`, IEEE style) |
| **Document Class** | Custom LaTeX Class (`nextmind-pdr.cls` — Working Filename, Visual Design Pending Approval) |
| **Version** | 1.2.0-draft |
| **Status** | **Draft — Pending Team Review** |
| **Previous Baseline Backups** | `backups/PRD.original.md` (v1.0.0), `backups/PRD.v1.1.0-draft.bak.md` (v1.1.0-draft) |

### Revision History

| Version | Date | Author / Role | Summary of Changes |
| --- | --- | --- | --- |
| `1.0.0` | 2026-11-24 | Initial Draft | Initial baseline PRD draft (archived unmodified in `backups/PRD.original.md`). |
| `1.1.0-draft` | 2026-11-24 | Revision Draft | Authoritative Assignment 02 revision for Team NextMind (archived unmodified in `backups/PRD.v1.1.0-draft.bak.md`). |
| `1.2.0-draft` | 2026-11-24 | Targeted Correction Pass | Clarified deliverables & human ownership (`PRD.md` Basmala Jamal; `PLAN.md` & `TODO.md` Maria Mnasra; `README.md` joint); scoped `Master`, `Research`, and `Design` roles with single-writer handoffs; marked disputed scope extras `"Unverified — pending source review"`; reclassified 5-agent setup & 5-part incident format as team workflow choices unless backed by actual lecturer citations; replaced premature `"Implemented / Tested"` with `"Planned — verification pending"` and separated artifact type from completion status; documented local `agy-multi-agent-mesh/` `.gitignore` exclusion; made 25-page budget flexibly rebalanceable without cramming references/appendices into 1 page or hard-coding `"Page X of 25"`; replaced arbitrary numeric targets with `"TBD — requires rationale and team approval"`. |

---

## 1. Purpose, Report Framing & Audience Separation

### 1.1 Purpose of This PRD
This Product Requirements Document (PRD) serves as the authoritative working specification for **Team NextMind** (**Maria Mnasra** and **Basmala Jamal**) to plan, govern, produce, verify, and submit **Assignment 02**. It defines:
1. The **Fuel&Go** core product scope (fueling and EV charging) and explicit separation from proposed extensions/future scope.
2. The **exact 25-page** English PDF deliverable structure, LuaLaTeX + Biber (IEEE) architecture, reproducible Python figure pipeline, and custom `.cls` styling governance.
3. The **5-role multi-agent workflow** (team workflow choice: Master, Research, Design, Detector, Fixer), partner ownership (`PRD.md`, `PLAN.md`, `TODO.md`, `README.md`), quality assurance separation, red-team expectations, and strict **zero-fabrication** evidence rules.
4. Clear provenance separating explicit lecturer requirements, confirmed team decisions, proposed choices, assumptions, and open decisions awaiting Maria and Basmala's sign-off.

### 1.2 Report Framing & Title Verification
- **Working Framing**: *Fuel&Go — Preliminary Design Report (Assignment 02)*.
- **Verification Requirement (`Q-02`)**: Before drafting final cover metadata and introductory framing, Maria and Basmala must verify against the official Assignment 02 lecturer instructions whether the required document framing/title is explicitly **"Preliminary Design Report"** or another course-specified document title (e.g., System Design Document, Engineering Design Report, Architecture Report). Until verified, *"Preliminary Design Report"* is treated as a working framing rather than a confirmed lecturer mandate.

### 1.3 Report Readers vs. Fuel&Go App Users
This PRD strictly separates **who reads the Assignment 02 report** from **who uses the Fuel&Go application**:

#### A. Report Readers (Audience of the 25-Page PDF)
| Reader Group | Classification | Primary Expectations | Status |
| --- | --- | --- | --- |
| **Course Lecturer & Graders / TAs** | Primary Reader (Confirmed) | Compliance with Assignment 02 requirements, exact 25-page execution, technical rigor, verified IEEE references, reproducible Python charts, authentic multi-agent evidence, and zero fabrication. | Confirmed |
| **Team NextMind Partners (Maria Mnasra & Basmala Jamal)** | Internal Author / Reviewer (Confirmed) | Clear division of genuine work, unambiguous acceptance criteria, maintainable modular LaTeX/Python assets, and traceable review sign-offs. | Confirmed |
| **Simulated Engineering / Product Review Panel** | Optional Secondary Reader | Decision-ready architecture trade-offs, risk visibility, and conceptual feasibility assessment. | **Open Decision (`Q-03`)** |
| **Simulated Investors / Non-Technical Business Stakeholders** | Optional Secondary Reader | Concise executive summary and value proposition without diluting engineering depth. | **Open Decision (`Q-03`)** |

#### B. Fuel&Go App Users (End Users of the Designed System)
| User Persona | Scope Classification | Core Interaction with Fuel&Go |
| --- | --- | --- |
| **ICE / Hybrid Vehicle Driver** | **Core Scope** | Locates nearby fuel stations with live prices and pump availability, authorizes pump activation, monitors live fuel dispensing, pays contactlessly, and receives a digital receipt. |
| **Electric Vehicle (EV) Driver** | **Core Scope** | Locates compatible EV charging stations (connector type, kW rating, live availability/pricing), initiates/stops charging sessions, monitors live kWh/SoC/cost telemetry, pays contactlessly, and receives a digital receipt. |
| **Fleet Manager / Commercial Driver** | *Proposed Extension / Future Scope (`Unverified — pending source review`)* | Corporate policy limits, multi-vehicle expense tracking, consolidated invoicing (excluded from core unless verified against original Fuel&Go sources and approved in `Q-05`). |
| **Station / Forecourt Operator** | *Proposed Extension / Future Scope (`Unverified — pending source review`)* | Operational dashboard, manual override visibility, pricing management, convenience order fulfillment (excluded from core unless verified against original Fuel&Go sources and approved in `Q-05`). |

---

## 2. Fuel&Go Product Scope Alignment

Fuel&Go is designed as a unified mobile refueling and EV charging platform enabling drivers of internal-combustion, hybrid, and electric vehicles to discover stations, authorize dispensers or chargers, monitor live energy delivery, and complete contactless payments through one cohesive experience.

### 2.1 Core Capabilities (In Scope for Assignment 02)
The following capabilities constitute the **core Fuel&Go scope** to be specified, architected, and verified conceptually in the report:

- **FR-01 — User Account, Authentication & Vehicle Energy Profile**: User registration, secure authentication (OAuth 2.0 / OIDC), and vehicle profile storing preferred fuel grade(s) and/or EV connector type(s) (e.g., CCS2, Type 2, CHAdeMO) and charging power preferences.
- **FR-02 — Unified Station & Charger Discovery**: Map and list search showing nearby fuel stations and EV charging hubs with live fuel prices per liter, EV tariff per kWh/minute, connector compatibility, live pump/charger occupancy status, and distance/route filtering.
- **FR-03 — Pump & EV Charger Selection and Session Authorization**: Selection via QR code, NFC, or station/bay identifier; geofence proximity verification; payment method pre-authorization hold; and remote authorization command to the fuel forecourt gateway or EV Charge Point Management System (CPMS).
- **FR-04 — Real-Time Fueling & EV Charging Telemetry**: Live session view showing dispensed fuel volume (liters) or delivered electrical energy (kWh), charging power (kW) / estimated State of Charge (SoC) where supported by the charger, elapsed time, and running cost, plus safe session stop / completion detection.
- **FR-05 — Contactless Payment Settlement & Basic Digital Receipt**: Final capture of exact dispensed/charged amount, automatic release of unused pre-authorization hold, and generation of a basic itemized digital receipt stored in session history.
- **FR-06 — Session Fault Handling & Basic User Support**: Graceful handling of authorization timeout, nozzle/cable disconnect failure, payment decline, or station connectivity loss, with transparent user notifications and basic receipt/session issue reporting.

### 2.2 Disputed Features & Proposed Extensions / Future Scope (Explicitly Out of Core Scope)
The following features appeared in `backups/PRD.original.md` (v1.0.0) without verified backing from the original Fuel&Go slides or prior project PRD. Because the original Fuel&Go slides/prior PRD are **not present in this project folder** (and unrelated personal folders were not scanned), their provenance cannot be cited yet and is marked **`Unverified — pending source review`**. They remain demoted out of core scope until Maria and Basmala review them against the original Fuel&Go source materials (`Q-05`):

| ID | Capability | Scope Classification | Source Provenance (Original Fuel&Go Slides / Prior PRD) | Notes |
| --- | --- | --- | --- | --- |
| **EXT-01** | Convenience-Store Pre-Ordering & Pickup | *Proposed Extension / Future Scope* | `Unverified — pending source review` | Retail catalog/fulfillment outside confirmed fueling + EV charging core. |
| **EXT-02** | Loyalty Points & Promotions Engine | *Proposed Extension / Future Scope* | `Unverified — pending source review` | Marketing/rewards add-on outside confirmed fueling + EV charging core. |
| **EXT-03** | Fleet Management Portal & Driver Policies | *Proposed Extension / Future Scope* | `Unverified — pending source review` | Separate B2B product surface; do not expand core scope without source verification. |
| **EXT-04** | Consolidated Corporate / VAT Invoicing | *Proposed Extension / Future Scope* | `Unverified — pending source review` | Distinct accounting workflow beyond basic per-session digital receipts. |
| **EXT-05** | Station Operator Forecourt Dashboard | *Proposed Extension / Future Scope* | `Unverified — pending source review` | Auxiliary operator console; core design focuses on driver platform and station/CPMS integration boundary. |

*Rule*: Never invent slide numbers or prior-PRD citations. Once Maria and Basmala inspect the original Fuel&Go slides/prior PRD, update each row with the exact slide/section citation or confirm permanent Future Scope status. If kept as Future Scope, these items may only appear briefly in a compact roadmap note so they do not consume core requirements, architecture, or page budget.

---

## 3. Strict 25-Page Target & Rebalanceable Section Budget

### 3.1 Page-Count Acceptance Criterion
- **Target & Acceptance Criterion**: The report length is **strictly 25 English pages** (exact).
- **Explicit Prohibition**: The target is **NOT** "at least 25 pages" and **NOT** an approximate range. Falling short of or exceeding 25 pages within the confirmed page-count boundary is a failed QA gate that must be logged by the Detector and resolved by the Fixer before release.

### 3.2 Open Question on Page-Count Boundary (`Q-01`)
> **Open Question (`Q-01` — Unresolved)**: Does the strict **25 English pages** requirement include the **cover page, table of contents / lists, references, and appendices** inside the 25 pages (i.e., `Total PDF Pages == 25`), OR does it require **25 body pages** excluding those front/back matter parts?
>
> **Handling Rule**: If the confirmed lecturer requirement specifies **25 body pages**, then excluded front/back matter parts (cover, table of contents/lists, IEEE references, and appendices) are **additional** to the 25 body pages (total PDF pages = `25 + excluded front/back matter`) rather than compressed or omitted. Maria and Basmala must verify this against the official Assignment 02 lecturer instructions before locking the final budget.

### 3.3 Proposed Section-by-Section Page Budget (Rebalanceable Working Baseline)
*Approval Status*: **Proposed Allocation — Pending Maria & Basmala's Approval**. Section allocations below are **rebalanceable** during drafting and layout integration to preserve readability and technical balance—**without forcing IEEE references and appendices into a single 1-page slot**.

- **Option A (Working Baseline — 25 Total PDF Pages including front/back matter)**:

| Section | Proposed Title | Indicative Budget (Rebalanceable) | Planned Technical Content & Visuals |
| --- | --- | :---: | --- |
| **Front** | Cover Page | 1.0 | NextMind identity, Maria Mnasra & Basmala Jamal, Assignment 02, Fuel&Go title, version/date |
| **Front** | Document Control, Executive Summary & Audience Framing | 1.0 | Metadata, scope summary (fueling + EV charging), key conceptual highlights, reader framing |
| **Front** | Table of Contents, List of Figures/Tables & Acronyms | 1.0 | Auto-generated ToC, compact LoF/LoT, domain acronyms (EV, OCPP, IFSF, PCI DSS, SoC, etc.) |
| **Sec. 1** | Introduction, Motivation & Scope Boundaries | 1.5–2.0 | Fueling + EV charging user pain points, project goals, Core vs. Future Scope boundary table |
| **Sec. 2** | Users, Stakeholders & Domain Context | 1.5–2.0 | App user personas (ICE/hybrid & EV drivers), report vs. system stakeholder distinction, reproducible Python chart #1 (with explicit provenance) |
| **Sec. 3** | System Requirements Specification (`FR` & `NFR`) | 2.5–3.0 | Core `FR-01..06`, `NFR` table with rationale/verification/status, TikZ use-case diagram, MoSCoW prioritization |
| **Sec. 4** | Preliminary System Architecture & Technology Trade-Offs | 3.5–4.0 | TikZ multi-layer architecture diagram (mobile, edge/API, fueling + EV orchestrator, forecourt & CPMS adapters), TikZ unified fueling/EV session state machine, candidate technology trade-off table |
| **Sec. 5** | Data Model & External Protocols (Forecourt, EV CPMS & Payment) | 2.5–3.0 | TikZ conceptual ERD, REST/WebSocket contract summary, TikZ end-to-end pump & EV charger authorization/settlement sequence diagram, reproducible Python chart #2 |
| **Sec. 6** | UX/UI Preliminary Flows & Accessibility | 1.5–2.0 | Core mobile journeys (station/charger discovery, scan/authorize, live fueling vs. EV telemetry, digital receipt), WCAG accessibility rules |
| **Sec. 7** | Security, Physical Safety, Privacy & Compliance | 2.0 | Threat model (STRIDE summary), PCI DSS tokenization & GDPR controls, TikZ physical safety interlock boundary diagram (fuel dispenser + EVSE local cutoffs) |
| **Sec. 8** | Verification, Validation, QA & Red-Team Summary | 1.5–2.0 | Separation of Product Design Verification vs. Report QA, requirement traceability matrix, Detector/Fixer incident & red-team summary, reproducible Python chart #3 |
| **Sec. 9** | Project Plan, Risks, Multi-Agent Process & Conclusions | 1.0–1.5 | Risk register, partner & agent workflow summary, transition to next phase, Future Scope roadmap note |
| **Back** | IEEE References (`biber`) | 1.0–1.5 *(flexible)* | Full verified IEEE bibliography sized naturally for readability |
| **Back** | Appendices (Optional / As Needed) | 0.5–1.5 *(flexible)* | Reproduction commands, provenance legend, or supplementary tables (rebalanced with body sections so Option A totals **exactly 25.0 pages**) |
| **TOTAL (Option A)** | **Complete Assignment 02 PDF** | **Exactly 25.0** | **Rebalanced across sections to hit strictly 25 English pages** |

- **Option B (If `Q-01` confirms 25 Body Pages excluding front/back matter)**: Sections 1–9 rebalance to **exactly 25.0 body pages**, and Cover, Front Matter (ToC/Lists), IEEE References, and Appendices appear as **additional** pages sized naturally without artificial 1-page compression.

---

## 4. Human Ownership, Multi-Agent Roles, Handoffs & Evidence Integrity

> **Governance Classification Note**: The **5-role multi-agent setup** (`Master`, `Research`, `Design`, `Detector`, `Fixer`), role-specific `SKILL.md` structure, and **5-part incident record format** are **Team NextMind Workflow Choices** (see Section 11.2), unless explicitly required by verified lecturer instruction files with exact filenames and page numbers.

### 4.1 Human Partner Ownership & Approval Authority
Human partners hold ultimate ownership and decision authority; agents assist within scoped roles and never replace partner ownership:

| Partner | Owned Core Deliverables | Decision & Sign-Off Authority |
| --- | --- | --- |
| **Basmala Jamal** | `PRD.md` (requirements, scope governance, acceptance criteria) | Approves requirements changes; co-approves all major project decisions and final release. |
| **Maria Mnasra** | `PLAN.md` (phases, dependencies, owners, quality gates) and `TODO.md` (tasks, owners, status, evidence) | Approves execution plan & task gating; co-approves all major project decisions and final release. |
| **Joint (Maria Mnasra & Basmala Jamal)** | `README.md` (project overview, both authors, build/reproduction steps, screenshots, figures, real agent evidence) | Jointly approve scope promotions, visual design, numerical targets, external submissions (Moodle), and final 25-page PDF sign-off. |

### 4.2 The Five Multi-Agent Roles & `SKILL.md` Files (Team Workflow Choice)
Each agent role has a dedicated, version-controlled `SKILL.md` file specifying its mandate, permitted tools, prohibited actions, input/output contracts, and handoff rules:

| Role | Skill File Path (Proposed) | Primary Mandate | Scoped Write Domain (During Active Handoff Lock) | Prohibited Actions |
| --- | --- | --- | --- | --- |
| **1. Master** | `agents/master/SKILL.md` | Coordinates workflow phases, dispatches handoffs, enforces single-writer locks and quality/page gates, tracks agent dependencies, and escalates major decisions to Maria & Basmala **without replacing human ownership**. | Coordination & handoff logs (`agents/messages/`) | Must NOT replace Basmala's ownership of `PRD.md`, Maria's ownership of `PLAN.md`/`TODO.md`, or joint partner sign-off; must not fabricate evidence or bypass unresolved Detector defects. |
| **2. Research** | `agents/research/SKILL.md` | Researches domain literature, verifies sources/standards/protocols (IFSF, OCPP, ISO 15118, PCI DSS, etc.), curates IEEE `.bib` entries and raw data sources, **and drafts technical report content**. | `bib/references.bib`, `data/sources/`, and technical content drafts (`sections/*.tex` or staged drafts during Research lock) | Must not invent citations, DOIs, URLs, standard versions, or empirical statistics; must not edit `.cls` or layout files while `Design` holds the lock. |
| **3. Design** | `agents/design/SKILL.md` | Handles **LaTeX engineering, custom `.cls` styling (once approved), document layout & pagination integration, TikZ/vector diagrams, and reproducible Python graphs**. | `nextmind-pdr.cls`, `main.tex`, `figures/*.tex`, `scripts/plots/*.py`, and layout integration of `sections/*.tex` (only after Research handoff) | Must not alter verified source citations without Research review, self-certify QA sign-off, or edit Detector incident logs. |
| **4. Detector** | `agents/detector/SKILL.md` | Independent auditor & red-teamer: executes Product Design Verification and Report QA, visually inspects rendered PDF pages, audits citations/provenance/reproducibility, logs 5-part incidents, and performs independent retests. | `qa/incidents/*.md`, `qa/redteam/*.md`, `qa/reports/*.md` | **Read-only on production report/code files**: must NOT directly edit `sections/`, `.cls`, `.bib`, or plotting scripts (strict separation of duties). |
| **5. Fixer** | `agents/fixer/SKILL.md` | Performs root-cause remediation of Detector-logged defects in LaTeX, `.cls`, bibliography, or Python scripts; documents exact changes and preventive guardrails; hands back to Detector for independent retest. | Scoped defect-referenced files (`sections/`, `.cls`, `bib/`, `scripts/plots/`) only while holding an active Fixer incident lock | Must not close Detector incidents, skip independent Detector retest, or edit files outside assigned incident scope. |

### 4.3 Real Cross-Session Messages & Single-Writer Handoff Protocol
- **Authentic Cross-Session Communication**: All inter-agent assignments, clarifications, incident escalations, and retest handoffs across sessions must be captured as **real logged messages** (timestamped files in `agents/messages/` or exported session logs). Simulated or post-hoc reconstructed dialogues are strictly prohibited.
- **Preventing Simultaneous Edits (Single-Writer Lock & Handoff Flow)**:
  1. **No Concurrent Writes**: Only one role (or partner) may hold write ownership of a given file at any time. `Research` and `Design` never edit the same `sections/*.tex` file simultaneously; `Design` and `Fixer` never edit `.cls`, `sections/`, or `scripts/plots/` simultaneously.
  2. **Standard Stage-Gate Handoff Sequence**:
     - `Master` logs handoff to `Research` -> `Research` verifies sources and drafts section content + `bib/references.bib` -> commits & logs handoff back to `Master`/`Design` (releasing write lock).
     - `Design` receives lock -> integrates content into LaTeX layout, builds TikZ diagrams & Python graphs, enforces page budget -> commits & logs handoff to `Detector` (releasing write lock).
     - `Detector` audits read-only -> logs 5-part incidents in `qa/incidents/` -> logs handoff to `Master`/`Fixer`.
     - `Fixer` acquires scoped lock on defect-referenced files -> applies minimal root-cause fix -> commits & logs handoff back to `Detector` (releasing write lock).
     - `Detector` independently retests -> records `PASS`/`FAIL` retest result.
     - Major scope, visual, or submission decisions always pause for explicit approval by **Basmala Jamal** and **Maria Mnasra**.
- **Standard Handoff Payload**: Every handoff message between roles must include:
  1. `Timestamp` and `Session ID`
  2. `From Role` -> `To Role`
  3. `Files Released / Lock Transferred` and `Commit Hash`
  4. `Scope of Request / Acceptance Checks`
  5. `Known Limitations or Open Questions`

### 4.4 Preserved Real Prompts, Evidence & Zero-Fabrication Policy
- **Preserved Real Prompts**: Every substantive user/team prompt driving project work must be saved verbatim in `prompts/` using sequential numbered filenames (e.g., `prompts/prompt_01_revise_prd.md`, `prompts/prompt_02_targeted_prd_corrections.md`).
- **Preserved Build & QA Evidence**: Actual LuaLaTeX/Biber logs, Python script outputs, PDF page-count checks, and incident records must be preserved honestly.
- **Zero Fabrication Rule (Non-Negotiable)**:
  - Never invent lecturer requirements, document filenames, slide numbers, or page numbers from files that were not actually read.
  - Never invent citations, authors, publication years, standard version numbers, or benchmark measurements.
  - Never fabricate cross-session agent messages, prompts, incident logs, or test passes.
  - Whenever an item cannot be verified (e.g., missing source file or inability to visually inspect a rendered page), explicitly log the limitation rather than guessing.

---

## 5. Verification, Quality Assurance, Incident Records & Red-Teaming

This PRD mandates a clear separation between **Product Design Verification** (evaluating Fuel&Go as an engineering system) and **Report Quality Assurance** (evaluating the 25-page Assignment 02 PDF and its reproducible artifacts).

### 5.1 Product Design Verification (Fuel&Go Engineering Soundness)
Evaluates whether the designed Fuel&Go system is internally coherent, safe, and feasible at a preliminary design level:
- **Requirements Completeness & Consistency**: Every core `FR-01..06` and `NFR-*` is unambiguous, testable, and aligned strictly to fueling + EV charging (no unapproved scope bleed).
- **State-Machine & Protocol Integrity**: Both fuel-dispensing and EV-charging lifecycles handle normal completion, user cancel, timeout, payment hold release, and hardware fault transitions without leaving a pump/charger stuck unlocked or double-charging a driver.
- **Safety & Security Boundary Audit**: Physical fuel-pump and EVSE electrical safety interlocks remain strictly local to certified hardware; zero raw payment card PANs touch Fuel&Go servers; geofence/QR spoofing mitigations are explicitly analyzed.
- **Traceability**: Every core requirement traces cleanly to architecture components, external interfaces, and a defined conceptual verification method.

### 5.2 Report Quality Assurance — Report QA (Deliverable Soundness)
Evaluates the compiled Assignment 02 PDF and repository package:
- **Exact Page Count Gate**: `pdfinfo` / LuaLaTeX log confirms **strictly 25 English pages** according to the confirmed `Q-01` boundary (either `Total PDF Pages == 25`, or `Body Pages == 25` with excluded front/back matter pages counted additionally).
- **Clean Deterministic Compilation**: `lualatex -> biber -> lualatex -> lualatex` completes with exit code `0`, zero LaTeX errors, zero Biber errors, zero `??` unresolved cross-references, and zero undefined citation keys.
- **Visual & Typographic Inspection**: Rendered PDF pages are visually inspected (converted to PNG or viewed directly) for clipped tables, overlapping TikZ labels, broken margins, widow/orphan headings, header/footer consistency, and readable text contrast. If visual inspection cannot be executed in a given environment, that limitation must be logged explicitly.
- **IEEE Citation & Standard Verification**: All citations render in consistent IEEE numerical style (`[1]`, `[2]`, ...) with verified sources and verified standard editions.
- **Python Figure Reproducibility**: Running the documented regeneration command in a clean environment reproduces all Python figures identically from committed scripts and data, with explicit provenance labels on every chart.

### 5.3 Detector vs. Fixer Workflow & Mandatory 5-Part Incident Records (Team Workflow Choice)
Every defect discovered during Product Design Verification, Report QA, or Red-Teaming must follow the strict **Detector -> Fixer -> Detector Retest** loop:
1. **Detector** discovers a defect and opens a numbered incident file (`qa/incidents/INC-XXX.md`) without modifying the production file.
2. **Master** (or automated handoff) assigns the incident to **Fixer**.
3. **Fixer** diagnoses the root cause, patches only the affected files, adds a preventive check where applicable, and hands the updated commit back to **Detector**.
4. **Detector** independently re-executes verification and records the **Retest Result** (`PASS` -> Close, or `FAIL` -> Reopen with new evidence).

Every incident record **must** contain all **5 mandatory parts**:
1. **What happened**: Exact symptom, severity, affected file(s), page/line number, and raw evidence (log snippet, screenshot reference, or text quote).
2. **Why it happened**: Technical or process root cause (not just a restatement of the symptom).
3. **Why earlier checks missed it**: Gap in earlier reviews, scripts, or guidelines that allowed the defect to slip through.
4. **What changed**: Exact edits applied (file paths, commit hash) plus any process/check improvement added to prevent recurrence.
5. **Retest result**: Independent Detector re-verification method, observed output, timestamp, and final status (`PASS` / `FAIL`).

### 5.4 Red-Team Requirements
Before final release, the **Detector** (acting in an adversarial Red-Team pass) must execute a documented Red-Team audit (`qa/redteam/redteam_audit.md`) covering two tracks:
- **Track A — Fuel&Go Design Red-Team**: Actively attempt to break the conceptual design across critical failure modes:
  - Remote activation of the wrong pump or EV charger (QR swap / GPS spoofing / bay mismatch).
  - Pre-authorization race conditions, duplicate settlement, or orphaned payment holds on network drop.
  - EV charging session hijacking, connector lock/unlock failures, or stale SoC/tariff updates.
  - Physical safety violation vectors at fuel forecourts and high-voltage DC fast chargers.
- **Track B — Report & Evidence Red-Team**: Actively audit the 25-page PDF and repository for:
  - Unverified or hallucinated claims, numbers, citations, or standard editions.
  - Disguised illustrative/simulated plots presented as real measurements.
  - Scope creep (proposed extensions accidentally presented as core requirements).
  - Missing prompts, missing cross-session logs, or incomplete 5-part incident records.

---

## 6. Reproducible Python Graphs & Vector Diagrams

### 6.1 Reproducible Python Graph Pipeline (Mandatory)
All quantitative charts and analytical plots included in the report must be generated by **reproducible Python scripts** exporting vector graphics (`.pdf` or `.svg` converted cleanly to `.pdf`) for inclusion in LaTeX:
- **Scripts**: Stored under `scripts/plots/` (one modular script per figure or a clean entry-point runner `scripts/generate_figures.py`).
- **Data & Sources**: Stored under `data/` with a `data/README.md` mapping every dataset file to its exact origin and license/citation.
- **Pinned Dependencies**: Exact Python version and pinned package versions (e.g., `matplotlib`, `numpy`, `pandas`) recorded in `requirements.txt` (or `pyproject.toml`).
- **Reproduction Steps**: Clear, tested step-by-step Windows PowerShell commands in `README.md` / `scripts/README.md` allowing any grader to regenerate every chart deterministically (including fixed random seeds if any simulation is used).

### 6.2 Mandatory Data Provenance Distinction
Every Python chart (both in its figure caption/footnote and in `data/README.md`) and every quantitative table in the report must explicitly tag its data into one or more of four distinct categories:

| Provenance Tag | Definition | Required Disclosure in Report |
| --- | --- | --- |
| **Sourced Measurement** | Empirical figure or dataset published by a verified external source. | IEEE citation `[N]` + exact source table/year + units. |
| **Calculation** | Deterministic mathematical result derived from cited measurements or explicit stated inputs. | Formula/method stated in text or appendix + input provenance. |
| **Assumption** | Engineering baseline chosen by Team NextMind for preliminary sizing without empirical field data. | Explicitly labeled *(Engineering Assumption)* with rationale. |
| **Illustrative / Simulated Data** | Synthetic curve, modeled scenario, or conceptual workload simulation created to illustrate system behavior. | Prominently labeled *(Illustrative / Simulated — Not Empirical Field Data)* in both caption and legend/subtitle. |

### 6.3 TikZ / Vector Architectural Diagrams
Structural and behavioral diagrams shall be authored as crisp **TikZ / vector diagrams** stored in `figures/`:
1. Core Use-Case & Actor Interaction Diagram (ICE/Hybrid & EV Drivers, Payment Gateway, Forecourt Controller, EV CPMS).
2. High-Level Fuel&Go Multi-Layer System Architecture Diagram.
3. Unified Fueling & EV Charging Session Finite State Machine (showing shared authorization/settlement spine and diverging dispensing vs. EV charging branches + fault transitions).
4. Conceptual Entity-Relationship Diagram (ERD).
5. End-to-End Pump & EV Charger Authorization/Settlement Sequence Diagram.
6. Physical Forecourt & EVSE Safety Interlock Boundary Diagram.

---

## 7. Citation Standard (`biber` + IEEE) & Source Verification

### 7.1 Mandatory Citation Style: IEEE Only
- **Engine**: `biblatex` with `backend=biber`, `style=ieee`, `sorting=none`.
- **Removal of APA**: APA style (and any mixed author-year / numeric style) is **explicitly prohibited**. All in-text citations must use consistent IEEE numeric brackets (`[1]`, `[2]–[4]`) matching the bibliography order of appearance.
- **Database**: All bibliography entries live in `bib/references.bib` (UTF-8).

### 7.2 Source Verification & Reference Count Target
- **Reference Count Target**: `TBD — requires rationale and team approval` (verified via `biber` audit and Research claim-to-source coverage review; not an arbitrary pre-set number or unverified lecturer minimum).
- **Verified Supporting Sources Only**: Every cited paper, specification, or technical report must be retrieved and verified by the Research role or team partners before entering `bib/references.bib`. Zero fabricated titles, DOIs, URLs, authors, or publication dates.

### 7.3 Candidate Standards Requiring Version Verification Before Final Citation
The following candidate standards are relevant to Fuel&Go (fueling + EV charging) and software engineering design. **Exact edition/version numbers must be verified by the Research agent prior to citation** (do not cite unverified versions):

| Domain | Candidate Standard / Specification | Version Verification Status |
| --- | --- | --- |
| Requirements Engineering | ISO/IEC/IEEE 29148 | *To Be Verified (e.g., 2018 edition / latest active)* |
| Architecture Description | ISO/IEC/IEEE 42010 / IEEE 1016 | *To Be Verified* |
| Payment Card Security | PCI DSS (v4.0 / v4.0.1) | *To Be Verified against PCI SSC current release* |
| Mobile & API Security | OWASP MASVS & OWASP API Security Top 10 | *To Be Verified (exact version/year)* |
| Accessibility | W3C WCAG (2.1 / 2.2 Level AA) | *To Be Verified* |
| Data Privacy | EU GDPR (Regulation 2016/679) / applicable local privacy framework | *To Be Verified* |
| EV Charging Protocols | OCPP (e.g., 2.0.1 / 2.1) & ISO 15118 (Plug & Charge) | *To Be Verified against OCA / ISO published editions* |
| Fuel Forecourt Integration | IFSF (International Forecourt Standards Forum) specifications | *To Be Verified* |

---

## 8. Visual Design & Custom `.cls` Architecture (Proposals Pending Approval)

> **Approval Notice (`Q-04`)**: All specific aesthetic choices below (colors, font pairings, cover layout, and callout box styles) are **Proposals Only — Pending Maria Mnasra and Basmala Jamal's Approval**. Design must not finalize visual branding until both partners review and approve a sample render.

### 8.1 Non-Negotiable Visual Principles (Preserved Across Any Approved Theme)
- **Custom Class Encapsulation**: All layout, typography, colors, headers/footers, cover page macros, and reusable environments must live in a custom LaTeX class file (`nextmind-pdr.cls`, built for LuaLaTeX).
- **Readability First**: Comfortable body font size, balanced line spacing, generous A4 margins, and zero cramped tables or microscopic figure labels (exact measurements finalized in `nextmind-pdr.cls` once Maria and Basmala approve the sample render).
- **Accessible Contrast**: Body text, headings, table headers, callout backgrounds, and Python/TikZ chart palettes must preserve strong legibility and accessible color contrast per W3C WCAG Level AA (`>= 4.5:1` for normal text and `>= 3:1` for large text/non-text UI/graphical elements; exact WCAG edition to be verified by Research), plus grayscale/print legibility.
- **LuaLaTeX Native Fonts**: Loaded via `fontspec` using fonts verified to exist in the target TeX/Windows environment (with deterministic fallbacks so builds never fail across Maria's and Basmala's machines).

### 8.2 Proposed Visual System (Pending Maria & Basmala's Approval)
- **Proposed Palette**: Deep Navy (`#0F2942`) primary headings/headers, Fuel Amber (`#D95D16`) or EV Emerald (`#0E7C66`) accents (highlighting dual fueling + EV charging identity), Charcoal (`#1E293B`) body text, and Soft Neutral Gray (`#F4F6F9`) callout/stripe tint.
- **Proposed Typography**: Clean sans-serif headings (`TeX Gyre Heros` / `Inter` / `Latin Modern Sans`), readable body (`Source Sans 3` / `TeX Gyre Pagella` / `Latin Modern`), and monospace (`Fira Code` / `TeX Gyre Cursor`) for technical identifiers and endpoints.
- **Proposed Class Macros & Environments**:
  - Metadata macros: `\projecttitle`, `\reportsubtitle`, `\assignmentcode`, `\teamname`, `\teammembers`, `\docversion`, `\docdate`.
  - Cover macro: `\makepdrcover` (vector TikZ cover layout, pending visual sign-off).
  - Dynamic running headers/footers via `fancyhdr` + `lastpage` (`Page \thepage\ of \pageref{LastPage}` — never hard-coding `"Page X of 25"` so pagination remains accurate regardless of `Q-01` resolution).
  - Styled callout boxes (`tcolorbox`), standardized `booktabs`/`tabularx` requirement tables, and consistent TikZ styles shared across all figures.

---

## 9. Targets & Candidate Technologies (Provenance, Artifact Type & Status)

### 9.1 Artifact Type vs. Completion Status Distinction
To uphold zero fabrication and complete academic transparency, this PRD strictly separates **Artifact Type** from **Completion Status**:
- **Artifact Type**:
  - *Conceptual System Design*: Fuel&Go runtime software/hardware components (mobile app, backend services, payment tokenization flow, forecourt gateway, EV CPMS adapter, database, and runtime targets) that are **designed and analyzed**, not built or field-tested in Assignment 02.
  - *Report / Pipeline Artifact*: Assignment 02 engineering deliverables that will actually be built and verified in this repository (custom LuaLaTeX `.cls`, LaTeX/Biber pipeline, Python plotting scripts, and automated QA checks).
- **Completion Status**: Nothing is marked `Implemented / Tested` until it has been built, executed, and verified with preserved real evidence. Until then, planned artifacts carry status **`Planned — verification pending`**.

### 9.2 System Targets (Justified Standards vs. TBD Numerical Targets)
Arbitrary numerical values without source backing are **prohibited**. Quantitative targets without an approved rationale/source are marked **`TBD — requires rationale and team approval`** alongside their verification method; justified standards-backed targets cite their governing standard (with exact version to be verified by Research):

| ID | Metric / Property | Target | Rationale / Source | Verification Method | Approval Status | Artifact Type |
| --- | --- | --- | --- | --- | --- | --- |
| **NFR-01a** | Station & Charger Discovery Latency (P95) | `TBD — requires rationale and team approval` | Must be anchored to a verified mobile UX responsiveness reference (e.g., Nielsen Norman Group / cited latency study verified by Research) before setting a number | Analytical latency budget (conceptual) / future API load benchmark | Pending Research rationale & team approval | Conceptual System Design |
| **NFR-01b** | Pump / EV Charger Authorization Round-Trip (P95) | `TBD — requires rationale and team approval` | Must be derived from cited PSP pre-authorization + forecourt/OCPP handshake timing budgets | Sequence-diagram timing breakdown (conceptual) / future simulator or HIL test | Pending Research rationale & team approval | Conceptual System Design |
| **NFR-02** | Live Telemetry Refresh Cadence (Fueling vs. EV Charging) | `TBD — requires rationale and team approval` | Fueling sessions are short (minutes) whereas EV sessions are longer; exact cadences must be justified from protocol specs (IFSF / OCPP) and payload math | Protocol payload & bandwidth calculation (conceptual) / future simulator test | Pending Research rationale & team approval | Conceptual System Design |
| **NFR-03** | Core Session Service Availability | `TBD — requires rationale and team approval` | Availability tier must be justified against redundancy architecture and operational cost trade-offs | Redundancy & failure-mode analysis (FMEA / conceptual) | Pending Research rationale & team approval | Conceptual System Design |
| **NFR-04** | Peak Concurrent Active Sessions | `TBD — requires rationale and team approval` | Concurrency sizing must be derived explicitly from cited station-count/demand assumptions in a reproducible Python sizing script | Reproducible Python analytical capacity calculation (explicitly tagged *Calculation* / *Assumption*) | Pending Research rationale & team approval | Conceptual System Design |
| **NFR-05** | Payment & Transport Security | `0` raw PANs stored on Fuel&Go servers; encrypted transit & storage | Justified by **PCI DSS** cardholder-data-environment scope reduction via PSP tokenization and **OWASP** transport/storage guidance *(exact versions to be verified by Research)* | Architecture & STRIDE threat-model review + Detector Red-Team audit | *Proposed — Pending Team Approval* | Conceptual System Design |
| **NFR-06** | Physical Safety Interlock Independence | `100%` local hardware enforcement | Justified by forecourt dispenser & EVSE safety isolation principle: cloud/mobile layers must never override certified physical emergency cutoffs *(applicable safety standard to be verified by Research)* | Safety boundary diagram review & Red-Team fault-injection analysis | *Proposed — Pending Team Approval* | Conceptual System Design |
| **NFR-07a** | Accessible Visual Contrast | WCAG Level AA (`>= 4.5:1` normal text; `>= 3:1` large text / UI components) | Justified by **W3C WCAG** Success Criteria 1.4.3 & 1.4.11 *(exact WCAG edition 2.1 vs. 2.2 to be verified by Research)* | Contrast-ratio calculation & wireframe / PDF visual inspection | *Proposed — Pending Team Approval* | Conceptual Design & Report QA |
| **NFR-07b** | Mobile Session-Start Interaction Complexity (Step/Tap Count) | `TBD — requires rationale and team approval` | Must be justified from wireframe task-flow walkthroughs rather than an arbitrary tap cap | Wireframe task-flow walkthrough & usability heuristic audit | Pending wireframe & team approval | Conceptual System Design |

### 9.3 Candidate Technologies (Separated by Artifact Type & Honest Completion Status)

| Layer / Domain | Candidate Technology | Rationale / Source | Verification Method | Approval Status | Artifact Type | Completion Status |
| --- | --- | --- | --- | --- | --- | --- |
| **Mobile App (Fuel&Go)** | Flutter or React Native (cross-platform iOS/Android) | Single codebase for iOS/Android with native QR/NFC/location support *(Trade-off matrix to be cited by Research)* | Comparative trade-off analysis in Sec. 4 | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **API & Backend Services** | Modular REST + WebSocket APIs (e.g., Node.js/TypeScript, Go, or Python/FastAPI) behind API Gateway | Clear domain separation between Station Discovery, Session Orchestrator, Payment, and Adapters | Interface contract & state-machine review | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **Data Storage** | PostgreSQL + PostGIS (transactional ledger & geospatial queries) + Redis (live pump/charger status cache) | ACID guarantees for payment/session ledger + low-latency geospatial & status lookups | Conceptual ERD & query-path analysis | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **Messaging / Telemetry** | Event broker (e.g., RabbitMQ or Kafka) + WebSockets/SSE to client | Decouples live fueling/EV telemetry from billing settlement | Architecture & fault-recovery analysis | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **Station & EV Integration** | Dedicated Adapter Layer: Forecourt Gateway (IFSF / vendor POS API) + EV CPMS Adapter (OCPP / ISO 15118) | Isolates vendor protocol heterogeneity and enforces safety boundaries *(Protocol versions to be verified)* | Protocol mapping & Red-Team review | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **Payment Processing** | Tokenized PSP (e.g., Stripe / Adyen / PCI-compliant gateway) | Eliminates raw cardholder data from Fuel&Go backend, reducing PCI DSS scope | Threat model & tokenization flow audit | *Proposed — Pending Team Approval* | Conceptual System Design | `Planned — verification pending` |
| **Report Typesetting** | LuaLaTeX + Biber (`biblatex`, IEEE) + custom `nextmind-pdr.cls` | Deterministic Unicode/font handling, vector layout, automated IEEE citations | Clean compilation + exact 25-page check + visual PDF inspection | **Confirmed Team Decision** | Report / Pipeline Artifact | `Planned — verification pending` |
| **Analytical Plotting** | Python 3 + `matplotlib` / `numpy` / `pandas` (pinned in `requirements.txt`) | Reproducible, script-driven vector figures with auditable data provenance | Clean-environment script regeneration + visual inspection | **Confirmed Team Decision** | Report / Pipeline Artifact | `Planned — verification pending` |

---

## 10. Deliverables & Repository Governance Rules

### 10.1 Complete Assignment 02 Deliverables Checklist (Separated by Artifact Type & Honest Completion Status)

| Deliverable | Owner | Required Scope / Contents | Expected Location / Channel | Artifact Type | Completion Status |
| --- | --- | --- | --- | --- | --- |
| **`PRD.md`** | **Basmala Jamal** | Authoritative requirements specification, scope governance, and acceptance criteria | `PRD.md` | Governance Doc | **Draft — Pending Team Review** |
| **`PLAN.md`** | **Maria Mnasra** | Execution phases, dependencies, owners, and quality gates | `PLAN.md` | Governance / Planning Doc | `Planned — verification pending` |
| **`TODO.md`** | **Maria Mnasra** | Actionable tasks, owners, status, and linked evidence | `TODO.md` | Governance / Tracking Doc | `Planned — verification pending` |
| **`README.md`** | **Joint (Maria Mnasra & Basmala Jamal)** | Project overview, both authors, build/reproduction steps, screenshots, figures, and real agent evidence | `README.md` | Repository Documentation | `Planned — verification pending` |
| **Compiled 25-Page English PDF Report** | Joint (Design build -> Detector QA -> Partner sign-off) | Strictly 25 English pages per confirmed `Q-01` boundary | `main.pdf` (or agreed release path) | Report Deliverable | `Planned — verification pending` |
| **Full LaTeX Source & Custom `.cls`** | Research (drafts) -> Design (LaTeX/layout/TikZ) | `main.tex`, `nextmind-pdr.cls`, `sections/*.tex`, `bib/references.bib`, `figures/*.tex` | Root / `sections/` / `bib/` / `figures/` | Report Source / Styling | `Planned — verification pending` |
| **Reproducible Python Graph Suite** | Research (data provenance) -> Design (scripts/plots) | Plot scripts, input data/sources, pinned dependencies (`requirements.txt`), and reproduction steps | `scripts/plots/`, `data/`, `requirements.txt` | Analytical Plot Pipeline | `Planned — verification pending` |
| **5 Role-Specific Agent Skill Files** | Joint / Master coordination | `SKILL.md` for Master, Research, Design, Detector, Fixer | `agents/{master,research,design,detector,fixer}/SKILL.md` | Team Workflow Governance | `Planned — verification pending` |
| **Preserved Real Prompts** | Joint | Verbatim real prompts saved sequentially | `prompts/prompt_01_revise_prd.md`, `prompts/prompt_02_targeted_prd_corrections.md`, ... | Evidence Artifact | In Progress (`01`–`02` saved) |
| **Baseline Draft Backups** | Basmala Jamal | Preserved pre-edit snapshots of `PRD.md` | `backups/PRD.original.md`, `backups/PRD.v1.1.0-draft.bak.md` | Archive / Evidence Artifact | In Progress (`v1.0.0` & `v1.1.0-draft` archived) |
| **Real Cross-Session Agent Messages & Handoffs** | Master & all roles | Authentic logged cross-session messages and lock handoffs | `agents/messages/` | Evidence Artifact | `Planned — verification pending` |
| **Detector/Fixer 5-Part Incident Records & Red-Team Audit** | Detector (audit/retest) & Fixer (remediation) | 5-part incident tickets, QA reports, and dual-track Red-Team audit | `qa/incidents/`, `qa/redteam/`, `qa/reports/` | QA Evidence Artifact | `Planned — verification pending` |
| **Separate Moodle Submission Form** | **Joint (Maria Mnasra & Basmala Jamal)** | External course Moodle portal form, required fields, uploads, and deadline verification | Course Moodle Portal (External to GitHub) | External Submission Gate | `Planned — tracked separately` |

### 10.2 Mandatory Repository & External Utility Rules
1. **Git Configuration**: Repository initialized in project root (`NextMind-ex02`), default branch strictly `main`, connected to `https://github.com/jamalbasmala907-ship-it/NextMind_02.git`.
2. **External Local Utility Setup (`agy-multi-agent-mesh/`)**:
   - The local utility directory `agy-multi-agent-mesh/` **may remain locally** inside `NextMind-ex02` if used by team members for multi-agent orchestration—**do not move or modify it**.
   - `agy-multi-agent-mesh/` **must be excluded via `.gitignore`** so it is never tracked, staged, or committed into `NextMind_02`.
   - **External Dependency Documentation**: `agy-multi-agent-mesh/` is documented strictly as an external local utility dependency (not authored project source). Any other nested utility repositories must similarly remain untracked/separate. Reproducing the 25-page PDF via LuaLaTeX + Biber and regenerating the Python graphs must remain independent of committing `agy-multi-agent-mesh/`.
3. **Permissions & Licensing Check for Provided Materials**: Before committing any lecturer-provided template, dataset, logo, image, or third-party asset into GitHub (especially if public), Maria and Basmala must verify distribution permissions and copyright/course rules. Restricted course materials must not be redistributed without explicit permission.
4. **Instructor Access**: Repository visibility and/or collaborator permissions must be verified so the course lecturer and graders have required access by the submission deadline (`Q-07`).
5. **Genuine Contributions from Both Partners**: Both **Maria Mnasra** and **Basmala Jamal** must make genuine, substantive, attributable contributions (reflected in Git commit authorship, deliverable ownership across `PRD.md`, `PLAN.md`, `TODO.md`, `README.md`, report production, reviews, and sign-offs).
6. **Separate Moodle Form Tracking**: Pushing to GitHub does **not** complete course submission. The **Moodle submission form** (required fields, partner names, links, PDF upload, declarations, and submission timestamp) must be tracked as a separate mandatory checklist item and verified before the deadline (`Q-08`).
7. **Clean Build Hygiene**: `.gitignore` excludes `agy-multi-agent-mesh/`, transient LaTeX auxiliary files (`*.aux`, `*.bbl`, `*.bcf`, `*.blg`, `*.out`, `*.run.xml`, `*.toc`, `*.lof`, `*.lot`, `build/`), and Python caches/venvs, while keeping curated QA/build evidence under `qa/`.

---

## 11. Governance & Provenance Separation Matrix

To prevent conflating verified course rules with team workflow choices, proposals, or unverified assumptions, all project directives are strictly partitioned into five categories:

### 11.1 Explicit Lecturer Requirements (Actual Source Filenames & Page Numbers Only)
> **Source Availability & Zero-Fabrication Notice**: As of `v1.2.0-draft`, **no official Assignment 02 lecturer instruction files exist inside** `C:\Users\jamal\OneDrive - Bar-Ilan University - Students\Desktop\NextMind-ex02`, and unrelated personal folders were intentionally **not** scanned. Accordingly, no requirement is promoted to "verified explicit lecturer requirement" with guessed filenames or page numbers. Only requirements backed by actual lecturer filenames and page numbers read directly by the team may be populated here (`Q-06`).

| Req. ID | Candidate Requirement to Verify Against Lecturer Files | Actual Source Filename | Page Number(s) | Verification Status |
| --- | --- | --- | :---: | --- |
| **LR-01** | Assignment 02 report length (`25 English pages`) and whether cover/ToC/references/appendices are included or additional | `Unverified — lecturer file not present in project folder` | `Unverified` | Pending Source Review |
| **LR-02** | Typesetting & citation requirements (English PDF, LuaLaTeX + Biber, custom `.cls`, IEEE citation style, reproducible Python graphs / TikZ) | `Unverified — lecturer file not present in project folder` | `Unverified` | Pending Source Review |
| **LR-03** | Required document framing/title (verify whether `"Preliminary Design Report"` is mandated) | `Unverified — lecturer file not present in project folder` | `Unverified` | Pending Source Review |
| **LR-04** | Multi-agent / evidence expectations (verify which agent roles, prompts, logs, or incident formats are explicitly mandated vs. team workflow choices) | `Unverified — lecturer file not present in project folder` | `Unverified` | Pending Source Review |
| **LR-05** | Repository deliverables (`PRD.md`, `PLAN.md`, `TODO.md`, `README.md`), instructor access, genuine contributions from both partners, and separate Moodle submission form | `Unverified — lecturer file not present in project folder` | `Unverified` | Pending Source Review |

### 11.2 Confirmed Team Decisions & Team Workflow Choices (Team NextMind)
- **TD-01**: Team name is **NextMind**; partners are **Maria Mnasra** and **Basmala Jamal**.
- **TD-02**: Core partner deliverable ownership: **Basmala Jamal** owns `PRD.md`; **Maria Mnasra** owns `PLAN.md` and `TODO.md`; both jointly own `README.md` and jointly approve all major decisions.
- **TD-03**: Project domain is **Fuel&Go**, with **core capabilities focused on fueling and EV charging**.
- **TD-04**: Target and acceptance criterion is **strictly 25 English pages** (exact, subject to `Q-01` boundary clarification; excluded front/back matter are additional if 25 body pages are required).
- **TD-05**: Report production toolchain is **LuaLaTeX + Biber + custom `.cls`** with **IEEE citation style only** (APA removed), plus **reproducible Python graphs** (with 4-category data provenance labeling) and **TikZ/vector diagrams**.
- **TD-06 (Team Workflow Choice)**: Unless explicitly mandated by verified lecturer files in Section 11.1, the **5-role multi-agent setup** (`Master`, `Research`, `Design`, `Detector`, `Fixer`), role-specific `SKILL.md` files, single-writer handoff locks, strict Detector/Fixer review & independent retesting, **5-part incident record format**, dual-track red-teaming, real cross-session messages, preserved real prompts, and **zero fabrication** are adopted as **Team NextMind Workflow Choices**.
- **TD-07**: GitHub remote is `https://github.com/jamalbasmala907-ship-it/NextMind_02.git` on branch `main`; `agy-multi-agent-mesh/` may exist locally untouched and is excluded via `.gitignore`; the Moodle submission form is tracked separately.

### 11.3 Proposed Choices (Pending Maria Mnasra & Basmala Jamal's Approval)
- **PC-01**: Rebalanceable section-by-section page budget in Section 3.3 (Option A vs. Option B depending on `Q-01`).
- **PC-02**: Visual design proposal in Section 8.2 (palette, font pairing, cover page style, callout styling, working class filename `nextmind-pdr.cls`).
- **PC-03**: Reference count target (currently `TBD — requires rationale and team approval`, Section 7.2).
- **PC-04**: Unbacked conceptual numerical targets (`NFR-01a`, `NFR-01b`, `NFR-02`, `NFR-03`, `NFR-04`, `NFR-07b` — all currently `TBD — requires rationale and team approval`, Section 9.2) and standards-backed security/safety/contrast targets (`NFR-05`, `NFR-06`, `NFR-07a` pending exact standard-version verification).
- **PC-05**: Candidate Fuel&Go runtime technology stack in Section 9.3.
- **PC-06**: Disputed scope extras (`EXT-01` through `EXT-05` — currently `Unverified — pending source review` against original Fuel&Go slides/prior PRD and kept out of core scope).

### 11.4 Assumptions
- **A-01**: Fuel stations expose a certified local forecourt controller and EV charging networks expose a standard CPMS interface (e.g., OCPP-capable) reachable via secure adapters while keeping physical safety interlocks strictly local.
- **A-02**: Both partners' build environments can run TeX Live or MiKTeX (`lualatex` + `biber`) and Python 3 with the pinned packages in `requirements.txt` (without modifying unauthorized global policies).
- **A-03**: Until `Q-01` is resolved, Option A in Section 3.3 serves only as an indicative working layout; if 25 body pages are required, excluded front/back matter will be additional (Option B).

### 11.5 Unresolved Questions Requiring Decision by Maria Mnasra & Basmala Jamal
| ID | Open Question | Impact if Unresolved | Owner(s) |
| --- | --- | --- | --- |
| **Q-01** | Do **cover page, table of contents/front matter, references, and appendices** count inside the strict 25 English pages (Option A), or are 25 body pages required with those excluded parts **additional** (Option B)? | Determines final body vs. total PDF page count and rebalancing plan. | Maria & Basmala (verify lecturer files) |
| **Q-02** | Is **"Preliminary Design Report"** the exact intended framing/title for Assignment 02? | Determines cover title, running headers, abstract, and tone. | Maria & Basmala (verify lecturer files) |
| **Q-03** | Beyond course lecturer/graders, which optional secondary **report readers** (e.g., engineering review board, investors) should the report address, if any? | Shapes Executive Summary and level of business vs. engineering framing. | Maria & Basmala |
| **Q-04** | Which **visual design** (color palette, font pairing, cover layout, class filename) do Maria and Basmala approve? | Blocks finalizing `nextmind-pdr.cls`. | Maria & Basmala |
| **Q-05** | After checking the original **Fuel&Go slides / prior PRD**, should each disputed feature (`EXT-01..05`) remain Future Scope or be cited and promoted to Core? | Determines final scope provenance and prevents unbacked scope creep. | Maria & Basmala |
| **Q-06** | What are the exact **lecturer instruction filenames and page numbers** to populate Section 11.1 (`LR-01..05`) and confirm which workflow items are lecturer mandates vs. team choices? | Required for complete, zero-fabrication requirement traceability. | Maria & Basmala |
| **Q-07** | Should the GitHub repository be **public or private with instructor collaborators**, and what permissions/licenses apply to any lecturer-provided materials? | Required for instructor access and academic/copyright compliance. | Maria & Basmala |
| **Q-08** | What are the exact fields, uploads, and deadline for the **separate Moodle submission form**? | Required to complete external course submission. | Maria & Basmala |
| **Q-09** | Beyond confirmed ownership (`PRD.md` -> Basmala; `PLAN.md`/`TODO.md` -> Maria; `README.md` -> Joint), how will **report chapters, Python graphs, `.cls`/TikZ, and QA/Red-Team reviews** be split between Maria Mnasra and Basmala Jamal? | Ensures balanced, genuine, attributable partner contributions. | Maria & Basmala |
| **Q-10** | What justified rationale/sources should replace each **`TBD — requires rationale and team approval`** target in Section 9.2 and Section 7.2, and which candidate technologies in Section 9.3 are approved? | Required before Research & Design finalize specifications and charts. | Maria & Basmala (with Research input) |
