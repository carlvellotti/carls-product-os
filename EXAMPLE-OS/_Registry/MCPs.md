# MCP Configuration

Model Context Protocol (MCP) servers configured for this workspace.

---

## Active MCPs

### Google Calendar

**Server:** `google-calendar`
**Purpose:** Access calendar events for meeting prep and scheduling context.

**Capabilities:**
- List upcoming events
- Get event details (attendees, description, location)
- Check availability

**Common Uses:**
- `meeting-prep` skill uses this to find upcoming meetings
- Daily standup pulls today's meetings
- Weekly planning checks the week ahead

**Setup:**
1. Configure OAuth credentials in Claude Desktop settings
2. Authorize GradeFlow Google Workspace account
3. Grant calendar read access

---

### Granola

**Server:** `granola`
**Purpose:** Access meeting transcripts and notes from Granola.

**Capabilities:**
- Search past meeting transcripts
- Get meeting summaries
- Find mentions of topics/people across meetings

**Common Uses:**
- Find what was discussed in previous meetings with a person
- Search for decisions made about a topic
- Extract action items from transcripts

**Setup:**
1. Install Granola MCP server
2. Configure API key in Claude Desktop settings
3. Ensure Granola is running for meetings

---

### Amplitude (Planned)

**Server:** `amplitude`
**Status:** Not yet configured

**Purpose:** Direct access to Amplitude analytics from Claude.

**Planned Capabilities:**
- Query event data
- Pull dashboard metrics
- Run segmentation queries

**Workaround:** Currently using `Tools/metrics-pull/` script with API credentials.

---

### Linear (Planned)

**Server:** `linear`
**Status:** Not yet configured

**Purpose:** Interact with Linear tickets and projects.

**Planned Capabilities:**
- List tickets in a project
- Create/update tickets
- Sync ticket status

**Workaround:** Manual copy-paste from Linear.

---

## Configuration Location

MCP servers are configured in Claude Desktop settings:
- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Example configuration:
```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-google-calendar"]
    },
    "granola": {
      "command": "npx",
      "args": ["-y", "granola-mcp-server"],
      "env": {
        "GRANOLA_API_KEY": "your-key-here"
      }
    }
  }
}
```

---

## MCP Usage in Skills

Skills can reference MCPs with conditional logic:

```markdown
## Instructions
1. Check if calendar MCP is available
2. If yes, fetch upcoming meetings
3. If no, ask user for meeting details
```

This allows skills to gracefully degrade when MCPs aren't configured.

---

## Adding New MCPs

1. Find or build MCP server for the service
2. Add configuration to Claude Desktop settings
3. Test connection: ask Claude to use the MCP
4. Document in this file with capabilities and use cases
5. Update relevant skills to use the MCP
