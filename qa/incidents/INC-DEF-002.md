# Incident Record — INC-DEF-002

- **Incident ID:** INC-DEF-002
- **Linked Defect ID:** DEF-002
- **Date:** 2026-11-26
- **Affected Deliverable / Component:** `docs/RESEARCH_NOTES.md`
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
`docs/RESEARCH_NOTES.md` line 70 tagged a broad statement on EV charging eMSP/CPO monetization models and eMSP cost drivers (CAC, roaming hub/interchange fees, PSP processing fees, cloud/telemetry operations, 24/7 driver support, working-capital/settlement timing gaps) as `[Sourced Fact]` with zero BibTeX keys or source citations attached.

## 2. Root Cause Analysis (Why did this occur?)
OCPI-verified architectural/commercial roles (CPO vs. eMSP and CDR settlement) were merged into a single `[Sourced Fact]` bullet alongside general industry monetization and cost-driver framing that lacked a direct verified citation in `bib/references.bib`.

## 3. Missed Detection Analysis (Why earlier checks missed it?)
The authoring pass checked epistemic tags manually without enforcing a strict rule that every `[Sourced Fact]` bullet must carry at least one explicit BibTeX key from `bib/references.bib`.

## 4. Remediation Implemented
- **Files modified:** `docs/RESEARCH_NOTES.md` (line 70)
- **Template version bump (if applicable):** N/A
- **Key code / text diff:**
  - Split line 70 into two distinct bullets:
    1. `[Sourced Fact]` (`evroaming2025ocpi`): restricted strictly to the OCPI-verified CPO/eMSP commercial and technical split and standardized CDR settlement roles.
    2. `[Assumption]` / Industry Context Pending Primary Source: reclassified the general eMSP/CPO monetization patterns and eMSP cost drivers lacking a direct verified citation.

## 5. Preventative Action
Enforce a pre-handoff audit rule that every `[Sourced Fact]` claim in `docs/RESEARCH_NOTES.md` must cite a verified BibTeX key from `bib/references.bib`; any uncited industry context must be tagged `[Assumption]` or `[Proposed Choice]`.

---
## 6. Retesting Sign-off (Detector Only)
- **Status:** **PASS — CLOSED**
- [x] Retest Passed
- [x] No Regressions Introduced
- **Method:** Direct read-only inspection of `docs/RESEARCH_NOTES.md:69-73` against `DEF-002` acceptance criteria.
- **Raw Observed Evidence:** Line 70 now reads `[Sourced Fact] (evroaming2025ocpi)` restricted strictly to OCPI CPO/eMSP roles and CDR settlement; line 71 separates general monetization patterns and eMSP cost drivers under `[Assumption] / Industry Context Pending Primary Source`.
- **Detector Signature / Verification Date:** Detector — 2026-11-26T19:50:00+02:00
