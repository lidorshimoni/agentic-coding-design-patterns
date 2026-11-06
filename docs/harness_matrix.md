# Agent Harness Compatibility Matrix

This document details the configuration files, slash command mechanisms, and memory discovery systems across all major AI coding harnesses supported by this repository.

---

## Harness Specification Overview

| Harness | Vendor / Project | Command Mechanism | Memory / Rules Location | Skill Discovery Format |
| :--- | :--- | :--- | :--- | :--- |
| **Claude Code** | Anthropic | `.claude/commands/<cmd>.md` | `CLAUDE.md` | Slash commands with `$ARGUMENTS` interpolation |
| **Antigravity (AGY)** | Google DeepMind | Slash command system & skills | `GEMINI.md`, `AGENTS.md` | `.agents/skills/<name>/SKILL.md` (YAML frontmatter) |
| **Cursor** | Anysphere | Dynamic rule injection | `.cursor/rules/*.mdc`, `.cursorrules` | `.mdc` files with `description` and `globs` frontmatter |
| **Roo Code / Cline** | Open Source | Custom mode system & prompts | `.clinerules`, `.roomodes` | Mode prompt configurations and instruction files |
| **Windsurf** | Codeium | Cascade rule system | `.windsurfrules`, `.codeium/` | Contextual memory rules |
| **GitHub Copilot** | Microsoft / GitHub | Chat instructions | `.github/copilot-instructions.md` | Hierarchical Markdown guidelines |
| **Aider & Generic** | Open Source | Chat conventions & prompts | `AGENTS.md`, `.aider.conf.yml` | Standard repository documentation |

---

## Harness Details & Compilation Mapping

### 1. Claude Code
- **Slash Commands**: Placed in `.claude/commands/<command>.md`. When the user types `/<command>`, Claude executes the template, injecting CLI arguments into `$ARGUMENTS`.
- **System Memory**: Reads `CLAUDE.md` in the repository root at startup.
- **Compiler Output**: Generates `.claude/commands/<cmd>.md` for each skill and appends references into `CLAUDE.md`.

### 2. Antigravity / AGY
- **Skills**: Discovered automatically by scanning `.agents/skills/<name>/SKILL.md` or `.gemini/skills/<name>/SKILL.md`.
- **Rules**: Discovered hierarchically by walking up the directory tree to find `GEMINI.md` or `.agents/rules/*.md`.
- **Compiler Output**: Generates `.agents/skills/<name>/SKILL.md` and appends an overview into `GEMINI.md`.

### 3. Cursor
- **Rules**: Stored in `.cursor/rules/<name>.mdc` with YAML frontmatter:
  ```yaml
  ---
  description: Rule description for agent retrieval
  globs: *
  alwaysApply: false
  ---
  ```
- **Fallback**: Legacy `.cursorrules` at repository root.
- **Compiler Output**: Compiles each skill into a `.cursor/rules/<name>.mdc` file and generates a consolidated `.cursorrules`.

### 4. Roo Code & Cline
- **Rules**: Stored in `.clinerules` in the repository root.
- **Modes**: Configured in `.roomodes` with specific system prompt role definitions (Architect, Code, Ask, Test).
- **Compiler Output**: Generates consolidated `.clinerules` referencing all pattern skills and command workflows.

### 5. Windsurf
- **Rules**: Stored in `.windsurfrules` at project root.
- **Compiler Output**: Appends command instructions and architectural patterns into `.windsurfrules`.

### 6. Universal / GitHub Copilot / Aider
- **Standards**: `AGENTS.md` and `.github/copilot-instructions.md`.
- **Compiler Output**: Compiles a single comprehensive, clean index of all commands, patterns, and instructions into `AGENTS.md` and `.github/copilot-instructions.md`.
