# /self-critic - Reflexion and verbal invariant verification pattern. Evaluates proposed actions, plans, or diffs against edge cases and invariants before execution.

Run the following workflow instructions for the provided input: $ARGUMENTS

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

---

## Citations & Provenance
1. **Reflexion**: Shinn, N., Cassano, F., Labash, B., Gopinath, A., Narasimhan, K., & Yao, S. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. Advances in Neural Information Processing Systems (NeurIPS 2023). arXiv:2303.11366.
2. **Self-Refine**: Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao, L., Wiegreffe, S., ... & Clark, P. (2023). *Self-Refine: Iterative Refinement with Self-Feedback*. NeurIPS 2023. arXiv:2303.17651.
3. **Large Language Models Cannot Self-Correct Without External Feedback**: Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2023). ICLR 2024. arXiv:2310.01798.
