# Product Requirements Document (PRD): Fuel&Go — Assignment 02 Report

| Field | Value |
| --- | --- |
| **Project Name** | Fuel&Go (Core: Smart Fueling & EV Charging Platform) |
| **Deliverable** | Assignment 02 Engineering Report (Working Framing: *Preliminary Design Report* — Pending Verification) |
| **Team** | NextMind |
| **Team Partners** | Maria Mnasra, Basmala Jamal |
| **Document Language** | English (en-US) |
| **Target & Acceptance Length** | Strictly 25 Pages (Exact) |
| **Typesetting Engine** | LuaLaTeX + Biber (`biblatex`, IEEE style) |
| **Document Class** | Custom LaTeX Class (`nextmind-pdr.cls` — Working Filename, Visual Design Pending Approval) |
| **Version** | 1.1.0-draft |
| **Status** | **Draft — Pending Team Review** |
| **Previous Baseline Backup** | `backups/PRD.original.md` (v1.0.0) |

### Revision History

| Version | Date | Author / Role | Summary of Changes |
| --- | --- | --- | --- |
| `1.0.0` | 2026-11-24 | Initial Draft | Initial baseline PRD draft (archived unmodified in `backups/PRD.original.md`). |
| `1.1.0-draft` | 2026-11-24 | Revision Draft | Authoritative Assignment 02 revision for Team NextMind (Maria Mnasra & Basmala Jamal): status set to `Draft — Pending Team Review`; aligned Fuel&Go core scope to fueling + EV charging; demoted unsupported extras to proposed extensions/future scope; locked strict 25-page target with inclusion open question; separated report readers from app users; added 5-agent roles/SKILL.md/handoffs/zero-fabrication governance; separated product design verification from report QA with Detector/Fixer 5-part incidents and red-teaming; mandated reproducible Python graphs with provenance labels; standardized on IEEE citations (removed APA); marked visual design as proposals pending team approval; added structured provenance for numerical targets & candidate tech; added full deliverables, repository rules, and 5-category provenance separation. |

---

## 1. Purpose, Report Framing & Audience Separation

### 1.1 Purpose of This PRD
This Product Requirements Document (PRD) serves as the authoritative working specification for **Team NextMind** (**Maria Mnasra** and **Basmala Jamal**) to plan, govern, produce, verify, and submit **Assignment 02**. It defines:
1. The **Fuel&Go** core product scope (fueling and EV charging) and explicit separation from proposed extensions/future scope.
2. The **exact 25-page** English PDF deliverable structure, LuaLaTeX + Biber (IEEE) architecture, reproducible Python figure pipeline, and custom `.cls` styling governance.
3. The **5-role multi-agent workflow** (Master, Research, Design, Detector, Fixer), quality assurance separation, red-team expectations, and strict **zero-fabrication** evidence rules.
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
| **Fleet Manager / Commercial Driver** | *Proposed Extension / Future Scope* | Corporate policy limits, multi-vehicle expense tracking, consolidated invoicing (excluded from core unless approved in `Q-05`). |
| **Station / Forecourt Operator** | *Proposed Extension / Future Scope* | Operational dashboard, manual override visibility, pricing management, convenience order fulfillment (excluded from core unless approved in `Q-05`). |

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

### 2.2 Proposed Extensions / Future Scope (Explicitly Out of Core Scope)
The following items appeared in `backups/PRD.original.md` (v1.0.0) without confirmed assignment backing. They are **demoted from core scope** and labeled strictly as **Proposed Extensions / Future Scope** unless Maria and Basmala explicitly vote to promote any specific item (`Q-05`):

| ID | Capability | Classification | Notes / Rationale for Demotion |
| --- | --- | --- | --- |
| **EXT-01** | Convenience-Store Pre-Ordering & Pickup | *Proposed Extension / Future Scope* | Adds retail catalog, inventory, and fulfillment complexity unrelated to core fueling + EV charging. |
| **EXT-02** | Loyalty Points & Promotions Engine | *Proposed Extension / Future Scope* | Commercial marketing add-on; not required to prove core fueling/EV charging engineering design. |
| **EXT-03** | Fleet Management Portal & Driver Policies | *Proposed Extension / Future Scope* | Separate B2B product surface; keep out of core scope to protect depth within 25 pages. |
| **EXT-04** | Consolidated Corporate / VAT Invoicing | *Proposed Extension / Future Scope* | Distinct tax/accounting workflow beyond basic per-session digital receipts. |
| **EXT-05** | Station Operator Forecourt Dashboard | *Proposed Extension / Future Scope* | Operator web console is an auxiliary B2B interface; core report focuses on driver-side platform and station/CPMS integration boundary. |

*Rule*: If kept as Future Scope, these extensions may be referenced briefly (at most a compact roadmap/future-work table) so they do not consume core requirements, architecture, or page budget.

---

## 3. Strict 25-Page Target & Realistic Section Budget

### 3.1 Page-Count Acceptance Criterion
- **Target & Acceptance Criterion**: The final compiled PDF must be **strictly 25 pages** (exact: `pages == 25`).
- **Explicit Prohibition**: The target is **NOT** "at least 25 pages" and **NOT** an approximate range. A 24-page or 26-page build is a failed QA gate that must be logged by the Detector and resolved by the Fixer before release.

### 3.2 Open Question on Page-Count Boundary (`Q-01`)
> **Open Question (`Q-01` — Unclarified)**: Does the strict **25-page** requirement count the **cover page, table of contents / lists, references, and appendices** inside the 25-page total (i.e., `Total PDF Pages = 25`), OR are cover, front matter, references, and/or appendices excluded from the 25-page count (i.e., `25 pages of main body + front/back matter`)?
>
> **Action Required**: Maria and Basmala must verify this directly against the official Assignment 02 lecturer instructions before chapter drafting begins.

### 3.3 Proposed Section-by-Section Page Budget (Working Baseline: 25 Total PDF Pages)
*Approval Status*: **Proposed Allocation — Pending Maria & Basmala's Approval** (assumes cover, ToC, references, and appendices are included in the 25-page PDF total; if `Q-01` resolves to "25 body pages excluding front/back matter", the ~4.0 pages of front/back matter will be reallocated proportionally into Sections 3–8).

| Section | Proposed Title | Target Pages | Page Range | Planned Technical Content & Visuals |
| --- | --- | :---: | :---: | --- |
| **Front** | Cover Page | 1.0 | p. 1 | NextMind identity, Maria Mnasra & Basmala Jamal, Assignment 02, Fuel&Go title, version/date |
| **Front** | Document Control, Executive Summary & Audience Framing | 1.0 | p. 2 | Metadata, scope summary (fueling + EV charging), key conceptual highlights, reader framing |
| **Front** | Table of Contents, List of Figures/Tables & Acronyms | 1.0 | p. 3 | Auto-generated ToC, compact LoF/LoT, domain acronyms (EV, OCPP, IFSF, PCI DSS, SoC, etc.) |
| **Sec. 1** | Introduction, Motivation & Scope Boundaries | 2.0 | pp. 4–5 | Fueling + EV charging user pain points, project goals, Core vs. Future Scope boundary table |
| **Sec. 2** | Users, Stakeholders & Market/Domain Context | 2.0 | pp. 6–7 | App user personas (ICE/hybrid & EV drivers), report vs. system stakeholder distinction, Python chart #1 (market/adoption or dwell-time comparison with explicit provenance) |
| **Sec. 3** | System Requirements Specification (`FR` & `NFR`) | 3.0 | pp. 8–10 | Core `FR-01..06`, quantified `NFR` table with rationale/verification/status, TikZ use-case diagram, MoSCoW prioritization |
| **Sec. 4** | Preliminary System Architecture & Technology Trade-Offs | 4.0 | pp. 11–14 | TikZ multi-layer architecture diagram (mobile, edge/API, fueling + EV orchestrator, forecourt & CPMS adapters), TikZ unified fueling/EV session state machine, candidate technology trade-off table (conceptual vs. implemented distinction) |
| **Sec. 5** | Data Model & External Protocols (Forecourt, EV CPMS & Payment) | 3.0 | pp. 15–17 | TikZ conceptual ERD, REST/WebSocket contract summary, TikZ end-to-end pump & EV charger authorization/settlement sequence diagram, Python chart #2 (conceptual latency/throughput budget or EV charging curve model) |
| **Sec. 6** | UX/UI Preliminary Flows & Accessibility | 2.0 | pp. 18–19 | Core mobile journeys (station/charger discovery, scan/authorize, live fueling vs. EV telemetry, digital receipt), WCAG accessibility rules |
| **Sec. 7** | Security, Physical Safety, Privacy & Compliance | 2.0 | pp. 20–21 | Threat model (STRIDE summary), PCI DSS tokenization & GDPR controls, TikZ physical safety interlock boundary diagram (fuel dispenser + EVSE local cutoffs) |
| **Sec. 8** | Verification, Validation, QA & Red-Team Summary | 2.0 | pp. 22–23 | Separation of Product Design Verification vs. Report QA, requirement traceability matrix, Detector/Fixer incident & red-team findings summary, Python chart #3 (conceptual reliability/error-budget or QA/traceability summary) |
| **Sec. 9** | Project Plan, Risks, Multi-Agent Process & Conclusions | 1.0 | p. 24 | Risk register, team roles (Maria & Basmala + 5-agent workflow summary), transition to next phase, Future Scope roadmap note |
| **Back** | IEEE References (`biber`) & Compact Appendix | 1.0 | p. 25 | Verified IEEE bibliography + compact appendix (reproduction commands / provenance legend); *if references exceed 0.7 pages, rebalance 0.5 pages from Sec. 4 or Sec. 8 to keep strictly 25 pages* |
| **TOTAL** | **Complete Assignment 02 PDF** | **25.0** | **pp. 1–25** | **Strictly 25 Pages (Exact)** |

---

## 4. Multi-Agent Architecture, Roles, Ownership & Evidence Integrity

Assignment 02 utilizes a structured **5-role multi-agent workflow** supervised by **Maria Mnasra** and **Basmala Jamal**.

### 4.1 The Five Multi-Agent Roles & `SKILL.md` Files
Each role must have a dedicated, version-controlled `SKILL.md` file specifying its mandate, permitted tools, prohibited actions, input/output contracts, and verification rules:

| Role | Skill File Path (Proposed) | Primary Mandate | Exclusive File Ownership | Prohibited Actions |
| --- | --- | --- | --- | --- |
| **1. Master** | `agents/master/SKILL.md` | Plans milestones, coordinates handoffs, resolves cross-role conflicts, enforces 25-page budget and team decisions, approves final merge readiness with Maria & Basmala. | `PRD.md` (with team approval), coordination logs (`agents/messages/`), release checklists | Must not fabricate evidence or override unresolved Detector critical defects without Fixer resolution and Detector retest. |
| **2. Research** | `agents/research/SKILL.md` | Gathers and verifies literature, standards versions, domain protocols (IFSF, OCPP, ISO 15118, PCI DSS, etc.), empirical data sources, and curated IEEE `.bib` entries. | `bib/references.bib`, `data/sources/` (source verification notes & raw cited data) | Must not invent citations, DOIs, URLs, standard versions, or empirical statistics. |
| **3. Design** | `agents/design/SKILL.md` | Authors custom `.cls` styling (once approved), modular LaTeX sections, TikZ/vector diagrams, and reproducible Python plotting scripts. | `nextmind-pdr.cls`, `main.tex`, `sections/*.tex`, `figures/*.tex`, `scripts/plots/*.py` | Must not self-certify QA sign-off or alter Detector incident logs. |
| **4. Detector** | `agents/detector/SKILL.md` | Independent auditor & red-teamer: executes Product Design Verification and Report QA, visually inspects rendered PDF pages, audits citations/provenance/reproducibility, logs 5-part incidents, and performs independent retests. | `qa/incidents/*.md`, `qa/redteam/*.md`, `qa/reports/*.md` | **Read-only on production report/code files**: must NOT directly edit `sections/`, `.cls`, `.bib`, or plotting scripts (strict separation of duties). |
| **5. Fixer** | `agents/fixer/SKILL.md` | Performs root-cause remediation of Detector-logged defects in LaTeX, `.cls`, bibliography, or Python scripts; documents exact changes and preventive guardrails; hands back to Detector for retest. | Targeted fixes on defect-referenced files (`sections/`, `.cls`, `bib/`, `scripts/plots/`) during assigned fix tickets | Must not close Detector incidents or skip independent Detector retest. |

### 4.2 Real Cross-Session Messages & Handoff Protocol
- **Authentic Cross-Session Communication**: All inter-agent assignments, clarifications, incident escalations, and retest handoffs across sessions must be captured as **real logged messages** (e.g., timestamped markdown/JSON files in `agents/messages/` or exported session logs). Simulated or post-hoc reconstructed dialogues are strictly prohibited.
- **Standard Handoff Payload**: Every handoff message between roles must include:
  1. `Timestamp` and `Session ID`
  2. `From Role` -> `To Role`
  3. `Artifact Paths / Commit Hash` being handed off
  4. `Scope of Request / Acceptance Checks`
  5. `Known Limitations or Open Questions`
- **Conflict Prevention**: Only the owning role (or Fixer operating under an active, logged Detector incident ticket) may modify a given file at any time.

### 4.3 Preserved Real Prompts, Evidence & Zero-Fabrication Policy
- **Preserved Real Prompts**: Every substantive user/team prompt driving project work must be saved verbatim in `prompts/` using sequential numbered filenames (e.g., `prompts/prompt_01_revise_prd.md`, `prompts/prompt_02_...md`).
- **Preserved Build & QA Evidence**: Actual LuaLaTeX/Biber logs, Python script outputs, PDF page-count checks, and incident records must be preserved honestly.
- **Zero Fabrication Rule (Non-Negotiable)**:
  - Never invent lecturer requirements, document filenames, or page numbers from files that were not actually read.
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
- **Exact Page Count Gate**: `pdfinfo` / LuaLaTeX log confirms **strictly 25 pages** (`pages == 25`).
- **Clean Deterministic Compilation**: `lualatex -> biber -> lualatex -> lualatex` completes with exit code `0`, zero LaTeX errors, zero Biber errors, zero `??` unresolved cross-references, and zero undefined citation keys.
- **Visual & Typographic Inspection**: Rendered PDF pages are visually inspected (converted to PNG or viewed directly) for clipped tables, overlapping TikZ labels, broken margins, widow/orphan headings, header/footer consistency, and readable text contrast. If visual inspection cannot be executed in a given environment, that limitation must be logged explicitly.
- **IEEE Citation & Standard Verification**: All citations render in consistent IEEE numerical style (`[1]`, `[2]`, ...) with verified sources and verified standard editions.
- **Python Figure Reproducibility**: Running the documented regeneration command in a clean environment reproduces all Python figures identically from committed scripts and data, with explicit provenance labels on every chart.

### 5.3 Detector vs. Fixer Workflow & Mandatory 5-Part Incident Records
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

### 7.2 Source Verification & Proposed Reference Count
- **Proposed Reference Count**: `15–20` verified authoritative references (**Proposed Target — Pending Team Approval**; not a confirmed lecturer minimum unless verified in the official Assignment 02 brief).
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
- **Readability First**: Comfortable body font size (`10pt`–`10.5pt`), clean line spacing (`1.12`–`1.15`), balanced A4 margins (`20mm`–`25mm`), and zero cramped tables or microscopic figure labels.
- **Accessible Contrast**: Body text, headings, table headers, callout backgrounds, and Python/TikZ chart palettes must preserve strong legibility and accessible color contrast (targeting WCAG AA contrast `>= 4.5:1` for normal text and `>= 3:1` for large text/graphical elements), plus grayscale/print legibility.
- **LuaLaTeX Native Fonts**: Loaded via `fontspec` using fonts verified to exist in the target TeX/Windows environment (with deterministic fallbacks so builds never fail across Maria's and Basmala's machines).

### 8.2 Proposed Visual System (Pending Maria & Basmala's Approval)
- **Proposed Palette**: Deep Navy (`#0F2942`) primary headings/headers, Fuel Amber (`#D95D16`) or EV Emerald (`#0E7C66`) accents (highlighting dual fueling + EV charging identity), Charcoal (`#1E293B`) body text, and Soft Neutral Gray (`#F4F6F9`) callout/stripe tint.
- **Proposed Typography**: Clean sans-serif headings (`TeX Gyre Heros` / `Inter` / `Latin Modern Sans`), readable body (`Source Sans 3` / `TeX Gyre Pagella` / `Latin Modern`), and monospace (`Fira Code` / `TeX Gyre Cursor`) for technical identifiers and endpoints.
- **Proposed Class Macros & Environments**:
  - Metadata macros: `\projecttitle`, `\reportsubtitle`, `\assignmentcode`, `\teamname`, `\teammembers`, `\docversion`, `\docdate`.
  - Cover macro: `\makepdrcover` (vector TikZ cover layout, pending visual sign-off).
  - Running headers/footers via `fancyhdr` + `lastpage` (`Page X of 25`).
  - Styled callout boxes (`tcolorbox`), standardized `booktabs`/`tabularx` requirement tables, and consistent TikZ styles shared across all figures.

---

## 9. Numerical Targets & Candidate Technologies (Provenance & Maturity)

### 9.1 Conceptual Design vs. Implemented / Tested Distinction
To uphold zero fabrication and complete academic transparency, the report must explicitly distinguish two maturity states everywhere:
- **Conceptual Design**: All Fuel&Go runtime software/hardware components (mobile app, backend microservices, payment tokenization pipeline, forecourt gateway, EV CPMS adapter, cloud database, and runtime SLA targets). These are **designed and analyzed**, not built or field-tested in Assignment 02.
- **Implemented / Tested**: Artifacts actually built and executed during Assignment 02 — specifically the custom LuaLaTeX `.cls` class, LaTeX/Biber compilation pipeline, Python chart generation scripts, automated PDF page-count/log verification scripts, and real multi-agent workflows/QA audits.

### 9.2 Proposed Numerical Targets (Conceptual Fuel&Go System)
All numerical values below are **Proposed Conceptual Targets** awaiting Maria and Basmala's approval and Research validation — they are **not** measured field benchmarks.

| ID | Metric | Proposed Target | Rationale / Source | Conceptual Verification Method | Approval Status | Design Maturity |
| --- | --- | --- | --- | --- | --- | --- |
| **NFR-01a** | Station & Charger Discovery Latency (P95) | `<= 500 ms` | Interactive mobile map UX responsiveness baseline *(Source to be verified by Research, e.g., Nielsen Norman Group response-time guidelines)* | Analytical latency budget (conceptual) / future API load test | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-01b** | Pump / EV Charger Authorization Round-Trip (P95) | `<= 3.0 s` | End-to-end payment pre-auth + station/CPMS handshake budget *(Proposed Engineering Baseline — Source Needed)* | Sequence-diagram timing breakdown & simulation (conceptual) / future HIL test | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-02** | Live Telemetry Refresh Cadence | Fueling: `1–2 s`; EV Charging: `5–15 s` | Fueling finishes in ~2–5 min (requires fast feedback); EV charging lasts ~20–60+ min (lower polling/WebSocket cadence saves bandwidth/battery) *(Proposed Engineering Baseline)* | Protocol payload calculation (conceptual) / future simulator test | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-03** | Core Session Service Availability | `>= 99.9%` (or `99.95%` — to be selected) | Balances retail mobility uptime with realistic preliminary architecture complexity *(Proposed Baseline — Source/Cost Trade-Off Needed)* | Redundancy & failure-mode analysis (FMEA / conceptual) | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-04** | Peak Concurrent Active Sessions | `>= 5,000` (regional launch baseline; scalable to `10,000+`) | Sized for regional multi-station rush-hour concurrency *(Assumption — to be parameterized in Python sizing calculation)* | Analytical capacity calculation in reproducible Python script | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-05** | Payment & Transport Security | `0` raw PANs stored; TLS 1.3; AES-256 at rest | Aligned with PCI DSS tokenization & OWASP cryptographic guidance *(Exact standard versions to be verified)* | Architecture & STRIDE threat-model review + Red-Team audit | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-06** | Physical Safety Interlock Independence | `100%` local hardware enforcement | Mobile/cloud layers must never bypass certified fuel-dispenser or EVSE emergency shutoffs *(Safety Principle — standard to be verified)* | Safety boundary diagram review & Red-Team fault-injection analysis | *Proposed — Pending Team Approval* | Conceptual Design |
| **NFR-07** | Mobile Flow Simplicity & Accessibility | `<= 4–5` taps to start session; WCAG AA contrast | Reduces forecourt distraction and ensures accessible UI *(W3C WCAG version to be verified)* | Wireframe walkthrough & contrast ratio check | *Proposed — Pending Team Approval* | Conceptual Design |

### 9.3 Candidate Technologies (Conceptual System vs. Implemented Report Toolchain)

| Layer / Domain | Candidate Technology | Rationale / Source | Verification Method | Approval Status | Design Maturity |
| --- | --- | --- | --- | --- | --- |
| **Mobile App (Fuel&Go)** | Flutter or React Native (cross-platform iOS/Android) | Single codebase for iOS/Android with native QR/NFC/location support *(Trade-off matrix to be cited)* | Comparative trade-off analysis in Sec. 4 | *Proposed — Pending Team Approval* | Conceptual Design |
| **API & Backend Services** | Modular REST + WebSocket APIs (e.g., Node.js/TypeScript, Go, or Python/FastAPI) behind API Gateway | Clear domain separation between Station Discovery, Session Orchestrator, Payment, and Adapters | Interface contract & state-machine review | *Proposed — Pending Team Approval* | Conceptual Design |
| **Data Storage** | PostgreSQL + PostGIS (transactional ledger & geospatial queries) + Redis (live pump/charger status cache) | ACID guarantees for payment/session ledger + low-latency geospatial & status lookups | Conceptual ERD & query-path analysis | *Proposed — Pending Team Approval* | Conceptual Design |
| **Messaging / Telemetry** | Event broker (e.g., RabbitMQ or Kafka) + WebSockets/SSE to client | Decouples high-frequency fueling/EV telemetry from billing settlement | Architecture & fault-recovery analysis | *Proposed — Pending Team Approval* | Conceptual Design |
| **Station & EV Integration** | Dedicated Adapter Layer: Forecourt Gateway (IFSF / vendor POS API) + EV CPMS Adapter (OCPP / ISO 15118) | Isolates vendor protocol heterogeneity and enforces safety boundaries *(Protocol versions to be verified)* | Protocol mapping & Red-Team review | *Proposed — Pending Team Approval* | Conceptual Design |
| **Payment Processing** | Tokenized PSP (e.g., Stripe / Adyen / local PCI-compliant gateway) | Eliminates raw cardholder data from Fuel&Go backend, reducing PCI DSS scope | Threat model & tokenization flow audit | *Proposed — Pending Team Approval* | Conceptual Design |
| **Report Typesetting** | LuaLaTeX + Biber (`biblatex`, IEEE) + custom `nextmind-pdr.cls` | Deterministic Unicode/font handling, vector layout, automated IEEE citations | Executed clean build + exact 25-page check | **Confirmed Team Decision** | **Implemented / Tested (in EX02)** |
| **Analytical Plotting** | Python 3 + `matplotlib` / `numpy` / `pandas` (pinned in `requirements.txt`) | Reproducible, script-driven vector figures with auditable data provenance | Executed script regeneration + visual inspection | **Confirmed Team Decision** | **Implemented / Tested (in EX02)** |

---

## 10. Deliverables & Repository Governance Rules

### 10.1 Complete Assignment 02 Deliverables Checklist
| Deliverable | Expected Location / Channel | Maturity Type | Tracking Status |
| --- | --- | --- | --- |
| Authoritative `PRD.md` (reviewed & approved by Maria & Basmala) | `PRD.md` (with original backup in `backups/PRD.original.md`) | Governance Doc | Draft — Pending Review |
| Compiled 25-Page English PDF Report | `main.pdf` (or agreed release path, strictly 25 pages) | Implemented / Tested | Not Started |
| Full LaTeX Source & Custom Class | `main.tex`, `nextmind-pdr.cls`, `sections/*.tex`, `bib/references.bib`, `figures/*.tex` | Implemented / Tested | Not Started |
| Reproducible Python Graph Suite | `scripts/plots/*.py`, `data/*`, `requirements.txt`, reproduction instructions | Implemented / Tested | Not Started |
| 5 Role-Specific Agent Skill Files | `agents/{master,research,design,detector,fixer}/SKILL.md` | Governance / Process | Not Started |
| Preserved Real Prompts | `prompts/prompt_01_revise_prd.md`, subsequent real prompts | Evidence Artifact | In Progress (`01` saved) |
| Real Cross-Session Agent Messages & Handoffs | `agents/messages/*` | Evidence Artifact | Not Started |
| Detector/Fixer 5-Part Incident Records & Red-Team Audit | `qa/incidents/*`, `qa/redteam/*`, `qa/reports/*` | QA Evidence | Not Started |
| **Separate Moodle Submission Form** | **Course Moodle Portal (External to GitHub)** | Submission Gate | **Tracked Separately — Pending** |

### 10.2 Mandatory Repository & Collaboration Rules
1. **Git Configuration**: Repository initialized in project root (`NextMind-ex02`), default branch strictly `main`, connected to `https://github.com/jamalbasmala907-ship-it/NextMind_02.git`.
2. **Keep Nested Utility Repositories Separate**: Do **not** embed or nest third-party or utility Git repositories (`.git` directories or vendored helper repos) inside `NextMind-ex02`. Any external utility tools must remain outside this repository to keep commit history, licensing, and project boundaries clean.
3. **Permissions & Licensing Check for Provided Materials**: Before committing any lecturer-provided template, dataset, logo, image, or third-party asset into GitHub (especially if public), Maria and Basmala must verify distribution permissions and copyright/course rules. Restricted course materials must not be redistributed without explicit permission.
4. **Instructor Access**: Repository visibility and/or collaborator permissions must be verified so the course lecturer and graders have required access by the submission deadline (`Q-07`).
5. **Genuine Contributions from Both Partners**: Both **Maria Mnasra** and **Basmala Jamal** must make genuine, substantive, attributable contributions (reflected in Git commit authorship, section/role responsibilities, reviews, and sign-offs).
6. **Separate Moodle Form Tracking**: Pushing to GitHub does **not** complete course submission. The **Moodle submission form** (required fields, partner names, links, PDF upload, declarations, and submission timestamp) must be tracked as a separate mandatory checklist item and verified before the deadline (`Q-08`).
7. **Clean Build Hygiene**: Once LaTeX compilation begins, exclude transient LaTeX auxiliary files (`*.aux`, `*.bbl`, `*.bcf`, `*.blg`, `*.out`, `*.run.xml`, `*.toc`, `*.lof`, `*.lot`) via `.gitignore`, while preserving required build/QA logs intentionally placed in `qa/`.

---

## 11. Governance & Provenance Separation Matrix

To prevent conflating course rules with team preferences or unverified assumptions, all project directives are strictly partitioned into five categories:

### 11.1 Explicit Lecturer Requirements (Source File & Page Number Required)
> **File-Reading Limitation Note**: As of v1.1.0-draft, **no official Assignment 02 lecturer instruction PDF or document is present inside** `C:\Users\jamal\OneDrive - Bar-Ilan University - Students\Desktop\NextMind-ex02`. In strict adherence to the **Zero-Fabrication Policy**, no filenames or page numbers have been guessed or invented. Maria and Basmala must verify each row below against the official lecturer brief and fill in the exact source filename and page number(s).

| Req. ID | Requirement Description | Source Filename | Page Number(s) | Verification Status |
| --- | --- | --- | :---: | --- |
| **LR-01** | Assignment 02 report exact length: **strictly 25 pages** (verify whether cover/ToC/refs/appendices are included) | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |
| **LR-02** | Report language: English PDF compiled with LuaLaTeX + Biber + custom `.cls` | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |
| **LR-03** | Required document framing/title (verify whether "Preliminary Design Report" is mandated) | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |
| **LR-04** | Multi-agent workflow requirements (5 roles: Master, Research, Design, Detector, Fixer; `SKILL.md` files; real cross-session messages; preserved real prompts; 5-part incident records; red-team; zero fabrication) | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |
| **LR-05** | Reproducible Python graphs + TikZ/vector diagrams + IEEE citation style | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |
| **LR-06** | Repository access for instructors, genuine contributions from both partners, and separate Moodle submission form | `[Pending — lecturer brief not in project folder]` | `[Pending]` | Needs Source Verification |

### 11.2 Confirmed Team Decisions (Team NextMind)
- **TD-01**: Team name is **NextMind**; partners are **Maria Mnasra** and **Basmala Jamal**.
- **TD-02**: Project domain is **Fuel&Go**, with **core capabilities focused on fueling and EV charging**.
- **TD-03**: Target and acceptance criterion is **strictly 25 pages** (exact).
- **TD-04**: Technical stack for report production is **LuaLaTeX + Biber + custom `.cls`** with **IEEE citation style only** (APA removed).
- **TD-05**: Analytical charts will be generated via **reproducible Python scripts** with explicit 4-category data provenance labeling, complemented by **TikZ/vector diagrams**.
- **TD-06**: Multi-agent governance uses the **5 roles** (Master, Research, Design, Detector, Fixer), strict Detector/Fixer separation, **5-part incident records**, red-teaming, real cross-session messages, preserved real prompts, and **zero fabrication**.
- **TD-07**: GitHub remote is `https://github.com/jamalbasmala907-ship-it/NextMind_02.git` on branch `main`, keeping nested utility repos separate and tracking the Moodle submission form independently.

### 11.3 Proposed Choices (Pending Maria Mnasra & Basmala Jamal's Approval)
- **PC-01**: Section-by-section 25-page budget in Section 3.3.
- **PC-02**: Visual design proposal in Section 8.2 (palette, font pairing, cover page style, callout styling, working class filename `nextmind-pdr.cls`).
- **PC-03**: Proposed reference count (`15–20` verified IEEE entries) in Section 7.2.
- **PC-04**: Proposed conceptual numerical targets (`NFR-01a` through `NFR-07`) in Section 9.2.
- **PC-05**: Candidate Fuel&Go runtime technology stack in Section 9.3.
- **PC-06**: Proposed Extensions / Future Scope list (`EXT-01` through `EXT-05` — convenience store, loyalty, fleet, VAT invoicing, operator dashboard) kept out of core scope.

### 11.4 Assumptions
- **A-01**: Fuel stations expose a certified local forecourt controller and EV charging networks expose a standard CPMS interface (e.g., OCPP-capable) reachable via secure adapters while keeping physical safety interlocks strictly local.
- **A-02**: Both partners' build environments can install/run TeX Live or MiKTeX (`lualatex` + `biber`) and Python 3 with the pinned packages in `requirements.txt` (without modifying unauthorized global policies).
- **A-03**: Until `Q-01` is resolved, the working page budget assumes cover, front matter, references, and appendices are counted inside the 25-page PDF total.

### 11.5 Unresolved Questions Requiring Decision by Maria Mnasra & Basmala Jamal
| ID | Open Question | Impact if Unresolved | Owner(s) |
| --- | --- | --- | --- |
| **Q-01** | Do **cover page, table of contents/front matter, references, and appendices** count inside the strict 25 pages, or are they excluded? | Directly changes body page budget by ~3–4 pages. | Maria & Basmala (verify lecturer brief) |
| **Q-02** | Is **"Preliminary Design Report"** the exact intended framing/title for Assignment 02? | Determines cover title, headers, abstract, and tone. | Maria & Basmala (verify lecturer brief) |
| **Q-03** | Beyond course lecturer/graders, which optional secondary **report readers** (e.g., engineering review board, investors) should the report address, if any? | Shapes Executive Summary and level of business vs. engineering framing. | Maria & Basmala |
| **Q-04** | Which **visual design** (color palette, font pairing, cover layout, class filename) do Maria and Basmala approve? | Blocks finalizing `nextmind-pdr.cls`. | Maria & Basmala |
| **Q-05** | Should all five **Proposed Extensions** (`EXT-01..05`) remain strictly Future Scope, or should any single extension be promoted to Core? | Impacts requirements, diagrams, and 25-page budget. | Maria & Basmala |
| **Q-06** | Where is the official **Assignment 02 lecturer brief** (filename & page numbers) so Section 11.1 (`LR-01..06`) can be verified and completed without fabrication? | Needed to lock down explicit lecturer requirements and permissions check. | Maria & Basmala |
| **Q-07** | Should the GitHub repository be **public or private with instructor collaborators**, and what permissions apply to any lecturer-provided materials? | Required for instructor access and academic/copyright compliance. | Maria & Basmala |
| **Q-08** | What are the exact fields, files, and deadline for the **separate Moodle submission form**? | Required to build the final external submission checklist. | Maria & Basmala |
| **Q-09** | What is the exact **division of ownership** between **Maria Mnasra** and **Basmala Jamal** across sections, Python plots, LaTeX class, and QA/red-team reviews? | Ensures balanced, genuine, attributable partner contributions. | Maria & Basmala |
| **Q-10** | Do Maria and Basmala approve the proposed **conceptual numerical targets** (Section 9.2), **candidate technologies** (Section 9.3), and **proposed reference count** (`15–20` IEEE entries)? | Required before Research & Design agents begin execution. | Maria & Basmala |
