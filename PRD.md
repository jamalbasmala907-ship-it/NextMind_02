# Product Requirements Document (PRD): Fuel&Go — Preliminary Design Report (EX02)

| Field | Value |
| --- | --- |
| **Project Name** | Fuel&Go |
| **Deliverable** | Preliminary Design Report (PDR) — Assignment EX02 |
| **Team** | TEAM NEXTMIND |
| **Document Language** | English (en-US) |
| **Target Length** | 25 Pages |
| **Typesetting Engine** | LuaLaTeX + Biber (`biblatex`) |
| **Document Class** | Custom LaTeX Class (`nextmind-pdr.cls`) |
| **Version** | 1.0.0 |
| **Status** | Draft — Baseline Approved for EX02 Implementation |

---

## 1. Executive Overview & Purpose

### 1.1 Background
Modern refueling stations face recurring operational bottlenecks: long queues at payment counters, fragmented loyalty experiences, opaque real-time fuel pricing, slow reconciliation for fleet drivers, and limited integration between forecourt fuel dispensers and convenience-store operations. **Fuel&Go** is a smart refueling and station-commerce platform designed to streamline the end-to-end driver journey—from station discovery and pump activation to contactless payment, convenience pre-ordering, and digital receipt management—while giving station operators real-time telemetry and management tools.

### 1.2 Purpose of This PRD
This Product Requirements Document defines the complete requirements for producing the **Fuel&Go Preliminary Design Report (Assignment EX02)** for **TEAM NEXTMIND**. It establishes:
1. The **technical and product scope** of the Fuel&Go system to be documented in the PDR.
2. The **structural blueprint and 25-page budget** ensuring balanced engineering depth across all required sections.
3. The **LaTeX publication architecture** utilizing **LuaLaTeX**, **Biber**, and a **custom `.cls` class file** to deliver a publication-grade English PDF.
4. The **quality, verification, and build standards** required before final submission.

### 1.3 Success Criteria
- **Exact Page Target**: Final compiled PDF is **25 pages**, with no sparse trailing overflow pages or unintended blank pages.
- **Reproducible Compilation**: Builds cleanly from source via `lualatex` + `biber` with zero compilation errors, zero undefined citations, and zero broken cross-references.
- **Custom Class Architecture**: All visual styling, typography, headers/footers, cover layout, callouts, and table helpers are encapsulated in a maintainable custom `.cls` file (`nextmind-pdr.cls`).
- **Engineering Rigor**: Full traceability from stakeholder needs and requirements (`FR-*`, `NFR-*`) to system architecture, interfaces, security/safety controls, and verification plans.

---

## 2. Target Audience & Stakeholders

| Stakeholder | Role / Interest | Primary Needs from the PDR |
| --- | --- | --- |
| **Course Instructors & Graders** | Academic evaluation of Assignment EX02 | Rubric compliance, technical rigor, clear diagrams, proper citations, consistent English prose, and exact 25-page execution. |
| **TEAM NEXTMIND Members** | Authors, architects, and editors | Modular `.tex` file layout, clear section ownership, page-budget guardrails, and Git-friendly text sources. |
| **Product & Engineering Reviewers** | Technical feasibility evaluators | Coherent architecture, justified technology trade-offs, explicit assumptions, safety/security controls, and realistic roadmap. |
| **Simulated Fuel&Go Stakeholders** | Drivers, fleet managers, station operators | Clear value proposition, UX journeys, and measurable KPIs. |

---

## 3. Fuel&Go Product Scope (Subject of the PDR)

The Preliminary Design Report must specify Fuel&Go at a preliminary engineering design level, bridging concept exploration and detailed implementation.

### 3.1 Core Value Proposition
- **For Drivers**: Discover nearby stations with live fuel prices and pump availability, authorize and activate a pump from a mobile app, pay contactlessly with automatic digital receipts, earn unified loyalty rewards, and pre-order convenience-store items for curbside or grab-and-go pickup.
- **For Fleet Managers**: Enforce per-driver spending/fuel-type policies, track odometer and fuel consumption logs, and receive consolidated VAT-ready monthly invoices.
- **For Station Operators**: Increase forecourt throughput, reduce POS counter congestion, monitor pump status and anomalies in real time, and run targeted in-store promotions.

### 3.2 User Personas
1. **Everyday Commuter (B2C Driver)**: Prioritizes speed, price transparency, and one-tap contactless refueling.
2. **Commercial / Fleet Driver**: Needs company-card policy enforcement, automatic receipt capture, and route-aware station lookup.
3. **Station Manager / Forecourt Operator**: Needs live pump status, transaction oversight, exception handling (e.g., pump jam, payment hold failure), and convenience-order fulfillment alerts.
4. **Platform Administrator**: Manages station onboarding, pricing feeds, settlement reconciliation, system health, and security/audit logs.

### 3.3 Functional Requirements (To Be Detailed & Traced in PDR)
- **FR-01 — User Onboarding & Authentication**: Registration, OAuth2/OIDC login, MFA for fleet/admin roles, vehicle & fuel-type profile setup.
- **FR-02 — Station Discovery & Live Pricing**: Geolocation map/list view, filter by fuel grade, live price per liter, pump occupancy, EV charger availability (future-ready), and store services.
- **FR-03 — Pump Selection & Authorization**: QR code / NFC / manual pump-number selection, geofence verification (confirming user is physically at the station), pre-authorization hold via payment gateway, and pump unlock command.
- **FR-04 — Real-Time Refueling Telemetry**: Live display of dispensed liters, running cost, fuel grade, and automatic completion detection when nozzle is returned.
- **FR-05 — Contactless Settlement & Digital Receipts**: Capture exact transaction amount, release unused pre-authorization hold, generate itemized PDF/email/in-app receipts, and sync fleet expense records.
- **FR-06 — Convenience Store Pre-Order**: Browse station-specific catalog while refueling or en route, pay in unified checkout, receive pickup ready notification.
- **FR-07 — Loyalty & Promotions Engine**: Points accrual per liter/purchase, tier benefits, redeemable coupons, and operator-configured campaigns.
- **FR-08 — Operator Forecourt Dashboard**: Real-time bay/pump status board, manual emergency stop visibility, transaction audit log, order fulfillment queue, and pricing management.
- **FR-09 — Fleet Management Portal**: Driver/vehicle roster, fuel-grade/spend limits, anomaly alerts, and exportable accounting reports.
- **FR-10 — Support, Disputes & Incident Logging**: In-app receipt dispute workflow, failed-dispense recovery, and automated ticket escalation.

### 3.4 Non-Functional Requirements (To Be Quantified in PDR)
- **NFR-01 — Performance & Latency**: Pump authorization round-trip `<= 2.5 s` (P95); station discovery query `<= 500 ms` (P95).
- **NFR-02 — Availability & Reliability**: Core refueling authorization service `>= 99.95%` availability; graceful degradation to traditional pay-at-counter if cloud connectivity drops.
- **NFR-03 — Payment & Data Security**: PCI-DSS compliance via tokenized payment processors (zero raw PAN storage on Fuel&Go servers), TLS 1.3 in transit, AES-256 at rest, OWASP MASVS / API Security Top 10 alignment.
- **NFR-04 — Forecourt Physical Safety**: Hardware safety interlocks remain strictly local to certified forecourt controllers; mobile app cannot override emergency shutoff or dispensing safety cutoffs.
- **NFR-05 — Privacy & Compliance**: GDPR-aligned data minimization, explicit location consent, configurable retention, and right-to-erasure workflows.
- **NFR-06 — Scalability**: Support peak rush-hour concurrency (`>= 10,000` simultaneous active refueling sessions across partner networks).
- **NFR-07 — Usability & Accessibility**: Mobile UI compliant with WCAG 2.1 Level AA; refueling flow completable in `<= 4` taps from app launch.
- **NFR-08 — Maintainability & Observability**: Structured logging, distributed tracing, metrics dashboards, and modular service boundaries.

### 3.5 Preliminary System Architecture Scope
The PDR must present a clear multi-layer architecture covering:
- **Client Layer**: Cross-platform Mobile App (iOS/Android), Operator Web Console, Fleet Admin Portal.
- **Edge & API Layer**: API Gateway, WAF, Rate Limiting, Identity Provider (OAuth 2.0 / JWT).
- **Application Services**: Station & Pricing Service, Refueling Session Orchestrator (state machine), Payment & Billing Service, Convenience Order Service, Loyalty Service, Notification Service.
- **Forecourt Integration Layer**: Secure Forecourt Gateway / Edge Adapter translating Fuel&Go commands to station Point-of-Sale (POS) / Forecourt Controller protocols (e.g., IFSF / vendor APIs) with strict local safety boundaries.
- **Data & Analytics Layer**: Relational OLTP database (transactions, accounts, ledger), geospatial/cache store (Redis/PostGIS), event bus (Kafka/RabbitMQ) for telemetry and receipts, and analytical reporting store.

---

## 4. Document Structure & 25-Page Budget Allocation

To strictly meet the **25-page** requirement with high visual polish and balanced technical density, the report shall follow this section-by-section page budget:

| Section | Title | Target Pages | Page Range | Key Deliverables & Visuals |
| --- | --- | :---: | :---: | --- |
| **Front** | Custom Cover Page | 1 | p. 1 | Team NextMind branding, Fuel&Go title, EX02 metadata, date, version |
| **Front** | Document Control & Executive Summary | 1 | p. 2 | Metadata/revision table, concise executive summary, key KPI highlights |
| **Front** | Table of Contents, Figures, Tables & Acronyms | 1 | p. 3 | Auto-generated ToC, LoF/LoT summary, core glossary/acronyms table |
| **Sec. 1** | Introduction, Context & Problem Statement | 2 | pp. 4–5 | Domain background, pain points, project goals, scope boundaries (in/out of scope) |
| **Sec. 2** | Stakeholders, User Personas & Market Positioning | 2 | pp. 6–7 | Stakeholder matrix, persona cards, competitive landscape comparison table |
| **Sec. 3** | System Requirements Specification | 3 | pp. 8–10 | Functional requirements (`FR-01..10`), non-functional requirements (`NFR-01..08`), use-case diagram, MoSCoW prioritization |
| **Sec. 4** | Preliminary System Architecture & Tech Stack | 4 | pp. 11–14 | C4 / high-level architecture diagram, refueling session state machine, component responsibilities, technology trade-off matrix |
| **Sec. 5** | Data Design, Forecourt IoT & External Interfaces | 3 | pp. 15–17 | Conceptual ERD, key REST/WebSocket API contract table, payment & forecourt controller sequence diagram |
| **Sec. 6** | UX/UI Preliminary Design & User Journeys | 2 | pp. 18–19 | Core mobile flow wireframes/mockups, operator dashboard layout, accessibility design rules |
| **Sec. 7** | Security, Forecourt Safety, Privacy & Compliance | 2 | pp. 20–21 | Threat model (STRIDE summary), PCI-DSS/GDPR controls, physical safety boundary diagram |
| **Sec. 8** | Verification, Validation & Testing Strategy | 1 | p. 22 | Test pyramid, forecourt hardware-in-the-loop simulation plan, requirement-to-test traceability matrix |
| **Sec. 9** | Project Management, Risks & Delivery Roadmap | 1 | p. 23 | Risk register (likelihood/impact/mitigation), milestones/Gantt timeline, team roles |
| **Sec. 10** | Conclusions & Transition to Detailed Design | 1 | p. 24 | Readiness summary, open design decisions, next-phase objectives |
| **Back** | References (Biber) & Technical Appendix | 1 | p. 25 | Formatted BibLaTeX bibliography + compact traceability/API summary appendix |
| **TOTAL** | **Complete Preliminary Design Report** | **25** | **pp. 1–25** | **Exact 25-page target** |

### 4.1 Pagination Governance Rules
- Every section must respect its allocated page budget; overflow of more than `+/- 0.25` pages in any section requires content tightening or figure resizing rather than pushing the total past 25 pages.
- Avoid widows and orphans (`\widowpenalty=10000`, `\clubpenalty=10000`).
- Prevent empty half-pages caused by oversized unbreakable floats by sizing TikZ/vector figures cleanly and using structured placement (`[htbp]` with balanced captions).

---

## 5. Typesetting, Custom `.cls` Class & Visual Design Requirements

### 5.1 Toolchain Requirements
- **Compiler**: `lualatex` (TeX Live 2023+ or MiKTeX equivalent).
- **Bibliography Engine**: `biber` paired with `biblatex` (`backend=biber`, `style=ieee` or `apa`, `sorting=none` or `nyt`).
- **Encoding**: UTF-8 throughout all `.tex`, `.cls`, and `.bib` files.
- **Cross-References & Links**: `hyperref` + `cleveref` for clickable internal links, PDF bookmarks, and clean references (`Section~\ref{...}`, `Figure~\ref{...}`, `Table~\ref{...}`).

### 5.2 Custom Document Class (`nextmind-pdr.cls`)
All formatting and layout logic must reside in a custom LaTeX class file `nextmind-pdr.cls` rather than cluttering `main.tex`.

#### Required Class Capabilities
1. **Base Class & Page Geometry**:
   - Built on `article` (or `scrartcl`) with A4 paper (`210mm x 297mm`), clean margins (`top=24mm`, `bottom=24mm`, `left=22mm`, `right=22mm`, `headheight=14pt`).
2. **Typography (`fontspec` + `microtype`)**:
   - Clean modern sans-serif headings and readable body font loaded natively via LuaLaTeX `fontspec` (with reliable cross-platform TeX Live fallbacks, e.g., `TeX Gyre Heros` / `Inter` / `Latin Modern Sans` for headings, `TeX Gyre Pagella` / `Source Sans 3` / `Latin Modern` for body, and `TeX Gyre Cursor` / `Fira Code` / `Latin Modern Mono` for technical identifiers and endpoints).
   - Consistent line spacing (`1.12`–`1.15`) and micro-typographic protrusion/expansion.
3. **Brand Color System (TEAM NEXTMIND / Fuel&Go)**:
   - `nmPrimary`: Deep Navy (`#0F2942`) — headings, cover bands, table headers.
   - `nmAccent`: Fuel Amber / Vibrant Orange (`#E86A17`) — accents, callout borders, badges, diagram highlights.
   - `nmSecondary`: Slate Teal (`#1D6F8A`) — subheadings, secondary diagram elements, links.
   - `nmNeutralBg`: Soft Cool Gray (`#F4F6F9`) — callout box backgrounds, alternating table stripes.
   - `nmText`: Charcoal (`#1E293B`) — primary body text (high contrast, easier on the eyes than pure `#000000`).
4. **Headers & Footers (`fancyhdr` + `lastpage`)**:
   - Suppressed on the cover page (`\thispagestyle{empty}`).
   - Standard pages: Left header displays `TEAM NEXTMIND | Fuel&Go — Preliminary Design Report (EX02)`; right header displays current section name (`\nouppercase{\rightmark}` or `\leftmark`).
   - Footer: Left displays document version/classification; right displays `Page \thepage\ of \pageref{LastPage}` with a thin accent rule.
5. **Custom Metadata & Cover Page Command**:
   - Declarative macros in the preamble: `\projecttitle{}`, `\reportsubtitle{}`, `\assignmentcode{}`, `\teamname{}`, `\teammembers{}`, `\coursename{}`, `\institutionname{}`, `\docversion{}`, `\docdate{}`.
   - `\makepdrcover` macro rendering a full-bleed geometric vector title page using TikZ overlays with TEAM NEXTMIND identity and Fuel&Go metadata block.
6. **Reusable Components & Environments**:
   - `nmcallout` (`tcolorbox`): Styled executive insight, design decision, and safety warning boxes.
   - `reqtable`: Standardized `tabularx` + `booktabs` styling with navy header bar, subtle row striping, and ID column formatting for `FR-*`, `NFR-*`, and Risk tables.
   - `\reqid{FR-01}` / `\nfrid{NFR-01}` / `\riskid{R-01}`: Consistent monospace pill/badge macros.
   - Custom TikZ styles (`nmNode`, `nmService`, `nmExternal`, `nmArrow`, `nmBoundary`) so every architecture, sequence, and state diagram shares one cohesive visual language.

---

## 6. Graphics, Diagrams & Tables Specification

All technical visuals must be crisp vector graphics (TikZ/PGFPlots or vector PDFs) rather than low-resolution bitmaps:
1. **Use-Case & Actor Interaction Diagram** (Section 3 — TikZ).
2. **High-Level System Architecture Diagram** (Section 4 — TikZ, showing Client, Edge, Core Services, Forecourt Adapter, External Gateways, Data Layer).
3. **Refueling Session Finite State Machine** (Section 4 — TikZ: `IDLE -> SELECTED -> PRE_AUTHORIZED -> DISPENSING -> COMPLETED -> SETTLED` + error/timeout transitions).
4. **Conceptual Entity-Relationship Diagram (ERD)** (Section 5 — TikZ).
5. **End-to-End Pump Activation & Payment Sequence Diagram** (Section 5 — TikZ).
6. **Mobile App Key Screen Wireframes** (Section 6 — clean vector UI frames for Station Map, Pump Scan/Confirm, Live Dispensing, Digital Receipt).
7. **Security & Physical Forecourt Safety Boundary Diagram** (Section 7 — TikZ).
8. **Project Delivery Roadmap / Milestone Chart** (Section 9 — TikZ/PGFPlots).

Every figure and table must:
- Have a descriptive caption and unique label (`\label{fig:...}`, `\label{tab:...}`).
- Be explicitly referenced and discussed in the surrounding narrative prose.

---

## 7. Bibliography & Citation Standards (`biber`)

- All external standards, frameworks, industry benchmarks, and literature must be stored in `bib/references.bib`.
- Minimum **10–15 credible references**, including:
  - Requirements & systems engineering standards (e.g., ISO/IEC/IEEE 29148, IEEE 1016 / ISO 42010).
  - Security & payment standards (e.g., PCI-DSS v4.0, OWASP Mobile Application Security Verification Standard [MASVS], OWASP API Security Top 10, NIST SP 800-53 / STRIDE).
  - Privacy & accessibility standards (e.g., EU GDPR, W3C WCAG 2.1).
  - Forecourt / mobility / retail-fueling industry specifications (e.g., IFSF forecourt communication standards, Conexxus / NACS convenience retail insights).
- Every entry in `references.bib` cited in the document must resolve cleanly via `biber` with zero warnings.

---

## 8. Repository Structure & Build Workflow

### 8.1 Target Directory Layout
```text
NextMind-ex02/
├── PRD.md                       # This Product Requirements Document
├── nextmind-pdr.cls             # Custom LuaLaTeX document class for TEAM NEXTMIND
├── main.tex                     # Root LaTeX entry point assembling all sections
├── bib/
│   └── references.bib           # Biber bibliography database
├── sections/
│   ├── 00_frontmatter.tex       # Document control, executive summary, acronyms
│   ├── 01_introduction.tex      # Introduction & problem statement
│   ├── 02_stakeholders.tex      # Stakeholders, personas & market positioning
│   ├── 03_requirements.tex      # Functional & non-functional requirements
│   ├── 04_architecture.tex      # Preliminary architecture & technology stack
│   ├── 05_data_interfaces.tex   # Data model, APIs & forecourt IoT integration
│   ├── 06_ux_design.tex         # Preliminary UX/UI & user journeys
│   ├── 07_security_safety.tex   # Security, safety, privacy & compliance
│   ├── 08_verification.tex      # V&V, testing & traceability strategy
│   ├── 09_project_plan.tex      # Risk register, team roles & roadmap
│   ├── 10_conclusion.tex        # Conclusions & transition to detailed design
│   └── 11_appendix.tex          # Compact technical appendix
├── figures/                     # Modular TikZ diagrams or vector PDF assets
├── scripts/
│   └── build.ps1                # PowerShell build script (LuaLaTeX + Biber)
└── build/                       # Auxiliary build artifacts (gitignored)
```

### 8.2 Standard Build Pipeline (Windows PowerShell)
The canonical compilation sequence is:
```powershell
lualatex -interaction=nonstopmode -halt-on-error main.tex
biber main
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```
Alternatively, `latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex` may be used for automated dependency tracking.

### 8.3 Version Control Conventions
- Default branch: `main`.
- Commit style: Conventional Commits (e.g., `docs:`, `feat:`, `style:`, `fix:`, `chore:`).
- Auxiliary LaTeX artifacts (`*.aux`, `*.bbl`, `*.bcf`, `*.blg`, `*.log`, `*.out`, `*.run.xml`, `*.toc`, `*.lof`, `*.lot`) shall be excluded via `.gitignore` once LaTeX sources are added; final release PDFs may be tagged or committed per course submission policy.

---

## 9. Quality Assurance & Acceptance Checklist

Before marking Assignment EX02 complete, the compiled `main.pdf` must pass all checks:

- [ ] **Page Count**: Total PDF page count equals **exactly 25 pages**.
- [ ] **Clean Build**: `lualatex` + `biber` completes with exit code `0`, zero LaTeX errors, and zero Biber errors.
- [ ] **Reference Integrity**: Zero `??` unresolved cross-references and zero undefined citation keys in `.log`.
- [ ] **Typography & Layout**: Zero severe `Overfull \hbox` (> 10pt) warnings, no clipped tables, no overlapping TikZ labels, consistent headers/footers.
- [ ] **Language & Tone**: Clear, formal technical English throughout; consistent terminology (`Fuel&Go`, `TEAM NEXTMIND`, `EX02`).
- [ ] **Traceability**: Every `FR-*` and `NFR-*` maps to at least one architecture component and one verification method.
- [ ] **PDF Metadata**: Embedded title, author (`TEAM NEXTMIND`), subject (`Fuel&Go Preliminary Design Report — EX02`), and navigable PDF outline bookmarks.

---

## 10. Assumptions, Constraints & Risks

| ID | Type | Description | Mitigation |
| --- | --- | --- | --- |
| **A-01** | Assumption | Fuel stations use a local certified forecourt controller capable of interfacing via a secure edge gateway. | Document the adapter abstraction layer and keep physical safety interlocks strictly local. |
| **A-02** | Assumption | Standard TeX Live / MiKTeX packages (`fontspec`, `biblatex`, `tikz`, `tcolorbox`, `booktabs`, `tabularx`, `hyperref`) are installed. | Restrict `.cls` dependencies to standard TeX distribution packages and include safe font fallbacks. |
| **R-01** | Risk | Page count drifts above or below 25 pages during collaborative editing. | Enforce per-section page budgets (Section 4) and verify page count on every build. |
| **R-02** | Risk | Missing system fonts cause LuaLaTeX build failures across different machines. | Use TeX-bundled OpenType fonts (e.g., TeX Gyre / Latin Modern / Fira) with automatic `fontspec` fallback checks. |
| **R-03** | Risk | Biber version mismatch with `biblatex` breaks bibliography compilation. | Keep TeX distribution packages synchronized and validate `biber --version` in build scripts. |
