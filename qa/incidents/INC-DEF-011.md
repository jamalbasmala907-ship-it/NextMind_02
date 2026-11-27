# Incident Record: INC-DEF-011

- **Incident ID:** INC-DEF-011
- **Linked Defect ID:** DEF-011
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `nextmind-pdr.cls` (`\fgchapter`), `main.pdf` (p. 3 ToC)
- **Logged By:** Fixer / Design
- **Reviewed & Retested By:** Detector (PASS — 2026-11-27)

---

## 1. Defect Summary & Symptoms
In the initial `main.pdf` build, the Table of Contents (Page 3) listed Chapter 4 on Page 8 (actual rendered banner: Page 11) and Chapter 8 on Page 19 (actual rendered banner: Page 20).

## 2. Root Cause Analysis (Why did this occur?)
`\fgchapter` in `nextmind-pdr.cls` executed `\refstepcounter{section}` and `\addcontentsline{toc}{section}{...}` *before* flushing pending floats (`\FloatBarrier`) or reserving vertical space (`\needspace`) for the chapter banner. When LaTeX pushed the chapter banner to the next page after pending floats, the ToC entry captured the earlier page number.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
Automated log checks verified zero undefined references (`??`) and zero build errors, but did not cross-check ToC page numbers against the actual rendered PNG page of each chapter banner.

## 4. Remediation Implemented
- **Files modified:** `nextmind-pdr.cls` (bumped to `Working v0.3.3`), `main.tex`
- **Key code / text diff:**
  - `nextmind-pdr.cls`: Updated `\fgchapter` to execute `\FloatBarrier` and `\needspace{7\baselineskip}` *prior* to `\refstepcounter{section}`, `\label`, and `\addcontentsline{toc}{section}`, ensuring every ToC chapter page number matches its rendered chapter banner page.
  - `main.tex`: Calibrated page geometry and vertical spacing cleanly (preserving 10pt body text) to maintain exact 25-page total pagination.

## 5. Preventative Action
- Enforce `\FloatBarrier` + `\needspace` inside `\fgchapter` at the document-class level (Rule of Reproducibility) so all future reports inherit accurate ToC page synchronization.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Verified `main.log` (`25 pages, 838144 bytes`, 0 errors, max overfull `1.60pt`), `main.toc`, and visual inspection of `qa/main-03.png`, `qa/main-08.png`, `qa/main-11.png`, `qa/main-17.png`, `qa/main-19.png`, `qa/main-21.png`, `qa/main-24.png`, and `qa/main-25.png`. Every chapter and back-matter ToC page number matches its rendered PDF page 100% (Ch. 3=p.8, Ch. 4=p.11, Ch. 6=p.17, Ch. 7=p.19, Ch. 8=p.21, Refs=p.24, Appendices=p.25).
- **Detector Signature / Verification Date:** `detector` — 2026-11-27T19:41:00+02:00
