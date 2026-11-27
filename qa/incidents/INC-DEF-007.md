# Incident Record: INC-DEF-007

- **Incident ID:** INC-DEF-007
- **Linked Defect ID:** DEF-007
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `sections/sec02_users_stakeholders.tex`, `scripts/plots/fig2_1_market_context.py`, `figures/fig2_1_market_context.pdf`, `draft_ch1_3.pdf` (Page 5, Sec. 2.1 & Figure 1)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Two data-provenance and epistemic-hygiene defects were identified on Page 5 (`sections/sec02_users_stakeholders.tex` and Figure 1 `figures/fig2_1_market_context.pdf`):
1. **Unverified secondary percentages in prose:** `sections/sec02_users_stakeholders.tex` line 16 printed unverified secondary Israel BEV new-car share numbers (`roughly 25% in 2024 and 20% in 2025`) derived from `PENDING_PRIMARY_SOURCE_URL` rows, despite stating they were not used as empirical evidence.
2. **Incomplete provenance tagging & mixed-unit clarity on Figure 1:** `scripts/plots/fig2_1_market_context.py` line 65 computes a reciprocal conversion (`china_evs_per_chg = 10.0 / china_chg_per_10` -> `<10 EVs/chg`), which is a `[Calculation]`, yet both the chart footer (line 181) and the LaTeX caption (`sec02_users_stakeholders.tex` line 28) tagged the figure solely as `[Sourced Measurement]`. Additionally, Panel A combined millions and percentages on a single y-axis without explicitly clarifying the left/right unit split in the axis label and caption.

## 2. Root Cause Analysis (Why did this occur?)
- **Prose leakage of excluded data:** While the CSV filter correctly excluded `PENDING_PRIMARY_SOURCE_URL` rows from Figure 1, the narrative disclaimer in Sec. 2.1 still echoed the unverified secondary percentages (`25%` and `20%`) inline.
- **Unflagged derived normalization:** The plotting script normalized China's IEA metric (`>1.0 public charger per 10 EVs`) into `EVs per public charger` (`<10 EVs/chg`) for visual comparability with the EU bar, but the provenance footer and LaTeX caption were written before that derived transformation was classified as `[Calculation]` per `PRD.md` Sec. 6.2.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
- Earlier checks verified that the Python script filtered out `PENDING_PRIMARY_SOURCE_URL` CSV rows and that all BibTeX keys resolved, but did not audit report body prose for leaked unverified numbers or cross-check derived arithmetic transformations inside plotting scripts against `PRD.md` Sec. 6.2 provenance tags (`[Sourced Measurement]` vs. `[Calculation]`).

## 4. Remediation Implemented
- **Files modified:** `sections/sec02_users_stakeholders.tex`, `scripts/plots/fig2_1_market_context.py`, `figures/fig2_1_market_context.pdf` (regenerated)
- **Template version bump (if applicable):** None
- **Key code / text diff:**
  - `sections/sec02_users_stakeholders.tex:16`: Removed `roughly 25\% in 2024 and 20\% in 2025` while retaining the transparent disclosure that direct CBS primary-source tables for Israeli BEV share remain pending verification and unverified secondary press figures are omitted from empirical claims and Figure 1.
  - `scripts/plots/fig2_1_market_context.py:128,178-190`: Clarified Panel A y-axis label to `"Value (Left: Millions; Right: %)"` and updated the two-line provenance footer to explicitly include both `[Sourced Measurement]` (IEA Global EV Outlook 2025, 5 verified rows) and `[Calculation]` (`China Panel B reciprocal normalization: 10 / (>1.0 chg per 10 EVs) = <10 EVs/chg`), adjusting `tight_layout(rect=[0.0, 0.11, 1.0, 1.0])`.
  - `sections/sec02_users_stakeholders.tex:28`: Updated Figure 1 caption to note Panel A mixed units and tag both `\texttt{[Sourced Measurement]}` and `\texttt{[Calculation]}` (`10 / >1.0 = <10 EVs/charger`).
  - Regenerated `figures/fig2_1_market_context.pdf` via `.\.venv\Scripts\python.exe scripts/generate_figures.py`.

## 5. Preventative Action
- **Zero-echo rule for unverified figures:** When data is excluded under `PENDING_PRIMARY_SOURCE_URL`, omit the unverified numeric values from prose as well as tables/charts; state only the verification status and exclusion rationale.
- **Plot provenance audit:** Any arithmetic transformation in a plotting script (including unit conversions or reciprocals) must carry an explicit `[Calculation]` tag alongside `[Sourced Measurement]` in both the figure footer and the LaTeX caption.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Read-only inspection of `sections/sec02_users_stakeholders.tex:16,28`, `scripts/plots/fig2_1_market_context.py:128,178-190`, `draft_ch1_3.log`, `draft_ch1_3.blg`, and visual inspection of `qa/draft_ch1_3-05.png` and `qa/draft_ch1_3_gray-05.png`. Confirmed: (a) unverified `25%` / `20%` secondary Israel percentages are completely removed from Sec. 2.1 prose while retaining the CBS pending-verification note; (b) Figure 1 footer and LaTeX caption explicitly tag both `[Sourced Measurement]` and `[Calculation]` (`10 / >1.0 = <10 EVs/chg`), and Panel A y-axis clarifies mixed units; (c) grayscale hatching and contrast preserved; 0 LaTeX/Biber errors/warnings and 0 overfull hbox > 5pt.
- **Detector Signature / Verification Date:** `detector` — **PASS (CLOSED)** — `2026-11-27T13:27:00+02:00`
