# Incident Record — INC-DEF-003

- **Incident ID:** INC-DEF-003
- **Linked Defect ID:** DEF-003
- **Date:** 2026-11-26
- **Affected Deliverable / Component:** `docs/RESEARCH_NOTES.md`, `data/ev_market_summary_verified.csv`
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Rows 5–6 of `data/ev_market_summary_verified.csv` included China (`public_chargers_per_10_evs = 1.0`, `exceeded`) and European Union (`evs_per_public_charger = 13.0`, `approx`) attributed to `iea2025gev`, but `docs/RESEARCH_NOTES.md` line 65 omitted both numerical figures from its Supported Claims column for `iea2025gev`.

## 2. Root Cause Analysis (Why did this occur?)
When populating `data/ev_market_summary_verified.csv` from the IEA *Global EV Outlook 2025* (`iea2025gev`), the regional public-charging density metrics were added to the CSV without mirroring them back into the `iea2025gev` summary cell in `docs/RESEARCH_NOTES.md`.

## 3. Missed Detection Analysis (Why earlier checks missed it?)
No row-by-row reconciliation check was performed between `data/ev_market_summary_verified.csv` and the Supported Claims table in `docs/RESEARCH_NOTES.md` prior to QA handoff.

## 4. Remediation Implemented
- **Files modified:** `docs/RESEARCH_NOTES.md` (line 65)
- **Template version bump (if applicable):** N/A
- **Key code / text diff:**
  - Explicitly documented both verified IEA 2025 charger-density figures in the `iea2025gev` row of `docs/RESEARCH_NOTES.md`: "Public charging density exceeded **1.0 public chargers per 10 EVs** in China and stood at approximately **13 EVs per public charger** in the European Union in 2024."
  - Every `iea2025gev` row in `data/ev_market_summary_verified.csv` is now explicitly traced in `docs/RESEARCH_NOTES.md`.

## 5. Preventative Action
Require a 1-to-1 reconciliation check between every numeric row in `data/*.csv` and its corresponding source entry in `docs/RESEARCH_NOTES.md` before handoff.

---
## 6. Retesting Sign-off (Detector Only)
- **Status:** **PASS — CLOSED**
- [x] Retest Passed
- [x] No Regressions Introduced
- **Method:** Direct read-only row-by-row comparison of `data/ev_market_summary_verified.csv:5-6` against `docs/RESEARCH_NOTES.md:65`.
- **Raw Observed Evidence:** `docs/RESEARCH_NOTES.md:65` now explicitly states: "Public charging density exceeded **1.0 public chargers per 10 EVs** in China and stood at approximately **13 EVs per public charger** in the European Union in 2024," matching CSV rows 5–6 (`iea2025gev`).
- **Detector Signature / Verification Date:** Detector — 2026-11-26T19:50:00+02:00
