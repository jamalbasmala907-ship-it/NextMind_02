# Incident Record: INC-DEF-009

- **Incident ID:** INC-DEF-009
- **Linked Defect ID:** DEF-009
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `figures/use_case_diagram.tex`, `draft_ch1_3.pdf` (Figure 2)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Regression of `DEF-006`: In `figures/use_case_diagram.tex` (lines 62–68), nested `\fgiconfuel[fgTerracotta]` and `\fgiconev[fgEcoGreen]` calls were reintroduced inside the `(ice)` and `(ev)` TikZ actor nodes during the `FR-06a`/`FR-06b` diagram update. Visual inspection of `qa/draft_ch1_3-10.png` and `qa/draft_ch1_3_gray-10.png` confirmed that the EV Driver icon again rendered as a distorted crosshair artifact instead of a clean lightning bolt. Additionally, multiple dashed `extlink` arrows entered `pos.west` (and `cpms.west` / `psp.west`) at identical y-coordinates, risking visual ambiguity in the dashed pattern.

## 2. Root Cause Analysis (Why did this occur?)
- **Regression overwrite during diagram update:** When `figures/use_case_diagram.tex` was edited to add the `FR-06a`/`FR-06b` split, the actor node definitions reverted to calling the inline `\fgiconfuel` and `\fgiconev` macros (which open nested `\begin{tikzpicture}...\end{tikzpicture}` environments) rather than preserving the native outer-picture scoped TikZ paths established in `INC-DEF-006`.
- **Unstaggered external-system entry anchors:** Multiple orthogonal `|-` dashed connectors converged onto the same `.west` anchor of `pos`, `cpms`, and `psp`.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
- Nested `tikzpicture` environments compile without LaTeX errors or warnings, so build-log verification passed.
- The `FR-06a`/`FR-06b` update was not followed by a zoomed visual regression check of the actor icons against `INC-DEF-006` preventative rules.

## 4. Remediation Implemented
- **Files modified:** `figures/use_case_diagram.tex`
- **Template version bump (if applicable):** None for DEF-009 (see `INC-DEF-010` for `nextmind-pdr.cls` v0.3.2)
- **Key code / text diff:**
  - Removed nested `\fgiconfuel[fgTerracotta]` and `\fgiconev[fgEcoGreen]` from `(ice)` and `(ev)` nodes.
  - Restored native TikZ fuel-pump and EV-bolt icons drawn directly in the outer `tikzpicture` inside scoped coordinate shifts (`\begin{scope}[shift={($(ice.north)+(-0.18cm,-0.46cm)$)}, scale=0.22]` and `\begin{scope}[shift={($(ev.north)+(-0.18cm,-0.46cm)$)}, scale=0.22]`).
  - Staggered dashed `extlink` entry anchors into `pos.west` (`yshift=+6pt,+2pt,-2pt,-6pt`), `cpms.west` (`yshift=+6pt,+2pt,-2pt,-6pt`), and `psp.west` (`yshift=+4pt,0pt,-4pt`) so dashed segments remain visually unambiguous.
  - Preserved all `>=9.5pt` labels, `FR-06a (Must)` / `FR-06b (Should)` split, staggered terracotta/green driver arrows, and `0` overfull hbox.

## 5. Preventative Action
- **Strict no-nested-`tikzpicture` gate on diagram edits:** Any future edit to `figures/*.tex` must grep for `\fgicon` inside `\begin{tikzpicture}` blocks and reject nested `tikzpicture` calls before handoff.
- **Anchor-staggering check:** Verify that multi-edge targets on both left and right diagram buses use distinct `yshift` anchors.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Read-only inspection of `figures/use_case_diagram.tex:62-127`, `draft_ch1_3.log`, `draft_ch1_3.blg`, and visual inspection of `qa/draft_ch1_3-09.png` and `qa/draft_ch1_3_gray-09.png`. Confirmed: (a) native TikZ fuel dispenser and EV lightning bolt icons render crisply with zero crosshair distortion; (b) staggered dashed external arrows into Forecourt/POS Gateway, EV CPMS, and PSP are unambiguous in color and grayscale; (c) `>=9.5pt` labels and `FR-06a (Must)` / `FR-06b (Should)` split intact; (d) 0 LaTeX/Biber errors/warnings and 0 overfull hbox > 5pt.
- **Detector Signature / Verification Date:** `detector` — **PASS (CLOSED)** — `2026-11-27T14:28:00+02:00`
