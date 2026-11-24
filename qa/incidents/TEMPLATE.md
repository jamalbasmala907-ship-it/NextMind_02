# Incident Record Template

- **Incident ID:** INC-DEF-XXX
- **Linked Defect ID:** DEF-XXX
- **Date:** YYYY-MM-DD
- **Affected Deliverable / Component:** e.g., `report/template.cls`, `report/chapters/ch03_literature.tex`
- **Logged By:** Fixer
- **Reviewed & Retested By:** Detector

---

## 1. Defect Summary & Symptoms
*Brief description of what failed, including page number and verbatim excerpt.*

## 2. Root Cause Analysis (Why did this occur?)
*Deep explanation of why the defect was introduced. Examples:*
- *Prompt ambiguity in task delegation*
- *Missing macro or package in `template.cls`*
- *Unhandled edge case in BiDi engine (e.g. currency symbol with decimals)*
- *Hallucinated citation or unverified DOI*

## 3. Missed Detection Analysis (Why did earlier checks miss it?)
*Detailed explanation of why the authoring agent or initial verification failed to catch this defect before it reached Detector. Examples:*
- *Authoring agent only checked compilation exit code without visually inspecting rendered PDF*
- *Lacked automated unit test for table column widths*
- *Overfull hbox warning was ignored in compilation log*

## 4. Remediation Implemented
*Exact changes applied to resolve the defect:*
- *Files modified:*
- *Template version bump (if applicable):*
- *Key code / text diff:*

## 5. Preventative Action
*What rule, check, or skill instruction was added to guarantee this defect never reoccurs in future rounds?*

---
## 6. Retesting Sign-off (Detector Only)
- [ ] Retest Passed
- [ ] No Regressions Introduced
- **Detector Signature / Verification Date:**
