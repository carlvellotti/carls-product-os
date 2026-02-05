#!/usr/bin/env python3
"""
Metrics Pull Tool
Pulls key product metrics from configured data sources and outputs a summary.

Usage:
    python run.py                    # Pull all configured metrics
    python run.py --metric dau       # Pull specific metric
    python run.py --period 7d        # Specify time period
    python run.py --output json      # Output as JSON instead of markdown
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Load configuration
CONFIG_PATH = Path(__file__).parent / "config.json"

def load_config():
    """Load metrics configuration from config.json"""
    with open(CONFIG_PATH) as f:
        return json.load(f)

def fetch_amplitude_metrics(config, period_days):
    """
    Fetch metrics from Amplitude.

    In production, this would use the Amplitude API:
    https://developers.amplitude.com/docs/dashboard-rest-api
    """
    # Placeholder - would make API call like:
    # response = requests.get(
    #     f"{config['amplitude']['endpoint']}/events/segmentation",
    #     headers={"Authorization": f"Bearer {config['amplitude']['api_key']}"},
    #     params={"e": json.dumps({"event_type": "page_view"}), "start": start_date, "end": end_date}
    # )

    return {
        "dau": {"current": 12450, "previous": 11890, "change": 4.7},
        "wau": {"current": 45200, "previous": 43100, "change": 4.9},
        "session_duration_avg": {"current": 8.3, "previous": 7.9, "change": 5.1, "unit": "minutes"},
        "grades_entered": {"current": 89400, "previous": 85200, "change": 4.9},
    }

def fetch_mixpanel_metrics(config, period_days):
    """
    Fetch metrics from Mixpanel.

    In production, this would use the Mixpanel API:
    https://developer.mixpanel.com/reference/overview
    """
    # Placeholder
    return {
        "feature_adoption_gradebook": {"current": 67.2, "previous": 64.5, "change": 4.2, "unit": "%"},
        "feature_adoption_reports": {"current": 43.1, "previous": 41.8, "change": 3.1, "unit": "%"},
    }

def fetch_database_metrics(config, period_days):
    """
    Fetch metrics directly from database.

    In production, this would connect to your analytics DB:
    """
    # Placeholder - would use something like:
    # conn = psycopg2.connect(config['database']['connection_string'])
    # cursor.execute("SELECT COUNT(*) FROM users WHERE created_at > %s", [start_date])

    return {
        "new_signups": {"current": 342, "previous": 298, "change": 14.8},
        "schools_active": {"current": 1847, "previous": 1802, "change": 2.5},
        "nps_score": {"current": 47, "previous": 45, "change": 4.4},
    }

def format_metric(name, data):
    """Format a single metric for display"""
    change_symbol = "+" if data["change"] > 0 else ""
    unit = data.get("unit", "")
    return f"- **{name}:** {data['current']}{unit} ({change_symbol}{data['change']}% vs prior period)"

def output_markdown(metrics, period_days):
    """Output metrics as markdown"""
    output = [
        f"# Metrics Summary",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Period:** Last {period_days} days",
        "",
        "## Engagement",
    ]

    engagement_metrics = ["dau", "wau", "session_duration_avg"]
    for name in engagement_metrics:
        if name in metrics:
            output.append(format_metric(name.upper().replace("_", " "), metrics[name]))

    output.extend(["", "## Product"])
    product_metrics = ["grades_entered", "feature_adoption_gradebook", "feature_adoption_reports"]
    for name in product_metrics:
        if name in metrics:
            output.append(format_metric(name.replace("_", " ").title(), metrics[name]))

    output.extend(["", "## Growth"])
    growth_metrics = ["new_signups", "schools_active", "nps_score"]
    for name in growth_metrics:
        if name in metrics:
            output.append(format_metric(name.replace("_", " ").title(), metrics[name]))

    return "\n".join(output)

def output_json(metrics):
    """Output metrics as JSON"""
    return json.dumps({
        "generated_at": datetime.now().isoformat(),
        "metrics": metrics
    }, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Pull product metrics")
    parser.add_argument("--metric", help="Specific metric to pull")
    parser.add_argument("--period", default="7d", help="Time period (e.g., 7d, 30d)")
    parser.add_argument("--output", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    # Parse period
    period_days = int(args.period.replace("d", ""))

    # Load config
    config = load_config()

    # Fetch metrics from all sources
    metrics = {}

    if config.get("amplitude", {}).get("enabled"):
        metrics.update(fetch_amplitude_metrics(config, period_days))

    if config.get("mixpanel", {}).get("enabled"):
        metrics.update(fetch_mixpanel_metrics(config, period_days))

    if config.get("database", {}).get("enabled"):
        metrics.update(fetch_database_metrics(config, period_days))

    # Filter to specific metric if requested
    if args.metric:
        metrics = {k: v for k, v in metrics.items() if args.metric.lower() in k.lower()}

    # Output
    if args.output == "json":
        print(output_json(metrics))
    else:
        print(output_markdown(metrics, period_days))

if __name__ == "__main__":
    main()
