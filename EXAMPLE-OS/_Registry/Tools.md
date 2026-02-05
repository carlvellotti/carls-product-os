# Tools

Inventory of custom tools built to automate PM workflows.

---

## Available Tools

### metrics-pull

**Location:** `Tools/metrics-pull/`

**Purpose:** Pull key product metrics from configured data sources (Amplitude, Mixpanel, database) and output formatted summaries.

**Usage:**
```bash
# Pull all metrics (last 7 days)
python Tools/metrics-pull/run.py

# Pull specific metric
python Tools/metrics-pull/run.py --metric dau

# Change time period
python Tools/metrics-pull/run.py --period 30d

# Output as JSON
python Tools/metrics-pull/run.py --output json
```

**Configuration:** Edit `Tools/metrics-pull/config.json` to configure data sources and credentials.

**Environment Variables Required:**
- `AMPLITUDE_API_KEY`
- `AMPLITUDE_API_SECRET`
- `MIXPANEL_API_SECRET`
- `ANALYTICS_DB_URL`

**Use Cases:**
- Weekly stakeholder updates
- PRD baseline metrics
- Trend investigation

---

### meeting-prep

**Location:** `Tools/meeting-prep/`

**Purpose:** Gather context for an upcoming meeting by searching relevant files and extracting action items.

**Usage:**
```bash
# Prep for 1:1 with a person
python Tools/meeting-prep/run.py "Sarah Kim"

# Prep for meeting type
python Tools/meeting-prep/run.py "Design Review" --type review

# Meeting types: 1on1, review, planning, customer
```

**Use Cases:**
- 1:1 preparation
- Stakeholder meeting prep
- Customer call prep

**What It Searches:**
- Previous meeting notes with the person
- Open action items
- Related documents
- Active projects

---

## Tool Development Guidelines

### Creating a New Tool

1. Create folder in `Tools/` with tool name
2. Add `run.py` with:
   - Clear docstring with usage
   - Argparse for CLI interface
   - Sensible defaults
3. Add `README.md` with:
   - Quick start examples
   - Configuration details
   - Integration notes
4. Add `config.json` if needed for settings
5. Update this file with tool entry

### Best Practices

- **Idempotent:** Running multiple times should be safe
- **Readable output:** Default to human-readable (markdown)
- **Machine output:** Support `--output json` for automation
- **Fail gracefully:** Handle missing files/data without crashing
- **Document dependencies:** List required env vars and packages

### Integration with Claude

Tools can be invoked by Claude via bash:
```
python Tools/tool-name/run.py [args]
```

Claude skills can wrap tools with additional context and formatting.

---

## Planned Tools

| Tool | Purpose | Status |
|------|---------|--------|
| `ticket-sync` | Sync Jira/Linear tickets to local markdown | Planned |
| `research-import` | Import Dovetail/similar research data | Planned |
| `changelog-gen` | Generate changelog from git commits | Planned |
| `stakeholder-report` | Auto-generate monthly stakeholder report | Planned |
