# Carl's Product OS

**A Personal Operating System for Claude Code**

---

## Introduction

The biggest question I get after my Claude Code course: *"How should I set up my space?"*

Claude Code is infinitely flexible. There's no single right way to organize it, which is both liberating and paralyzing. This repo shows how I personally use Claude Code day-to-day, plus the principles behind each decision.

This setup is battle-tested across content creation, product work, and running a small business. But it's not gospel. Try things, break things, and see what actually works for your workflow.

---

## Structure Overview

*[Screenshot placeholder - will add image]*

| Folder/File | Purpose |
|-------------|---------|
| `CLAUDE.md` | Entry point. Claude reads this automatically on every conversation. |
| `GOALS.md` | Your identity, what you own, and current goals. |
| `Tasks/` | Simple backlog → active → archive flow. |
| `Projects/` | Discrete work with its own context, research, and outputs. |
| `Workflows/` | Repeatable processes. Mini-workspaces you run again and again. |
| `Meetings/` | Notes organized by meeting type. |
| `Knowledge/` | Persistent reference material that spans projects. |
| `Templates/` | Document structures for consistent outputs. |
| `.claude/skills/` | Slash commands. Type `/skillname` to trigger. |
| `Tools/` | Scripts, utilities, and automations. |
| `_Registry/` | System reference and documentation. |
| `_temp/` | Drop zone for files in transit. |

---

## Key Concepts

### Projects vs Workflows

- **Projects** are one-off. They have a clear end state. When done, they're archived.
- **Workflows** are repeatable. They're processes you run many times with different inputs.

*Example: "Launch newsletter" is a project. "Write weekly newsletter" is a workflow.*

### Templates vs Workflows

- **Templates** provide structure. They're the skeleton of a document.
- **Workflows** provide process. They're instructions for Claude to follow.

*A template says what the output looks like. A workflow says how to create it.*

### Knowledge vs Project Research

- **Knowledge** is persistent. It's reference material useful across many projects.
- **Project research** is scoped. It lives inside the project folder and gets archived with it.

*Your company's brand guidelines go in Knowledge. Competitor research for a specific launch goes in the project.*

---

## Getting Started

1. **Browse `EXAMPLE-OS/`** — See a working example with real content
2. **Copy `BLANK-OS/`** — Rename it to your workspace name
3. **Start with `CLAUDE.md` + `GOALS.md`** — These two files give you 80% of the value
4. **Add workflows and skills as you repeat things** — Don't over-engineer upfront

You don't need everything on day one. Start minimal, add structure when friction appears.

---

## FAQ

**Where does planning go?**

Depends on scope:
- High-level goals and priorities → `GOALS.md`
- Planning for a specific deliverable → Inside that `Project/`
- Planning that's part of a repeatable process → Inside that `Workflow/`

**When do I create a template vs a workflow?**

- If you just need consistent document structure → Template
- If you need Claude to follow steps, do research, or make decisions → Workflow
- Often you'll have both: a workflow that uses a template for its output

**What goes in `.claude/skills/` vs `Workflows/`?**

- Skills are quick commands triggered with `/skillname`
- Workflows are fuller processes, often with their own context files
- Start with workflows. Promote to skills when you want faster access.

---

## About

Built by **Carl Vellotti** as part of teaching product managers to use Claude Code effectively.

- **Course**: [Claude Code for PMs](https://ccforpms.com)
- **Twitter/X**: [@carlvellotti](https://twitter.com/carlvellotti)
- **LinkedIn**: [linkedin.com/in/carlvellotti](https://linkedin.com/in/carlvellotti)
