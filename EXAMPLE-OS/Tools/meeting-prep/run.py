#!/usr/bin/env python3
"""
Meeting Prep Tool
Gathers context for an upcoming meeting by searching relevant files.

Usage:
    python run.py "Sarah Kim"                    # Prep for meeting with person
    python run.py "Design Review" --type review  # Prep for specific meeting type
    python run.py --calendar                     # Prep for next meeting from calendar
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
import re

# Base paths
BASE_PATH = Path(__file__).parent.parent.parent
PROJECTS_PATH = BASE_PATH / "Projects"
TEMPLATES_PATH = BASE_PATH / "Templates"

def find_related_files(search_term, base_path=BASE_PATH):
    """Find files related to a person or topic"""
    related = []
    search_lower = search_term.lower()

    for path in base_path.rglob("*.md"):
        # Skip templates and registry
        if "Templates" in str(path) or "_Registry" in str(path):
            continue

        try:
            content = path.read_text()
            filename = path.name.lower()

            # Check filename and content
            if search_lower in filename or search_lower in content.lower():
                # Score by relevance
                score = 0
                if search_lower in filename:
                    score += 10
                score += content.lower().count(search_lower)

                related.append({
                    "path": str(path.relative_to(base_path)),
                    "name": path.name,
                    "score": score,
                    "modified": datetime.fromtimestamp(path.stat().st_mtime)
                })
        except Exception:
            continue

    # Sort by score descending, then by recency
    related.sort(key=lambda x: (-x["score"], -x["modified"].timestamp()))
    return related[:10]

def extract_action_items(file_path):
    """Extract open action items from a file"""
    actions = []
    try:
        content = Path(file_path).read_text()
        # Find unchecked items
        for line in content.split("\n"):
            if re.match(r"^\s*-\s*\[\s*\]", line):
                actions.append(line.strip())
    except Exception:
        pass
    return actions

def find_previous_meetings(person_name, base_path=BASE_PATH):
    """Find previous 1:1 or meeting notes with a person"""
    meetings = []
    search_lower = person_name.lower()

    for path in base_path.rglob("*.md"):
        filename_lower = path.name.lower()
        if "1on1" in filename_lower or "meeting" in filename_lower:
            try:
                content = path.read_text()
                if search_lower in content.lower() or search_lower in filename_lower:
                    meetings.append({
                        "path": str(path.relative_to(base_path)),
                        "name": path.name,
                        "modified": datetime.fromtimestamp(path.stat().st_mtime)
                    })
            except Exception:
                continue

    meetings.sort(key=lambda x: -x["modified"].timestamp())
    return meetings[:5]

def get_active_projects():
    """Get list of active projects"""
    projects = []
    if PROJECTS_PATH.exists():
        for path in PROJECTS_PATH.iterdir():
            if path.is_dir() and not path.name.startswith("_"):
                projects.append(path.name)
    return projects

def prep_for_person(person_name):
    """Prepare context for a meeting with a specific person"""
    output = [
        f"# Meeting Prep: {person_name}",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    # Find previous meetings
    prev_meetings = find_previous_meetings(person_name)
    if prev_meetings:
        output.append("## Previous Meetings")
        for m in prev_meetings[:3]:
            output.append(f"- [[{m['name']}]] - {m['modified'].strftime('%Y-%m-%d')}")
        output.append("")

        # Extract action items from most recent
        if prev_meetings:
            recent_path = BASE_PATH / prev_meetings[0]["path"]
            actions = extract_action_items(recent_path)
            if actions:
                output.append("## Open Action Items (from last meeting)")
                for action in actions[:5]:
                    output.append(action)
                output.append("")

    # Find related files
    related = find_related_files(person_name)
    if related:
        output.append("## Related Documents")
        for r in related[:5]:
            output.append(f"- [[{r['name']}]]")
        output.append("")

    # Active projects for context
    projects = get_active_projects()
    if projects:
        output.append("## Active Projects (for context)")
        for p in projects[:5]:
            output.append(f"- {p}")
        output.append("")

    # Suggested topics
    output.extend([
        "## Suggested Topics",
        "- [ ] Follow up on action items above",
        "- [ ] Share relevant project updates",
        "- [ ] ",
        "",
        "## Notes Space",
        "_Use this space during the meeting_",
        "",
        "-",
    ])

    return "\n".join(output)

def prep_for_meeting_type(meeting_name, meeting_type):
    """Prepare context for a specific type of meeting"""
    output = [
        f"# Meeting Prep: {meeting_name}",
        f"**Type:** {meeting_type}",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]

    # Type-specific prep
    if meeting_type == "review":
        output.extend([
            "## Review Checklist",
            "- [ ] PRD/spec document ready",
            "- [ ] Key decisions documented",
            "- [ ] Open questions listed",
            "- [ ] Success metrics defined",
            "",
        ])
    elif meeting_type == "planning":
        output.extend([
            "## Planning Checklist",
            "- [ ] Previous sprint/period retro done",
            "- [ ] Backlog prioritized",
            "- [ ] Dependencies identified",
            "- [ ] Capacity confirmed",
            "",
        ])
    elif meeting_type == "customer":
        output.extend([
            "## Customer Call Checklist",
            "- [ ] Customer context reviewed",
            "- [ ] Research questions prepared",
            "- [ ] Recording permission planned",
            "- [ ] Note-taker assigned",
            "",
            "## Do NOT Promise",
            "- Specific timelines",
            "- Unplanned features",
            "",
        ])

    # Find related files
    related = find_related_files(meeting_name)
    if related:
        output.append("## Related Documents")
        for r in related[:5]:
            output.append(f"- [[{r['name']}]]")
        output.append("")

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Prepare for upcoming meeting")
    parser.add_argument("meeting", nargs="?", help="Person name or meeting name")
    parser.add_argument("--type", choices=["1on1", "review", "planning", "customer"],
                       help="Meeting type")
    parser.add_argument("--calendar", action="store_true",
                       help="Prep for next meeting from calendar")
    parser.add_argument("--output", default="markdown", choices=["markdown", "json"])
    args = parser.parse_args()

    if args.calendar:
        # Would integrate with calendar MCP
        print("Calendar integration not configured. Specify meeting name or person.")
        return

    if not args.meeting:
        print("Please specify a person name or meeting name")
        return

    # Determine if this is a person or meeting type
    if args.type:
        result = prep_for_meeting_type(args.meeting, args.type)
    else:
        # Assume it's a person name
        result = prep_for_person(args.meeting)

    print(result)

if __name__ == "__main__":
    main()
