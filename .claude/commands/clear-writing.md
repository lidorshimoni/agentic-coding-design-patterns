# /clear-writing - Write, explain, or edit prose across any subject with maximum clarity and zero fluff. Blends ASD-STE100 Simplified Technical English clarity rules with Andrej Karpathy's pragmatic builder communication style. Features dual modes: default direct explanation (objective, active, <=25 words/sentence) and first-person builder/essay mode (grounded in hands-on work, honest hedging, dry wit, and quantitative precision).

Run the following workflow instructions for the provided input: $ARGUMENTS

# Clear Writing Style Guide

A universal writing and editing skill designed to produce crystal-clear, fluff-free prose across any domain. It synthesizes two complementary communication frameworks:

1. **ASD-STE100 Simplified Technical English (STE)**: Structural clarity, concise sentences, active voice, and minimal cognitive decoding overhead.
2. **Karpathy's Builder Voice**: First-person empirical grounding ("Curious. Built it. Write it up."), honest epistemic hedges, cross-domain analogies, and precision over cheap hype.

---

## The Core Philosophy

> **Explain the subject so the reader understands it immediately without decoding the prose.**
> **Ground claims in concrete reality. If you built, measured, or tested it — report what happened.**

Good communication does not impress through complexity; it clarifies through directness. Adjectives are cheap; exact numbers, mechanisms, and verifiable results are earned.

---

## Operating Modes

This skill operates in two distinct modes. Default to **Mode 1** unless the user explicitly requests an essay, retrospective, personal writeup, or opinion piece.

```
┌────────────────────────────────────────────────────────────────────────┐
│                          CLEAR WRITING SYSTEM                          │
├───────────────────────────────────┬────────────────────────────────────┤
│ MODE 1: Direct Explanation        │ MODE 2: First-Person Builder       │
│ (Default)                         │ (Essays, Retrospectives, Opinion)  │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Objective, neutral register     │ • First-person ("I" / "we")        │
│ • Sentences <= 25 words           │ • Grounded in a concrete artifact  │
│ • Clear topic sentences           │ • Honest epistemic hedges          │
│ • Prerequisite before action      │ • Dry humor & parenthetical asides │
│ • Zero corporate or filler jargon │ • Cross-domain analogies           │
│ • Fast, effortless comprehension  │ • Forward-looking extrapolation    │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## Mode 1: Direct Explanation & Documentation (Default)

Use for: Documentation, tutorials, scientific and engineering explanations, conceptual primers, business memos, standard operating procedures, and product guides.

### 1. Structural Constraints
- **Sentence length**: Aim for 25 words or fewer for descriptions; 20 words or fewer for instructions.
- **Paragraph length**: One coherent idea per paragraph. Never exceed 5–6 sentences in a single paragraph.
- **Single term per concept**: Choose one precise noun for an entity and stick to it. Never swap synonyms for "decorative variety" (e.g., do not cycle between *component*, *element*, *unit*, and *module* if they refer to the same thing).
- **Break noun clusters**: Unpack chains of more than three consecutive nouns. 
  - *Avoid:* "High pressure liquid fuel injection valve assembly"
  - *Prefer:* "Valve assembly for injecting liquid fuel at high pressure"

### 2. Action & Flow
- **Active voice with concrete subjects**: State who or what performs the action.
  - *Avoid:* "The parameters should be adjusted accordingly by the operator."
  - *Prefer:* "Adjust the parameters to match your target."
- **Prerequisite before action**: Tell the reader what must be true before telling them what to do.
  - *Avoid:* "Click Submit after verifying your credentials."
  - *Prefer:* "Verify your credentials, then click Submit."
- **Direct order**: State the main conclusion or topic in the first sentence; explain the mechanism immediately after.

---

## Mode 2: First-Person Builder & Retrospective Essay

Use when the user requests an essay, personal technical writeup, year-in-review, post-mortem, thought piece, or a writeup "in Karpathy's style."

### 1. The North Star
> **Curious. Built it. Write it up.**

The piece must anchor to something concrete: code written, a model trained, data measured, hardware assembled, or an experiment lived through. Prose exists to contextualize an artifact, not to substitute for one.

### 2. Voice & Perspective
- **"I" for the author**: Use for actions, hypotheses, surprises, and personal opinions (*"I set out to test...", "I suspect that..."*).
- **"We" for collaborative walkthroughs**: Use when taking the reader along through a build or calculation (*"Now we compute the residuals...", "We can see that..."*).
- **Confident humility**: State working theories directly without defensiveness, while openly admitting what remains unknown.
- **Honest epistemic hedges**: Hedge only when genuinely uncertain or interpreting between the lines (*"I suspect"*, *"most likely"*, *"as far as I can tell"*, *"probably"*). Do not hedge on facts you verified.
- **Dry, self-aware wit**: Keep humor grounded in scope, taste, or human quirks, never undermining technical rigor (*"hah, opposite of what you'd hope"*, *"yolo"*, *"¯\\_(ツ)_/¯"*).

### 3. Rhetorical Moves
- **Multipliers over adjectives**: Do not write *"this is exceptionally fast"*. Write *"approximately 14x faster"* or *"reduced cycle time from 12 hours to 45 minutes"*.
- **Cross-domain analogies**: Reach across disciplines to explain an unfamiliar mechanism (e.g., memory hierarchies for biological metabolism; bit-mixers for hash functions). **Rule:** Use the analogy *once* to establish intuition, then return to standard domain terms. Do not belabor the metaphor.
- **Vivid dichotomies**: Frame complex tensions cleanly (*"simple in theory, jagged in practice"*, *"brilliant at synthesis, confused by arithmetic"*).
- **Time-travel comparison**: Compare an old method or historical baseline against modern capabilities (*"What has actually changed in 20 years?"*).
- **Inline results**: Interleave measurements, curves, or data outputs directly within the narrative flow as they occur, rather than dumping them into an isolated appendix.

---

## Universal Sentence & Word Patterns

Applicable across both modes:

### Sentence Rhythms
- **Short punchy conclusions**: Follow a nuanced, multi-part explanation with a short declarative statement.
  - *"Code is suddenly malleable and cheap to discard."*
  - *"The bottleneck was never the network; it was the disk."*
- **Parenthetical asides**: Use for quick clarifications, dates, or light color without derailing narrative momentum: *(built around ~2018)*, *(and paradoxically, cheaper)*.
- **Em-dashes for cadence**: Use em-dashes (`—`) to insert sharp, clarifying pivots.
- **Tilde for approximations**: Use `~` for quick order-of-magnitude estimates: *~500 ms*, *~2015*, *~30% gain*.

### Word Choice Matrix

| Prefer | Avoid | Why |
|---|---|---|
| **emerged as** | became / revolutionized | Describes observable evolution without hype |
| **convincing demonstration** | paradigm shift / game changer | Focuses on evidence rather than marketing labels |
| **chewing through / processing** | leveraging / utilizing | Concrete action over corporate jargon |
| **jagged** | inconsistent / disparate | Concrete visual descriptor |
| **spike in capability** | massive leap forward | Measurable trend over subjective cheerleading |
| **straightforward** | facile / simplistic | Honest assessment of difficulty |
| **I suspect / most likely** | it could be argued that | Genuine personal calibration over passive armor |
| **before you X, do Y** | prior to X, ensure Y is done | Active instructional sequence |

---

## Strict Anti-Patterns (The "Do Not" List)

1. **Zero marketing buzzwords**: Never use *"unlock the power of"*, *"dive deep into"*, *"in today's rapidly evolving landscape"*, *"game-changing"*, or *"revolutionary"*.
2. **Zero transitional throat-clearing**: Never write *"Now that we have covered X, let us turn our attention to Y"*. Just move directly to Y.
3. **No corporate passive voice**: Do not hide behind *"Mistakes were made"* or *"It was observed that"*. Write *"We observed"* or *"The system failed because"*.
4. **No emoji decoration**: No decorative emojis (🚀, ✨, 💡, 🔥, 🎉). Unicode emoticons like *¯\\_(ツ)_/¯* are permitted only when carrying intentional comedic weight in Mode 2.
5. **No decorative synonym cycling**: Never swap technical terms mid-explanation to avoid word repetition. Repetition of the correct term is superior to ambiguity.
6. **No hollow closers**: Never end with *"Thanks for reading!"*, *"What do you think? Let me know in the comments"*, or *"Subscribe for more"*. End when the substance is complete.
7. **No dutiful recap headers**: Avoid standard "Conclusion" sections that merely repeat earlier bullet points. Instead, extrapolate into the future, outline open questions, or provide next pointers.

---

## Transformation Examples

### Example 1: Technical Explanation (Mode 1)
- **Bloated / Passive:**
  > "It is of paramount importance that system administrators take into consideration the latency implications inherent in multi-region database replications prior to executing architectural migrations, as network overhead can frequently cause significant degradations in user experience."
- **Clear Writing:**
  > "Before you migrate your database across multiple regions, test cross-region network latency. Replicating data across long distances often creates noticeable delays for end users."

### Example 2: Retrospective / Engineering Build (Mode 2)
- **Generic Tech Blog:**
  > "In this article, we demonstrate how contemporary caching paradigms can be leveraged to dramatically elevate application throughput. Through a series of benchmark evaluations, we reveal that notable optimization gains are attainable with minimal refactoring."
- **Karpathy / Builder Style:**
  > "I wanted to see how far a simple local in-memory cache could carry our search service before we needed Redis. Adding a 50MB LRU cache with a 60-second TTL cut average query latency from 180ms down to 11ms — about a 16x speedup. The memory footprint barely moved, and we avoided adding another distributed dependency to the stack. Sometimes the boring fix is the right one."

### Example 3: Everyday / Business Proposal
- **Corporate Fluff:**
  > "We are proactively synergizing cross-functional bandwidth to seamlessly optimize customer onboarding throughput and unlock strategic lifetime value."
- **Clear Writing:**
  > "We are redesigning customer onboarding to cut setup time from five days to one. Faster setup directly lowers account drop-offs during the first month."

---

## Pre-Flight Checklist

Before finalizing any text, verify:

- [ ] **Mode match**: Is this purely instructional/explanatory (Mode 1) or a personal build/essay (Mode 2)?
- [ ] **Direct opening**: Does the first paragraph introduce the core subject or hook without introductory throat-clearing?
- [ ] **Sentence control**: Are descriptive sentences under 25 words? Are instructions under 20 words?
- [ ] **Concrete evidence**: Are vague adjectives (*"much faster"*, *"huge"*) replaced by exact multipliers or measurements (*"3x"*, *"40% lower"*)?
- [ ] **Term consistency**: Is every core concept referred to by one single, unchanging name?
- [ ] **Honest hedging**: Are hedges restricted to genuinely uncertain points rather than used as rhetorical armor?
- [ ] **Fluff scrubbed**: Are marketing buzzwords, decorative synonyms, passive hedges, and emoji padding eliminated?
- [ ] **Ending check**: Does the piece conclude without a redundant "Conclusion" summary or hollow social sign-off?

---

## Structural Skeletons

### Mode 1 Skeleton (Direct Explanation)
```markdown
## [Core Subject / Problem Statement]

[One or two short sentences stating what this is, what problem it solves, and the primary takeaway.]

### How it Works

[Step-by-step breakdown or mechanism. Short sentences (<=25 words). Concrete subjects and active verbs.]

1. **[First Stage / Prerequisite]**: [Direct explanation]
2. **[Core Action / Transformation]**: [Direct explanation]
3. **[Outcome / Verification]**: [Direct explanation]

### Key Constraints & Trade-offs

- **[Trade-off 1]**: [Measurable limitation or cost]
- **[Trade-off 2]**: [Condition where this approach does not apply]
```

### Mode 2 Skeleton (Builder Essay)
```markdown
> "[Optional relevant quote or epigraph]" — Author [Optional]

[Opening: One punchy paragraph. Why this project, why now. Grounded in a concrete artifact or personal question.]

[Conceptual setup: 1–2 paragraphs. Introduce the key cross-domain analogy once, then drop it.]

### [Section 1: What was built or tested]

[Prose interleaved with code, measurements, or observations. Short paragraphs. Include specific before/after numbers.]

### [Section 2: What changed and what surprised me]

[Honest reflections. What was harder or easier than expected. Epistemic hedges ("I suspect...", "most likely...") belong here.]

### Looking Forward / TLDR

**TLDR**: [2–3 sentence distillation of the core insight, paradox, or takeaway.]

[Extrapolate: Project N years out, highlight open questions, or provide links to the source artifacts. End without a dutiful recap.]
```

---

## Citations & Provenance
1. **Simplified Technical English**: AeroSpace and Defence Industries Association of Europe (ASD). *ASD-STE100 Simplified Technical English (Issue 9, 2025)*. Specification for preparation of technical documentation in a controlled language.
2. **Pragmatic Builder Communication**: Karpathy, A. (2011–2026). *Essays, Notes, and Technical Writeups* (https://karpathy.github.io).
3. **Repository Source**: Shimoni, L. (2026). *Universal clear-writing skill* (https://github.com/lidorshimoni/clear-writing).
4. **Cognitive Efficiency in Technical Documentation**: Hartley, J. (2004). *Designing Instructional Text*. Routledge.
