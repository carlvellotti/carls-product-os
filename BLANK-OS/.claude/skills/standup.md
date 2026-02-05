# Standup

<!--
This is a Claude Code skill. Skills are triggered by saying the skill name.
Customize this to define what "standup" does for you.
-->

<command-name>standup</command-name>

<description>
Daily standup routine - reviews tasks and plans the day.
</description>

<instructions>
When the user says "standup", do the following:

1. Read `Tasks/active.md` to see current work
2. Read `Tasks/backlog.md` for upcoming items
3. Check for any meetings today (if calendar integration exists)

Then provide:
- **Yesterday:** Summary of what was completed
- **Today:** What's planned for today
- **Blockers:** Anything that needs attention

Ask if there are any updates to tasks or priorities.
</instructions>

<!-- TODO: Customize this skill for your workflow -->
