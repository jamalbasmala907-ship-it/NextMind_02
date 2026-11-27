# Incident Record — INC-DEF-005

- **Incident ID:** INC-DEF-005
- **Linked Defect ID:** DEF-005
- **Date:** 2026-11-26
- **Affected Deliverable / Component:** `figures/arch_integration_preview.tex` (rendered in `visual_preview.pdf`, Page 3)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
`visual_preview.log` (line 1330) reported `Overfull \hbox (13.1888pt too wide) in paragraph at lines 83--187` for Figure 1 (`figures/arch_integration_preview.tex` on Page 3), exceeding the `qa-typeset` threshold of `5pt`. Visually, the TikZ architecture diagram and its single-line bottom legend (`*Candidate protocols pending verification`) protruded ~13.2pt past the right text margin.

## 2. Root Cause Analysis (Why did this occur?)
The horizontal coordinate scale (`x=0.92cm`), node widths (`minimum width=31mm`/`35mm`/`30mm`), and wide single-line bottom legend (`\qquad` separators starting at `x=-1.5`) summed to ~17.03cm, exceeding the A4 text width (`\linewidth` $\approx$ 16.5cm) by 13.1888pt.

## 3. Missed Detection Analysis (Why earlier checks missed it?)
The initial preview compilation verified a zero exit code and visually inspected overall aesthetics without checking `visual_preview.log` for `Overfull \hbox` warnings exceeding `5pt`.

## 4. Remediation Implemented
- **Files modified:**
  - `figures/arch_integration_preview.tex` (lines 8–83)
  - Recompiled `visual_preview.pdf` (twice with `lualatex --disable-installer -interaction=nonstopmode -halt-on-error visual_preview.tex`) and re-rendered `qa/visual_preview-1..3.png` (150 DPI color) and `qa/visual_preview_gray-1..3.png` (120 DPI grayscale).
- **Template version bump (if applicable):** N/A (figure-level root-cause fix; `nextmind-pdr.cls` unchanged)
- **Key code / text diff:**
  - Adjusted horizontal scale from `x=0.92cm` to `x=0.86cm` and tightened node minimum widths (`mobile`: `26mm`, `core`: `29mm`, `fgnode`: `28mm`, `extnode`: `27mm`) while keeping all text and labels at `8.5pt` (preserving solid vs. dashed grayscale distinction).
  - Rebalanced node coordinates (`mobile` at `-0.3`, `core` at `5.2`, `cpms`/`pos` at `10.0`, `evse`/`ev` at `15.0`, vertical separation `3.85` / `1.35`), gave clean breathing room to `(1) REST / WS` (`above=5pt`) and `(3) OCPP*` (`above=5pt`), and centered `(4) ISO 15118*` on the vertical EVSE–EV arrow inside `extbox` so it never crosses the dashed enclosure border.
  - Refactored the bottom legend into a centered two-line block (`anchor=north, align=center` at `(7.35, -1.55)`) strictly within `\linewidth`.
- **Verification log result:** `visual_preview.pdf` compiled cleanly to strictly **3 pages** (`237781 bytes`), with **0 overfull hbox** on Page 3 and **0 overfull hbox > 5pt** document-wide (only `1.59998pt` on Page 2).

## 5. Preventative Action
Always grep `*.log` for `Overfull \hbox` warnings $> 5\text{pt}$ after every LuaLaTeX compilation and keep TikZ diagram horizontal extents and legends strictly within `\linewidth`.

---
## 6. Retesting Sign-off (Detector Only)
- **Status:** **PASS — CLOSED**
- [x] Retest Passed
- [x] No Regressions Introduced
- **Method:** Direct read-only inspection of `visual_preview.log:1329-1361`, `figures/arch_integration_preview.tex`, `qa/visual_preview-3.png`, and `qa/visual_preview_gray-3.png` against `DEF-005` acceptance criteria.
- **Raw Observed Evidence:** `visual_preview.log:1329-1356` shows **0 overfull hbox on Page 3** (0 overfull hbox > 5pt document-wide; only benign `1.59998pt` on Page 2) and `Output written on visual_preview.pdf (3 pages, 237781 bytes)`. Visual inspection of both color (`qa/visual_preview-3.png`) and grayscale (`qa/visual_preview_gray-3.png`) confirms zero clipping/overlap, `>= 8.5pt` labels, centered two-line legend strictly within margins, `(4) ISO 15118*` cleanly centered inside the dashed `External Context Only` box, and unambiguous solid-vs-dashed grayscale distinction.
- **Detector Signature / Verification Date:** Detector — 2026-11-26T22:27:00+02:00
