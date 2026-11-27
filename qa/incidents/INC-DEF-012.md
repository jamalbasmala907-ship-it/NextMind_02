# Incident Record: INC-DEF-012

- **Incident ID:** INC-DEF-012
- **Linked Defect ID:** DEF-012
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `figures/session_fsm.tex` (Figure 4), `main.pdf`
- **Logged By:** Fixer / Design
- **Reviewed & Retested By:** Detector (PASS — 2026-11-27)

---

## 1. Defect Summary & Symptoms
In `figures/session_fsm.tex` (Figure 4), the bottom Idempotency & Lock Invariant note box used a fixed `0.92 cm` tall rectangle, causing the wrapped 4-line text to overflow above the top border and below the bottom border.

## 2. Root Cause Analysis (Why did this occur?)
After expanding the idempotency and bay-lock explanation for Part A fixes (A3/A4), the text wrapped to 4 lines while the surrounding `\draw rectangle` remained hardcoded to `y = -0.62..0.30` (`0.92 cm`).

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
TikZ nodes placed inside separate `\draw` rectangles do not trigger LaTeX `\hbox` overflow warnings when vertical height exceeds the drawn border.

## 4. Remediation Implemented
- **Files modified:** `figures/session_fsm.tex`
- **Key code / text diff:**
  - Replaced the separate fixed-height `\draw rectangle` and centered `\node` with a single self-sizing bordered TikZ node (`rounded corners=3pt`, `fill=fgSoftCream`, `draw=fgRuleGray`, `inner sep=4.5pt`, `text width=15.9cm`) so the border automatically wraps all lines with generous padding.

## 5. Preventative Action
- Always use self-sizing bordered TikZ nodes (never separate fixed-height `\draw rectangle` frames) for multi-line callout and invariant notes inside diagrams.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Visual inspection of `qa/main-12.png` (Page 12, Figure 4) confirms the self-sizing cream callout node cleanly encloses all 4 lines of `Idempotency & Lock Invariant (FR-06a)` with generous vertical padding and zero border overflow.
- **Detector Signature / Verification Date:** `detector` — 2026-11-27T19:41:00+02:00
