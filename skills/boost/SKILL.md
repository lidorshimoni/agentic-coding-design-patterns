---
name: boost
description: Deep cognitive deliberation using Tree-of-Thoughts and multi-perspective expert debate before tackling complex, high-risk tasks.
version: 1.0.0
triggers:
  - "/boost"
  - "deep thinking"
  - "deliberate trade-offs"
  - "multi-perspective analysis"
---

# Boost: Tree-of-Thoughts & Cognitive Deliberation Pattern

## Intent
Before executing high-risk, irreversible, or highly complex engineering operations, pause rapid execution and conduct deep, multi-perspective deliberation to explore divergent paths, uncover non-obvious traps, and synthesize the highest-leverage solution.

## Theoretical Foundation
Synthesizes the **Tree of Thoughts (ToT)** framework (Yao et al., 2023) and **Society of Mind / Multi-Persona Debate** (Minsky, 1986; Du et al., 2023). By forcing deliberation across orthogonal engineering priorities (velocity, correctness, security, operability), agents avoid premature convergence on naive solutions.

## Operational Workflow

### Step 1: Deliberation Setup
Identify the core technical challenge, unknowns, and critical constraints.

### Step 2: Multi-Persona Perspective Synthesis
Examine the problem through four distinct senior engineering lenses:

1. **The Principal System Architect**:
   - Focus: Long-term maintainability, clean separation of concerns, abstraction boundaries, extensibility.
   - Question: *How does this change impact the system architecture 12 months from now?*

2. **The Adversarial Security Auditor**:
   - Focus: Attack surfaces, threat vectors, privilege escalation, injection risks, secret exposure.
   - Question: *How could a malicious actor exploit this design or its dependencies?*

3. **The Production SRE / Operability Lead**:
   - Focus: Observability, telemetry, latency, resource consumption, partial outages, failover recovery.
   - Question: *How will we know this is failing in production at 3:00 AM, and how do we roll back?*

4. **The Pragmatic Staff Hacker**:
   - Focus: Velocity, simplicity, avoiding over-engineering, YAGNI (You Aren't Gonna Need It), minimal diff.
   - Question: *What is the simplest 20% effort that yields 80% of the value without unnecessary bloat?*

### Step 3: Comparative Decision Matrix
Compare 2 to 3 candidate strategies against the perspectives:

| Evaluation Criteria | Strategy A: Minimalist | Strategy B: Full Refactor | Strategy C: Adapter Pattern |
| :--- | :--- | :--- | :--- |
| **Correctness & Robustness** | High | Very High | High |
| **Blast Radius / Risk** | Very Low | High | Low |
| **Implementation Complexity** | Low | High | Medium |
| **Operability & Observability**| Medium | High | High |

### Step 4: Synthesis & Execution Plan
1. Formulate the consensus recommendation combining the best elements of each perspective.
2. Explicitly document trade-offs accepted.
3. Output the optimized, de-risked implementation plan and proceed to execution.
