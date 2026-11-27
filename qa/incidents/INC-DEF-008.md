# Incident Record: INC-DEF-008

- **Incident ID:** INC-DEF-008
- **Linked Defect ID:** DEF-008
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `nextmind-pdr.cls`, `sections/sec03_requirements.tex`, `draft_ch1_3.pdf` (Page 10, Table 4)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
In Table 4 (`sections/sec03_requirements.tex`, rendered on Page 10 of `draft_ch1_3.pdf` and `qa/draft_ch1_3-10.png`), standard justified narrow `p{27mm}` columns caused:
1. A line break inside the contrast ratio in `NFR-07a` (`(>= 4.5 :` / `1 text`), splitting the ratio across two lines.
2. Awkward inter-word stretching (rivers) in narrow cells (`NFR-01b`, `NFR-05`, `NFR-06`, and `NFR-07a`).

## 2. Root Cause Analysis (Why did this occur?)
- **Missing ragged-right fixed-width column helper in `nextmind-pdr.cls`:** The document class defined `L` (`>{\raggedright\arraybackslash}X`) for flexible columns, but provided no ragged-right fixed-width `P{<width>}` column type; tables therefore fell back to LaTeX's default fully justified `p{...}` column, which stretches inter-word glue in narrow widths.
- **Breakable math relation colon:** Writing `$\ge 4.5:1$` in math mode treats `:` as a relation symbol with breakable surrounding glue, allowing TeX to break the line immediately after `:`.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
- Fully justified narrow cells produce underfull/stretched spacing rather than compilation errors or overfull hboxes > 5pt, so log-only checks did not flag Table 4.
- Initial visual checks focused on page breaks and margin alignment rather than micro-typography inside narrow table cells.

## 4. Remediation Implemented
- **Files modified:** `nextmind-pdr.cls`, `sections/sec03_requirements.tex`
- **Template version bump (if applicable):** `nextmind-pdr.cls` bumped from `Working v0.3` to `Working v0.3.1` (backward-compatible).
- **Key code / text diff:**
  - `nextmind-pdr.cls:385`: Added `\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}` alongside `L` for reusable ragged-right fixed-width columns (Rule of Reproducibility).
  - `sections/sec03_requirements.tex:39,64`: Updated narrow `p{...}` columns in Table 3 and Table 4 to `P{...}`.
  - `sections/sec03_requirements.tex:76`: Wrapped contrast ratios in `NFR-07a` as `\mbox{$\ge 4.5{:}1$}` and `\mbox{$\ge 3{:}1$}` so ratios use tight ratio spacing and can never split across lines.

## 5. Preventative Action
- **Use `P{<width>}` for narrow table columns:** All fixed-width text columns in `tabularx` tables must use the class-level `P{...}` column type rather than justified `p{...}`.
- **Non-breaking ratios/units:** Wrap compact numeric ratios (e.g., `4.5:1`, `3:1`) in `\mbox{...}` with `{:}` so TeX never breaks across the colon.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Read-only inspection of `nextmind-pdr.cls:385` (`\newcolumntype{P}`), `sections/sec03_requirements.tex:39,64,76`, `draft_ch1_3.log`, and visual inspection of `qa/draft_ch1_3-09.png` and `qa/draft_ch1_3-10.png`. Confirmed: (a) Tables 3 and 4 render cleanly ragged-right with zero stretched inter-word rivers; (b) `NFR-07a` contrast ratios (`>= 4.5:1`, `>= 3:1`) stay intact on single lines via `\mbox{...}`; (c) 0 LaTeX/Biber errors/warnings, 0 overfull hbox > 5pt, and `PRD.md` / `visual_preview.pdf` / `visual_sample.pdf` untouched.
- **Detector Signature / Verification Date:** `detector` — **PASS (CLOSED)** — `2026-11-27T13:27:00+02:00`
