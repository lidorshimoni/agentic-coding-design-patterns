---
name: grill-me
description: Interactive requirements elicitation interview. Walks down each branch of the design tree, resolving dependencies between decisions one-by-one with recommended options.
version: 1.0.0
triggers:
  - "/grill-me"
  - "grill me"
  - "interview me about the plan"
---

# Grill-Me: Socratic Requirements Elicitation Pattern

## Intent
Before writing any code or architecture documents, systematically interview the user to resolve ambiguities, technical trade-offs, and design dependencies. Avoid assumptions by walking down the decision tree one branch at a time.

## Theoretical Foundation
Grounded in Socratic dialogue, DDD (Domain-Driven Design) ubiquitous language discovery, and decision-tree traversal. By resolving root architectural dependencies before leaf implementations, rework is minimized.

## Operational Workflow

### Step 1: Codebase & Context Exploration (Silent Pre-check)
- Before asking the user any question, inspect the repository to see if the answer is already dictated by existing patterns, frameworks, dependencies, or configuration.
- If existing code already provides an unambiguous answer, adopt it silently and do not waste user attention.

### Step 2: Establish the Decision Tree
Map out the required architectural decisions and their dependency order:
1. **Core Domain & Boundaries**: What problem is being solved? What is explicitly out of scope?
2. **Architecture & Storage**: Where does data live? How is state managed?
3. **Contracts & Interfaces**: API formats, data schemas, communication protocols.
4. **Execution & Runtime**: Libraries, frameworks, performance budgets.
5. **Edge Cases & Failure Modes**: Error handling, fallbacks, recovery.

### Step 3: Interactive Interview Protocol
Execute the interview following strict operational rules:
1. **One Question at a Time**: Never overwhelm the user with multi-part questions or lists of open-ended queries. Focus on the immediate next decision node.
2. **Provide Concrete Options**: Offer 2 to 4 distinct, mutually exclusive choices.
3. **Always Recommend**: Mark the first option with `(Recommended)` and briefly state the technical justification.
4. **Resolve Dependencies Top-Down**: Do not ask about UI styling before API contracts are agreed upon; do not ask about database schema before storage technology is selected.
5. **Acknowledge and Advance**: When the user answers, record the decision, prune invalid branches of the tree, and immediately advance to the next dependent question.

### Step 4: Completion & Transition
When all critical architectural branches have been traversed and resolved:
- Present a concise summary of all agreed-upon decisions.
- Suggest transitioning to specification generation via `/to-spec`.
