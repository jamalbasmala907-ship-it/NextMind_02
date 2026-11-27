# Research Notes & Source Verification Log — Fuel&Go (Assignment 02)

- **Project**: Fuel&Go — Unified Smart Fueling & EV Charging Platform (Assignment 02 Engineering Report)
- **Team**: NextMind (Maria Mnasra, Basmala Jamal)
- **Author**: `research` agent (verified primary-source curation)
- **Date**: 2026-11-26
- **Governing References**: `PRD.md` (v1.2.0-draft), `docs/REPORT_OUTLINE.md`, `docs/REQUIREMENTS_CHECKLIST.md`, `agents/research/SKILL.md`
- **Bibliography File**: `bib/references.bib` (UTF-8, `biblatex`/`biber`, IEEE style)

---

## 1. Epistemic Classification & Zero-Fabrication Rules

Every item in this document and downstream report chapters is strictly classified into four provenance categories:
1. **`[Sourced Fact]`**: Directly verified from an official specification, statutory/regulatory text, government/agency report, or inspected local course PDF.
2. **`[Proposed Choice]`**: Engineering, architectural, or product design decision proposed by Team NextMind (pending partner sign-off where noted).
3. **`[Calculation]`**: Deterministic mathematical derivation from stated inputs (formulas documented explicitly).
4. **`[Assumption]`**: Preliminary sizing, commercial, or operational baseline chosen without empirical field measurement.

**Zero-Fabrication Notice**: No profitability figures, unit costs, adoption forecasts, DOIs, URLs, or standard edition numbers have been invented. Paywalled or member-restricted normative specifications are explicitly flagged in Section 6.

---

## 2. Assignment 02 PDF Inspection Findings (`materials/assignment02/`)

Direct visual and text inspection was performed on three local PDFs in `materials/assignment02/` to check unresolved governance questions, especially **`Q-01` (25-page counting rule)**:

### 2.1 `materials/assignment02/BIU26-27-A-ex02-pdf-via-LaTex-print.pdf`
- **Metadata**: 5 pages total; Dr. Yoram Segal, November 2026 (*"מטלה 02 – הכנת קובץ PDF באמצעות LaTeX"*).
- **Verified Findings**:
  - **Page 1 (Sec. 1)**: States Assignment 02 applies tools and principles from Lectures 04 & 05 (LuaLaTeX + LaTeX, custom `.cls` template for reproducibility, LaTeX project as a full software project with planning/QA/documentation, QA Skills orchestration, prompt engineering).
  - **Page 2 (Sec. 2, Table 1 — "דרישות המסמך הסופי")**: Explicitly mandates:
    - Length: `25 עמודים (English) או 15 עמודים (עברית + אנגלית משולבת)`.
    - Content: images, graphs, summaries, texts, tables (Excellence: at least one image, one table, optional mathematical formula).
    - Structure: division into chapters, Table of Contents, IEEE bibliography (Excellence: professional Footer + Banner).
    - Design: custom `CLS` file.
  - **Page 2–3 (Sec. 3–4)**: Mandates LuaLaTeX (MiKTeX), custom `.cls`, folder structure (`main.tex`, modular `.tex`, `.cls`, `PRD.md`, `PLAN.md`, `TODO.md`, `README.md`), and the Rule of Reproducibility (*"חוק ברזל: ראפטביליות"* — fix systemic issues in `.cls` or Skill, never directly in `.tex`).
  - **Page 4 (Sec. 5–6, Table 2)**: Mandates 8 QA Skills families (`qa-super`, `qa-BiDi`, `qa-table`, `qa-code`, `qa-img`, `qa-typeset`, `qa-infra`, `qa-cls-version`) and single joint GitHub repository submission.
  - **Page 5 (Sec. 7)**: Shows 4-pass compilation (`lualatex main.tex`, `biber main`, `lualatex main.tex`, `lualatex main.tex`).
- **`Q-01` Finding**: **UNRESOLVED.** Page 2, Table 1 specifies `25 עמודים (English)` without stating whether the cover page, Table of Contents, IEEE bibliography, and appendices are counted inside the 25 pages or excluded.

### 2.2 `materials/assignment02/l04-summary.pdf`
- **Metadata**: 64 PDF pages (front matter pp. i–x + body pp. 1–54); Dr. Yoram Segal, Bar-Ilan University, Department of Management, 04-11-2026 (*"הרצאה 4: מסמכים כקוד — PDF מקצועי עם LaTeX, LuaLaTeX ותבנית CLS"*).
- **Verified Findings**:
  - Covers managerial authority vs. responsibility (Ch. 1, body pp. 1–4), LaTeX content/design separation (Ch. 2, pp. 5–8), deterministic compilation vs. probabilistic LLM PDF generation (Ch. 3, pp. 9–12), MiKTeX/LuaLaTeX/`TikZ`/`pgfplots`/`biber` and 4-pass compilation (Ch. 4, pp. 13–16), custom `.cls` architecture (Ch. 5, pp. 17–30), class exercises (Ch. 6, pp. 31–35), BiDi rules and QA agent families/orchestration (Ch. 7, pp. 36–47), and IEEE references (pp. 52–54).
  - **Body p. 35 (PDF p. 45, Sec. 6.6 — "לקראת המטלה הבאה")**: States only that the next assignment will be given in the following lecture to prepare an organized, designed document using LaTeX and a `.cls` template.
- **`Q-01` Finding**: **NOT ADDRESSED.** Does not specify a 25-page count or front/back matter inclusion rule.

### 2.3 `materials/assignment02/l04+5.pdf`
- **Metadata**: 44 PDF pages (cover + numbered pp. 1–43); Dr. Yoram Segal, University of Haifa, 10-11-2026 (*"שיעור 4: צוות של סוכני AI — L04: Multi-Agent Orchestration with AI Coding Agents"*).
- **Verified Findings**:
  - Covers multi-agent orchestration, `agymesh` (`127.0.0.1:9877`, inbox/wait/reply, shared TODO board), ReAct loop, and Claude Code vs. Antigravity CLI.
  - **Numbered pp. 29–30 (PDF pp. 30–31, Ch. 9 — "מטלה 2: דוח מכין", Table 9)**: Describes the **University of Haifa** course variant of Assignment 2: a Preparatory Report (*"דוח מכין"*) of **approx. 40 pages** (*"דוח מכין של כ-40 עמודים"*), in pairs, modular `.tex` per chapter, Python-generated graphs, and TikZ diagrams.
- **`Q-01` Finding**: **DOES NOT RESOLVE BIU `Q-01`.** This file documents a 40-page University of Haifa course variant and does not clarify the Bar-Ilan University 25-page English counting rule in `BIU26-27-A-ex02-pdf-via-LaTex-print.pdf`.

### 2.4 Conclusion on `Q-01`
Across all three inspected assignment/lecture PDFs, **no lecturer clarification exists** regarding whether front/back matter count toward the 25 English pages. `Q-01` remains legitimately **Pending Lecturer Clarification**; Option A (25 total PDF pages) remains a working baseline assumption only.

---

## 3. Market Context & Business-Model Evidence (Chapters 1 & 2)

| BibTeX Key | Source Title & Publisher | Date / Version | URL / Identifier | Supported Claims (`[Sourced Fact]`) | Intended Chapters |
| --- | --- | --- | --- | --- | --- |
| `iea2025gev` | *Global EV Outlook 2025*, International Energy Agency (IEA) | 2025 (2024 data; inspected 2026-11-27) | `https://www.iea.org/reports/global-ev-outlook-2025/executive-summary` & `https://www.iea.org/reports/global-ev-outlook-2025/electric-vehicle-charging` | Directly verified verbatim: global electric car sales (BEV + PHEV) **exceeded 17 million** in 2024 (**more than 25%** YoY growth vs. 2023), reaching a sales share of **more than 20%** of new cars worldwide. Public charging coverage: **more than 1 public charger for every 10 electric cars** in China (reciprocal upper bound `< 10` electric cars per public charger, not an exact value of 10), and **on average 1 charger for every 13 electric cars** in the European Union. | Ch. 1, Ch. 2 (Fig. 2.1) |
| *Unverified — Excluded* *(no BibTeX key)* | Israel 2024–2025 BEV New-Car Market Share (secondary press summaries without directly inspected CBS primary table) | 2024–2025 | **UNVERIFIED** — no official Israel CBS primary source directly inspected | **`[UNVERIFIED — EXCLUDED]`**: Secondary press figures for Israeli 2024–2025 BEV new-car share are **unverified** and **strictly excluded** from all report empirical claims, charts, and calculations. Do not cite or plot unless an official CBS primary dataset is directly inspected and archived. | None (Excluded) |
| `evroaming2025ocpi` | *Open Charge Point Interface (OCPI) Specification*, EVRoaming Foundation | v2.2.1 (widely deployed) & v2.3.0 (active release) | `https://evroaming.org/ocpi/` | Defines the commercial and technical split between **CPO** (Charge Point Operator: owns/operates hardware & CSMS) and **eMSP** (e-Mobility Service Provider: owns driver app, authentication tokens, billing). Standardizes Locations, Tariffs, Tokens, Sessions, CDRs, and Commands for multi-network roaming. | Ch. 2, Ch. 5 |

### Business-Model Evidence vs. Assumptions (Ch. 2)
- **`[Sourced Fact]` (`evroaming2025ocpi`)**: Under OCPI, the EV charging ecosystem separates the **CPO** (Charge Point Operator, operating charging hardware/CSMS and publishing Locations, Tariffs, Sessions, and Charge Detail Records [CDRs]) from the **eMSP** (e-Mobility Service Provider, owning the driver app, authentication Tokens, and driver billing), with standardized CDRs serving as the settlement records between CPO and eMSP.
- **`[Assumption]` / Industry Context Pending Primary Source**: General EV charging monetization patterns (eMSP subscriptions/memberships, tariff markups/commissions over wholesale CPO rates, and B2B/fleet SaaS; CPO kWh energy sales, session/connection fees, and idle fees) and major eMSP cost drivers (customer acquisition cost [CAC], roaming hub/interchange fees, PSP payment processing fees, cloud/telemetry operations, 24/7 driver support, and working-capital/settlement timing gaps) are documented as industry context pending direct primary-source citations.
- **`[Proposed Choice]`**: Fuel&Go's proposed revenue mechanisms (per-transaction/partner commission, B2B API integration fees, future fleet/driver subscriptions) and KPIs (session completion rate, authorization latency, active repeat drivers) are **proposed design choices**, with numeric KPI targets kept `TBD` pending partner approval.
- **`[Assumption]` / Prohibition**: No profitability, margin percentages, unit costs, or adoption forecasts are claimed as empirical facts.

---

## 4. Six External Integration Boundaries (Chapter 5)

| Boundary # | Interface / Domain (per `REPORT_OUTLINE.md` Ch. 5) | Ownership | Candidate Protocol / Standard | Verified Edition / Date | BibTeX Key | Verification Notes (`[Sourced Fact]` vs. `[Proposed Choice]`) |
| :---: | --- | --- | --- | --- | --- | --- |
| **1** | Mobile application $\leftrightarrow$ Fuel&Go backend | **Proposed Fuel&Go Core Interface** | HTTP/REST + WebSocket | RFC 9110 (June 2022); RFC 6455 (Dec 2011) | `rfc9110`, `rfc6455` | `[Sourced Fact]` IETF standards for stateless HTTP semantics and full-duplex WebSocket streaming. `[Proposed Choice]` Candidate transport for discovery, auth, and live telemetry. |
| **2** | Fuel&Go backend $\leftrightarrow$ charging operator / roaming backend | **Proposed Fuel&Go Core Interface** | OCPI (EVRoaming Foundation) | v2.2.1 (widely deployed) / v2.3.0 (active) | `evroaming2025ocpi` | `[Sourced Fact]` Connects eMSP and CPO/roaming backends (Locations, Tariffs, Tokens, Sessions, CDRs, Commands). v2.3.0 adds AFIR/NAP and Plug & Charge indicators. |
| **3** | Charging station $\leftrightarrow$ charging-management system (CPMS/CSMS) | **External Context Only** | OCPP (Open Charge Alliance) | v2.0.1 (Mar 31, 2020; IEC 63584, late 2024) & v2.1 (Jan 2025) | `oca2020ocpp201`, `oca2025ocpp21` | `[Sourced Fact]` Governs charger-to-CSMS communication (authorization, meter values, firmware, security). Outside Fuel&Go's direct implementation boundary. |
| **4** | Vehicle $\leftrightarrow$ charging station (EVSE) | **External Context Only** | ISO 15118-2 & ISO 15118-20 | Part 2: Apr 2014; Part 20: Apr 2022 | `iso15118_2_2014`, `iso15118_20_2022` | `[Sourced Fact]` Defines EV-to-EVSE digital communication (Plug & Charge; Part 20 adds bidirectional V2G/V2H, mandatory TLS 1.3, multi-contract). Not application-layer backward-compatible between Part 2 and Part 20. Surfaced to Fuel&Go only indirectly via operator telemetry. |
| **5** | Fuel&Go backend $\leftrightarrow$ forecourt / POS gateway | **Proposed Fuel&Go Core Interface** | IFSF (International Forecourt Standards Forum) | Part II (Comm: LonWorks / TCP-IP) & Part III (App: FP / CDA) | `ifsf_specs` | `[Sourced Fact]` Industry standard for forecourt controller (FCC) and dispenser interoperability (Fuelling Point state machine: Idle, Authorised, Calling, Fuelling, Delivered). `[Access Limitation]` Exact current revision numbers are member-restricted; see Sec. 6. |
| **6** | Fuel&Go backend $\leftrightarrow$ Payment Service Provider (PSP) | **Proposed Fuel&Go Core Interface** | Tokenized PSP APIs under PCI DSS | PCI DSS v4.0.1 (June 11, 2024; all future-dated reqs mandatory Mar 31, 2025) | `pcissc2024pcidss401` | `[Sourced Fact]` Tokenization replaces PANs with non-sensitive surrogate tokens to shrink the Cardholder Data Environment (CDE), **without by itself establishing PCI DSS compliance** (client SDKs, operational controls, and formal assessment remain required). |

---

## 5. Candidate Technical, Security, Accessibility & Regulatory Standards (Chapters 3, 4, 6, 7)

| Domain | Standard / Legislation | Verified Version / Date | BibTeX Key | Supported Claims (`[Sourced Fact]`) | Intended Chapters |
| --- | --- | --- | --- | --- | --- |
| **Requirements Engineering** | ISO/IEC/IEEE 29148:2018 | Published Nov 30, 2018 | `iso29148_2018` | International standard for systems and software requirements engineering (characteristics of good requirements: unambiguous, verifiable, traceable). | Ch. 3, Ch. 8 |
| **Architecture Description** | ISO/IEC/IEEE 42010:2022 | Published Nov 7, 2022 | `iso42010_2022` | International standard for software, systems, and enterprise architecture description (viewpoints, stakeholders, concerns). | Ch. 4 |
| **Payment Card Security** | PCI DSS v4.0.1 (PCI SSC) | Published June 11, 2024; v4.0 retired Dec 31, 2024; future-dated reqs mandatory Mar 31, 2025 | `pcissc2024pcidss401` | Governs protection of cardholder data. Tokenization concentrates CDE scope at the PSP/vault and reduces merchant scope only if out-of-scope systems cannot access PANs or de-tokenize. | Ch. 3, Ch. 5, Ch. 7 |
| **Mobile App Security** | OWASP MASVS v2.1.0 | Released Jan 18, 2024 | `owasp2024masvs` | Baseline mobile security verification standard; v2.1.0 added `MASVS-PRIVACY` (data minimization, anti-identification, transparency, user controls) and CycloneDX SBOM support. | Ch. 3, Ch. 7 |
| **API Security** | OWASP API Security Top 10 (2023) | Released 2023 | `owasp2023apitop10` | Enumerates critical API risks including API1 (BOLA), API2 (Broken Authentication), API4 (Unrestricted Resource Consumption), API6 (Unrestricted Access to Sensitive Business Flows), and API10 (Unsafe Consumption of APIs). | Ch. 3, Ch. 7 |
| **Accessibility** | W3C WCAG 2.2 (Level AA) | W3C Recommendation Oct 5, 2023 (editorial update Dec 12, 2024) | `w3c2023wcag22` | Success Criterion 1.4.3 Contrast (Minimum): $\ge 4.5:1$ normal text, $\ge 3:1$ large text; SC 1.4.11 Non-text Contrast (from WCAG 2.1): $\ge 3:1$ for UI components and graphical objects. | Ch. 3, Ch. 6 |
| **Privacy (Israel)** | Israel Protection of Privacy Law, 5741-1981 (as amended by Amendment 13, 2024–2025) | Enacted 1981; Amendment 13 passed 2024, effective 2025 | `israel1981ppl` | **Territorial** jurisdiction governing entities and personal-data databases in Israel. Amendment 13 strengthens enforcement via direct administrative monetary sanctions by the Privacy Protection Authority (PPA) and mandatory DPO rules for qualifying entities. | Ch. 7 |
| **Privacy (EU — Conditional)** | EU General Data Protection Regulation (Regulation (EU) 2016/679) | Adopted Apr 27, 2016; effective May 25, 2018 | `eu2016gdpr` | **Extraterritorial** reach under Article 3 (applies only if Fuel&Go establishes in the EU, offers goods/services to data subjects in the EU, or monitors their behavior in the EU). Does **not** apply automatically to an Israel-only deployment. | Ch. 7 |

---

## 6. Reading & Access Limitations (Honest Audit)

| Source / Artifact | Status | Explicit Limitation |
| --- | --- | --- |
| `materials/assignment02/BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` | **Directly Inspected (Full, pp. 1–5)** | Complete visual + OCR review performed. `Q-01` not answered in file. |
| `materials/assignment02/l04-summary.pdf` | **Directly Inspected (Full, 64 PDF pp.)** | Complete visual + OCR review performed. `Q-01` not addressed. |
| `materials/assignment02/l04+5.pdf` | **Directly Inspected (Full, 44 PDF pp.)** | Complete visual + OCR review performed. Covers Haifa 40-page variant, not BIU 25-page rule. |
| ISO 15118-2:2014, ISO 15118-20:2022, ISO/IEC/IEEE 29148:2018, ISO/IEC/IEEE 42010:2022 | **Metadata & Scope Verified; Full Normative Text Paywalled** | Official titles, publication dates, and architectural scopes were verified via ISO/IEC/IEEE catalog summaries. Full normative clause-by-clause PDFs are paywalled and were **not** read. Do not cite specific internal clause numbers from these ISO standards. |
| IFSF Specifications (Part II & Part III) | **Architecture Verified; Normative PDFs Member-Restricted** | Public technical documentation confirms the Part II (Communication: LonWorks/TCP-IP) and Part III (Application: Fuelling Point state machine & CDA) structure. Exact current revision numbers and member-only normative PDFs are inaccessible without IFSF membership. |
| Israel CBS Raw EV Time-Series Tables | **UNVERIFIED — Excluded from Report and Charts** | No official Israel Central Bureau of Statistics (CBS) primary source page or raw dataset has been directly inspected. Secondary press summaries for 2024–2025 Israeli BEV share are marked **`UNVERIFIED_EXCLUDED`** in `data/ev_market_summary_verified.csv` and are strictly excluded from all report empirical claims, charts, and calculations until an official CBS primary dataset is directly inspected and archived. |


---

## 7. Original Fuel&Go Presentation Slide Traceability & PRD Conflict Log (2026-11-27)

Direct read-only OOXML extraction was performed on `materials/fuel-and-go/Fuel&Go Whole Tasks.pptx` (78 slides) to trace every product claim in Chapters 1–3 to exact slide numbers and surface conflicts against `PRD.md` (v1.2.0-draft):

| Slide(s) | Verified Presentation Content (`Fuel&Go Whole Tasks.pptx`) | Alignment / Conflict with `PRD.md` (v1.2.0-draft) |
| --- | --- | --- |
| **Slide 1** | Title: *Fuel&Go — Unified Service Application for Fueling and Charging Vehicles* (*"Driving the future of mobility"*). Authors: Maria Mnasra, Mona Azab, Basmala Jamal, Nuha Younis. | Aligned with dual-energy core vision. |
| **Slide 2** | Problem & Market Needs: long queues, moving between pumps and payment counters, separate apps per fuel company, fuel-type selection errors, and EV charging availability management in Israel. | Aligned with Ch. 1 motivation and Israel deployment context (jurisdiction pending partner confirmation). |
| **Slide 3** | High-level solution: user profile + vehicle setup, mobile pump/charger activation, digital payment (credit card, Apple Pay, Google Pay), smart navigation, real-time pump/charger availability, **AI Digital Assistant + monthly AI-generated consumption reports**. | **Conflict flagged**: AI Digital Assistant and monthly AI reports are listed on Slides 3 & 40 but are **not** in `PRD.md` core `FR-01`–`FR-06`. Quarantined pending `Q-05` partner ruling. |
| **Slide 4** | Target Users: private drivers, fleet/company drivers, tourists, gasoline/diesel/LPG/EV owners, and users with physical disabilities, psychological disorders, or low digital skills. | Core `PRD.md` focuses on ICE/hybrid and EV drivers; fleet/company drivers (`EXT-03`) and multilingual tourist features remain in proposed roadmap pending `Q-05`. |
| **Slides 8, 12, 13** | Industry insights (Israel EV shift, operator digitalization, brand-specific app fragmentation), qualitative TAM/SAM/SOM definitions (no invented market-size numbers), and direct/indirect competitor list (Waze, Google Maps, Paz, Sonol, Delek, EV-Edge, Dor-Alon Charge, Afcon EV, Pazomat, Delek Dalkan). | Used for Ch. 2 market/competitor framing; all external competitor claims independently verified in Sec. 8 below. |
| **Slide 27** | Goal 3: Multi-Sided Platform Ecosystem KPIs (Number of Ecosystem Partners, Number of API-Based Integrations, Payment Volume Processed). | Supports `EXT-05` as B2B API partner integration rather than a standalone station-operator web dashboard. |
| **Slide 30** | Full Value Proposition Statement (private drivers, EV owners, fleet operators, tourists, accessibility-challenged users; cross-network universal solution in Israel). | Core value proposition aligned; automatic vehicle recognition and AI guidance flagged as outside current `PRD.md` `FR-01`–`FR-06`. |
| **Slide 40** | Complete Feature Set divided into *Functional Features* (pump/EV activation, compatible type selection, in-app payment, live availability, profile, 2-car manual registration, cross-network integration, **AI assistant**) and *Additional Features* (AI monthly usage/financial reports, multilingual support, digital receipts, Apple/Google Pay, GPS recommendations, route optimization, low-fuel/battery alerts, discounts/coupons/promotions, station ratings, trip cost estimation, queue alerts, fleet management, subscriptions, referral rewards). | **Direct source backing for `EXT-02` (loyalty/promotions), `EXT-03` (fleet management & subscriptions), and `EXT-04` partial (AI monthly reports)**. Confirms `EXT-01` (C-store pre-ordering) and corporate VAT invoicing are **not** present in the presentation. |
| **Slide 50** | Persona 2 / User Story 4 (Safe Fuel Selection): restrict fuel selection to vehicle profile's predefined fuel type, disable/hide incompatible options, require confirmation before fueling. | Directly informs `FR-01`, `FR-03`, and Ch. 6 error-prevention guardrails. |
| **Slides 74–75, 78** | Competitive comparison vs. Waze (navigation-first) and Yellow App (discount-first); Fuel&Go positioned as refueling-/experience-first with Product-Led Growth (PLG); Launch KPIs (MAU, flow completion rate, repeat usage, payment volume). | Slide 74's claim that Yellow's EV charging is limited is updated with current official product verification in Sec. 8 (Paz yellow app now includes Paz Charge, though it remains brand-locked to Paz). |

---

## 8. Verified Competitor & UX Responsiveness Audit (Directly Inspected 2026-11-27)

| BibTeX Key | Product / Source | Exact Inspected URL & Page Title (Accessed 2026-11-27) | Documented Capabilities (`[Sourced Fact]`) | Bounded Positioning vs. Fuel&Go Core Concept |
| --- | --- | --- | --- | --- |
| `waze2025help`, `waze2025gas` | **Waze** (Google LLC) | `https://support.google.com/waze/answer/13259753?hl=en` (*Find EV charging stations along your route - Waze Help*) & `https://support.google.com/waze/answer/13739802?hl=en` (*Edit gas types and prices - Waze Help*) | Official Waze Help articles document route-based EV charging station discovery (filtered by plug type and preferred network) and community-reported fuel types and gas prices. | Inspected official help articles focus on discovery, routing, and community price reporting; remote pump/charger activation, live energy telemetry, and in-app payment settlement are not documented in these official feature guides. |
| `paz2025yellow` | **yellow app** (Paz Oil Company Ltd.) | `https://www.paz.co.il/paz-club` (*אפליקציית יילו - מתדלקים, קונים ומקבלים כסף לארנק \| yellow פז*) | Official Paz product page documents digital wallet and cashback loyalty features for fueling at Paz stations, yellow convenience store purchases, Paz Charge EV charging, and partner benefits. | Inspected official page positions yellow around the Paz and yellow partner ecosystem rather than cross-operator roaming across competing fuel chains and third-party EV CPOs. |
| `evedge2025app` | **EV-Edge** (Union Group) | `https://evedge.co.il/%D7%A8%D7%A9%D7%AA-%D7%A2%D7%9E%D7%93%D7%95%D7%AA/` (*רשת עמדות – EV-Edge*) | Official EV-Edge public charging network page documents public EV charging station discovery, charger speed tiers, live availability, and mobile app/RFID payment across the EV-Edge network in Israel. | Inspected official page documents EV charging services; liquid-fuel forecourt dispensing is not part of the documented EV-Edge public charging offering. |
| `afconev2025on` | **ON App** (Afcon EV) | `https://www.afconev.co.il/%D7%90%D7%A4%D7%9C%D7%99%D7%A7%D7%A6%D7%99%D7%99%D7%AA-on/` (*אפליקציית ON - AfconEV*) | Official Afcon EV ON application page documents public EV station discovery, connector/speed filtering, live availability and tariffs, remote session start/stop, and billing across the ON network in Israel. | Inspected official page documents EV charging services; liquid-fuel forecourt dispensing is not part of the documented ON application offering. |
| `nielsen1993responsetimes` | **Nielsen Norman Group** (Jakob Nielsen) | `https://www.nngroup.com/articles/response-times-3-important-limits/` (*Response Times: The 3 Important Limits*) | Establishes three human-computer interaction response-time limits: **0.1 s** (instantaneous), **1.0 s** (unbroken flow of thought), and **10 s** (attention limit before progress feedback is required). | Cited strictly as UX responsiveness guidance for `NFR-01a` / `NFR-01b`, distinct from an approved engineering performance target (exact P95 targets remain provisional pending engineering sign-off). |


---

## 9. Chapters 4–6 Verified Sources, Analytical Sizing Model & Remaining Gaps (2026-11-27)

### 9.1 Newly Verified Official Sources (Accessed 2026-11-27)
- **W3C WCAG 2.2 (`w3c2023wcag22`)**: Directly verified verbatim on `https://www.w3.org/TR/WCAG22/`:
  - **SC 1.4.3 Contrast (Minimum) (Level AA)**: $\ge 4.5{:}1$ normal text; $\ge 3{:}1$ large text.
  - **SC 1.4.11 Non-text Contrast (Level AA)**: $\ge 3{:}1$ for UI components and graphical objects.
  - **SC 2.5.8 Target Size (Minimum) (Level AA)**: *"The size of the target for pointer inputs is at least 24 by 24 CSS pixels"* (with documented spacing/inline exceptions).
- **Candidate Technology Official Documentation** (for Table 4.1 Weighted Decision Matrix):
  - `flutter2025docs` (`https://docs.flutter.dev/` — *Flutter documentation*, HTTP 200)
  - `postgis2025docs` (`https://postgis.net/documentation/` — *Documentation | PostGIS*, HTTP 200)
  - `rabbitmq2025docs` (`https://www.rabbitmq.com/docs` — *RabbitMQ Documentation*, HTTP 200)
  - `redis2025docs` (`https://redis.io/docs/latest/` — *Docs*, HTTP 200)

### 9.2 Analytical Telemetry Bandwidth & Latency Sizing Model (Spec for Design's Figure 5.2)
All inputs below are explicitly classified as **`[Assumption]`** and outputs as **`[Calculation]`** (zero invented empirical field measurements; NFR targets remain provisional):
1. **Aggregate Telemetry Bandwidth Scaling (`[Calculation]` + `[Assumption]`)**:
   - Formula: $B_{\text{total}}(N) = N \cdot \frac{P_{\text{bytes}} \times 8}{T_{\text{interval}} \times 1000}\;\text{kbps}$ (converted to Mbps by dividing by $1000$).
   - **Liquid-Fuel Dispensing Scenario (`[Assumption]`)**: $P_{\text{fuel}} = 512\;\text{bytes/event}$ (JSON telemetry frame over WebSocket/SSE), $T_{\text{fuel}} = 2\;\text{s}$ refresh interval $\Rightarrow 2.048\;\text{kbps}$ per active session. At $N = 100, 500, 1000, 2500, 5000$ concurrent sessions: $0.20, 1.02, 2.05, 5.12, 10.24\;\text{Mbps}$.
   - **EV Charging Scenario (`[Assumption]`)**: $P_{\text{ev}} = 768\;\text{bytes/event}$ (kWh, kW, SoC, tariff metadata), $T_{\text{ev}} = 15\;\text{s}$ refresh interval $\Rightarrow 0.4096\;\text{kbps}$ per active session. At $N = 100, 500, 1000, 2500, 5000$ concurrent sessions: $0.04, 0.20, 0.41, 1.02, 2.05\;\text{Mbps}$.
2. **Illustrative Authorization Latency Budget (`[Calculation]` + `[Assumption]`)**:
   - Formula: $L_{\text{auth}} = L_{\text{client-gw}} + L_{\text{orchestrator}} + L_{\text{psp-hold}} + L_{\text{operator-cmd}}$.
   - Illustrative component assumptions: $L_{\text{client-gw}} = 150\;\text{ms}$, $L_{\text{orchestrator}} = 120\;\text{ms}$, $L_{\text{psp-hold}} = 900\;\text{ms}$, $L_{\text{operator-cmd}} = 1200\;\text{ms}$ (forecourt gateway) or $1800\;\text{ms}$ (EV roaming/CPMS) $\Rightarrow L_{\text{auth,fuel}} = 2.37\;\text{s}$ and $L_{\text{auth,ev}} = 2.97\;\text{s}$. Demonstrates that external PSP and operator round-trips dominate end-to-end latency and exceed NN/g's $1.0\;\text{s}$ unbroken-flow threshold, requiring explicit progress indicators.

### 9.3 Remaining Evidence Gaps (Chapters 4–6)
- **Paywalled / Member-Restricted Standards**: ISO/IEC/IEEE 42010:2022, ISO 15118-2/20, and IFSF normative clauses remain inaccessible beyond verified catalog metadata/public scope.
- **No Empirical Field Telemetry or Vendor SLAs**: Bandwidth and latency figures in Ch. 5 are analytical `[Assumption]`/`[Calculation]` models only; real operator/PSP latencies require future sandbox/HIL measurement.

---

## 10. Full-Report Completion Notes (Chapters 7–9 & Front/Back Matter — 2026-11-27)
- Chapters 7–9, Front Matter, and Appendices were authored exclusively from the verified 27-entry `bib/references.bib` and Sections 1–9 above (PCI DSS v4.0.1, OWASP MASVS v2.1.0, OWASP API Top 10 2023, Israel Protection of Privacy Law Amendment 13, conditional EU GDPR Art. 3, ISO 29148/42010, and verified presentation slide audit).
- Zero unverified external claims, Israeli CBS statistics, empirical benchmarks, partnerships, or approvals were added.
- Unresolved lecturer counting boundary (`Q-01`), paywalled ISO/IFSF normative clauses, analytical-only sizing/risk assumptions, and partner review/sign-off (`Q-02`–`Q-10`, including Basmala's review & `README.md`) remain explicitly open.
