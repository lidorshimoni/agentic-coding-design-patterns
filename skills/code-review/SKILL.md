---
name: code-review
description: Adversarial multi-lens code review. Evaluates pull requests or git diffs across correctness, security, concurrency, performance, and maintainability.
version: 1.0.0
triggers:
  - "/code-review"
  - "review code"
  - "review PR"
  - "audit changes"
---

# Code-Review: Adversarial Multi-Lens Code Review Pattern

## Intent
Conduct a rigorous, senior-staff-level architectural and security code review on proposed changes or git diffs before merging. Surface hidden bugs, performance bottlenecks, race conditions, and architectural drift.

## Theoretical Foundation
Rooted in formal inspection methods (Fagan Inspection) and Google's Engineering Practices on Code Review. Instead of vague approval, the reviewer adopts an adversarial posture, methodically examining the diff through specialized analytical lenses.

## Operational Workflow

### Step 1: Diff & Scope Extraction
1. Inspect the git diff against the target branch (e.g. `main` or `master`):
   \`\`\`bash
   git diff main...HEAD
   \`\`\`
2. Check git status to ensure working directory is clean.
3. Identify all modified, added, and deleted files.

### Step 2: Multi-Lens Evaluation Matrix
Evaluate the changes systematically against six core dimensions:

| Lens | Focus Areas | Key Verification Questions |
| :--- | :--- | :--- |
| **1. Correctness & Invariants** | Logic, edge cases, contracts, nullability | Does the code violate any domain invariants? Are boundary conditions handled (0, empty, max limits)? |
| **2. Security & Safety** | OWASP Top 10, sanitization, secrets, permissions | Are user inputs sanitized? Are SQL queries parameterized? Are sensitive values exposed in logs? |
| **3. Concurrency & State** | Race conditions, deadlocks, shared mutable state | Is mutable state thread-safe? Are asynchronous operations awaited properly? Are DB transactions atomic? |
| **4. Performance & Complexity** | Time/space complexity, N+1 queries, memory leaks | What is the algorithmic complexity ($O(N)$ vs $O(N^2)$)? Are database queries indexed? Are streams/buffers closed? |
| **5. Resilience & Errors** | Graceful degradation, circuit breakers, error typing | Are errors caught with typed exceptions? Is diagnostic context logged? Is fallback behavior defined? |
| **6. Testing & Coverage** | Regression tests, mocking boundaries, flakiness | Are negative paths and failure modes tested? Are unit tests decoupled from implementation details? |

### Step 3: Findings Classification & Reporting
Group all observations using standard severity tags:
- `[BLOCKER]`: Critical bug, security vulnerability, data loss risk, or broken contract. Must be resolved before merge.
- `[WARNING]`: Suboptimal pattern, performance concern, or missing edge case test. Strong recommendation.
- `[NIT]`: Minor styling, naming, or readability improvement. Optional.
- `[PRAISE]`: Commend particularly elegant, robust, or clever implementations.

### Step 4: Line-by-Line Remediation Diff
For every `[BLOCKER]` or `[WARNING]`, provide:
1. Exact file path and line number range.
2. Root cause explanation of the risk.
3. Drop-in replacement code snippet.

---

## Citations & Provenance
1. **Formal Inspection Methodology**: Fagan, M. E. (1976). *Design and code inspections to reduce errors in program development*. IBM Systems Journal, 15(3), 182-211.
2. **Google Engineering Practices**: Google Engineering (2020). *Google's Code Review Developer Guide* (https://google.github.io/eng-practices/review/).
3. **Application Security Standards**: OWASP Foundation (2021). *OWASP Top Ten Web Application Security Risks*.
4. **Automated Static Analysis Principles**: McConnell, S. (2004). *Code Complete (2nd ed.)*. Microsoft Press.

