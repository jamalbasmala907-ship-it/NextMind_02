# Authoritative Requirements Checklist & Source Verification Audit
**Project:** Fuel&Go — Assignment 02 Engineering Report  
**Team:** NextMind (Maria Mnasra, Basmala Jamal)  
**Governing Documents:** [PLAN.md](../PLAN.md) (v1.1.0), [TODO.md](../TODO.md), [PRD](../<PRD (1).md>) (v1.2.0-draft)  
**Audit Date:** November 2026  
**Status:** Source Verification Completed — Baseline Evidence Documented

---

## 1. Explicit Lecturer Requirements vs. Preparation-Book Guidelines

To maintain rigorous technical compliance and avoid treating pedagogical textbook examples as binding rules, requirements are strictly distinguished across two normative tiers:
1. **Explicit Assignment 02 Mandates**: Requirements explicitly stated in the formal course assignment brief (`materials/assignment02/BIU26-27-A-ex02-pdf-via-LaTex-print.pdf`, Dr. Yoram Segal, Nov 2026).
2. **Preparation Book Pedagogical Models & Recommendations**: Guidelines, templates, and illustrative exercises from the course textbook (`materials/assignment02/preparation-report-book.pdf`, Dr. Yoram Segal, 83 pages). Their formal applicability to Assignment 02 is tracked as **Applicability Pending Verification / Recommended Practice** unless explicitly incorporated by the assignment brief.
3. **Multi-Agent Orchestration Directives**: Guidelines from the multi-agent mesh guide (`materials/assignment02/Multi-Agent-With-Antigravity.pdf`, Dr. Yoram Segal, 43 pages).

### 1.1 Explicit Assignment 02 Mandates (Binding Criteria)

| ID | Exact Assignment Mandate | Source Citation | Acceptance Criteria |
| --- | --- | --- | --- |
| **REQ-DOC-01** | **Deliverable Length**:<br>`25 עמודים (English) או 15 עמודים (עברית + אנגלית משולבת)` | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Table 1 | Exact 25-page target for English deliverable. **The assignment text does not specify whether front/back matter count toward this total.** Unresolved boundary tracked in `Q-01`. |
| **REQ-DOC-02** | **Required Document Content Elements** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Table 1 | Must include: images, graphs, summaries, texts, tables. (Excellence notes: at least one image, one table, optional mathematical formula). |
| **REQ-DOC-03** | **Required Document Structure** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Table 1 | Division into chapters, Table of Contents, Bibliography list in IEEE format. (Excellence notes: professional header banner and footer). |
| **REQ-DOC-04** | **Custom Template Class (`.cls`)** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Table 1 & Sec. 3.2 | Document styling must be encapsulated in a dedicated custom `.cls` class file. |
| **REQ-DOC-05** | **Compiler Pipeline** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2, Sec. 3.1; p. 5 | Compilation via **LuaLaTeX** (MiKTeX distribution) + **Biber**. Standard clean multi-pass execution (exit code 0, 0 errors, 0 undefined citations `[?]`, 0 broken cross-references `??`). |
| **REQ-DOC-06** | **Folder Structure Baseline** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 3, Sec. 3.3 | Project root must contain: `main.tex`, modular chapter `.tex` files (e.g. one per chapter), `.cls` template, `PRD.md`, `PLAN.md`, `TODO.md`, and `README.md`. |
| **REQ-DOC-07** | **Rule of Reproducibility ("חוק ברזל: ראפטביליות")** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 3, Sec. 4 | Never fix styling or layout problems directly in `.tex` chapters. All systemic fixes must be engineered in the `.cls` template or Skill. |
| **REQ-DOC-08** | **Mandatory QA Skills Families** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 4, Table 2 | Auditing against 8 QA families: `qa-super`, `qa-BiDi`, `qa-table`, `qa-code`, `qa-img`, `qa-typeset`, `qa-infra`, `qa-cls-version`. |
| **REQ-DOC-09** | **Submission Deliverables** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 4, Sec. 6 | Single joint GitHub repository containing: source files (`.tex`, `.cls`, `.bib`), documentation (`PRD.md`, `PLAN.md`, `TODO.md`, `README.md`), compiled final PDF, and skills files used. |
| **REQ-DOC-10** | **Topic Selection Scope** | `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 2 ("המלצה על בחירת נושא") | Practical and applied topic (seminar, professional report, paper, business plan, detailed RFP/PDR). |

### 1.2 Preparation-Book Pedagogical Models (Applicability Pending Verification)

The following items are defined in `preparation-report-book.pdf` as pedagogical models, reusable templates, and illustrative examples for a standard 40-page preparatory report. **Because the Assignment 02 brief does not explicitly incorporate these specific quantitative metrics, their formal applicability to Assignment 02 remains pending verification / recommended practice:**

| Pedagogical Component | Book Reference & Exemplar Details | Status for Assignment 02 |
| --- | --- | --- |
| **Report Framing** | Framed as a *"דוח מכין" / Preliminary Design Report (PDR)* serving as an engineering contract (`book` p. 2, Sec. 1.1). | **Adopted as Recommended Working Framing**; consistent with course objectives. |
| **40-Page Outline Model** | 8 core chapters (Problem, Literature/Flagship, Market, Alternatives, Plan, Risks, Summary) totaling 40 body pages (pp. 1–40) + 4 front-matter pages (pp. א'–ד') (`book` p. 4, Table 1.1). | **Pedagogical Model — Applicability Pending**. Assignment 02 mandates 25 English pages, not 40 pages. |
| **15 Peer-Reviewed Papers Target** | Exemplar in `book` p. 12, Table 5.1 & p. 72 (Prompt 3) suggests at least 15 papers from recent 5 years. | **Recommended Practice — Applicability Pending**. Assignment brief specifies IEEE bibliography format without prescribing a mandatory minimum paper count. |
| **14-Week Gantt Schedule** | Exemplar schedule spanning 14 weeks with 2 milestones (`book` pp. 26–27, Table 8.3, Fig. 8.2). | **Illustrative Template — Applicability Pending**. Assignment brief does not mandate a 14-week duration. |
| **Exactly 5 Work Packages (WBS)** | Exemplar hierarchical breakdown into `WP 1.0` through `WP 5.0` (`book` p. 24, Table 8.1, Fig. 8.1). | **Illustrative Template — Applicability Pending**. Standard engineering decomposition; specific count of 5 packages is an example. |
| **Specific Typography Parameters** | Exemplar layout in `book` p. 32, Table 11.1 specifies: David CLM / Times New Roman, line spacing 1.5, margins 2.5cm + 0.5cm gutter. | **Recommended Layout Guidelines — Applicability Pending**. Assignment brief requires custom CLS without hardcoding these exact dimensions. |
| **Pugh Decision Matrix & Quantitative Risks** | Pugh matrix formula $S_j = \sum w_i c_{ij}$ (`book` p. 20) and risk formula $R = P \times I \ge 12$ (`book` p. 29). | **Recommended Best Practice**. Standard engineering methods suitable for PDR sections. |

### 1.3 Multi-Agent Mesh Directives

| ID | Directive | Source Citation | Acceptance Criteria |
| --- | --- | --- | --- |
| **REQ-MSH-01** | **Authentic Multi-Agent Sessions** | `Multi-Agent-With-Antigravity.pdf` p. 15, 24–25 | Separate interactive sessions communicating over local hub (`127.0.0.1:9877`). Every message carries authentic session PID. |
| **REQ-MSH-02** | **Zero Simulation Rule** | `Multi-Agent-With-Antigravity.pdf` p. 24–25; User Directives | Strict prohibition against mock peer responses, simulated turns, or fake PONGs. |
| **REQ-MSH-03** | **Master Delegation** | `Multi-Agent-With-Antigravity.pdf` p. 10, 24 | Master orchestrates and delegates; Master never drafts report chapters or writes code directly. |

---

## 2. Original Fuel&Go Product Content & Feature Verification

The following findings are verified against the primary product source documents:
- `materials/fuel-and-go/Fuel&Go Whole Tasks.pptx` (78 slides by Maria Mnasra, Mona Azab, Basmala Jamal, Nuha Younis)
- `materials/fuel-and-go/PRD.md` (Prior HTML Presentation PRD, v1.0.0)

### 2.1 Core Verified Product Concept
Fuel&Go is an all-in-one mobile platform integrating fossil fuel dispensers and EV chargers into a continuous digital journey: Discovery $\rightarrow$ Selection $\rightarrow$ Remote Activation $\rightarrow$ In-App Payment $\rightarrow$ Telemetry & Digital Receipt.

### 2.2 Source Verification of Extension Features (`EXT-01..05`)

| Feature ID | Feature Description | Found in Reviewed Sources? | Exact Slide Citation & Evidence | Status & Technical Finding |
| --- | --- | :---: | --- | --- |
| **EXT-01** | **C-Store Food & Coffee Pre-Ordering** | **NO** | **Slide 74–75** (*Competitive Comparison*):<br>Slide 74 compares Yellow App (*"Messaging Focus: Saving money and earning benefits at fuel stations and convenience stores... Limitations: Yellow is discount-first"*).<br>Slide 75 notes Fuel&Go: *"Unlike Yellow, Fuel&Go is not discount-first but experience-first... refueling-first."* | **Not found in the reviewed sources**. In the 78 slides of `Fuel&Go Whole Tasks.pptx` and prior `PRD.md`, C-store pre-ordering is not included. The comparison with Yellow highlights a differing product focus, but the comparison alone does not establish formal exclusion. |
| **EXT-02** | **Loyalty Points, Coupons & Rewards** | **YES** | **Slide 40** (*Complete Feature Set — Additional Features*):<br>- *"Discounts, coupons, and partner promotions within the app"*<br>- *"Referral rewards program – user invites user"* | **Supported by reviewed sources**. Listed in Slide 40 under Additional Features (beyond the MVP flow). Candidate for compact roadmap presentation in Section 9. |
| **EXT-03** | **Fleet Management System** | **YES** | **Slides 4, 30, 40**:<br>- Slide 4 (*Target Users*): *"Fleet/ company Drivers"*<br>- Slide 30 (*Value Prop*): *"For private drivers, EV owners, fleet operators..."*<br>- Slide 40 (*Additional Features*): *"Fleet management system (for business customers)"*<br>- Slide 40: *"Subscription plans for frequent drivers or vehicle fleets"* | **Supported by reviewed sources**. Authored as an identified user segment and an Additional Feature on Slide 40. |
| **EXT-04** | **Monthly AI Financial / Usage Reports vs. Corporate VAT Invoicing** | **PARTIAL** | **Slide 40** (*Additional Features*):<br>- *"Monthly usage history reports automatically generated by AI"*<br>- *"Monthly financial reports automatically generated by AI"* | **Distinction Required**:<br>1. *Monthly AI usage & financial summaries*: **Directly supported** by Slide 40.<br>2. *Corporate / VAT tax invoicing*: **Unverified in reviewed sources**. Slide 40 specifies user-facing AI financial reports and digital receipts, but does not describe consolidated corporate VAT invoicing. Invoicing remains unverified pending partner clarification. |
| **EXT-05** | **Station Operator Dashboard / Portal** | **PARTIAL** | **Slides 8, 27**:<br>- Slide 8: *"Fuel station operators are investing in digital transformation and automation."*<br>- Slide 27 (*Goal 3*): *"Build Multi-Sided Platform Ecosystem... Number of Ecosystem Partners... Number of API-Based Integrations"* | **Architectural backend capability**. Operator connectivity is framed as B2B API integrations rather than a dedicated end-user web dashboard. |

---

## 3. Discrepancy & Conflict Analysis against Current `PRD (1).md`

| Item | Current Statement in `PRD (1).md` (v1.2.0-draft) | Actual Evidence from Source Verification | Recommended Resolution |
| --- | --- | --- | --- |
| **EXT-01..05 Status** (lines 75–87) | Labels all five extensions as *"Unverified — pending source review against original Fuel&Go slides"*. | Slide 40 directly supports **`EXT-02` (Loyalty/Promotions), `EXT-03` (Fleet Management), and AI monthly financial/usage summaries (`EXT-04 partial`)**. `EXT-01` (C-store) is not found in the reviewed sources. Corporate VAT invoicing remains unverified. | Basmala to update PRD Section 2: Distinguish supported roadmap features (`EXT-02`, `EXT-03`, AI reports) from unverified items (VAT invoicing, C-store ordering). |
| **Page-Count Boundary** (lines 91–101) | Outlines Option A (25 total PDF pages) and Option B (25 body pages). | Assignment 02 brief specifies `25 עמודים (English)` without stating whether front/back matter count toward the total. | Keep both interpretations visible as an **unresolved question (`Q-01`)**. Neither interpretation is asserted as safer without evidence. |
| **Proposed Section Outline** (lines 107–123) | Proposes a 9-section outline for a 25-page report. | Course textbook illustrates an 8-chapter model for a 40-page book. Whether the proposed 9-section outline covers every required concept remains **pending validation** until an explicit section-to-requirement mapping is authored and approved by Maria and Basmala (`TASK-P4-05`). | Remove unverified claims of total coverage; require formal section-to-requirement mapping during outline finalization. |

---

## 4. Separation of Governance Levels

```
+----------------------------------------------------------------------------------------------------+
| 1. EXPLICIT LECTURER MANDATES (Assignment Brief: BIU26-27-A-ex02-pdf-via-LaTex-print.pdf)          |
|    - Strict 25 English pages (or 15 mixed) [p. 2, Table 1]                                         |
|    - LuaLaTeX + Biber compilation, 0 errors, 0 undefined citations, no overfull hbox > 5pt         |
|    - Custom CLS class required [p. 2]                                                              |
|    - Required elements: images, graphs, summaries, texts, tables [p. 2]                            |
|    - Structure: chapters, Table of Contents, IEEE bibliography [p. 2]                              |
|    - 8 QA Skills families & rule of reproducibility [pp. 3-4]                                      |
|    - Single GitHub repository with sources, docs, PDF, and skills [p. 4]                           |
+----------------------------------------------------------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| 2. PREPARATION BOOK PEDAGOGICAL MODELS (Guidelines: preparation-report-book.pdf)                   |
|    *Applicability to Assignment 02 Pending Verification / Recommended Practice*                    |
|    - Preliminary Design Report framing ("דוח מכין" / PDR contract)                                 |
|    - Illustrative 40-page / 8-chapter textbook model (Ch. 1-8 body + 4 front-matter pages)         |
|    - Pedagogical exemplars: 15 papers target, 14-week Gantt, 5-WP WBS, Pugh & Risk matrices        |
|    - Typography guidelines: David CLM / Times New Roman, 1.5 line spacing, 2.5cm + 0.5cm margins   |
+----------------------------------------------------------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| 3. ORIGINAL FUEL&GO PRODUCT BASELINE (Source Slides: Fuel&Go Whole Tasks.pptx)                     |
|    - Dual-energy mobile platform (ICE fueling + EV charging)                                       |
|    - Core MVP: Discovery, Pump/Charger Selection, Remote Activation, Payment, Telemetry [Slides]  |
|    - Supported Additional Features: Discounts/promotions (Slide 40), Fleet management (Slide 40),  |
|      Monthly AI financial & usage summaries (Slide 40)                                             |
|    - Not found in reviewed sources: C-store food/coffee pre-ordering                               |
|    - Unverified in reviewed sources: Corporate / VAT tax invoicing                                 |
+----------------------------------------------------------------------------------------------------+
                                                  |
+-------------------------------------------------v--------------------------------------------------+
| 4. TEAM NEXTMIND WORKFLOW CHOICES (Governance Choices)                                             |
|    - 5-role agent division (Master, Research, Design, Detector, Fixer)                             |
|    - 5-part incident record format (qa/incidents/INC-xxx.md)                                       |
|    - Dual-track red-team auditing (Product Design Verification vs. Report QA)                      |
|    - Visual design proposals & rebalanceable page budget models (Option A / B)                     |
+----------------------------------------------------------------------------------------------------+
```

---

## 5. Reading Limitations & Unresolved Questions

### 5.1 Explicit Reading Limitations
1. `materials/assignment02/l04+5.pdf` and `materials/assignment02/l04-summary.pdf`: These lecture slide files have **not undergone direct, line-by-line review**. Reading related documents (`BIU26-27-A-ex02-pdf-via-LaTex-print.pdf`, `preparation-report-book.pdf`, `Multi-Agent-With-Antigravity.pdf`) provides valuable context on course concepts, but does **not** constitute direct review of `l04+5.pdf` or `l04-summary.pdf`.
2. `materials/fuel-and-go/PRD.md`: Directly reviewed; verified as the prior HTML presentation system PRD (v1.0.0), serving as historical background rather than the Assignment 02 report specification.

### 5.2 Key Decisions Awaiting Partner Resolution
- **`Q-01` (Page Boundary)**: Leave front/back matter inclusion unresolved pending lecturer clarification; do not assume either Option A (25 total PDF pages) or Option B (25 body pages) is safer without evidence.
- **`Q-04` (Visual Design)**: Maria and Basmala to inspect and approve Design's 1-page visual sample prototype before finalizing `nextmind-pdr.cls`.
- **`Q-05` (PRD Scope Alignment)**: Basmala and Maria to review Slide 40 evidence, decide whether to include supported roadmap items (`EXT-02`, `EXT-03`, AI reports) in Section 9, resolve unverified invoicing status, and sign off on PRD content baseline.
- **`TASK-P2-03` (Git Setup)**: Maria and Basmala to inspect remote history and authorize early Git setup.

---
*Checklist updated by Team NextMind.*  
*Evidence paths: `materials/assignment02/`, `materials/fuel-and-go/`.*
