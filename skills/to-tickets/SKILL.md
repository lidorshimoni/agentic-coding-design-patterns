---
name: to-tickets
description: Decomposes a technical specification into an executable Directed Acyclic Graph (DAG) of atomic, verifiable tickets with strict acceptance criteria.
version: 1.0.0
triggers:
  - "/to-tickets"
  - "break down into tickets"
  - "generate task DAG"
---

# To-Tickets: DAG Task Decomposition Pattern

## Intent
Decompose an approved technical specification into an ordered, dependency-aware backlog of atomic, independently verifiable implementation tickets.

## Theoretical Foundation
Rooted in Directed Acyclic Graphs (DAG), Work Breakdown Structures (WBS), and Behavior-Driven Development (BDD). For autonomous agents, large tasks fail due to context overflow and error compounding. Breaking work into atomic tickets with explicit verification criteria bounds agent reasoning to a single verifiable unit of work.

## Ticket Schema & Ordering Rules

### Decomposition Principles
1. **Atomicity**: Each ticket represents a single logical unit of change that can be implemented, tested, and committed in one pass.
2. **Explicit Dependency DAG**: Every ticket lists its explicit upstream dependencies (`blocked_by`).
3. **Automated Verification**: Every ticket MUST include a deterministic verification command (e.g., test command, linter, or health check script).
4. **File Scope**: Every ticket defines the exact files and symbols it intends to touch to prevent merge conflicts in multi-agent workflows.

### Standard Ticket Structure
Store tickets in `docs/tickets/` or write a consolidated execution manifest to `docs/tickets/INDEX.md`:

```markdown
### [TASK-001] <Short Descriptive Title>
- **Status**: `Ready` | `In Progress` | `Blocked` | `Done`
- **Dependencies**: `None` | `[TASK-XYZ]`
- **Target Files**:
  - `src/models/user.py`
  - `tests/test_user.py`
- **Specification Ref**: `docs/specs/feature.md#section-4`

#### Description
Concise summary of the architectural work required.

#### Acceptance Criteria (BDD / Gherkin)
- **Given** an unauthenticated session
- **When** the login endpoint receives invalid credentials
- **Then** it must return HTTP 401 with error code `INVALID_CREDENTIALS`

#### Verification Command
\`\`\`bash
pytest tests/test_user.py -k "test_invalid_credentials"
\`\`\`
```

## Topological Ordering Protocol
1. Calculate the topological sort of the ticket DAG.
2. Verify there are no circular dependencies.
3. Group independent tickets that can be executed in parallel (e.g. Phase 1 Foundations -> Phase 2 Core -> Phase 3 Polish).
4. Transition to `/implement` to execute tickets in topological order.
