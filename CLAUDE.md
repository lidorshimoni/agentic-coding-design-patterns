# Claude Code Project Guidelines

## Available Slash Commands
- `/boost`: Deep cognitive deliberation using Tree-of-Thoughts and multi-perspective expert debate before tackling complex, high-risk tasks.
- `/code-review`: Adversarial multi-lens code review. Evaluates pull requests or git diffs across correctness, security, concurrency, performance, and maintainability.
- `/goal`: Autonomous long-running execution loop. Drives complex objectives to completion using step budgets, empirical verification oracles, and state checkpointing.
- `/grill-me`: Interactive requirements elicitation interview. Walks down each branch of the design tree, resolving dependencies between decisions one-by-one with recommended options.
- `/grill-me-with-docs`: Documentation-grounded requirements interview. Retrieves official documentation, API references, or web sources to validate architectural options before presenting choices.
- `/implement`: Executes tasks using Test-Driven Development (TDD) and atomic commits. Enforces Red-Green-Refactor cycles and regression verification.
- `/retro-learn`: Post-session reflection and continual learning. Extracts lessons from errors, user corrections, and project patterns to update persistent harness rules.
- `/schedule-loop`: Idempotent periodic reconciliation loop pattern for recurring maintenance, health checks, dependency monitoring, and automated triage.
- `/self-critic`: Reflexion and verbal invariant verification pattern. Evaluates proposed actions, plans, or diffs against edge cases and invariants before execution.
- `/teamwork`: Hierarchical multi-agent coordinator-subagent orchestration pattern for parallelized, context-isolated task execution.
- `/to-spec`: Transforms requirements, interview transcripts, or raw ideas into an authoritative, RFC-grade technical specification and PRD.
- `/to-tickets`: Decomposes a technical specification into an executable Directed Acyclic Graph (DAG) of atomic, verifiable tickets with strict acceptance criteria.
- `/visualize`: Architecture and flow visualization pattern. Generates standardized, syntactically valid Mermaid and C4 diagrams for system designs, data flows, and state machines.

## Agentic Coding Best Practices
- Always explore the codebase first before asking the user.
- Enforce TDD (Red-Green-Refactor) and atomic commits.
- Adhere to strict task decomposition and acceptance criteria.
