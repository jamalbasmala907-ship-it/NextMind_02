# Incident Record: INC-DEF-013

- **Incident ID:** INC-DEF-013
- **Linked Defect ID:** DEF-013
- **Date:** 2026-11-27
- **Affected Deliverable / Component:** `figures/safety_trust_boundary.tex` (Figure 8), `main.pdf`
- **Logged By:** Fixer / Design
- **Reviewed & Retested By:** Detector (PASS — 2026-11-27)

---

## 1. Defect Summary & Symptoms
In `figures/safety_trust_boundary.tex` (Figure 8), three visual collisions occurred: (1) the dashed `sdk -> psp` arrow cut through the `Bay Verification` box; (2) the `orch <-> psp` arrow overlapped the `Z3: External PSP Vault` header; and (3) the `fcc -> hwfuel` arrow cut through the `No Safety Override` label.

## 2. Root Cause Analysis (Why did this occur?)
Direct orthogonal TikZ paths (`|-` and `--`) were routed across occupied node coordinates without intermediate waypoints or offset label anchors.

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
TikZ compiles overlapping paths and labels with zero warnings; collisions are only detectable via rendered PNG visual inspection.

## 4. Remediation Implemented
- **Files modified:** `figures/safety_trust_boundary.tex`
- **Key code / text diff:**
  - Rerouted `sdk -> psp` from `sdk.east` cleanly through the gutter between Z1 and Z3 around `Bay Verification`.
  - Repositioned the `Z3: External PSP Vault (PCI DSS CDE)` label to the bottom of Z3 so `orch <-> psp` crosses cleanly without overlapping text.
  - Shifted the `fcc -> hwfuel` arrow to the left side of the Z4 column and placed `No Safety Override` cleanly to its right with zero overlap.

## 5. Preventative Action
- Route inter-zone TikZ arrows through dedicated inter-zone gutters and verify every diagram on rendered 150 DPI PNGs before QA handoff.

---
## 6. Retesting Sign-off (Detector Only)
- [x] Retest Passed
- [x] No Regressions Introduced
- **Retest Method & Observed Evidence:** Visual inspection of `qa/main-19.png` (Page 19, Figure 8) confirms all three collisions are resolved: `sdk -> psp` dashed arrow routes cleanly through the Z1–Z2 gutter around `Bay Verification`; `Z3: External PSP Vault (PCI DSS CDE)` sits cleanly at the bottom of Z3 with zero overlap from `orch <-> psp`; `fcc -> hwfuel` routes cleanly on the left with `NFR-06 Hardware Isolation` and `No Safety Override` completely unobstructed.
- **Detector Signature / Verification Date:** `detector` — 2026-11-27T19:41:00+02:00
