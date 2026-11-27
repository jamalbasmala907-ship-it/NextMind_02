# Incident Record — INC-DEF-001

- **Incident ID:** INC-DEF-001
- **Linked Defect ID:** DEF-001
- **Date:** 2026-11-26
- **Affected Deliverable / Component:** `docs/RESEARCH_NOTES.md`, `data/ev_market_summary_verified.csv`, `data/README.md`, `bib/references.bib`
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
BibTeX key `israel_ev_2025_toi` was referenced in `docs/RESEARCH_NOTES.md` (line 66), `data/ev_market_summary_verified.csv` (lines 7–8), and `data/README.md` (line 16), but did not exist in `bib/references.bib` (17 entries total). Furthermore, `docs/RESEARCH_NOTES.md` line 66 cited only "Verified via web search summaries" with no canonical article URL or publication date.

## 2. Root Cause Analysis (Why did this occur?)
During research curation, a placeholder BibTeX key (`israel_ev_2025_toi`) was written into the notes and CSV dataset for secondary web-search summaries of Israel 2024–2025 BEV market share, while the corresponding entry was omitted from `bib/references.bib` because no primary CBS table or canonical article URL had been verified.

## 3. Missed Detection Analysis (Why earlier checks missed it?)
No automated cross-reference check was run comparing every BibTeX key cited in `docs/RESEARCH_NOTES.md`, `data/ev_market_summary_verified.csv`, and `data/README.md` against the keys defined in `bib/references.bib` before handoff to Detector.

## 4. Remediation Implemented
- **Files modified:**
  - `docs/RESEARCH_NOTES.md` (line 66)
  - `data/ev_market_summary_verified.csv` (lines 7–8)
  - `data/README.md` (lines 16–17)
- **Template version bump (if applicable):** N/A (not a `.cls` change)
- **Key code / text diff:**
  - Removed the dangling BibTeX key `israel_ev_2025_toi` from all three files so zero unresolved BibTeX keys remain.
  - Explicitly marked the Israel 2024–2025 rows in `docs/RESEARCH_NOTES.md`, `data/ev_market_summary_verified.csv`, and `data/README.md` as `Unverified Secondary Summary Pending Primary Source URL` (`source_key = PENDING_PRIMARY_SOURCE_URL`), complying strictly with the Zero-Fabrication policy (no URL was invented).

## 5. Preventative Action
Before submitting any research or data artifact, run a key-existence check ensuring every BibTeX key referenced in `docs/` and `data/` exists in `bib/references.bib` with a verified URL or statutory reference; never introduce a BibTeX key for an unverified secondary summary.

---
## 6. Retesting Sign-off (Detector Only)
- **Status:** **PASS — CLOSED**
- [x] Retest Passed
- [x] No Regressions Introduced
- **Method:** Direct read-only inspection of `docs/RESEARCH_NOTES.md:66`, `data/ev_market_summary_verified.csv:7-8`, `data/README.md:16-17`, and `bib/references.bib` against `DEF-001` acceptance criteria.
- **Raw Observed Evidence:** Dangling key `israel_ev_2025_toi` removed from all three files; `docs/RESEARCH_NOTES.md:66` now reads `*Pending primary URL* *(no BibTeX key)*` with `[Unverified Secondary Summary — Pending Primary Source URL]`; `data/ev_market_summary_verified.csv:7-8` uses `PENDING_PRIMARY_SOURCE_URL` and `Unverified Secondary Summary Pending Primary Source URL`; `data/README.md:16-17` matches. Zero unresolved BibTeX keys remain and zero URLs were fabricated.
- **Detector Signature / Verification Date:** Detector — 2026-11-26T19:50:00+02:00
