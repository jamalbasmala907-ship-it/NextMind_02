# Multi-Agent Mesh Operations & Launch Guide
**Team:** NextMind  
**Project:** Fuel&Go Preparatory Report (Assignment 02)  

---

## 1. Overview
Team NextMind operates with 5 specialized agent sessions connected over the `agymesh` local hub:
- **Master (`master`)**: Orchestrates goals and manages the board.
- **Research (`research`)**: Literature, market sizing, citations.
- **Design (`design`)**: LaTeX architecture, CLS, Python graphics.
- **Detector (`detector`)**: Independent QA, defect logging, retesting.
- **Fixer (`fixer`)**: Defect remediation, incident records.

---

## 2. Security & Permission Policy
- **Preserve Permission Checks (Mandatory)**:
  - Do NOT run with `--dangerously-skip-permissions`.
  - Permission checks ensure the human operator retains oversight over file system modifications and execution boundaries.
- **Safe Execution Path**:
  - The local python virtual environment executable is located at:
    `.\agy-multi-agent-mesh\.venv\Scripts\python.exe`
  - Mesh operations run strictly via project-local configuration (`config/setup.json`).

---

## 3. Documented Commands (For Future Execution)

### Step 1: Start Hub and Initialize Instructions
```powershell
# In the NextMind-ex02 root directory:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json init
```

### Step 2: Launch Mesh Sessions
> [!IMPORTANT]
> Do NOT execute these commands now. Run them only when instructed to start the multi-agent session.

To launch the full team in separate interactive windows:
```powershell
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json up --with-master
```

To launch specific worker agents individually:
```powershell
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json launch research design
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json launch detector fixer
```

### Step 3: Verify Mesh Connectivity
From the `master` session or a diagnostic terminal:
```powershell
# Check online peers:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json peers

# Health check (all peers must reply PONG with PID):
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json ping-all --name master

# Full 5x5 reachability matrix:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json mesh-check --name master
```

### Step 4: Shared Board & Task Delegation
```powershell
# Add milestone tasks to the shared TODO board:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json todo-add --name master --title "Research: 15 IEEE citations" --title "Design: draft ch01_intro.tex"

# Worker claims next task:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json todo-claim --name research

# Worker marks task completed with note:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json todo-done --name research --id T001 --note "15 papers added to references.bib"

# Inspect board progress:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config --team agents/team.json todo-list
```

### Step 5: Shutdown Mesh
```powershell
# Close agent windows, then shutdown the background hub:
& ".\agy-multi-agent-mesh\.venv\Scripts\python.exe" -m agymesh --config-dir config down
```
