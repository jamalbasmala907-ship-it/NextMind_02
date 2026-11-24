# Project Execution Plan (PLAN): Fuel&Go — Assignment 02 Report

| Field | Value |
| --- | --- |
| **Project Name** | Fuel&Go (Core: Smart Fueling & EV Charging Platform) |
| **Deliverable** | Assignment 02 Engineering Report (Preliminary Design Report — Working Framing) |
| **Team** | NextMind |
| **Partners** | Maria Mnasra, Basmala Jamal |
| **PLAN Owner** | Maria Mnasra (Planning & Task Governance Owner; Joint Major-Decision Approval with Basmala Jamal) |
| **Specification Reference** | [PRD](<PRD (1).md>) (v1.2.0-draft — File/version verified; content approval pending) |
| **Target Document Length** | Strictly 25 English Pages (Exact; boundary subject to `Q-01` resolution) |
| **Document Status** | Working Baseline — Active Execution Plan |
| **Version** | 1.1.0 |

---

## 1. Report Objective & Scope Linkage

### 1.1 Objective
This Project Execution Plan (`PLAN.md`) governs the end-to-end execution, multi-agent collaboration, verification, and submission of the **Assignment 02 Engineering Report** for team **NextMind**. The plan is anchored directly to the working specification defined in [PRD](<PRD (1).md>) (v1.2.0-draft).

### 1.2 Scope Boundaries
- **Core Product Scope (In-Scope)**: Architecture and conceptual preliminary design of the core Fuel&Go dual-energy platform:
  - `FR-01`: User Account, Authentication & Vehicle Energy Profile (ICE & EV).
  - `FR-02`: Unified Station & Charger Discovery (live fuel pricing, EV tariffs, connector types, availability).
  - `FR-03`: Pump & EV Charger Selection and Remote Session Authorization (geofencing, pre-auth holds, forecourt/CPMS commands).
  - `FR-04`: Real-Time Fueling & EV Charging Telemetry (liters/kWh, kW power, SoC, elapsed time, running cost).
  - `FR-05`: Contactless Payment Settlement & Basic Digital Receipt (unused hold release, itemized receipts).
  - `FR-06`: Session Fault Handling & Basic User Support (disconnects, timeouts, payment decline, hardware cutoff).
- **Proposed Extensions / Future Scope (Explicitly Out of Core Scope)**:
  - `EXT-01` (C-store pre-ordering), `EXT-02` (loyalty promotions), `EXT-03` (fleet management portal), `EXT-04` (consolidated corporate VAT invoicing), and `EXT-05` (station operator dashboard).
  - *Rule*: These items remain classified as `Unverified — pending source review` against original Fuel&Go slides/prior PRD (`Q-05`). They shall not consume core requirement chapters, architecture depth, or page budget unless verified and approved by Maria and Basmala.

---

## 2. Current Project State

| Domain / Artifact | Current Status | State Classification | Evidence / Verification Location |
| --- | --- | --- | --- |
| **PRD Specification** | `v1.2.0-draft` anchored at root; partner review and approval pending | **File/version verified; content approval pending** | [PRD](<PRD (1).md>) at project root |
| **Team Setup Prompts** | `001-team-setup.txt`, `002-setup-review.txt`, `003-prepare-plan.txt` saved verbatim | **Verified Completed** | `prompts/` |
| **Agent Skill Profiles** | 5 role-specific `SKILL.md` files created and verified non-empty | **Verified Completed** | `agents/{master,research,design,detector,fixer}/SKILL.md` |
| **Multi-Agent Infrastructure** | Hub running (port 9877), junctions active, 5 real sessions active | **Verified Completed** | Local hub process (PID 12872), background task logs |
| **Mesh Health & Inter-Session Comms** | Genuine `ping-all` round completed; all 4 workers replied `PONG` | **Verified Completed** | Master session `ping-all` output log (all 4 peers answered) |
| **Assignment Source Review** | Initial scan completed; PDF guidelines and textbook available | **Verified Completed (with noted reading limits)** | `docs/REQUIREMENTS_CHECKLIST.md` |
| **Report Outline & Budget Sign-Off** | Rebalanceable 25-page budget drafted; boundary open (`Q-01`) | **Planned — Verification Pending** | Pending team decision on `Q-01` |
| **Visual Design System** | Palette and font proposals formulated; class unfinalized (`Q-04`) | **Planned — Pending Approval** | Pending visual sample approval by Maria & Basmala |
| **Content Drafting & Research** | IEEE bibliography, literature matrix, and LaTeX chapter drafting | **Planned — Verification Pending** | `bib/`, `evidence/`, `sections/` |
| **Python Plot Pipeline** | Reproducible plotting scripts and data provenance tracking | **Planned — Verification Pending** | `scripts/plots/`, `data/` |
| **Independent QA & Incidents** | Red-team audits, defect register, 5-part incident records | **Planned — Verification Pending** | `qa/` |
| **Git Setup & Collaboration Checkpoints** | Scheduled early; target identified; operations not yet executed | **Planned — Verification Pending** | Target: `https://github.com/jamalbasmala907-ship-it/NextMind_02` |

---

## 3. Human Responsibilities & Approval Authority

Human partners hold ultimate project ownership, governance authority, and decision-making responsibility. Multi-agent tools assist within strict operational boundaries and never replace human sign-off.

```
                           +------------------------------------------+
                           |  NextMind Partners (Joint Governance)    |
                           |  Maria Mnasra & Basmala Jamal            |
                           |  - Major Architectural Decisions         |
                           |  - Visual Design & Scope Approval        |
                           |  - Final 25-Page Report Sign-Off         |
                           |  - Independent Moodle Submissions        |
                           +--------------------+---------------------+
                                                |
                   +----------------------------+----------------------------+
                   |                                                         |
+------------------v-------------------+                 +-------------------v------------------+
| Basmala Jamal (Requirements Owner)   |                 | Maria Mnasra (Execution Owner)       |
| - Primary Owner of PRD.md            |                 | - Primary Owner of PLAN.md & TODO.md |
| - Scope Boundary Governance          |                 | - Work Phases, Gating & Milestones   |
| - Requirements Traceability & NFRs   |                 | - Task Board & Progress Tracking     |
+--------------------------------------+                 +--------------------------------------+
```

### Detailed Partner Allocations
- **Basmala Jamal**:
  - Authoritative owner of `PRD.md` (requirements definitions, scope boundaries, acceptance criteria, user personas).
  - Approves requirements changes, scope promotions/demotions, and conceptual feature baselines.
  - Jointly reviews major architectural trade-offs, visual design, and the final deliverable.
  - Submits individual Moodle submission form.
- **Maria Mnasra**:
  - Authoritative owner of `PLAN.md` and `TODO.md` (execution workflow, milestones, task dependencies, delivery schedule).
  - Manages task board gating, handoff pacing, and progress tracking across phases.
  - Jointly reviews major architectural trade-offs, visual design, and the final deliverable.
  - Submits individual Moodle submission form.
- **Joint Responsibilities (Maria Mnasra & Basmala Jamal)**:
  - Jointly own `README.md` (team attribution, reproduction guide, evidence summary).
  - Jointly approve open decisions (`Q-01` through `Q-10`).
  - Jointly inspect and sign off on the final compiled 25-page PDF report prior to any external publication or submission.

---

## 4. Multi-Agent Responsibilities & Single-Writer Handoff Protocol

### 4.1 The Five Agent Roles
The 5-role structure is a **Team NextMind Workflow Choice** designed to ensure separation of concerns, high technical rigor, and zero fabrication:

1. **Master (`agents/master/SKILL.md`)**:
   - Coordinates workflow execution, dispatches tasks via `agymesh`, and enforces single-writer locks.
   - Monitors agent progress against `TODO.md` and escalates blockers to Maria and Basmala.
   - *Strict Directive*: Delegate, never self-generate content; never bypass unresolved Detector defects; never replace human partner ownership.
2. **Research (`agents/research/SKILL.md`)**:
   - Conducts academic literature surveys, verified standard analysis (IFSF, OCPP, ISO 15118, PCI DSS), and market research (TAM/SAM/SOM).
   - Owns `bib/references.bib` (strict IEEE style, verified DOIs/URLs, zero invented citations).
   - Drafts technical section content into staged text files during its active write lock.
3. **Design (`agents/design/SKILL.md`)**:
   - Owns LaTeX engineering, custom class implementation (`nextmind-pdr.cls`), document layout, and pagination budgeting.
   - Authors clean TikZ vector architectural and sequence diagrams in `figures/`.
   - Develops reproducible Python figure scripts (`scripts/plots/`) exporting publication-grade vector graphics.
4. **Detector (`agents/detector/SKILL.md`)**:
   - Acts as independent Quality Assurance Lead (Red Team), auditing rendered deliverables.
   - Inspects PDF layout, typography, page budget, citation consistency, and data provenance tags.
   - *Strict Independence*: Read-only on production source/code; logs defects into `qa/incidents/INC-xxx.md`; conducts independent retesting after fixes.
5. **Fixer (`agents/fixer/SKILL.md`)**:
   - Performs root-cause remediation for defects assigned by Master from Detector logs.
   - Applies minimal targeted edits to `.tex`, `.cls`, `.bib`, or `.py` files.
   - Formulates mandatory 5-part incident records (`qa/incidents/INC-xxx.md`) and hands them back to Detector for retesting.

### 4.2 Single-Writer Handoff Flow
To prevent race conditions and concurrent write conflicts, files are edited under strict single-writer stage locks:

```
[Master Dispatch]
       |
       v
[Research Lock] ----(Draft text & IEEE .bib)----> [Design Lock]
                                                        |
                                            (Integrate LaTeX, TikZ, Plots)
                                                        |
                                                        v
                                                 [Detector Audit] <-----+
                                                  (Read-Only QA)        |
                                                        |               |
                                             Defects?   |               |
                                            +-----------+               |
                                            | PASS      | FAIL          |
                                            v           v               |
                                      [Sign-Off]   [Fixer Lock] --------+
                                      (Partners)  (5-Part INC) (Retest)
```

---

## 5. Work Phases, Dependencies, Expected Outputs & Completion Criteria

### 5.1 Parallel Work Decoupling
To maintain momentum and avoid artificial blocking, independent preparatory work streams are explicitly permitted to proceed while unrelated open decisions remain under partner deliberation:
- **Source Research & Citation Cataloging**: Academic literature retrieval, empirical data collection, and candidate standard version verification may proceed independently of visual design choices or title framing (`Q-02`, `Q-04`).
- **Toolchain Validation**: Local LuaLaTeX, Biber, and Python environment checks may proceed independently of page budget boundary resolution (`Q-01`).
- **Visual Sample Prototyping**: Generating preliminary 1-page visual snippets and font rendering tests may proceed independently of product extension scope decisions (`Q-05`).

```
+----------------------------------------------------------------------------------------------------+
| Phase 1: Source Verification & Scope Alignment                                                     |
| Inputs: materials/, PRD (1).md | Outputs: Scope clarification note, updated Q-01..10 log          |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 2: Report Outline & Indicative 25-Page Budget Approval                                       |
| Inputs: PRD Section 3.3 | Outputs: Approved section outline & page targets (Option A / B)          |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 3: Research, Standards & Data Verification                                                   |
| Inputs: Domain protocols, academic venues | Outputs: bib/references.bib, data/sources/             |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 4: Content Drafting & Citation Assembly                                                      |
| Inputs: Verified sources, PRD FRs/NFRs | Outputs: Staged chapter drafts (Sec. 1-9)                 |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 5: Visual Sample Approval & LaTeX / Figure Integration                                       |
| Sequence: 1. Visual sample -> 2. Partner approval -> 3. Finalize cls/figures/text                 |
| Inputs: Draft text, visual sample | Outputs: nextmind-pdr.cls, main.tex, TikZ, Python plots        |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 6: Compilation, Independent QA Review, Incident Remediation & Retesting                      |
| Inputs: Full LaTeX project | Outputs: Clean main.pdf (exact 25 p), qa/incidents/, Red-Team report  |
+-------------------------------------------------+--------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| Phase 7: Repository Documentation & Final Submission Checks                                        |
| Inputs: Verified deliverable package | Outputs: README.md, clean Git repo, partner Moodle checklists|
+----------------------------------------------------------------------------------------------------+
```

### Detailed Phase Specifications

#### Phase 1: Source Verification & Scope Alignment
- **Objective**: Review available lecturer materials, document unreadable sources, and confirm core fueling/EV scope boundaries.
- **Dependencies**: Access to `materials/assignment02/` and `materials/fuel-and-go/`.
- **Expected Outputs**: Verified source checklist, explicit limitations note, resolved or documented open questions (`Q-01` to `Q-10`).
- **Completion Criteria**: Maria and Basmala confirm core scope; disputed extensions (`EXT-01..05`) remain strictly quarantined.

#### Phase 2: Report Outline & Indicative 25-Page Budget Approval
- **Objective**: Finalize section outline and indicative page budgets matching the strict 25 English pages criterion. Schedule early Git repository setup.
- **Dependencies**: Phase 1 completion; team decision on `Q-01` (Option A: 25 total PDF pages vs. Option B: 25 body pages + front/back matter).
- **Expected Outputs**: Approved section budget table incorporated into execution milestones; early Git setup scheduled with documented checkpoints.
- **Completion Criteria**: Partner sign-off on section-by-section target allocations without artificial 1-page compression of references.

#### Phase 3: Research, Standards & Data Verification
- **Objective**: Retrieve, verify, and catalog empirical sources, protocol editions, and academic literature.
- **Dependencies**: Phase 2 approved outline. (May proceed in parallel with visual prototyping).
- **Expected Outputs**: `bib/references.bib` with verified IEEE entries; raw data files in `data/` with `data/README.md` provenance tags; verified standard versions (PCI DSS, OCPP, ISO 15118, IFSF, WCAG).
- **Completion Criteria**: Zero unverified DOIs or placeholder citations; 100% of candidate standards verified by Research.

#### Phase 4: Content Drafting & Citation Assembly
- **Objective**: Author rigorous technical prose for Sections 1 through 9.
- **Dependencies**: Phase 3 verified sources; single-writer lock held by Research.
- **Expected Outputs**: Modular text files (`sections/sec01_intro.tex` through `sections/sec09_conclusions.tex`) incorporating formal IEEE citations.
- **Completion Criteria**: All functional requirements (`FR-01..06`) and non-functional requirements (`NFR-*`) fully covered with technical rationale.

#### Phase 5: Visual Sample Approval & LaTeX / Figure Integration
- **Objective**: Build custom document class, author vector diagrams, generate reproducible plots, and integrate text under a strict 3-step sequence.
- **Strict Sequencing**:
  1. *Visual Sample Creation*: Design creates an initial 1-page visual sample render showcasing proposed typography, colors, headers/footers, and callout styles.
  2. *Partner Review & Approval*: Maria and Basmala inspect the visual sample render and explicitly approve or adjust the visual design system (`Q-04`).
  3. *Styling Finalization & Integration*: Upon partner sign-off, Design finalizes `nextmind-pdr.cls`, authors TikZ diagrams, runs Python plotting scripts, and integrates modular chapter text into `main.tex`.
- **Dependencies**: Content drafts from Phase 4; partner approval of visual sample (`Q-04`); single-writer lock transferred to Design.
- **Expected Outputs**:
  - 1-page visual sample render reviewed and approved by Maria and Basmala.
  - Finalized `nextmind-pdr.cls` encapsulating approved styling, fonts, headers/footers, and callouts.
  - TikZ architectural and state-machine diagrams in `figures/`.
  - Reproducible Python plotting scripts in `scripts/plots/` producing vector graphics.
  - Assembled `main.tex` orchestrating all components.
- **Completion Criteria**: Partner sign-off on visual sample; successful test compilation of all modular chapters.

#### Phase 6: Compilation, Independent QA Review, Incident Remediation & Retesting
- **Objective**: Deterministic build execution, independent defect detection, root-cause fixing, and regression-free retesting.
- **Dependencies**: Assembled LaTeX project; Detector read-only audit lock.
- **Expected Outputs**:
  - Clean LuaLaTeX + Biber compilation (exit code 0, 0 errors, 0 undefined citations/references).
  - Exact 25 English pages confirmed by `pdfinfo` per `Q-01`.
  - Numbered incident files in `qa/incidents/INC-xxx.md` containing all 5 mandatory sections.
  - Retest records confirming `PASS` on all resolved defects.
  - Dual-track Red-Team audit report (`qa/redteam/redteam_audit.md`).
- **Completion Criteria**: 0 open defects; 100% incident retest pass rate; exact page count verified.

#### Phase 7: Repository Documentation & Final Submission Checks
- **Objective**: Package repository, document reproduction instructions, and prepare submission records.
- **Dependencies**: Phase 6 sign-off by Maria, Basmala, and Detector.
- **Expected Outputs**:
  - Comprehensive `README.md` (joint authorship, reproduction guide, figures/screenshots, agent evidence).
  - Clean `.gitignore` strictly excluding `agy-multi-agent-mesh/` and build artifacts.
  - Attributable Git history with meaningful commits from both partners.
  - Verified Moodle submission forms and required upload checks for Maria and Basmala.
- **Completion Criteria**: Both partners sign off on repository state, final report PDF, and personal Moodle submissions.

---

## 6. Reproducible Build & Python Graph Pipeline Verification

### 6.1 Deterministic LaTeX & Biber Toolchain
- **Engine**: LuaLaTeX with Biber backend (`biblatex`, IEEE numerical style).
- **Execution Pipeline**: `lualatex -> biber -> lualatex -> lualatex`.
- **Quality Gates**:
  1. Exit code `0` on all compilation steps.
  2. Zero unresolved cross-references (no `??` marks).
  3. Zero undefined bibliography keys.
  4. Exact 25 English pages verified via `pdfinfo` and LuaLaTeX build log.

### 6.2 Python Figure Pipeline & Data Provenance
- **Environment**: Python 3.12 with dependencies pinned in `requirements.txt` (e.g., `matplotlib`, `numpy`, `pandas`).
- **Execution Runner**: `scripts/generate_figures.py` (or individual modular scripts under `scripts/plots/`).
- **Export Format**: Vector PDF graphics (`.pdf`) saved to `figures/` for direct inclusion in LaTeX.
- **Mandatory 4-Category Data Provenance Tagging**:
  Every quantitative figure and table must carry an explicit provenance label:
  - `[Sourced Measurement]`: Verified empirical data with exact IEEE citation.
  - `[Calculation]`: Deterministic mathematical output with documented formula.
  - `[Assumption]`: Stated engineering baseline chosen by NextMind.
  - `[Illustrative / Simulated Data]`: Synthetic or simulated curve clearly labeled as non-empirical.
- **Verification Gate**: Running the documented regeneration command in a clean shell reproduces identical vector figures without manual intervention.

---

## 7. Evidence Integrity & Artifact Preservation

Team NextMind enforces strict academic transparency and a non-negotiable **Zero Fabrication Policy**:

1. **Preserved Real Prompts**:
   - Every substantive prompt issued by the team must be saved verbatim in `prompts/` using sequential filenames (`prompts/001-team-setup.txt`, `prompts/002-setup-review.txt`, `prompts/003-prepare-plan.txt`, etc.).
2. **Preserved Multi-Agent Evidence**:
   - Authentic cross-session communications must be captured as real logged artifacts (`agents/messages/`, hub journal, task logs). Simulated dialogues or mock logs are strictly prohibited.
3. **Mandatory 5-Part Incident Records**:
   - All defects logged by Detector and remediated by Fixer must contain:
     1. *What happened* (exact symptoms, affected files, line numbers, raw evidence).
     2. *Why it happened* (technical/process root cause).
     3. *Why earlier checks missed it* (gap analysis).
     4. *What changed* (exact code/text diff and preventive guardrail).
     5. *Retest result* (independent Detector verification method and `PASS`/`FAIL` outcome).
4. **Authenticity Guarantee**:
   - No fabricated citations, DOIs, authors, or benchmark data.
   - If a source or environment tool is unavailable, document the limitation honestly rather than guessing.

---

## 8. Git Collaboration Checkpoints & Repository Hygiene

### 8.1 Remote Repository & Early Setup Scheduling
- **Remote URL**: `https://github.com/jamalbasmala907-ship-it/NextMind_02.git`
- **Default Branch**: `main`
- **Early Scheduling**: Git repository initialization, `.gitignore` setup, and remote connection are scheduled early in the project lifecycle to enable continuous version control and establish meaningful collaboration checkpoints throughout drafting, layout, and review.
- **Operational Constraint**: **Do not execute Git operations now.** Git commands (`git init`, `git commit`, `git push`) will only be run when explicitly authorized by Maria and Basmala.

### 8.2 Strict Exclusion of Lecturer Utility Repository
- **Directory**: `agy-multi-agent-mesh/`
- **Isolation Rule**:
  - The local utility directory `agy-multi-agent-mesh/` remains untouched locally for multi-agent orchestration.
  - It is strictly excluded from Git tracking via `.gitignore`:
    ```gitignore
    # Lecturer utility mesh (local execution only)
    agy-multi-agent-mesh/
    .mesh/
    ```
  - Report compilation and Python plot generation must remain completely standalone and reproducible without committing `agy-multi-agent-mesh/`.

### 8.3 Genuine Two-Partner Git Attribution & Checkpoints
- Both **Maria Mnasra** and **Basmala Jamal** must have substantive, attributable Git commits reflecting their genuine contributions across project phases.
- Checkpoints will be logged at each stage-gate handoff:
  - *Checkpoint 1 (Early Setup)*: Baseline governance documents (`PRD.md`, `PLAN.md`, `prompts/`).
  - *Checkpoint 2 (Research Gate)*: Verified bibliography (`bib/references.bib`) and data provenance files.
  - *Checkpoint 3 (Design Gate)*: Approved `.cls` styling, TikZ figures, and plotting scripts.
  - *Checkpoint 4 (Drafting Gate)*: Modular chapter drafts committed with partner co-authorship.
  - *Checkpoint 5 (QA Gate)*: Defect logs and incident remediation records.
  - *Checkpoint 6 (Final Release)*: Complete repository sign-off and release tagging (Phase 7).

---

## 9. Open Decisions, Technical Risks & Mitigation Strategies

### 9.1 Open Decisions Register (Requiring Partner Resolution)

| ID | Decision / Open Question | Options / Alternatives | Impact if Unresolved | Responsible Owner(s) |
| --- | --- | --- | --- | --- |
| **Q-01** | **25-Page Boundary Interpretation** | **Option A**: 25 Total PDF Pages (including front/back matter).<br>**Option B**: 25 Body Pages (front matter, references, appendices are additional). | Governs section budget allocations and rebalancing targets. | Maria Mnasra & Basmala Jamal |
| **Q-02** | **Report Framing / Title Verification** | Working title: *"Preliminary Design Report"*. Verify if lecturer mandates an alternate course title. | Affects cover title, headers, and document tone. | Maria Mnasra & Basmala Jamal |
| **Q-03** | **Intended Report Audience** | Determine whether optional secondary readers (e.g., simulated engineering review panel, technical investors) are addressed beyond course grader/lecturer. | Shapes Executive Summary depth and level of business vs. technical framing. | Maria Mnasra & Basmala Jamal |
| **Q-04** | **Visual Design System Sign-Off** | Proposed Deep Navy / Fuel Amber / EV Emerald palette; font pairings (sans headings + serif body); custom cover. | Blocks finalizing `nextmind-pdr.cls`. | Maria Mnasra & Basmala Jamal |
| **Q-05** | **Disputed Scope Extras (`EXT-01..05`)** | C-store, loyalty, fleet, corporate invoicing, operator portal.<br>Verify against original Fuel&Go slides. | Prevents unbacked scope creep; determines roadmap inclusion. | Maria Mnasra & Basmala Jamal |
| **Q-06** | **Lecturer Instruction Provenance** | Identify exact lecturer instruction filenames and page numbers for requirements checklist. | Necessary for zero-fabrication traceability. | Maria Mnasra & Basmala Jamal |
| **Q-07** | **GitHub Access & Material Permissions** | Public vs. Private repo with instructor invite; verify copyright/distribution permissions for course materials. | Affects grading access and compliance. | Maria Mnasra & Basmala Jamal |
| **Q-08** | **Moodle Submission Requirements** | Identify specific portal upload formats, file naming, and deadline. | Critical for course grade completion. | Maria Mnasra & Basmala Jamal |
| **Q-09** | **Partner Work Breakdown** | Distribution of chapters, plotting scripts, and review roles between Maria and Basmala. | Ensures balanced attribution and accountability. | Maria Mnasra & Basmala Jamal |
| **Q-10** | **Numerical Target Rationales** | Provide justified rationale/sources for `NFR-01a..04` currently marked `TBD`. | Required before finalizing requirements table. | Maria & Basmala (with Research) |

### 9.2 Technical Risk Management

| Risk ID | Description | Severity | Likelihood | Mitigation Strategy |
| --- | --- | :---: | :---: | --- |
| **R-01** | **Page Count Drift**: Report compiles to 24 or 26 pages instead of strictly 25. | High | Medium | Enforce rebalanceable section budgets; use `nextmind-pdr.cls` layout hooks; Detector inspects PDF page count at every commit. |
| **R-02** | **Toolchain Divergence**: LuaLaTeX / Python compilation fails on one partner's machine. | High | Low | Pin exact package versions in `requirements.txt`; use standard TeX Live / MiKTeX packages; test clean builds early. |
| **R-03** | **Unintentional Scope Creep**: Future scope items (`EXT-01..05`) bleed into core architecture chapters. | Medium | Medium | Strict PRD scope quarantine; Detector red-team audit flags any unapproved extension prose. |
| **R-04** | **Permission Prompts Halting Automation**: Long wait timeouts on agent mesh commands due to interactive approvals. | Medium | Low | Preserve permission checks; human partners review and approve necessary scoped commands in interactive console sessions as needed without global bypasses. |
| **R-05** | **Citation Inconsistencies**: Mixed APA / IEEE styles or unverified references. | Medium | Low | Strict Biber IEEE configuration; automated check rejecting any manual non-numeric citation format. |

---

## 10. Separate Partner Moodle Submission Checklist

Submission to GitHub does **not** complete the course requirement. The course Moodle portal requires separate, independent submissions by each partner.

> **Important Distinction on Deliverables**:
> - **Final Report PDF (`main.pdf`)**: The compiled 25-page English engineering report produced from LaTeX.
> - **Moodle Submission-Form PDF**: The personal confirmation/receipt document generated by the course Moodle portal upon form submission.
> - **Verification Requirement**: Partners must verify exact Moodle portal upload requirements from course guidelines (confirming whether Moodle requires uploading the compiled 25-page report PDF, a portal-generated submission form, repository links, or specific declaration files) rather than assuming the report PDF itself must be directly uploaded to Moodle.

### Maria Mnasra — Submission Checklist
- [ ] Confirm finalized compiled 25-page report PDF (`main.pdf`) meets exact page-count criteria.
- [ ] Verify GitHub repository (`https://github.com/jamalbasmala907-ship-it/NextMind_02`) is accessible to course graders.
- [ ] Verify attributable Git commits under Maria Mnasra's identity are pushed to `main`.
- [ ] Verify exact Moodle upload requirements from course instructions (confirm whether Moodle requires the compiled report PDF, a portal-generated submission form, or declaration files).
- [ ] Upload required submission artifact(s) to personal Moodle portal slot per verified course instructions.
- [ ] Enter GitHub repository URL and partner details (Basmala Jamal) in designated Moodle fields.
- [ ] Download and archive personal timestamped Moodle submission-form confirmation PDF.

### Basmala Jamal — Submission Checklist
- [ ] Confirm finalized compiled 25-page report PDF (`main.pdf`) meets exact page-count criteria.
- [ ] Verify GitHub repository (`https://github.com/jamalbasmala907-ship-it/NextMind_02`) is accessible to course graders.
- [ ] Verify attributable Git commits under Basmala Jamal's identity are pushed to `main`.
- [ ] Verify exact Moodle upload requirements from course instructions (confirm whether Moodle requires the compiled report PDF, a portal-generated submission form, or declaration files).
- [ ] Upload required submission artifact(s) to personal Moodle portal slot per verified course instructions.
- [ ] Enter GitHub repository URL and partner details (Maria Mnasra) in designated Moodle fields.
- [ ] Download and archive personal timestamped Moodle submission-form confirmation PDF.

---
*Document author: Maria Mnasra (Plan Owner) & Team NextMind.*  
*Anchored specification: `PRD (1).md` (v1.2.0-draft — File/version verified; content approval pending).*
