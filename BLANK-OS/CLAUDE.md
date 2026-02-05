# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Who I Am

<!-- TODO: Describe yourself and your role -->
<!-- Example: I'm a Senior PM at [Company] working on [Product Area]. -->

**Name:** <!-- TODO: Your name -->
**Role:** <!-- TODO: Your title -->
**Team:** <!-- TODO: Your team/org -->

## How This System Works

This is a personal knowledge and task management system designed to work with Claude Code. It organizes:

- **Tasks/** - Active work and backlog items
- **Projects/** - Larger initiatives and project documentation
- **Workflows/** - Repeatable processes and playbooks
- **Meetings/** - Notes from 1:1s, standups, and other meetings
- **Knowledge/** - Reference materials, research, and people notes
- **Templates/** - Reusable document templates
- **Tools/** - Scripts and utilities

## Key Directories

```
Tasks/           → Active tasks and backlog
Projects/        → Project documentation
Workflows/       → Repeatable processes
Meetings/        → Meeting notes (1on1s, standups, one-offs)
Knowledge/       → Reference, Research, People notes
Templates/       → Document templates
Tools/           → Scripts and utilities
_Registry/       → System documentation (tags, tools, MCPs)
_temp/           → Scratch space
```

## Key Commands

<!-- TODO: Add your custom commands/trigger phrases -->

| Say | Does |
|-----|------|
| "standup" | <!-- TODO: Define what this does --> |
| "weekly update" | <!-- TODO: Define what this does --> |
| "new project [name]" | <!-- TODO: Define what this does --> |

## Context Files

When starting work, Claude should read:
- `GOALS.md` - Current objectives and stakeholders
- `Tasks/active.md` - What I'm currently working on

## Notes

- All files are Markdown
- Use `[[wikilinks]]` to connect notes
- Templates in `Templates/` for new documents
