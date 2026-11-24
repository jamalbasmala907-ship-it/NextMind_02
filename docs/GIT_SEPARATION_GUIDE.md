# Git Repository Separation Guide
**Team:** NextMind  
**Project:** NextMind-ex02 (Fuel&Go Preparatory Report)  
**Date:** November 2026  

---

## 1. Context & Objective
The `NextMind-ex02` workspace currently includes a cloned copy of the lecturer's utility repository:
```text
NextMind-ex02/
├── agents/                  # Team NextMind agent definitions & skills
├── config/                  # Local agymesh launch configuration
├── docs/                    # Architectural guides & checklists
├── evidence/                # Verified research sources & data
├── figures/                 # Report figures and plots
├── materials/               # Lecturer assignment materials & background PRD
├── prompts/                 # Exact prompt logs
├── python/                  # Visualization generation scripts
├── qa/                      # Defect logs, incident records, audit reports
├── report/                  # LaTeX sources, custom CLS, BibTeX, final PDF
└── agy-multi-agent-mesh/    # LECTURER'S UTILITY REPOSITORY (External tool)
```

The lecturer's repository `agy-multi-agent-mesh` has its own `.git`, `.venv`, dependencies (`uv.lock`), and internal documentation.  
**Objective:** Maintain a strict boundary between the lecturer's utility engine and Team NextMind's future assignment submission repository, ensuring:
1. No accidental commits or modifications to the lecturer's repository.
2. No nested submodule complications or git repository conflicts.
3. A clean, independent student submission conforming to the assignment rubric.
4. **Strict Compliance Directive**: Do NOT initialize Git, commit, push, or publish anything at this stage.

---

## 2. Why the Lecturer's Repository Must Remain Separate
1. **Tool vs. Deliverable**: `agymesh` is runtime multi-agent infrastructure provided by the lecturer (like Python, LuaLaTeX, or Git itself). It is not part of the Fuel&Go Preparatory Report deliverable.
2. **Copyright & Integrity**: `agy-multi-agent-mesh` is copyrighted by Dr. Yoram Segal / Gal Technologies AI Ltd. Modifying or submitting it as student work violates academic and licensing guidelines.
3. **Repository Cleanliness**: The lecturer repository contains virtual environments (`.venv`), lockfiles, caches, and test suites totaling tens of megabytes that do not belong in the student submission.

---

## 3. Separation Strategy: Clean Isolation

When the user decides to initialize Git for Assignment 02 submission, the following separation strategy must be followed:

### Strategy Option A: Strict `.gitignore` Exclusion (Recommended)
Keep `agy-multi-agent-mesh` in place on the local PC for running the mesh, but explicitly ignore it from the NextMind Git tree:

Create a root `.gitignore` containing:
```gitignore
# ==============================================================================
# Lecturer Utility Mesh Repository (DO NOT TRACK / DO NOT COMMIT)
# ==============================================================================
/agy-multi-agent-mesh/
.mesh/
*.ipc

# ==============================================================================
# LaTeX Compilation Artifacts
# ==============================================================================
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.run.xml
*.synctex.gz
*.toc
*.lof
*.lot

# ==============================================================================
# Python & Environment Artifacts
# ==============================================================================
__pycache__/
*.py[cod]
*$py.class
.venv/
env/
venv/
*.env

# ==============================================================================
# OS & Editor Artifacts
# ==============================================================================
.DS_Store
Thumbs.db
.vscode/
.idea/
```

### Strategy Option B: Standalone External Tool Placement
Alternatively, `agy-multi-agent-mesh` can be moved to an external sibling directory (e.g., `../agy-multi-agent-mesh`) or installed globally. The local `config/setup.json` will then point to its python executable via absolute or sibling relative path.

---

## 4. Student Submission Deliverables (What Gets Submitted)
Per Assignment 02 instructions (`BIU26-27-A-ex02-pdf-via-LaTex-print.pdf` p. 4, Sec 6):
The student submission repository must contain **only**:
1. **Source Files**:
   - `report/main.tex`
   - `report/template.cls`
   - `report/references.bib`
   - `report/chapters/*.tex`
2. **Documentation**:
   - `README.md` (Project overview, build instructions, team details)
   - `PRD.md` (Product Requirements Document for Assignment 02 report)
   - `PLAN.md` (Work breakdown and chapter architecture)
   - `TODO.md` (Atomic milestone checklist)
3. **The Final Report Deliverable**:
   - `report/report.pdf` (The compiled, defect-free PDF)
4. **Skills & QA Artifacts**:
   - `agents/master/SKILL.md`
   - `agents/research/SKILL.md`
   - `agents/design/SKILL.md`
   - `agents/detector/SKILL.md`
   - `agents/fixer/SKILL.md`
   - `qa/defects.json` and `qa/DEFECTS.md`
   - `qa/incidents/` (All incident records)
   - `python/` (Visualization scripts)
   - `figures/` (Generated plots and diagrams)
   - `prompts/` (Prompt engineering logs)

---

## 5. Explicit Directive for Current Turn
- **DO NOT** run `git init`.
- **DO NOT** run `git add` or `git commit`.
- **DO NOT** run `git push` or publish to GitHub.
- Any git initialization and remote setup will be performed only when explicitly instructed by the user in future steps.
