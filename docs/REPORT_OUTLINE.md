# Proposed Report Outline & Visual Brief: Fuel&Go — Assignment 02

| Field | Value |
| --- | --- |
| **Project** | Fuel&Go — Unified Smart Fueling & EV Charging Platform |
| **Proposed Report Title** | *Fuel&Go: Preliminary Design Report for a Unified Smart Fueling and EV Charging Platform* *(Proposed Working Title — Pending `Q-02` Confirmation)* |
| **Team & Partners** | Team NextMind — Maria Mnasra (`PLAN.md` / `TODO.md` Owner) & Basmala Jamal (`PRD.md` Owner) |
| **Proposed Audience** | **Primary Decision Audience**: Executive Management & Product/Engineering Decision-Makers *(Proposed — Pending `Q-03`)*<br>**Academic Evaluator**: Course Lecturer & Graders / TAs *(Confirmed)* |
| **Proposed Core Scope** | Unified ICE Fueling & EV Charging Platform (`FR-01`–`FR-06`) *(Proposed — Subject to source verification & partner approval in `TASK-P1-01` / `Q-05`)* |
| **Governing Specification** | [PRD.md](../PRD.md) (`v1.2.0-draft` — Pending Team Review) |
| **Execution & Verification Baselines** | [PLAN.md](../PLAN.md), [TODO.md](../TODO.md), [docs/REQUIREMENTS_CHECKLIST.md](REQUIREMENTS_CHECKLIST.md) |
| **Provisional Page Target** | **Exactly 25.0 PDF Pages** *(Working Assumption: Option A — Total PDF Pages; counting rule `Q-01` remains Pending Lecturer Clarification)* |
| **Visual Reference Direction** | **Confirmed Team Decision**: Derived from `materials/fuel-and-go/Fuel&Go Whole Tasks.pptx` *(Approval of rendered 1-page visual sample remains Pending — `Q-04`)* |
| **Document Status** | **Revised Proposal — Pending Partner Review by Maria Mnasra & Basmala Jamal** |

---

## 1. Strategic Framing, Audience & Scope Governance

### 1.1 Proposed Report Title & Framing (`Q-02` — Pending)
- **Proposed Title**: *Fuel&Go: Preliminary Design Report for a Unified Smart Fueling and EV Charging Platform*
- **Subtitle**: *Business Context, System Architecture, Integration Boundaries, Safety Controls, and Verification Plan (Assignment 02)*
- **Governance Status**: Proposed working title aligned with the course textbook's *"Preliminary Design Report (PDR)"* framing (`preparation-report-book.pdf`, p. 2 — pedagogical reference to be checked for applicability) and Assignment 02's applied technical report rubric (`REQ-DOC-10`, `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf`, p. 2). Final confirmation remains pending partner decision (`Q-02` / `TASK-P1-04`).

### 1.2 Proposed Audience Separation (`Q-03` — Pending)
This outline strictly separates **report readers** from **application end users**:

| Reader Category | Role & Purpose | What the Report Must Deliver | Approval Status |
| --- | --- | --- | --- |
| **Executive Management & Product/Engineering Decision-Makers** | **Proposed Primary Decision Audience** | Concise commercial framing (business model, revenue mechanisms, major cost drivers, feasibility constraints, success metrics), disciplined scope boundaries, architectural trade-offs, security/safety residual-risk visibility, and phased product delivery roadmap. | **Proposed — Pending `Q-03` Approval** |
| **Course Lecturer & Graders / TAs** | **Confirmed Academic Evaluator** | Compliance with verified Assignment 02 mandates (`REQ-DOC-01`–`REQ-DOC-10`), exact 25-page execution, custom `.cls`, LuaLaTeX + Biber IEEE bibliography, reproducible Python plots, authentic multi-agent QA evidence, and zero fabrication. | **Confirmed** |
| **Application End Users** *(Not Report Readers)* | ICE/Hybrid & EV Drivers (Proposed Core); Fleet/Business Users (Proposed Roadmap) | Modeled inside Chapters 2, 3, and 6 as system actors and UX personas rather than report audience. | **Proposed — Pending `Q-05` Approval** |

### 1.3 Proposed Core Scope vs. Roadmap & Flagged Features (`Q-05` — Pending)
Core scope is proposed as **unified fueling and EV charging** (`FR-01`–`FR-06` in `PRD.md`), subject to final source verification and partner approval in `TASK-P1-01`. Slide references below serve as **source references to be checked** during partner scope sign-off rather than unilaterally promoted commitments:

| Classification | Scope Item | Reference Status (`REQUIREMENTS_CHECKLIST.md` & Original Deck) | Proposed Treatment in Outline |
| --- | --- | --- | --- |
| **Proposed Core Scope** *(Pending `Q-05`)* | `FR-01` Account, Auth & Vehicle Energy Profile; `FR-02` Unified Station & Charger Discovery; `FR-03` Pump/Charger Selection & Remote Authorization; `FR-04` Real-Time Fueling & EV Telemetry; `FR-05` Contactless Payment Settlement & Basic Digital Receipt; `FR-06` Session Fault Handling & Basic Support | Checked against `Fuel&Go Whole Tasks.pptx` (Slides 2–3, 30, 40) and `PRD.md` Sec. 2.1. **Partner approval pending (`TASK-P1-01`).** | Full specification, architecture, integration boundaries, UX flows, security/safety controls, and planned verification across **Ch. 1–8**. |
| **Source-Supported Roadmap Extensions** *(Pending `Q-05`)* | - `EXT-02`: Discounts, coupons, partner promotions & referral rewards<br>- `EXT-03`: Fleet management system & frequent-driver/fleet subscriptions<br>- `EXT-04 (Supported Part)`: Monthly AI-generated usage & financial summary reports<br>- `EXT-05 (Supported Part)`: Multi-sided B2B ecosystem & API partner integrations<br>- *Additional Slide 40 candidates*: Multilingual support, route optimization, smart queue alerts, trip cost estimation | Referenced in `Fuel&Go Whole Tasks.pptx` (Slides 4, 8, 27, 30, 40) as additional or ecosystem features. **Roadmap placement pending partner approval.** | Excluded from Core architecture depth; summarized concisely in **Ch. 1 scope boundary** and **Ch. 9 staged product roadmap**. |
| **Flagged — Unsupported or Disputed Features** *(Quarantined)* | - **`EXT-01` Convenience-Store Food & Coffee Pre-Ordering**: Not found in reviewed sources (Slides 74–75 contrast Fuel&Go as refueling-/experience-first vs. Yellow).<br>- **`EXT-04` Consolidated Corporate VAT Invoicing**: Unverified in reviewed sources (Slide 40 lists user AI financial summaries & digital receipts, not corporate VAT invoicing).<br>- **`EXT-05` Dedicated Station Operator Web Dashboard**: Unverified as standalone UI (Slides 8 & 27 reference B2B API integrations).<br>- **AI Guidance Assistant (Slides 3 & 40 Functional Features)**: Appears in original slides but **not currently in `PRD.md` `FR-01`–`FR-06`**. | Flagged for explicit partner ruling in `TASK-P1-01` / `Q-05`. | **Quarantined**: Shall NOT enter Core requirements or architecture unless Basmala and Maria explicitly approve promotion; flagged transparently in Ch. 1. |

---

## 2. Requirements & PRD Traceability Map

| Verified Mandate / PRD Governance Item | Source Reference | Mapped Chapters & Report Artifacts |
| --- | --- | --- |
| **`REQ-DOC-01`** Strictly 25 English pages | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Table 1; `PRD.md` Sec. 3 | Enforced via Section 3 indicative space budget & `nextmind-pdr.cls` (`Q-01` pending lecturer clarification). |
| **`REQ-DOC-02`** Images, graphs, summaries, texts, tables (+ optional math formula) | Assignment Brief p. 2, Table 1; `PRD.md` Sec. 6 | Executive Summary; Reproducible Python plots (Ch. 2, 5, and conditionally Ch. 8); TikZ diagrams (Ch. 3, 4, 5, 6, 7); engineering/business tables (Ch. 1–9); analytical formulas in Ch. 4 (weighted decision matrix) & Ch. 5/9 (sizing/risk). |
| **`REQ-DOC-03`** Chapters, ToC, IEEE bibliography, professional headers/footers | Assignment Brief p. 2, Table 1; `PRD.md` Sec. 7–8 | Front C (ToC only); Chapters 1–9; Back A (`biber` IEEE bibliography); custom `.cls` running header/footer. |
| **`REQ-DOC-04` & `REQ-DOC-07`** Custom `.cls` template & Rule of Reproducibility | Assignment Brief pp. 2–3; `PRD.md` Sec. 8 | `nextmind-pdr.cls` encapsulating approved visual rules from Section 5 Visual Brief (no ad-hoc layout overrides in `.tex` chapters). |
| **`REQ-DOC-05`** Deterministic LuaLaTeX + Biber build (0 errors, 0 `??` / `[?]`) | Assignment Brief pp. 2, 5; `PRD.md` Sec. 5.2 | Executed and evidenced in Phase 6; summarized in Ch. 8 (Report QA track) & Appendix A. |
| **`REQ-DOC-06` & `REQ-DOC-09`** Root structure, docs, source files, skills, final PDF | Assignment Brief pp. 3–4; `PRD.md` Sec. 10 | Repository-level deliverables (`main.tex`, modular chapters, `.cls`, `.bib`, `PRD.md`, `PLAN.md`, `TODO.md`, `README.md`, skills). |
| **`REQ-DOC-08`** 8 QA Skills families & independent verification | Assignment Brief p. 4, Table 2; `PRD.md` Sec. 5 | Audited read-only by Detector across 8 QA families + dual-track Red-Team; summarized in Ch. 8. |
| **Textbook Engineering Methods** *(Recommended Practice — Applicability Pending)* | `preparation-report-book.pdf` (pp. 2, 20, 24–29; reference to check) | PDR framing, weighted decision matrix (Ch. 4), quantitative risk scoring $R = P \times I$ (Ch. 9), and phased delivery roadmap (Ch. 9) used selectively as recommended best practice, never mislabeled as binding mandates. |

---

## 3. Provisional 25.0-Page Allocation (`Q-01` Pending Lecturer Clarification)

### 3.1 Layout Feasibility Rules & Counting-Rule Assumption
- **Working Assumption (Option A — Total PDF Pages = 25.0)**:
  - **Cover Page** (`1.0 p.`), **Document Control & Executive Summary** (`1.0 p.`), **Table of Contents** (`1.0 p.`, navigation only — redundant LoF/LoT omitted and Domain Acronyms placed in Back B to avoid single-page crowding), **IEEE References** (`1.5 p.`, sized naturally without 1-page cramming), and **Appendices** (`1.0 p.`, rebalanceable) are **counted inside the 25.0-page total**, leaving **19.5 pages** for Body Chapters 1–9.
- **Indicative Space Budgets (Not Forced Page Breaks)**:
  - Fractional allocations (e.g., `1.5`, `2.5`) represent **indicative space budgets** across continuous document flow—**not** mandatory `\clearpage` breaks at every chapter boundary.
  - **Typography Protection**: Readable body font size, line spacing, and A4 margins are non-negotiable; pagination adjustments must rebalance prose/visual density rather than compressing typography.
- **Counting Rule Status (`Q-01`)**: Explicitly **`Pending Lecturer Clarification`**. As noted in `docs/REQUIREMENTS_CHECKLIST.md`, the Assignment 02 brief specifies `25 עמודים (English)` without stating whether front/back matter count toward the total.
- **Fallback Rule (Option B — If 25 Body Pages Confirmed)**: If lecturer guidance confirms 25 body pages excluding front/back matter, Chapters 1–9 rebalance to **exactly 25.0 body pages**, and Cover, Front Matter, IEEE References, and Appendices appear as **additional pages** without artificial compression.

### 3.2 Summary Page Budget Table (Exact 25.0-Page Provisional Total)

| Unit | Proposed Title | Indicative Budget (Pages) | Cumulative (Pages) | Human Review Owner *(Preserving Existing Ownership)* |
| --- | --- | :---: | :---: | --- |
| **Front A** | Cover Page | `1.0` | `1.0` | Joint (Maria Mnasra & Basmala Jamal) |
| **Front B** | Document Control, Executive Summary & Audience Framing | `1.0` | `2.0` | Joint (Maria Mnasra & Basmala Jamal) |
| **Front C** | Table of Contents *(Navigation Only)* | `1.0` | `3.0` | Maria Mnasra *(Document Governance)* |
| **Ch. 1** | Introduction, Business Motivation & Scope Boundaries | `1.5` | `4.5` | Basmala Jamal *(Scope/PRD Owner)*; co-review *pending (`Q-09`)* |
| **Ch. 2** | Market Context, Business Model, Users & Stakeholders | `2.5` | `7.0` | *Pending partner assignment (`Q-09`)* |
| **Ch. 3** | System Requirements Specification (`FR` & `NFR`) | `2.5` | `9.5` | Basmala Jamal *(Requirements Owner)* |
| **Ch. 4** | Preliminary System Architecture & Technology Trade-Offs | `3.0` | `12.5` | Joint sign-off *(Major Architecture)*; primary reviewer *pending (`Q-09`)* |
| **Ch. 5** | Data Model & External Integration Boundaries | `2.5` | `15.0` | *Pending partner assignment (`Q-09`)* |
| **Ch. 6** | UX/UI Preliminary Flows, Visual Identity & Accessibility | `2.0` | `17.0` | Joint *(Visual Sign-Off `Q-04`)*; primary reviewer *pending (`Q-09`)* |
| **Ch. 7** | Security, Physical Safety, Privacy & Regulatory Compliance | `2.0` | `19.0` | *Pending partner assignment (`Q-09`)* |
| **Ch. 8** | Planned Product Verification vs. Actual Report QA & Red-Team Summary | `2.0` | `21.0` | Maria Mnasra *(Report QA/Governance)*; product-traceability co-review *pending (`Q-09`)* |
| **Ch. 9** | Product Delivery Plan, Risk Register, Roadmap & Conclusions | `1.5` | `22.5` | Maria Mnasra *(PLAN/TODO Owner)*; roadmap co-review Basmala Jamal |
| **Back A** | IEEE References (`biblatex` + `biber`) | `1.5` | `24.0` | *Pending partner assignment (`Q-09`)* *(Research-curated, Detector-audited)* |
| **Back B** | Appendices (Reproducibility, Data Provenance Legend & Acronyms) | `1.0` | `25.0` | *Pending partner assignment (`Q-09`)* |
| **TOTAL** | **Complete Assignment 02 PDF (Provisional Option A)** | **`25.0`** | **`25.0`** | **Final Sign-Off: Joint (Maria Mnasra & Basmala Jamal)** |

---

## 4. Detailed Chapter-by-Chapter Breakdown

### Front Matter (`3.0` Pages Indicative Total)
- **Front A — Cover Page (`1.0 p.`)**: Fuel&Go logo, proposed report title/subtitle, Team NextMind attribution (Maria Mnasra & Basmala Jamal), Assignment 02 metadata, version/date, styled per the approved visual sample.
- **Front B — Document Control, Executive Summary & Audience Framing (`1.0 p.`)**: Revision metadata, management-ready executive synthesis (market gap, unified fueling + EV scope, business-model drivers, architectural highlights, top residual risks, key decision gates), and explicit decision-maker vs. academic-evaluator framing.
- **Front C — Table of Contents (`1.0 p.`)**: Auto-generated **Table of Contents only** (`REQ-DOC-03`), keeping generous leading and readable font size. Separate Lists of Figures/Tables are omitted unless space permits naturally without compression; the **Domain Acronym Glossary** is placed in **Back B (Appendix B)**.
- **Human Review Owner**: Joint (Maria Mnasra & Basmala Jamal) for Front A & B; Maria Mnasra for Front C navigation governance.

---

### Chapter 1: Introduction, Business Motivation & Scope Boundaries (`1.5` Pages Indicative)
- **Purpose**: Frame the operational and commercial problem of fragmented fueling and EV charging experiences, state the proposed core product scope (`FR-01`–`FR-06`), establish target deployment jurisdiction assumptions, and quarantine unsupported or disputed features.
- **Key Questions Answered**:
  1. What driver and station-ecosystem pain points justify a unified ICE + EV mobile platform?
  2. What exact capabilities belong to the proposed Core Scope vs. staged roadmap vs. excluded/flagged items?
  3. What target market/jurisdiction anchors subsequent commercial and regulatory choices (e.g., Israel as referenced in original slides — pending partner confirmation)?
- **Evidence Needs**: Original Fuel&Go deck references to check (`Fuel&Go Whole Tasks.pptx`, Slides 2–3, 8, 30, 40, 74–75); IEEE-cited industry context on EV transition and charging-app fragmentation (Phase 3 Research); `PRD.md` Section 2 scope boundary.
- **Proposed Figures / Tables**:
  - *Table 1.1*: Core Scope vs. Source-Supported Roadmap vs. Flagged/Disputed Features Boundary Matrix (with source-reference status).
- **Human Review Owner**: **Basmala Jamal** (existing `PRD.md` & Scope Boundary Owner); co-reviewer *pending partner assignment (`Q-09`)*.

---

### Chapter 2: Market Context, Business Model, Users & Stakeholders (`2.5` Pages Indicative)
- **Purpose**: Provide decision-makers with grounded market context, competitive positioning, user/stakeholder roles, and a concise commercial feasibility overview covering Fuel&Go's proposed business model, revenue mechanisms, major cost drivers, and product success metrics.
- **Key Questions Answered**:
  1. What sourced market trends characterize ICE fueling and EV charging adoption in the target market?
  2. How does Fuel&Go differentiate from navigation-first (e.g., Waze) and discount-first (e.g., Yellow) competitors, and who are the core end users vs. ecosystem partners?
  3. What are the proposed **revenue mechanisms** (e.g., per-transaction/partner commission, B2B integration fees, future fleet/driver subscriptions), **major cost drivers** (PSP processing fees, cloud/telemetry infrastructure, station/CPMS onboarding & maintenance, security/compliance audits, user acquisition), **feasibility constraints** (multi-operator partner onboarding, margin sensitivity), and **product success metrics (KPIs)**?
- **Evidence Needs**: Verified IEEE-cited market and EV-adoption data (`TASK-P3-02`/`03`); public competitor facts checked against original Fuel&Go slides (Slides 8, 12–13, 30, 74–75, 78 — treated as references to be checked). **Zero-Fabrication Rule**: Every factual figure requires a verified citation; any illustrative commercial/demand scenario assumptions must be explicitly tagged `[Assumption]` / `[Illustrative / Simulated Data]`; **do NOT invent profitability, cost savings, adoption rates, or unit costs**.
- **Proposed Figures / Tables**:
  - *Figure 2.1 (Reproducible Python Plot #1)*: Sourced EV Charging & Dual-Energy Market Context Trend (`[Sourced Measurement]` + `[Calculation]` if normalized; exact source citation in caption & `data/README.md`).
  - *Table 2.1*: Commercial Overview & Stakeholder Matrix (Candidate Revenue Mechanisms, Major Cost Drivers, Feasibility Constraints, Product Success KPIs [targets `TBD` unless sourced], and Ecosystem Actor Roles).
- **Human Review Owner**: *Pending partner assignment (`Q-09`)* (Basmala Jamal verifies alignment with `PRD.md` personas & scope).

---

### Chapter 3: System Requirements Specification (`FR` & `NFR`) (`2.5` Pages Indicative)
- **Purpose**: Define unambiguous, testable core functional requirements (`FR-01`–`FR-06`) and non-functional requirements (`NFR-01a`–`NFR-07b`), prioritized via MoSCoW and anchored either to verified standards or explicit rationales (keeping unbacked numeric targets marked `TBD` until approved in `Q-10`).
- **Key Questions Answered**:
  1. What end-to-end functional capabilities govern ICE fueling and EV charging sessions?
  2. What performance, availability, security, safety-boundary, and accessibility requirements govern the system, and what verified source or engineering rationale backs each target (`Q-10`)?
  3. How do core human and external-system actors interact across the Fuel&Go boundary?
- **Evidence Needs**: Candidate standards to verify in `TASK-P3-01` (ISO/IEC/IEEE 29148, PCI DSS, OWASP MASVS/API, W3C WCAG 2.1/2.2 AA); verified UX/protocol rationales replacing `TBD` entries (`Q-10`). All runtime NFRs are explicitly labeled *Conceptual System Design — Proposed Targets*.
- **Proposed Figures / Tables**:
  - *Figure 3.1 (TikZ Vector Diagram #1)*: Core Use-Case & Actor Interaction Diagram (ICE/Hybrid Driver, EV Driver, PSP, Forecourt Gateway, EV CPMS).
  - *Table 3.1*: Core Functional Requirements (`FR-01`–`FR-06`) with MoSCoW priority & conceptual acceptance criteria.
  - *Table 3.2*: Non-Functional Requirements (`NFR-01a`–`NFR-07b`) with target/status (`TBD` where pending `Q-10`), rationale/source, planned verification method, and artifact type.
- **Human Review Owner**: **Basmala Jamal** (existing Requirements & `PRD.md` Owner).

---

### Chapter 4: Preliminary System Architecture & Technology Trade-Offs (`3.0` Pages Indicative)
- **Purpose**: Define Fuel&Go's conceptual multi-layer architecture and unified session state machine, clearly separating internal application layers from external station/EV integration domains, and justify candidate technology choices through a transparent **weighted decision matrix**.
- **Key Questions Answered**:
  1. How are mobile clients, backend orchestration services, payment services, and heterogeneous hardware/operator adapters decoupled?
  2. How does a single session state machine handle both short fuel-dispensing sessions and longer EV charging sessions—including authorization timeouts, user cancellations, connectivity loss, and pre-authorization hold release?
  3. On what weighted engineering criteria were candidate technologies evaluated against alternatives?
- **Evidence Needs**: Candidate architecture standards to verify (ISO/IEC/IEEE 42010 / IEEE 1016); verified literature on event-driven orchestration, cross-platform mobile trade-offs, and ACID/geospatial data stores; **weighted decision matrix** formula $S_j = \sum w_i c_{ij}$ *(using explicit terminology "weighted decision matrix" rather than "Pugh matrix", unless a genuine datum-based `+`/`-`/`0` Pugh comparison is adopted)*.
- **Proposed Figures / Tables**:
  - *Figure 4.1 (TikZ Vector Diagram #2)*: Fuel&Go Multi-Layer System Architecture Diagram (clearly distinguishing Mobile Client, API Gateway, Core Backend Services, PSP Integration, Charging-Management/Roaming Interface, and Forecourt Gateway Adapter).
  - *Figure 4.2 (TikZ Vector Diagram #3)*: Unified Fueling & EV Charging Session Finite State Machine (shared auth/settlement spine, diverging dispensing vs. EV telemetry branches, and fault/hold-release recovery).
  - *Table 4.1*: Candidate Technology Stack & **Weighted Decision Matrix** ($S_j = \sum w_i c_{ij}$, criteria weights & comparative rationale — all candidates pending `Q-10` team approval).
- **Human Review Owner**: **Joint Approval (Maria Mnasra & Basmala Jamal)** for major architectural trade-offs; primary chapter reviewer *pending partner assignment (`Q-09`)*.

---

### Chapter 5: Data Model & External Integration Boundaries (`2.5` Pages Indicative)
- **Purpose**: Specify the conceptual transactional data model and clearly partition six explicit integration interfaces/domains—distinguishing interfaces implemented by Fuel&Go from external domains shown only for context—while treating all protocols and version numbers as **candidates requiring source verification**, alongside an analytical latency/bandwidth sizing model.
- **Key Questions Answered**:
  1. What core data entities and transactional invariants (idempotency keys, ledger states, hold/capture reconciliation) mitigate duplicate settlement and orphaned payment holds?
  2. How are the **six explicit interfaces/domains** separated between Fuel&Go-implemented interfaces and external context-only domains:
     - **Interfaces Implemented by Fuel&Go**:
       1. *Mobile application ↔ Fuel&Go backend* (candidate REST + WebSocket/SSE APIs for discovery, authentication, telemetry streaming, and receipts).
       2. *Fuel&Go backend ↔ charging operator/roaming backend* (candidate e-roaming or operator B2B charging-management APIs, e.g., OCPI — edition to be verified).
       5. *Fuel&Go backend ↔ forecourt/POS gateway* (candidate forecourt controller or vendor POS gateway interfaces, e.g., IFSF — edition to be verified).
       6. *Fuel&Go backend ↔ payment service provider* (candidate tokenized pre-authorization, capture, and hold-release PSP APIs).
     - **External Domains Shown Only for Context** *(Outside Fuel&Go implementation boundary)*:
       3. *Charging station ↔ charging-management system* (candidate charger-to-CPMS protocol, e.g., OCPP — edition to be verified).
       4. *Vehicle ↔ charging station* (candidate vehicle-to-charger communication, e.g., ISO 15118 and low-level control signaling — edition to be verified; surfaced to Fuel&Go only indirectly via operator telemetry where supported).
  3. Under explicitly stated scenario assumptions, what end-to-end latency and telemetry bandwidth profile results across fueling vs. EV sessions?
- **Evidence Needs**: Candidate protocol specifications to verify in `TASK-P3-01` (exact active editions and architectural scope of candidate REST/WebSocket patterns, OCPI/operator APIs, OCPP, ISO 15118, IFSF/forecourt interfaces, and PSP tokenization APIs); reproducible Python analytical sizing script with explicit `[Calculation]` / `[Assumption]` / `[Illustrative / Simulated Data]` provenance tags in `data/README.md`.
- **Proposed Figures / Tables** *(Lean, layout-feasible set of 3 visuals for 2.5 pages)*:
  - *Figure 5.1 (TikZ Vector Diagram #4)*: End-to-End Session Authorization, Telemetry & Settlement Sequence Diagram explicitly labeling all six interfaces/domains—(1) Mobile application ↔ Fuel&Go backend, (2) Fuel&Go backend ↔ charging operator/roaming backend, (5) Fuel&Go backend ↔ forecourt/POS gateway, and (6) Fuel&Go backend ↔ payment service provider (Fuel&Go-implemented), visually distinguished from (3) Charging station ↔ charging-management system and (4) Vehicle ↔ charging station (external domains shown for context only).
  - *Figure 5.2 (Reproducible Python Plot #2)*: Analytical Latency Budget & Telemetry Bandwidth Scaling for Fueling vs. EV Sessions (`[Calculation]` / `[Assumption]` explicitly disclosed; no fabricated field measurements).
  - *Table 5.1*: Consolidated Core Data Entities, Transactional Invariants & Six-Interface/Domain Candidate Protocol Matrix *(maps all six consistent labels—(1) Mobile application ↔ Fuel&Go backend, (2) Fuel&Go backend ↔ charging operator/roaming backend, (3) Charging station ↔ charging-management system [external context], (4) Vehicle ↔ charging station [external context], (5) Fuel&Go backend ↔ forecourt/POS gateway, and (6) Fuel&Go backend ↔ payment service provider—noting ownership boundary and candidate protocols/versions pending verification)*.
- **Human Review Owner**: *Pending partner assignment (`Q-09`)*.

---

### Chapter 6: UX/UI Preliminary Flows, Visual Identity & Accessibility (`2.0` Pages Indicative)
- **Purpose**: Translate Fuel&Go's driver-first workflow into error-resistant mobile journeys for ICE and EV users, align conceptual UI ergonomics with the confirmed presentation-derived brand identity, and define measurable WCAG Level AA accessibility controls.
- **Key Questions Answered**:
  1. How do ICE and EV drivers progress from station discovery to bay verification (QR/NFC/bay ID), live telemetry, digital receipt, and fault recovery with minimal cognitive load?
  2. What UX guardrails reduce driver error (wrong fuel grade, mismatched pump/charger bay, incompatible EV connector)?
  3. How are contrast ratios, outdoor legibility, and accessible interaction targets evaluated against candidate WCAG Level AA criteria?
- **Evidence Needs**: Original Fuel&Go UX problem/flow references to check (Slides 2–3, 30, 50); candidate W3C WCAG 2.1/2.2 Level AA edition verified in `TASK-P3-01`; mathematically calculated contrast ratios for the adapted palette (verified again on rendered visual sample).
- **Proposed Figures / Tables**:
  - *Figure 6.1 (TikZ Vector Diagram #5)*: Dual-Energy Mobile User Journey & Error-Prevention Flow (Discovery $\rightarrow$ Bay/Connector Verification $\rightarrow$ Live Fueling vs. EV SoC Telemetry $\rightarrow$ Digital Receipt / Fault Recovery).
  - *Table 6.1*: Driver Error-Prevention Guardrails & WCAG Level AA Accessibility Criteria Matrix.
- **Human Review Owner**: **Joint (Maria Mnasra & Basmala Jamal)** for brand/visual alignment (`Q-04`); primary chapter reviewer *pending partner assignment (`Q-09`)*.

---

### Chapter 7: Security, Physical Safety, Privacy & Regulatory Compliance (`2.0` Pages Indicative)
- **Purpose**: Present a realistic cyber-physical risk posture detailing proposed security controls, physical safety boundary assumptions, payment-scope reduction limits, jurisdiction-dependent privacy obligations, residual risks, and required future validation.
- **Key Questions Answered**:
  1. What high-severity threats (STRIDE: QR sticker replacement, GPS spoofing, session hijacking, replay/duplicate settlement, API abuse) target Fuel&Go, what controls are proposed, and what **residual risks** remain?
  2. How does PSP payment tokenization **reduce cardholder-data exposure and potentially narrow PCI DSS compliance scope—without by itself establishing PCI DSS compliance** (which still requires compliant client/SDK handling, operational controls, and formal assessment)?
  3. What **proposed safety controls, hardware-independence assumptions** (certified local forecourt dispenser & EVSE emergency cutoffs remaining autonomous from cloud/mobile failures), **residual cyber-physical risks**, and **required real-world validation** (HIL/certified station testing) apply?
  4. Given the **intended deployment jurisdiction** (e.g., Israel as referenced in original slides — **jurisdiction must be confirmed by partners before finalizing legal obligations**), which privacy and payment/energy regulations apply—avoiding the assumption that EU GDPR applies automatically unless operating in or serving EU jurisdictions?
- **Evidence Needs**: Candidate standards to verify in `TASK-P3-01` (PCI DSS v4.0/4.0.1 scope guidance, OWASP MASVS & API Security Top 10, applicable jurisdiction privacy framework—e.g., Israeli Privacy Protection Law vs. EU GDPR if multi-region—and relevant forecourt/EVSE safety isolation references).
- **Proposed Figures / Tables**:
  - *Figure 7.1 (TikZ Vector Diagram #6)*: Trust Boundaries, Tokenization Scope & Local Hardware Safety Interlock Isolation Diagram (explicitly annotating assumed local hardware safety controls vs. cloud/mobile control boundaries).
  - *Table 7.1*: Condensed STRIDE Threat Model, Proposed Controls, Residual Risks, Key Assumptions & Required Validation.
- **Human Review Owner**: *Pending partner assignment (`Q-09`)*.

---

### Chapter 8: Planned Product Verification vs. Actual Report QA & Red-Team Summary (`2.0` Pages Indicative)
- **Purpose**: Maintain a strict, transparent boundary between **Planned Product Design Verification** (conceptual, unexecuted validation plans for Fuel&Go) and **Actual Report Quality Assurance** (real executed verification of the Assignment 02 PDF and reproducible pipeline), ensuring **a clean report build is never conflated with validating the runtime product**.
- **Key Questions Answered**:
  1. **Track 1 — Planned Product Verification (Conceptual / Unexecuted)**: How does each core `FR`/`NFR` map to architecture components, proposed future test levels (unit, integration, simulator, HIL, security audit), and acceptance criteria—while explicitly stating that runtime tests and performance targets remain proposed until genuinely built and evidenced?
  2. **Track 2 — Actual Report QA & Red-Team (Executed in Phase 6)**: What real build checks (`lualatex`/`biber`/`pdfinfo`), 8 QA skill families (`REQ-DOC-08`), Detector defect findings, 5-part Fixer/Detector incident records, and dual-track Red-Team findings were actually executed on this deliverable?
- **Evidence Needs**: Authentic Phase 6 build logs, real Detector defect logs (`qa/defects.json`, `qa/DEFECTS.md`), mandatory 5-part incident records (`qa/incidents/INC-*.md`), and Red-Team audit (`qa/redteam/redteam_audit*.md`).
- **Proposed Figures / Tables**:
  - *Table 8.1*: Requirements-to-Architecture-to-Planned-Verification Traceability Matrix (clearly labeled *Planned / Conceptual Product Verification*).
  - *Table 8.2*: Actual Report QA & Incident Remediation Summary (executed checks, defined denominators, defect statuses, and Red-Team outcomes).
  - *Conditional Figure 8.1 (Reproducible Python Plot #3 — Conditional)*: Actual Report QA Audit & Defect-Closure Chart built **strictly from recorded Phase 6 outcomes with explicitly defined denominators** (e.g., passed checks / total audited checks, closed defects / total logged defects). **Omission Rule**: If Phase 6 yields insufficient quantitative records to justify an informative chart, omit Figure 8.1 rather than padding or fabricating data, and retain Table 8.2 only.
- **Human Review Owner**: **Maria Mnasra** (existing Report QA & Execution Governance Owner); conceptual product-traceability co-review *pending partner assignment (`Q-09`)*.

---

### Chapter 9: Product Delivery Plan, Risk Register, Roadmap & Conclusions (`1.5` Pages Indicative)
- **Purpose**: Provide decision-makers with a realistic **Fuel&Go product delivery plan** (explicitly distinct from academic report production), a prioritized product/program risk register, a disciplined phased product roadmap (source-supported extensions only), and actionable go/no-go conclusions.
- **Key Questions Answered**:
  1. **Product Delivery Plan (Distinct from Assignment 02 Report Production)**: What phased engineering milestones transition Fuel&Go from Preliminary Design to MVP prototype, partner/CPMS sandbox integration, controlled station pilot, and commercial rollout—and what readiness gates govern each phase? *(Academic report workflow/multi-agent governance is summarized briefly in Ch. 8 / Appendix B, not conflated with product delivery.)*
  2. What are the highest-priority technical, partner-integration, commercial-feasibility, and regulatory risks ($R = P \times I$), with concrete mitigations and owners?
  3. How do source-supported extensions (`EXT-02`, `EXT-03`, AI monthly reports, B2B APIs) sequence onto the post-MVP roadmap without diluting MVP execution?
- **Evidence Needs**: Original Fuel&Go roadmap/launch references to check (Slides 8, 27, 40, 78); quantitative risk formula $R = P \times I$ *(recommended engineering practice)*; explicit labeling of delivery phase durations/estimates as `[Assumption]` (never presented as empirical benchmarks).
- **Proposed Figures / Tables**:
  - *Table 9.1*: Prioritized Product & Integration Risk Register ($P$, $I$, $R = P \times I$, Mitigation & Residual Exposure).
  - *Table 9.2*: Phased Fuel&Go Product Delivery Roadmap (Phase 1 MVP Core vs. Phase 2 Pilot/Partner Integration vs. Phase 3 Source-Supported Extensions — explicitly separating excluded/disputed items).
- **Human Review Owner**: **Maria Mnasra** (existing `PLAN.md`/`TODO.md` Owner), with **Basmala Jamal** co-reviewing product roadmap & scope alignment.

---

### Back Matter (`2.5` Pages Indicative Total)
- **Back A — IEEE References (`1.5 p.`)**: Auto-generated via `biblatex` + `biber` (`style=ieee`, `sorting=none`) from verified `bib/references.bib`. Sized naturally for readability (never compressed artificially into 1 page).
  - *Human Review Owner*: *Pending partner assignment (`Q-09`)* (curated by Research, audited read-only by Detector).
- **Back B — Appendices (`1.0 p.`)**:
  - *Appendix A*: Deterministic Report Reproduction Guide (PowerShell commands for `lualatex`/`biber` and `scripts/generate_figures.py`, pinned dependencies, toolchain versions, and concise Assignment 02 multi-agent evidence index).
  - *Appendix B*: 4-Category Data Provenance Legend (`[Sourced Measurement]`, `[Calculation]`, `[Assumption]`, `[Illustrative / Simulated Data]`) & Domain Acronym Glossary (moved here from Front C to keep the ToC clean and uncrowded).
  - *Human Review Owner*: *Pending partner assignment (`Q-09`)*.

---

## 5. Concise Visual Brief (Derived from the Original Fuel&Go Presentation)

> **Decision Status**:
> - **Confirmed Team Decision**: Use the original Fuel&Go presentation (`materials/fuel-and-go/Fuel&Go Whole Tasks.pptx`) as the visual reference direction for the report.
> - **Pending Partner Approval (`Q-04` / `TASK-P5-03`)**: All proposed report adaptations below remain proposals until Maria Mnasra and Basmala Jamal inspect and approve a rendered 1-page visual sample (`visual_sample.pdf`) prior to finalizing `nextmind-pdr.cls`.

### 5.1 Inspection Method & Provenance
- **Direct Visual Rendering Inspection**: 10 representative slides (`Slides 1, 2, 3, 6, 12, 15, 30, 40, 74, 75`) were exported directly via Microsoft PowerPoint to `1280x720` PNG images and visually inspected alongside extracted embedded media (`image26.png`, `image19.png`, `image1.png`, `image2.png`).
- **Structural OOXML Extraction**: All 78 slides, masters, themes, color runs (`a:srgbClr`), Latin font declarations (`a:latin`), and media links were inspected programmatically.

### 5.2 Observed Presentation Design Elements *(Directly Verified — Not Proposed)*

| Visual Dimension | Directly Observed in `Fuel&Go Whole Tasks.pptx` | Evidence / Reference |
| --- | --- | --- |
| **Brand Logo** | Black-outlined **fuel droplet** enclosing: (1) warm yellow-orange arc at top, (2) vibrant eco-green fuel nozzle angled right-upward, and (3) lime-to-green leaf/splash gradient at bottom-right; paired with bold uppercase geometric sans-serif wordmark **`FUEL&GO`** in dark charcoal below. | `image26.png` (38 slides), `image19.png` (8 divider slides), `image20.png` (5 slides), Slide 1 phone mockup (`image2.png`). |
| **Observed Color Palette (Hex Codes)** | Warm earthy eco-energy palette:<br>- **Canvas Fill**: Warm cream/parchment `#F6EBD4` (89 XML runs; dominant slide fill)<br>- **Primary Ink / Headings**: Deep espresso brown `#403011` (571 runs)<br>- **Primary Olive Green**: `#626C3B` (102 runs), lighter sage `#7B8554` / `#879450`, pale sage tint `#EAEDDE`<br>- **Olive-Gold / Ochre**: `#83792E` (71 runs) & `#9C9247` (32 runs)<br>- **Golden Amber**: `#E8AF3B` (69 runs) & `#CE9521` (22 runs)<br>- **Terracotta / Copper**: `#CC914D` (26 runs) & `#B27733` | OOXML extraction across 78 slides + rendered Slides 1, 2, 3, 6, 12, 30, 40, 74, 75. |
| **Observed Typography** | XML declares **`Brygada 1918`** (Semi Bold: 367 runs; Regular: 364 runs; Light/Bold: 10 runs), plus 2 runs of `Eras Bold ITC` (Slide 1 tagline). **Observed Rendering Limitation**: `Brygada 1918` is not installed locally in Windows on this workstation, so PowerPoint silently substituted a clean sans-serif fallback during PNG export. | OOXML font audit + rendered PNG inspection. |
| **Observed Layout Motifs & Issues** | - **Cover / Dividers (Slides 1, 6)**: Flat-illustrated green/yellow forecourt banner (`image1.png`) cropped by a curved wave over cream; dashed amber footer line on Slide 1.<br>- **Cards & Callouts**: Thin rounded cards (Slide 2), colored card header strips with line icons (Slide 3), thick left-accent vertical spine cards (Slide 12), olive-to-amber numbered pill headers (Slide 75), vertical olive stepper rail (Slide 74), framed quote box (Slide 30).<br>- **Observed Weaknesses**: Inconsistent logo placement (top-left on Slides 2, 3, 15, 30, 40 vs. top-right on Slides 12, 74, 75); low-contrast golden-amber kicker text (`#E8AF3B` on `#F6EBD4`, Slide 75 = **1.67:1** calculated WCAG 2.1 contrast — fails AA); raster AI-generated chart with garbled labels on Slide 15. | Rendered Slides 1, 2, 3, 6, 12, 15, 30, 40, 74, 75 + WCAG 2.1 luminance calculation. |

### 5.3 Proposed Report Adaptations & Improvements *(Proposals Only — Pending `Q-04` Visual Sample Approval)*

1. **Readable White Body Pages with Brand Accent Surfaces**:
   - Use **clean white (`#FFFFFF`)** for body pages to maximize printability, table clarity, and diagram crispness.
   - Preserve the presentation's warm cream (**`#F6EBD4`** / softer **`#FAF4E6`**) and pale sage (**`#EAEDDE`**) selectively for the **cover page panel, executive callout boxes, Slide-12-style left-spine summary cards, and subtle table shading**.
2. **Calculated WCAG 2.1 Level AA Contrast Hardening**:
   - All numeric contrast ratios below were **calculated deterministically via the WCAG 2.1 relative-luminance formula** (final rendered-PDF visual verification remains pending the 1-page sample):
     - **Deep Espresso `#403011` on White `#FFFFFF`**: **`12.74:1`** (passes AAA) — proposed primary body/heading ink.
     - **Deep Espresso `#403011` on Cream `#F6EBD4` / Soft Cream `#FAF4E6` / Pale Sage `#EAEDDE`**: **`10.77:1` / `11.61:1` / `10.71:1`** (passes AAA) — proposed callout and shaded-card ink.
     - **White `#FFFFFF` on Observed Olive `#626C3B`**: **`5.63:1`** (passes AA normal text; optional darkened olive `#4E572E` reaches **`7.70:1`**) — proposed table header / accent bar pairing.
     - **Deep Espresso `#403011` on Golden Amber `#E8AF3B`**: **`6.44:1`** (passes AA normal text) — safe for pill/badge accents.
     - **Darkened Text Amber `#8C5A00` on White `#FFFFFF` (`5.87:1`) and on Cream `#F6EBD4` (`4.96:1`)**: replaces observed `#E8AF3B` text (`1.98:1` on white; `1.67:1` on cream) for kickers and hyperlinks so all text meets WCAG AA (`>= 4.5:1`), keeping `#E8AF3B` strictly for graphical lines, borders, and chart fills.
3. **Deterministic LuaLaTeX Typography**:
   - Eliminate silent font substitution by verifying available system/TeX fonts in `TASK-P5-01` across both partners' machines before locking `nextmind-pdr.cls`.
   - *Proposed Pairing (to evaluate on visual sample)*: Verified editorial serif headings (`TeX Gyre Pagella` or portable bundled open-source `Brygada 1918` if verified) paired with clean sans-serif body (`Source Sans 3` / `TeX Gyre Heros`)—or clean sans headings with serif body—plus `TeX Gyre Cursor` monospace for requirement IDs, endpoints, and paths. Readable body size (e.g., `10–11 pt`) and comfortable leading are preserved across all 25 pages.
4. **Consistent Logo & Running Header/Footer**:
   - Standardize placement of the Fuel&Go droplet logo (`image26.png` / clean extracted asset pending approval) on the **cover page** and optionally as a restrained mark in the running header, with thin olive/amber rule and dynamic pagination (`Page \thepage\ of \pageref{LastPage}` — never hardcoded to 25).
5. **Cohesive Vector Diagram & Python Chart Palette**:
   - Use one disciplined, grayscale- and colorblind-aware palette across all TikZ diagrams and Python plots: Olive (`#626C3B`), Deep Espresso (`#403011`), Warm Amber (`#D48B22`), Muted Ochre (`#83792E`), and optional Deep Slate-Teal (`#2E5E63`) if a 5th series is needed (grayscale print distinction to be verified on the visual sample). Raster AI-generated charts are strictly prohibited.
6. **Approval Gate**:
   - Produce a **1-page representative visual sample (`visual_sample.pdf`)** showcasing heading hierarchy, body text, left-spine callout box, styled `booktabs` table, running header/footer, and palette swatch for **Maria Mnasra and Basmala Jamal's explicit approval (`TASK-P5-03`)** before finalizing `nextmind-pdr.cls`.

---
*Revised proposal for partner review by Maria Mnasra & Basmala Jamal. Keeps `PRD.md` unchanged and does not initiate chapter drafting.*
