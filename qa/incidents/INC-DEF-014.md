# Incident Record: INC-DEF-014

- **Incident ID:** INC-DEF-014
- **Linked Defect ID:** DEF-014
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `nextmind-pdr.cls` (`\fgchapter`), `main.tex`, `main.pdf`
- **Logged By:** Fixer / Design
- **Reviewed & Retested By:** Detector (PASS — 2026-11-27)

---

## 1. Defect Summary & Symptoms
In the initial `main.pdf` build, Chapter 03 and Chapter 07 banners appeared orphaned near page bottoms (pp. 7 and 17), Figure 6 (Sec. 5.3) floated onto an isolated page after Chapter 6 started, and Table 7 (Sec. 6.2) floated past the Chapter 7 banner.

## 2. Root Cause Analysis (Why did this occur?)
`\fgchapter` lacked `\FloatBarrier` and `\needspace`, allowing floats from the preceding chapter to drift past the next chapter banner and allowing chapter banners to sit at the bottom of a page without their opening paragraph.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
Continuous-flow pagination was tuned for total page count (25 pages) without enforcing chapter-boundary float barriers in `nextmind-pdr.cls`.

## 4. Remediation Implemented
- **Files modified:** `nextmind-pdr.cls` (`Working v0.3.3`), `main.tex`
- **Key code / text diff:**
  - Added `\FloatBarrier` and `\needspace{7\baselineskip}` inside `\fgchapter` so every chapter flushes prior floats before starting and never leaves an orphan chapter banner at the bottom of a page.
  - Tuned vertical geometry and spacing cleanly in `main.tex` (preserving 10pt body font) so all chapters, figures, and tables fit in strict chapter order within 25 total pages.

## 5. Preventative Action
- Keep `\FloatBarrier` and `\needspace` permanently embedded in `\fgchapter` in `nextmind-pdr.cls` so chapter-level float containment and orphan prevention are automatic.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Visual inspection of `qa/main-08.png` (Ch. 3 top), `qa/main-16.png` (Fig. 6 inside Ch. 5), `qa/main-17.png` (Ch. 6 top), `qa/main-19.png` (Ch. 7 top), and `qa/main-21.png` (Ch. 8 top) confirms zero orphan chapter banners, zero cross-chapter float drift, exact 25-page total count, and max overfull `1.60pt`.
- **Detector Signature / Verification Date:** `detector` — 2026-11-27T19:41:00+02:00
