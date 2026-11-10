#!/usr/bin/env python3
"""
Agentic Coding Design Patterns - Cross-Harness Compiler & Sync CLI
Zero-dependency Python 3 standard library implementation.
Exports canonical skills into configurations for Claude Code, Antigravity,
Cursor, Windsurf, Roo/Cline, GitHub Copilot, and Universal AGENTS.md.
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any

# Root of the canonical repository
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
TEMPLATES_DIR = REPO_ROOT / "templates"


def parse_frontmatter(content: str) -> tuple[Dict[str, Any], str]:
    """Parse YAML-style frontmatter without external dependencies."""
    frontmatter: Dict[str, Any] = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1].strip()
            body = parts[2].strip()

            current_list_key = None
            for line in raw_fm.splitlines():
                line = line.rstrip()
                if not line or line.startswith("#"):
                    continue

                # List item under key
                if line.startswith("  - ") and current_list_key:
                    val = line[4:].strip().strip('"').strip("'")
                    frontmatter[current_list_key].append(val)
                    continue

                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip()

                    if val == "" or val is None:
                        # Might be a list starting
                        current_list_key = key
                        frontmatter[key] = []
                    else:
                        current_list_key = None
                        val = val.strip('"').strip("'")
                        frontmatter[key] = val

    return frontmatter, body


def load_canonical_skills() -> List[Dict[str, Any]]:
    """Load all canonical skills from skills/<name>/SKILL.md."""
    skills = []
    if not SKILLS_DIR.exists():
        print(f"Error: Skills directory not found at {SKILLS_DIR}", file=sys.stderr)
        return skills

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if skill_dir.is_dir() and skill_file.exists():
            raw_content = skill_file.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(raw_content)
            name = fm.get("name", skill_dir.name)
            desc = fm.get("description", "")
            version = fm.get("version", "1.0.0")
            triggers = fm.get("triggers", [f"/{name}"])

            skills.append({
                "id": skill_dir.name,
                "name": name,
                "description": desc,
                "version": version,
                "triggers": triggers,
                "body": body,
                "raw": raw_content,
                "path": skill_file
            })

    return skills


# ---------------------------------------------------------------------------
# Exporters for specific agent harnesses
# ---------------------------------------------------------------------------

def export_claude_code(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to Anthropic Claude Code (.claude/commands/*.md and CLAUDE.md)."""
    commands_dir = target_dir / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        cmd_file = commands_dir / f"{skill['name']}.md"
        # Claude Code command format with $ARGUMENTS interpolation
        content = f"""# /{skill['name']} - {skill['description']}

Run the following workflow instructions for the provided input: $ARGUMENTS

{skill['body']}
"""
        cmd_file.write_text(content, encoding="utf-8")

    # Update or create CLAUDE.md
    claude_md = target_dir / "CLAUDE.md"
    overview_lines = [
        "# Claude Code Project Guidelines",
        "",
        "## Available Slash Commands",
    ]
    for skill in skills:
        overview_lines.append(f"- `/{skill['name']}`: {skill['description']}")

    overview_lines.extend([
        "",
        "## Agentic Coding Best Practices",
        "- Always explore the codebase first before asking the user.",
        "- Enforce TDD (Red-Green-Refactor) and atomic commits.",
        "- Adhere to strict task decomposition and acceptance criteria.",
        ""
    ])

    if not claude_md.exists() or "## Available Slash Commands" in claude_md.read_text(encoding="utf-8"):
        claude_md.write_text("\n".join(overview_lines), encoding="utf-8")
    else:
        existing = claude_md.read_text(encoding="utf-8")
        claude_md.write_text(existing.rstrip() + "\n\n" + "\n".join(overview_lines[2:]), encoding="utf-8")

    print(f"  ✓ Exported Claude Code: {len(skills)} commands into {commands_dir}")


def export_antigravity(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to Google Antigravity (.agents/skills/<name>/SKILL.md and GEMINI.md)."""
    agents_dir = target_dir / ".agents" / "skills"
    agents_dir.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        dest_dir = agents_dir / skill["name"]
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / "SKILL.md").write_text(skill["raw"], encoding="utf-8")

        # Copy any auxiliary files from the source skill directory (e.g. *-FORMAT.md)
        src_dir = skill["path"].parent
        for extra_file in src_dir.iterdir():
            if extra_file.is_file() and extra_file.name != "SKILL.md":
                (dest_dir / extra_file.name).write_bytes(extra_file.read_bytes())

    # Update or create GEMINI.md
    gemini_md = target_dir / "GEMINI.md"
    overview_lines = [
        "# Antigravity Project Rules & Capabilities",
        "",
        "## Mounted Agent Skills",
    ]
    for skill in skills:
        overview_lines.append(f"- **{skill['name']}**: {skill['description']}")

    overview_lines.extend([
        "",
        "## Core Behavioral Invariants",
        "- Follow Test-Driven Development; never commit untested code.",
        "- Review changes through multi-lens verification before completion.",
        "- Check codebase context before asking the user questions.",
        ""
    ])

    if not gemini_md.exists() or "## Mounted Agent Skills" in gemini_md.read_text(encoding="utf-8"):
        gemini_md.write_text("\n".join(overview_lines), encoding="utf-8")
    else:
        existing = gemini_md.read_text(encoding="utf-8")
        gemini_md.write_text(existing.rstrip() + "\n\n" + "\n".join(overview_lines[2:]), encoding="utf-8")

    print(f"  ✓ Exported Antigravity: {len(skills)} skills into {agents_dir}")


def export_cursor(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to Cursor (.cursor/rules/*.mdc and .cursorrules)."""
    rules_dir = target_dir / ".cursor" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)

    cursorrules_lines = [
        "# Cursor Project Rules & Agentic Patterns",
        "",
        "## Design Patterns & Slash Commands",
    ]

    for skill in skills:
        mdc_file = rules_dir / f"{skill['name']}.mdc"
        mdc_content = f"""---
description: {skill['description']}
globs: *
alwaysApply: false
---

# /{skill['name']}

{skill['body']}
"""
        mdc_file.write_text(mdc_content, encoding="utf-8")
        cursorrules_lines.append(f"- `/{skill['name']}`: {skill['description']}")

    # Write fallback .cursorrules
    cursorrules_lines.extend([
        "",
        "## Standard Engineering Guardrails",
        "- Verify with unit tests before declaring task completion.",
        "- Perform self-critic check against invariants before applying large diffs.",
        ""
    ])
    (target_dir / ".cursorrules").write_text("\n".join(cursorrules_lines), encoding="utf-8")

    print(f"  ✓ Exported Cursor: {len(skills)} rules into {rules_dir} & .cursorrules")


def export_windsurf(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to Windsurf (.windsurfrules)."""
    windsurfrules = target_dir / ".windsurfrules"
    lines = [
        "# Windsurf Cascade Rules & Agentic Patterns",
        "",
        "## Available Workflows & Slash Commands",
    ]
    for skill in skills:
        lines.append(f"### `/{skill['name']}`")
        lines.append(f"Description: {skill['description']}")
        lines.append("")
        lines.append(skill["body"].strip())
        lines.append("\n---\n")

    windsurfrules.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✓ Exported Windsurf: {len(skills)} patterns into {windsurfrules}")


def export_roo_cline(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to Roo Code & Cline (.clinerules and .roomodes)."""
    clinerules = target_dir / ".clinerules"
    lines = [
        "# Roo Code & Cline Operational Instructions",
        "",
        "## Custom Agentic Commands & Patterns",
    ]
    for skill in skills:
        lines.append(f"### Pattern: {skill['name']}")
        lines.append(f"Triggers: {', '.join(skill['triggers'])}")
        lines.append(f"Description: {skill['description']}")
        lines.append("")
        lines.append(skill["body"].strip())
        lines.append("\n---\n")

    clinerules.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✓ Exported Roo Code / Cline: {len(skills)} patterns into {clinerules}")


def export_copilot_and_agents(skills: List[Dict[str, Any]], target_dir: Path):
    """Export to GitHub Copilot (.github/copilot-instructions.md) and Universal AGENTS.md."""
    # Copilot instructions
    github_dir = target_dir / ".github"
    github_dir.mkdir(parents=True, exist_ok=True)
    copilot_file = github_dir / "copilot-instructions.md"

    # Universal AGENTS.md
    agents_file = target_dir / "AGENTS.md"

    lines = [
        "# Agentic Coding Guidelines & Design Patterns",
        "",
        "This project adheres to structured agentic coding workflows to ensure",
        "high code quality, regression prevention, and clean architectural boundaries.",
        "",
        "## Available Workflows & Triggers",
    ]

    for skill in skills:
        lines.append(f"### `/{skill['name']}`")
        lines.append(f"**Description**: {skill['description']}")
        lines.append(f"**Triggers**: `{', '.join(skill['triggers'])}`")
        lines.append("")
        lines.append(skill["body"].strip())
        lines.append("\n---\n")

    content = "\n".join(lines)
    copilot_file.write_text(content, encoding="utf-8")
    agents_file.write_text(content, encoding="utf-8")

    print(f"  ✓ Exported Copilot & Universal: {copilot_file} and {agents_file}")


# ---------------------------------------------------------------------------
# CLI Command Dispatcher
# ---------------------------------------------------------------------------

EXPORTERS = {
    "claude": export_claude_code,
    "antigravity": export_antigravity,
    "cursor": export_cursor,
    "windsurf": export_windsurf,
    "roo": export_roo_cline,
    "copilot": export_copilot_and_agents,
    "agents": export_copilot_and_agents,
}


def main():
    parser = argparse.ArgumentParser(
        description="Cross-Harness Compiler & Sync for Agentic Coding Design Patterns"
    )
    parser.add_argument(
        "--target",
        "-t",
        default="all",
        help="Target harness(es) to export to: all, claude, antigravity, cursor, windsurf, roo, copilot, agents (comma-separated)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default=".",
        help="Target project directory to install patterns into (default: current directory)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all canonical skills and exit",
    )

    args = parser.parse_args()

    skills = load_canonical_skills()
    if not skills:
        print("No canonical skills found in skills directory.", file=sys.stderr)
        sys.exit(1)

    if args.list:
        print(f"\nCanonical Agentic Design Patterns ({len(skills)} available):\n")
        print(f"{'Command':<22} | {'Description'}")
        print("-" * 80)
        for s in skills:
            print(f"/{s['name']:<21} | {s['description']}")
        print()
        sys.exit(0)

    target_dir = Path(args.output_dir).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n🚀 Syncing {len(skills)} Agentic Patterns into: {target_dir}")

    targets = [t.strip().lower() for t in args.target.split(",")]
    if "all" in targets:
        # Use unique exporter functions to avoid duplicate runs
        seen_funcs = set()
        active_exporters = []
        for name, func in EXPORTERS.items():
            if func not in seen_funcs:
                seen_funcs.add(func)
                active_exporters.append((name, func))
    else:
        seen_funcs = set()
        active_exporters = []
        for t in targets:
            if t in EXPORTERS and EXPORTERS[t] not in seen_funcs:
                seen_funcs.add(EXPORTERS[t])
                active_exporters.append((t, EXPORTERS[t]))
        unrecognized = [t for t in targets if t not in EXPORTERS and t != "all"]
        if unrecognized:
            print(f"Warning: Unrecognized target harness(es): {', '.join(unrecognized)}", file=sys.stderr)

    for name, exporter_func in active_exporters:
        exporter_func(skills, target_dir)

    print("\n✨ Pattern synchronization complete!\n")


if __name__ == "__main__":
    main()
