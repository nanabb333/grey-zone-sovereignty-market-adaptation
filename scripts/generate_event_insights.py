import csv
import json
from pathlib import Path


DASHBOARD_DATA_FILE = Path("results/dashboard_data.csv")
MECHANISM_SUMMARY_FILE = Path("results/mechanism_summary.csv")
EVENT_INSIGHTS_FILE = Path("results/event_insights.json")


def read_csv_rows(path):
    with path.open(newline="") as file:
        return list(csv.DictReader(file))


def parse_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def format_percent(value):
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


def build_mechanism_lookup(mechanism_rows):
    lookup = {}
    for row in mechanism_rows:
        lookup[row["mechanism"]] = {
            "mean_car_value": parse_float(row["mean_car_value"]),
            "event_count": row["event_count"],
            "successful_event_count": row["successful_event_count"],
            "failed_event_count": row["failed_event_count"],
        }
    return lookup


def add_insight(insights, event, category, title, explanation, evidence):
    insights.append(
        {
            "event_id": event["event_id"],
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "mechanism": event["mechanism"],
            "category": category,
            "title": title,
            "explanation": explanation,
            "evidence": evidence,
            "use_note": "Rule-based educational insight. Not investment advice.",
        }
    )


def generate_insights(events, mechanism_lookup):
    insights = []

    for event in sorted(events, key=lambda row: row["event_id"]):
        if event["status"] != "success":
            continue

        car_value = parse_float(event["car_value"])
        if car_value is None:
            continue

        mechanism = event["mechanism"]
        mechanism_summary = mechanism_lookup.get(mechanism, {})
        mechanism_mean = mechanism_summary.get("mean_car_value")

        if mechanism == "Risk" and car_value > 0:
            add_insight(
                insights,
                event,
                "Positive reaction despite Risk classification",
                "Positive abnormal CAR for a Risk event",
                (
                    f"{event['event_name']} is classified as Risk, but the selected "
                    f"asset outperformed its benchmark during the event window."
                ),
                {
                    "rule": "mechanism == Risk and car_value > 0",
                    "car_value": car_value,
                    "car_percent": format_percent(car_value),
                },
            )

        if mechanism == "Strategic_Importance" and car_value < 0:
            add_insight(
                insights,
                event,
                "Negative reaction despite Strategic Importance classification",
                "Negative abnormal CAR for a Strategic_Importance event",
                (
                    f"{event['event_name']} is classified as Strategic_Importance, "
                    "but the selected asset underperformed its benchmark during the "
                    "event window."
                ),
                {
                    "rule": "mechanism == Strategic_Importance and car_value < 0",
                    "car_value": car_value,
                    "car_percent": format_percent(car_value),
                },
            )

        if mechanism_mean is None:
            continue

        event_strength = abs(car_value)
        average_strength = abs(mechanism_mean)

        if event_strength > average_strength:
            add_insight(
                insights,
                event,
                "Reaction stronger than historical average",
                "Event reaction exceeds mechanism average magnitude",
                (
                    f"{event['event_name']} had a larger abnormal-CAR magnitude "
                    f"than the current {mechanism} mechanism average."
                ),
                {
                    "rule": "abs(car_value) > abs(mechanism_mean_car)",
                    "car_value": car_value,
                    "car_percent": format_percent(car_value),
                    "mechanism_mean_car": mechanism_mean,
                    "mechanism_mean_percent": format_percent(mechanism_mean),
                },
            )
        elif event_strength < average_strength:
            add_insight(
                insights,
                event,
                "Reaction weaker than historical average",
                "Event reaction is below mechanism average magnitude",
                (
                    f"{event['event_name']} had a smaller abnormal-CAR magnitude "
                    f"than the current {mechanism} mechanism average."
                ),
                {
                    "rule": "abs(car_value) < abs(mechanism_mean_car)",
                    "car_value": car_value,
                    "car_percent": format_percent(car_value),
                    "mechanism_mean_car": mechanism_mean,
                    "mechanism_mean_percent": format_percent(mechanism_mean),
                },
            )

    return insights


def main():
    events = read_csv_rows(DASHBOARD_DATA_FILE)
    mechanism_rows = read_csv_rows(MECHANISM_SUMMARY_FILE)
    mechanism_lookup = build_mechanism_lookup(mechanism_rows)
    insights = generate_insights(events, mechanism_lookup)

    output = {
        "source_files": [
            str(DASHBOARD_DATA_FILE),
            str(MECHANISM_SUMMARY_FILE),
        ],
        "method": "deterministic_rule_based_insight_generator",
        "rules": [
            "Positive reaction despite Risk classification: mechanism == Risk and car_value > 0",
            "Negative reaction despite Strategic Importance classification: mechanism == Strategic_Importance and car_value < 0",
            "Reaction stronger than historical average: abs(car_value) > abs(mechanism_mean_car)",
            "Reaction weaker than historical average: abs(car_value) < abs(mechanism_mean_car)",
        ],
        "insight_count": len(insights),
        "insights": insights,
    }

    EVENT_INSIGHTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EVENT_INSIGHTS_FILE.write_text(json.dumps(output, indent=2))
    print(f"event insights saved to {EVENT_INSIGHTS_FILE}")
    print(f"insights generated: {len(insights)}")


if __name__ == "__main__":
    main()
