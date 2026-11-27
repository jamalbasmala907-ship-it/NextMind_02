# Incident Record: INC-DEF-010

- **Incident ID:** INC-DEF-010
- **Linked Defect ID:** DEF-010
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `nextmind-pdr.cls`, `sections/sec03_requirements.tex`, `figures/use_case_diagram.tex`, `draft_ch1_3.pdf` (Chapter 3 float placement)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Figure 2 (`\label{fig:use-case}`) is introduced in Section 3.2 (`sections/sec03_requirements.tex`) on Page 7 before Table 3 (Page 8) and Section 3.3 / Table 4 (Page 9), but floated out of section order past both tables and Section 3.3 onto an isolated trailing float page (Page 10).

## 2. Root Cause Analysis (Why did this occur?)
- **Missing float-barrier package in `nextmind-pdr.cls`:** The document class did not load `placeins`, so no `\FloatBarrier` prevented Section 3.2 floats from drifting across the `\subsection{Non-Functional Requirements}` boundary.
- **Increased diagram height after `FR-06a`/`FR-06b` split:** Adding a seventh use-case box increased Figure 2's height to `~9.5cm`, exceeding LaTeX's default `[htbp]` placement threshold on Page 7 after the Section 3.2 intro paragraphs and pushing it to the end of the float queue.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
- Build logs showed 0 errors, 0 warnings, and 0 overfull hbox > 5pt.
- Earlier checks verified that Figure 2 rendered cleanly on its own page without checking sequential section-to-float ordering across Pages 7–10.

## 4. Remediation Implemented
- **Files modified:** `nextmind-pdr.cls`, `sections/sec03_requirements.tex`, `figures/use_case_diagram.tex`
- **Template version bump (if applicable):** `nextmind-pdr.cls` bumped from `Working v0.3.1` to `Working v0.3.2` (backward-compatible).
- **Key code / text diff:**
  - `nextmind-pdr.cls:121`: Added portable float-barrier support (`\IfFileExists{placeins.sty}{\RequirePackage{placeins}}{\providecommand{\FloatBarrier}{\clearpage}}`) in Core Packages so `\FloatBarrier` works cleanly even when `placeins.sty` is absent in minimal MiKTeX installs.
  - `sections/sec03_requirements.tex:29,57`: Updated Figure 2 placement specifier to `[!htbp]` and added `\FloatBarrier` immediately before `\subsection{Non-Functional Requirements (\texttt{NFR-01a}--\texttt{NFR-07b})}`.
  - `figures/use_case_diagram.tex`: Modestly compacted vertical node pitch (`0.98cm -> 0.86cm`) and legend spacing (total height `~8.14cm` vs `~9.50cm`) while preserving all `>=9.5pt` labels and body typography untouched.

## 5. Preventative Action
- **Section-boundary float discipline:** Load `placeins` in `nextmind-pdr.cls` and place `\FloatBarrier` before major subsection transitions when a subsection contains large figures or tables, preventing floats from crossing into subsequent subsections.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Read-only inspection of `sections/sec03_requirements.tex:29,57`, `draft_ch1_3.log`, `draft_ch1_3.blg`, and visual inspection of `qa/draft_ch1_3-07.png`, `-08.png`, `-09.png`, `-10.png`, `-11.png`. Confirmed: (a) Figure 2 renders on Page 9 strictly inside Section 3.2 before `\FloatBarrier` and Section 3.3 / Table 4 (Page 10); (b) no body font shrinking or clipping; (c) 0 LaTeX/Biber errors/warnings (15/15 citekeys), 0 `Missing character` (RTL Hebrew intact on Page 11), 0 `??`/`[?]`, 0 overfull hbox > 5pt; (d) `PRD.md`, `visual_preview.pdf`, and `visual_sample.pdf` untouched.
- **Detector Signature / Verification Date:** `detector` — **PASS (CLOSED)** — `2026-11-27T14:28:00+02:00`
