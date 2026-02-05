# Metrics Pull Tool

Pulls key product metrics from configured data sources and outputs a formatted summary.

## Quick Start

```bash
# Pull all metrics (last 7 days)
python run.py

# Pull specific metric
python run.py --metric dau

# Change time period
python run.py --period 30d

# Output as JSON
python run.py --output json
```

## Output Example

```markdown
# Metrics Summary
**Generated:** 2025-01-15 09:30
**Period:** Last 7 days

## Engagement
- **DAU:** 12,450 (+4.7% vs prior period)
- **WAU:** 45,200 (+4.9% vs prior period)
- **Session Duration Avg:** 8.3 minutes (+5.1% vs prior period)

## Product
- **Grades Entered:** 89,400 (+4.9% vs prior period)
- **Feature Adoption Gradebook:** 67.2% (+4.2% vs prior period)

## Growth
- **New Signups:** 342 (+14.8% vs prior period)
- **Schools Active:** 1,847 (+2.5% vs prior period)
- **NPS Score:** 47 (+4.4% vs prior period)
```

## Configuration

Edit `config.json` to configure data sources:

### Amplitude
- Set `api_key_env` and `api_secret_env` to environment variable names containing credentials
- Configure `project_id` for your Amplitude project
- List metrics to pull in the `metrics` array

### Mixpanel
- Set `api_secret_env` to environment variable name
- Configure `project_id`
- List metrics to pull

### Database
- Set `connection_string_env` to environment variable with DB connection string
- Direct SQL queries for metrics not available in product analytics tools

## Environment Variables

Set these before running:

```bash
export AMPLITUDE_API_KEY="your-key"
export AMPLITUDE_API_SECRET="your-secret"
export MIXPANEL_API_SECRET="your-secret"
export ANALYTICS_DB_URL="postgresql://..."
```

## Adding New Metrics

1. Add metric name to the appropriate source in `config.json`
2. Add fetch logic in the corresponding `fetch_*_metrics()` function in `run.py`
3. Add display logic in `output_markdown()` under the appropriate category

## Integration with Claude

Claude can run this tool to get current metrics for:
- Weekly stakeholder updates
- PRD success metrics baselines
- Identifying trends to investigate

Example prompt: "Pull current metrics and include them in my weekly update"

## Alerts

Configure `alerts` in `config.json` to flag concerning changes:
- `dau_drop_threshold`: Alert if DAU drops more than this % (default: -10%)
- `nps_drop_threshold`: Alert if NPS drops more than this % (default: -5%)
