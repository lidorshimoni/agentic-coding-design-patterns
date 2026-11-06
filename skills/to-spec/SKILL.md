---
name: to-spec
description: Transforms requirements, interview transcripts, or raw ideas into an authoritative, RFC-grade technical specification and PRD.
version: 1.0.0
triggers:
  - "/to-spec"
  - "generate spec"
  - "write technical specification"
---

# To-Spec: Spec-Driven Development Pattern

## Intent
Transform high-level feature requests, interview transcripts (such as from `/grill-me`), or design notes into an authoritative, unambiguous Technical Specification Document (RFC / PRD) before implementation starts.

## Theoretical Foundation
Rooted in Spec-Driven Development (SDD), Amazon PR/FAQ methodology, RFC 2119 requirement conventions, and Architecture Decision Records (ADRs). Writing specifications first eliminates ambiguity, sets explicit verification boundaries, and provides an objective benchmark for code review.

## Standard Specification Structure
When producing a specification, write it to `docs/specs/<feature-name>.md` (or the project's preferred docs directory) using the following sections:

### 1. Metadata & Status
- **Title**: Descriptive feature name
- **Authors**: Author / Agent
- **Date**: ISO-8601 date
- **Status**: `Draft` | `In Review` | `Approved` | `Superseded`

### 2. Context & Problem Statement
- Why are we doing this?
- What pain point or capability does this address?
- What evidence or user feedback motivates this change?

### 3. Goals & Non-Goals (Strict Boundary Setting)
- **Goals**: Explicit, measurable outcomes that define success.
- **Non-Goals (Out of Scope)**: Explicit list of what this project will *not* do, preventing scope creep.

### 4. Normative Requirements (RFC 2119)
Use standardized RFC 2119 keywords:
- **MUST / SHALL**: Mandatory requirement.
- **SHOULD**: Highly recommended unless strong justification exists.
- **MAY**: Optional capability.

### 5. Architectural Design & Component Diagram
- High-level architecture and system boundaries.
- Mermaid diagram showing data flow and component relationships.
- File and directory changes (new files, modified files, deprecated files).

### 6. Data Models & API Contracts
- Exact schemas, TypeScript interfaces, Pydantic models, or protobufs.
- Request/Response payloads with HTTP status codes or RPC signatures.
- Error codes and exception taxonomy.

### 7. Invariants & Security Considerations
- Data invariants that must never be violated (e.g. idempotency, immutability, thread safety).
- Authentication, authorization, sanitization, and secrets management.

### 8. Failure Modes & Rollback Strategy
- What happens when a downstream dependency fails?
- Circuit breakers, timeout configurations, and fallback values.
- Rollback procedure if deployment fails.

## Transition
Once the specification is written and accepted, use `/to-tickets` to break it into an executable task DAG.
