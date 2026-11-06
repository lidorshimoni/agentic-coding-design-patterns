# /visualize - Architecture and flow visualization pattern. Generates standardized, syntactically valid Mermaid and C4 diagrams for system designs, data flows, and state machines.

Run the following workflow instructions for the provided input: $ARGUMENTS

# Visualize: Architecture & Flow Visualization Pattern

## Intent
Transform textual architectures, complex algorithms, multi-agent interactions, and data models into unambiguous visual diagrams using standard Mermaid syntax.

## Theoretical Foundation
Rooted in cognitive load theory and the **C4 Model for Software Architecture** (Brown, 2018). Visual models ground abstract system descriptions, making boundaries, data flows, and state transitions instantly verifiable by humans and agents alike.

## Standard Diagram Archetypes

### 1. Component & Boundary Architecture (C4 Container / Component)
Use `flowchart TD` or `flowchart LR` with subgraphs to depict architectural layers:

```mermaid
flowchart TD
    subgraph Client["Client Layer"]
        Web["Web Application (React)"]
        CLI["CLI Tool (Python)"]
    end

    subgraph Gateway["API Gateway"]
        Proxy["Reverse Proxy / Nginx"]
        Auth["Auth Service (JWT)"]
    end

    subgraph Core["Core Services"]
        App["Application Engine"]
        Worker["Async Background Worker"]
    end

    subgraph Data["Persistence Layer"]
        DB[("PostgreSQL")]
        Queue[("Redis Queue")]
    end

    Web --> Proxy
    CLI --> Proxy
    Proxy --> Auth
    Auth --> App
    App --> Queue
    Queue --> Worker
    Worker --> DB
    App --> DB
```

### 2. Request / Response & Protocol Flow (Sequence Diagram)
Use `sequenceDiagram` with activation lifelines to show chronological interactions:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Agent as Coding Agent
    participant Tool as Tool Runner
    participant Git as Version Control

    User->>Agent: Request feature implementation
    Agent->>Tool: Run failing test (Red)
    Tool-->>Agent: Test failed as expected
    Agent->>Tool: Write minimal code (Green)
    Agent->>Tool: Run test suite
    Tool-->>Agent: All tests passed
    Agent->>Git: Commit atomic change
    Git-->>Agent: Commit hash generated
    Agent-->>User: Report completed task
```

### 3. State Machines & Lifecycles (State Diagram)
Use `stateDiagram-v2` for entity states, task statuses, or connection lifecycles:

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> InReview: Submit for Review
    InReview --> Approved: Pass Verification
    InReview --> NeedsChanges: Blocker Found
    NeedsChanges --> InReview: Resubmit Fix
    Approved --> InProgress: Start Implementation
    InProgress --> Completed: All Tests Pass
    Completed --> [*]
```

### 4. Data Models & Relationships (Entity-Relationship Diagram)
Use `erDiagram` for relational schemas and domain models:

```mermaid
erDiagram
    PROJECT ||--o{ SPECIFICATION : contains
    SPECIFICATION ||--o{ TICKET : decomposes_into
    TICKET ||--o{ COMMIT : implemented_by
    TICKET {
        string id PK
        string title
        string status
        string blocked_by
    }
```

## Mermaid Syntax Safety Rules
1. **Always Quote Node Labels with Special Characters**:
   - `id["Label (Extra Info)"]` instead of `id[Label (Extra Info)]`.
2. **Supported Diagram Types Only**:
   - Flowcharts (`flowchart TD`), Sequence (`sequenceDiagram`), State (`stateDiagram-v2`), Class (`classDiagram`), ER (`erDiagram`).
3. **Avoid Raw HTML in Node Text**: Use pure Markdown or clean text inside node strings.

---

## Citations & Provenance
1. **The C4 Model for Software Architecture**: Brown, S. (2018). *Software Architecture for Developers: Visualise, document and explore your software architecture*. Leanpub.
2. **Mermaid Graphing Standard**: Sveidqvist, K., et al. (2014-2026). *Mermaid: Markdown-inspired syntax for generating charts and diagrams* (https://mermaid.js.org/).
3. **Cognitive Load Theory in Software Visualization**: Sweller, J. (2011). *Cognitive Load Theory*. Psychology of Learning and Motivation, Vol. 55.
