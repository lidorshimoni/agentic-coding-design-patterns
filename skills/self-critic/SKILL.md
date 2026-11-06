---
name: self-critic
description: Reflexion and verbal invariant verification pattern. Evaluates proposed actions, plans, or diffs against edge cases and invariants before execution.
version: 1.0.0
triggers:
  - "/self-critic"
  - "critique yourself"
  - "verify before acting"
  - "audit own diff"
---

# Self-Critic: Reflexion & Verbal Invariant Verification Pattern

## Intent
Intercept an agent's plan, tool call, or code diff immediately before execution, subjecting it to an objective internal audit to catch hallucinations, broken invariants, unhandled edge cases, and unintended side effects.

## Theoretical Foundation
Rooted in the **Reflexion** framework (Shinn et al., 2023) and **Self-Refine** (Madaan et al., 2023). Language models suffer from forward-generation bias, where early minor errors compound into catastrophic failures. Forcing an explicit, detached self-criticism step breaks the error chain and dramatically raises solution accuracy.

## Operational Workflow

### Step 1: Pre-Execution Interception
Before executing a significant change (e.g. running destructive shell commands, applying a large diff, or finalizing an architectural plan), pause and run the Self-Critic protocol.

### Step 2: The Invariant & Hallucination Audit
Inspect the proposed action against five foundational sanity checks:

1. **Existence & Grounding Check**:
   - Are any invoked imports, files, classes, CLI flags, or API methods fabricated or hallucinated?
   - *Verification*: Confirm each referenced symbol exists in the codebase or official documentation.

2. **Invariant & Boundary Audit**:
   - What happens with empty inputs (`[]`, `""`, `None`, `0`, `NaN`)?
   - What happens with maximal or overflow inputs (unbounded lists, large files)?
   - Are idempotency and state boundaries respected?

3. **Silent Side Effect Check**:
   - Does this change accidentally alter global state, modify shared configuration, delete untracked files, or bypass authentication?

4. **Regression & Blast Radius**:
   - Will this change break downstream callers or external consumers of this interface?
   - Is backward compatibility preserved?

5. **Simplicity / Occam's Razor**:
   - Is this the simplest possible solution?
   - Does it introduce gratuitous complexity, unnecessary dependencies, or redundant abstractions?

### Step 3: Verbal Evaluation & Score
Produce a concise internal audit:
- **Flaws Detected**: List any issues identified.
- **Verdict**:
  - `PASSED`: Plan/diff is watertight; proceed with execution.
  - `REVISE`: Flaws found; detail exact adjustments needed and refine the action before executing.
