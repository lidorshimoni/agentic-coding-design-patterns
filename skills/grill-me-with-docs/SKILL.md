---
name: grill-me-with-docs
description: Documentation-grounded requirements interview. Retrieves official documentation, API references, or web sources to validate architectural options before presenting choices.
version: 1.0.0
triggers:
  - "/grill-me-with-docs"
  - "grill me with docs"
  - "interview me with documentation"
---

# Grill-Me-With-Docs: Grounded Socratic Elicitation Pattern

## Intent
Conduct a Socratic design interview where every technical choice is pre-validated against official library documentation, API specifications, and real-world reference architectures, avoiding hallucinations and deprecated patterns.

## Theoretical Foundation
Combines Retrieval-Augmented Generation (RAG) with Socratic inquiry. In software engineering, architectural decisions frequently depend on third-party API constraints, breaking changes, or version-specific features. Grounding options in authoritative documentation ensures all choices presented to the user are viable and state-of-the-art.

## Operational Workflow

### Step 1: Query & Verify Documentation
Before posing any design branch to the user involving libraries, tools, protocols, or external services:
1. Identify relevant documentation resources (official docs, GitHub READMEs, OpenAPI specs, MDN, library source code).
2. Use available retrieval tools (web search, documentation search, local package inspection) to retrieve exact version capabilities, breaking changes, and canonical recommendations.
3. Verify that candidate approaches are currently supported and not deprecated.

### Step 2: Formulate Grounded Questions
When presenting options to the user:
- Cite the official reference or API version for each candidate option (e.g., *"Based on FastAPI 0.110+ lifespan events..."* or *"According to PostgreSQL 16 pgvector benchmarks..."*).
- Highlight official caveats, rate limits, licensing, or deprecation notices directly in the option descriptions.
- Ensure the `(Recommended)` option aligns with current industry best practices and official framework documentation.

### Step 3: Interactive Interview Protocol
- Ask one question at a time.
- Include 2 to 4 grounded options with brief rationale.
- Prune impossible paths immediately based on retrieved constraints.
- Link to relevant reference URLs or doc files in the rationale.

### Step 4: Completion & Artifact Generation
- Summarize the decisions, embedding authoritative doc links for each adopted component.
- Recommend proceeding to `/to-spec` to lock in the grounded architecture.

---

## Citations & Provenance
1. **Retrieval-Augmented Generation**: Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. arXiv:2005.11401.
2. **Context Engineering for Coding Assistants**: Anthropic Engineering (2024). *Effective Context Retrieval in Claude Code and Tool Grounding*.
3. **API Specification Verification**: OpenAPI Initiative (2021). *OpenAPI Specification v3.1.0*.

