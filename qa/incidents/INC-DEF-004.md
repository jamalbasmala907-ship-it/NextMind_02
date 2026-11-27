# Incident Record — INC-DEF-004

- **Incident ID:** INC-DEF-004
- **Linked Defect ID:** DEF-004
- **Date:** 2026-11-26
- **Affected Deliverable / Component:** `bib/references.bib`
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
Seven entries in `bib/references.bib` (`iso15118_2_2014`, `iso15118_20_2022`, `w3c2023wcag22`, `iso29148_2018`, `iso42010_2022`, `eu2016gdpr`, `israel1981ppl`) used non-standard `biblatex-ieee` entry types (`@standard` and `@legislation`), which fall back to `@misc` in `biblatex` `style=ieee` and risk silently dropping `number` (ISO identifiers) and `journaltitle` (`Official Journal of the European Union`) during `biber`/`lualatex` rendering.

## 2. Root Cause Analysis (Why did this occur?)
Semantic BibTeX entry types (`@standard`, `@legislation`) were authored without verifying whether `biblatex-ieee` defines dedicated drivers for those types.

## 3. Missed Detection Analysis (Why earlier checks missed it?)
The bibliography was authored before full `biber` + `lualatex` compilation with `style=ieee` was executed to inspect rendered ISO numbers and EU Official Journal metadata.

## 4. Remediation Implemented
- **Files modified:** `bib/references.bib` (lines 41, 51, 97, 107, 117, 127, 136)
- **Template version bump (if applicable):** N/A
- **Key code / text diff:**
  - Converted the five `@standard` entries (`iso15118_2_2014`, `iso15118_20_2022`, `w3c2023wcag22`, `iso29148_2018`, `iso42010_2022`) to `@manual`, preserving all `author`, `title`, `organization`, `number`, `date`, `url`, `urldate`, and `note` fields.
  - Converted the two `@legislation` entries (`eu2016gdpr`, `israel1981ppl`) to `@misc`, replacing `journaltitle` with `howpublished = {Official Journal of the European Union}` on `eu2016gdpr` so `biblatex-ieee` renders the publication venue without dropping fields. All verified dates, URLs, and notes were preserved intact.

## 5. Preventative Action
Restrict `bib/references.bib` entries to standard `biblatex-ieee` supported types (`@article`, `@book`, `@inproceedings`, `@manual`, `@report`, `@techreport`, `@online`, `@misc`) and verify rendered output in `biber`/`lualatex` logs.

---
## 6. Retesting Sign-off (Detector Only)
- **Status:** **PASS — CLOSED**
- [x] Retest Passed
- [x] No Regressions Introduced
- **Method:** Direct read-only inspection of `bib/references.bib` (lines 41, 51, 97, 107, 117, 127, 136) against `DEF-004` acceptance criteria.
- **Raw Observed Evidence:** All five `@standard` entries (`iso15118_2_2014`, `iso15118_20_2022`, `w3c2023wcag22`, `iso29148_2018`, `iso42010_2022`) converted to `@manual`; both `@legislation` entries (`eu2016gdpr`, `israel1981ppl`) converted to `@misc`, with `howpublished = {Official Journal of the European Union}` on `eu2016gdpr` (line 130). All 17 entries now use standard `biblatex-ieee` types.
- **Detector Signature / Verification Date:** Detector — 2026-11-26T19:50:00+02:00
