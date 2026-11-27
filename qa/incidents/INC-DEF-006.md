# Incident Record: INC-DEF-006

- **Incident ID:** INC-DEF-006
- **Linked Defect ID:** DEF-006
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `figures/use_case_diagram.tex`, `draft_ch1_3.pdf` (Page 8, Figure 2)
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Three visual and completeness defects were identified in Figure 2 (`figures/use_case_diagram.tex`, rendered on Page 8 of `draft_ch1_3.pdf` and `qa/draft_ch1_3-08.png`):
1. **Incomplete actor linkage:** `ICE / Hybrid Driver` connected only to `FR-01`..`FR-05` (omitting `FR-06` Fault Handling & User Support), whereas `EV Driver` connected to all six core use cases `FR-01`..`FR-06`.
2. **Distorted nested icon rendering:** Invoking `\fgiconev[fgEcoGreen]` (and `\fgiconfuel[fgTerracotta]`) inside TikZ actor nodes nested a `tikzpicture` inside an outer `tikzpicture`, causing outer TikZ styling/options to leak into the inner icon and distort the EV bolt into a crosshair artifact.
3. **Overlapping horizontal arrow segments:** Both terracotta (`fuellink`) and green (`evlink`) orthogonal connectors terminated at identical `fr1.west`..`fr5.west` anchor points, causing the horizontal segments and arrowheads to overlap directly.

## 2. Root Cause Analysis (Why did this occur?)
- **Omitted `FR-06` edge:** Manual enumeration of `\draw[fuellink]` paths missed the sixth use case (`fr6.west`).
- **Nested `tikzpicture` anti-pattern:** Inline icon macros (`\fgiconfuel`, `\fgiconev`) in `nextmind-pdr.cls` are implemented as standalone `\begin{tikzpicture}...\end{tikzpicture}` environments intended for body text/banners, not for embedding inside another TikZ node where TikZ option inheritance corrupts coordinate transforms and path styles.
- **Unstaggered target anchors:** Orthogonal `|-` connectors from two parallel actor buses targeted the exact same `.west` anchor without a vertical `yshift` offset.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
- The diagram compiled with zero LaTeX errors and zero overfull hboxes, so automated build-log checks passed.
- Earlier authoring verification did not perform a zoomed visual inspection of the rendered Page 8 PNG for icon geometry distortion, overlapping connector tips, or edge-by-edge traceability against all six functional requirements (`FR-01`..`FR-06`).

## 4. Remediation Implemented
- **Files modified:** `figures/use_case_diagram.tex`
- **Template version bump (if applicable):** None (diagram-local fix)
- **Key code / text diff:**
  - Replaced nested `\fgiconfuel` and `\fgiconev` calls inside `(ice)` and `(ev)` nodes with native TikZ paths drawn directly in the outer `tikzpicture` inside scoped coordinate shifts (`\begin{scope}[shift={($(ice.north)+(-0.18cm,-0.46cm)$)}, scale=0.22]` and `\begin{scope}[shift={($(ev.north)+(-0.18cm,-0.46cm)$)}, scale=0.22]`), reserving clean vertical header space inside the actor boxes.
  - Added the missing `ICE / Hybrid Driver -> FR-06` connector (`\draw[fuellink] (ice.east) -- ++(0.45,0) |- ([yshift=2.8pt]fr6.west);`).
  - Staggered horizontal entry anchors for all six use cases: `fuellink` enters at `([yshift=2.8pt]fr1.west)`..`([yshift=2.8pt]fr6.west)` and `evlink` enters at `([yshift=-2.8pt]fr1.west)`..`([yshift=-2.8pt]fr6.west)`.
  - Preserved all `>=9.5pt` labels, `Proposed Core Interface (Solid)` vs. `External System Context (Dashed)` legend wording, and `0` overfull hbox.

## 5. Preventative Action
- **No nested `tikzpicture` rule:** Never invoke inline TikZ icon macros (`\fgiconfuel`, `\fgiconev`, `\fgiconcore`) inside a TikZ node; draw native TikZ paths/scopes or `pic` definitions in the outer `tikzpicture` instead.
- **Dual-bus anchor staggering & traceability check:** Whenever multiple actors connect to shared use-case nodes, stagger entry anchors with explicit `yshift` offsets and verify 1:1 edge completeness against the requirements matrix on rendered PNGs (color and grayscale).

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Read-only inspection of `figures/use_case_diagram.tex:60-105`, `draft_ch1_3.log`, `draft_ch1_3.blg`, and visual inspection of `qa/draft_ch1_3-08.png` and `qa/draft_ch1_3_gray-08.png`. Confirmed: (a) `ICE / Hybrid Driver` connects to all 6 core use cases `FR-01`–`FR-06`; (b) both fuel dispenser and EV lightning bolt icons render crisply via native TikZ scopes with zero crosshair distortion; (c) terracotta (`+2.8pt`) and green (`-2.8pt`) horizontal arrow segments are cleanly separated with zero overlap in both color and grayscale; (d) 0 LaTeX/Biber errors/warnings and 0 overfull hbox > 5pt.
- **Detector Signature / Verification Date:** `detector` — **PASS (CLOSED)** — `2026-11-27T13:27:00+02:00`
