# /teach - Multi-session stateful teaching workspace. Teaches any skill or concept across sessions using ZPD, retrieval practice, HTML lessons, and ADR-style learning records.

Run the following workflow instructions for the provided input: $ARGUMENTS

# Teach: Stateful Pedagogical Learning Workspace Pattern

## Intent
Transform the working directory into a standing, stateful pedagogical workspace to teach any chosen topic (programming languages, unfamiliar codebases, frameworks, mathematics, languages, certifications, or physical skills) over multiple sessions. Instead of superficial in-context explanations that vanish after one conversation, this pattern accumulates enduring understanding through bite-sized, self-contained HTML lessons, high-trust external citations, and ADR-style learning records.

## Theoretical Foundation
Rooted in cognitive science, learning theory, and modern AI engineering pedagogy:
1. **Desirable Difficulties & Storage Strength** (Bjork & Bjork, 2011): Distinguishes illusory fluency (in-the-moment recall that fades quickly) from true storage strength (long-term retention). Builds durable mental models through retrieval practice, spaced repetition, and interleaving.
2. **Testing Effect & Effortful Retrieval** (Roediger & Karpicke, 2006): Active recall and formative self-quizzing produce significantly greater retention than passive reading.
3. **Zone of Proximal Development (ZPD)** (Vygotsky, 1978): Calibrates every lesson to be challenging enough to demand cognitive effort, yet strictly within reach given the learner's established baseline.
4. **Cognitive Load Theory** (Sweller, 1988): Minimizes extraneous cognitive load during initial concept acquisition (short lessons, single tangible win, clean typography), reserving working memory for skill mastery.
5. **AI Hero & Real Engineer Pedagogy** (Matt Pocock, 2026): Treats parametric model knowledge as untrusted; mandates empirical grounding in curated resources and isolates learning state into disk artifacts.

---

## Workspace Anatomy & File Structure

A teaching workspace is isolated to its own directory and maintains persistent state across sessions via the following artifacts:

| Path | Purpose | Format Specification |
| :--- | :--- | :--- |
| `MISSION.md` | Grounding anchor: the concrete, real-world reason the user is learning this. | [MISSION-FORMAT.md](./MISSION-FORMAT.md) |
| `RESOURCES.md` | Vetted external sources, divided into **Knowledge** (texts/specs) and **Wisdom** (communities). | [RESOURCES-FORMAT.md](./RESOURCES-FORMAT.md) |
| `./lessons/*.html` | Sequenced, self-contained HTML lessons (`0001-<slug>.html`) designed with Tufte-style typography. | Core unit of instruction |
| `./reference/*.html` | Compressed cheat-sheets, syntax guides, algorithms, and diagrams returned to over time. | Reusable reference |
| `./learning-records/*.md` | Sequential ADR-style notes (`0001-<slug>.md`) capturing demonstrated mastery and misconceptions. | [LEARNING-RECORD-FORMAT.md](./LEARNING-RECORD-FORMAT.md) |
| `./assets/*` | Reusable course components: shared stylesheets, quiz widgets, simulators, and diagrams. | Course component library |
| `GLOSSARY.md` | Canonical vocabulary and tight definitions for domain nomenclature. | [GLOSSARY-FORMAT.md](./GLOSSARY-FORMAT.md) |
| `NOTES.md` | Scratchpad recording user preferences, pedagogical pacing, and working notes. | Freeform notes |

---

## Operational Workflow

### Phase 1: Workspace Initialization & Socratic Mission Interview
1. Inspect the workspace root for `MISSION.md`.
2. If `MISSION.md` is missing or incomplete, **do not generate a lesson**. Intercept the session and conduct a structured interview to discover:
   - **Why**: What concrete real-world capability or outcome is the learner pursuing? (Reject vague answers like "to learn Rust"; require "to ship a memory-safe CLI for my team").
   - **Success Criteria**: 2–4 observable, verifiable things the user will be able to do.
   - **Constraints**: Time commitment, technical background, budget, or preferred modality.
   - **Out of Scope**: Explicit list of adjacent rabbit holes to avoid.
3. Write `MISSION.md`. Ground all subsequent teaching decisions in this file.

### Phase 2: High-Trust Resource Curation (`RESOURCES.md`)
1. **Never teach from untrusted parametric memory alone.**
2. Search and verify primary documentation, standard specifications, seminal textbooks, and moderated expert communities.
3. Populate `RESOURCES.md` before generating lessons, categorized into:
   - **Knowledge Sources**: Peer-reviewed papers, official API references, canonical books.
   - **Wisdom (Communities)**: Moderated forums (e.g. specialized subreddits, Discord groups, local meetups) where real-world nuance is practiced.
4. Annotate each entry with what it covers and when to reach for it.

### Phase 3: ZPD Assessment & Lesson Planning
1. Scan `./learning-records/` to evaluate what the user has demonstrably mastered.
2. Cross-reference the user's current baseline against `MISSION.md` to compute the next step in their Zone of Proximal Development.
3. Pick a tightly scoped topic that delivers **one tangible, cumulative win**.

### Phase 4: Self-Contained HTML Lesson Construction
Author each lesson as a standalone HTML file in `./lessons/0001-<dash-case-name>.html` following these design constraints:
1. **Typography & Layout**: Clean, distraction-free typography (Tufte-inspired). Link to the shared stylesheet in `../assets/style.css`.
2. **Short & Focused**: Completable in 10–15 minutes without overwhelming working memory.
3. **Primary Source Recommendation**: Highlight one curated primary source from `RESOURCES.md` for deeper reading.
4. **External Citations**: Link factual claims directly to authoritative sources.
5. **Interactive Feedback Loop**:
   - Embed lightweight interactive elements (quizzes, micro-exercises, or step-by-step physical drills).
   - **Quiz Balance Rule**: Every multiple-choice option must have approximately equal word and character length. Randomize correct answer positions to eliminate formatting cues.
6. **Follow-up Prompt**: Include a reminder prompting the user to discuss unclear points with the agent.
7. Attempt to open the lesson automatically using a platform CLI command (e.g. `start <file>` on Windows, `open <file>` on macOS).

### Phase 5: Knowledge Acquisition vs. Skill Drills
- **When teaching Knowledge**: Keep cognitive friction near zero. Clarity, concise analogies, and visual hierarchy take priority.
- **When building Skills**: Introduce desirable difficulty. Force active retrieval, require the user to write code or execute steps from memory, and provide immediate, automated feedback.

### Phase 6: Sequential Learning Records (ADRs for Learning)
1. When the user demonstrates genuine understanding (not just passive exposure), write a new learning record to `./learning-records/NNNN-<slug>.md`.
2. Record:
   - What concept or technique was established.
   - What evidence demonstrated mastery.
   - How this changes what to teach next.
   - Corrected misconceptions (high value for avoiding future pitfalls).
3. If later learning supersedes an earlier understanding, update the old record's header to `Status: superseded by LR-NNNN` rather than deleting it.

### Phase 7: Reference Materials & Compressed Glossaries
1. As patterns and terminology stabilize, distill them into:
   - `./reference/<topic>.html`: Print-ready, high-density reference sheets.
   - `GLOSSARY.md`: Precise 1–2 sentence definitions of domain terms.
2. Add a term to `GLOSSARY.md` only after the learner has demonstrated working command of it.

### Phase 8: Wisdom Delegation
When questions hinge on judgment, trade-offs, or real-world edge cases that require lived experience:
1. Provide the foundational technical context.
2. Point the user to the verified communities listed in `RESOURCES.md` to validate their approach among practicing peers.

---

## Document Format Specifications & Templates

### Template 1: `MISSION.md`
```markdown
# Mission: {Topic}

## Why
{1-3 sentences. The concrete real-world goal. What changes when you have this skill? Avoid abstract goals.}

## Success looks like
- {A specific, observable capability}
- {Another verifiable outcome}

## Constraints
- {Time budget, prior commitments, environment constraints}

## Out of scope
- {Adjacent topics explicitly deferred to protect focus}
```

### Template 2: `RESOURCES.md`
```markdown
# {Topic} Resources

## Knowledge
- [{Source Title}]({URL})
  {Author/Authority}. Use for: {specific topics/phases}.

## Wisdom (Communities)
- [{Community Name}]({URL})
  {Description and moderation quality}. Use for: {critiques, troubleshooting, peer review}.

## Gaps
- {Missing or low-quality areas requiring further search}
```

### Template 3: `learning-records/NNNN-slug.md`
```markdown
# {Short Title of Mastery or Prior Knowledge}

{1-3 sentences: what was demonstrated or established, evidence of understanding, and how this shifts the ZPD for subsequent sessions.}
```

### Template 4: `GLOSSARY.md`
```markdown
# {Topic} Glossary

{Brief description of scope.}

## Terms
**{Term}**:
{Tight 1-2 sentence definition of what it IS.}
_Avoid_: {Misleading synonyms or anti-patterns}
```

---

## Citations & Provenance
1. **The /teach Skill & Real Engineering Pedagogy**: Pocock, M. (2026). *The /teach Skill - AI Skills for Real Engineers*. AI Hero (https://www.aihero.dev/skills-teach).
2. **Storage Strength vs. Retrieval Strength & Desirable Difficulties**: Bjork, E. L., & Bjork, R. A. (2011). *Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning*. Psychology and the Real World, 2(1), 56-64.
3. **Zone of Proximal Development (ZPD)**: Vygotsky, L. S. (1978). *Mind in Society: The Development of Higher Psychological Processes*. Harvard University Press.
4. **Cognitive Load Theory**: Sweller, J. (1988). *Cognitive load during problem solving: Effects on learning*. Cognitive Science, 12(2), 257-285.
5. **The Testing Effect**: Roediger, H. L., & Karpicke, J. D. (2006). *Test-enhanced learning: Taking memory tests improves long-term retention*. Psychological Science, 17(3), 249-255.
