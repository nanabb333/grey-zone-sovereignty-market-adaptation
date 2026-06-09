from pathlib import Path

import pandas as pd


RESULTS_FILE = Path("results/event_results.csv")
EVENT_WINDOWS_DIR = Path("results/event_windows")
RUN_SUMMARY_FILE = Path("results/run_summary.md")
MECHANISM_SUMMARY_FILE = Path("results/mechanism_summary.csv")
DASHBOARD_DATA_FILE = Path("results/dashboard_data.csv")
EXECUTIVE_SUMMARY_FILE = Path("results/executive_summary.md")


RESULT_COLUMNS = [
    "event_id",
    "event_name",
    "event_date",
    "mechanism",
    "event_type",
    "asset",
    "benchmark",
    "event_window_start",
    "event_window_end",
    "trading_days_in_window",
    "car_value",
    "status",
    "error_message",
]


def initialize_event_results():
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if RESULTS_FILE.exists():
        RESULTS_FILE.unlink()


def append_event_result(result_row):
    event_results = pd.DataFrame([result_row], columns=RESULT_COLUMNS)
    event_results.to_csv(
        RESULTS_FILE,
        mode="a",
        header=not RESULTS_FILE.exists(),
        index=False,
    )


def save_event_results(event, car_value, event_window_data):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EVENT_WINDOWS_DIR.mkdir(parents=True, exist_ok=True)

    append_event_result(
        {
            "event_id": event["event_id"],
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "mechanism": event["mechanism"],
            "event_type": event["event_type"],
            "asset": event["asset"],
            "benchmark": event["benchmark"],
            "event_window_start": event["event_window_start"],
            "event_window_end": event["event_window_end"],
            "trading_days_in_window": len(event_window_data),
            "car_value": car_value,
            "status": "success",
            "error_message": "",
        }
    )

    event_window_output = event_window_data[
        ["date", "asset_return", "benchmark_return", "abnormal_return"]
    ].copy()
    event_window_data_file = (
        EVENT_WINDOWS_DIR / f"{event['event_id']}_event_window_data.csv"
    )
    event_window_output.to_csv(event_window_data_file, index=False)

    return RESULTS_FILE, event_window_data_file


def save_failed_event_result(event, error_message):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)

    append_event_result(
        {
            "event_id": event["event_id"],
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "mechanism": event["mechanism"],
            "event_type": event["event_type"],
            "asset": event["asset"],
            "benchmark": event["benchmark"],
            "event_window_start": event["event_window_start"],
            "event_window_end": event["event_window_end"],
            "trading_days_in_window": "",
            "car_value": "",
            "status": "failed",
            "error_message": error_message,
        }
    )

    return RESULTS_FILE


def write_run_summary():
    event_results = pd.read_csv(RESULTS_FILE)

    total_events = len(event_results)
    successful_events = (event_results["status"] == "success").sum()
    failed_events = (event_results["status"] == "failed").sum()

    status_rows = event_results[
        [
            "event_id",
            "event_name",
            "mechanism",
            "status",
            "car_value",
            "error_message",
        ]
    ].fillna("")

    status_table_lines = [
        "| event_id | event_name | mechanism | status | car_value | error_message |",
        "|---|---|---|---|---:|---|",
    ]
    for _, row in status_rows.iterrows():
        status_table_lines.append(
            "| "
            + " | ".join(
                [
                    str(row["event_id"]),
                    str(row["event_name"]),
                    str(row["mechanism"]),
                    str(row["status"]),
                    str(row["car_value"]),
                    str(row["error_message"]),
                ]
            )
            + " |"
        )
    status_table = "\n".join(status_table_lines)

    summary = f"""# Taiwan Geopolitical Risk Event Study Engine - Run Summary

## Run-Level Counts

| Metric | Count |
|---|---:|
| Total events | {total_events} |
| Successful events | {successful_events} |
| Failed events | {failed_events} |

## Event Status

{status_table}

## Output Locations

- results/event_results.csv
- results/mechanism_summary.csv
- results/dashboard_data.csv
- results/executive_summary.md
- results/event_windows/
- reports/
- figures/

## Notes

- `status=success` means the event was processed successfully.
- `status=failed` means the event failed but the batch continued.
- `car_value` is benchmark-adjusted abnormal CAR based on the current engine definition.
"""

    RUN_SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    RUN_SUMMARY_FILE.write_text(summary)

    return RUN_SUMMARY_FILE


def write_mechanism_summary():
    event_results = pd.read_csv(RESULTS_FILE)
    successful_events = event_results[event_results["status"] == "success"].copy()
    successful_events["car_value"] = pd.to_numeric(
        successful_events["car_value"],
        errors="coerce",
    )

    summary_rows = []
    for mechanism, mechanism_rows in event_results.groupby("mechanism", sort=True):
        successful_mechanism_rows = successful_events[
            successful_events["mechanism"] == mechanism
        ]
        failed_event_count = (mechanism_rows["status"] == "failed").sum()

        summary_rows.append(
            {
                "mechanism": mechanism,
                "event_count": len(mechanism_rows),
                "mean_car_value": successful_mechanism_rows["car_value"].mean(),
                "min_car_value": successful_mechanism_rows["car_value"].min(),
                "max_car_value": successful_mechanism_rows["car_value"].max(),
                "successful_event_count": len(successful_mechanism_rows),
                "failed_event_count": failed_event_count,
            }
        )

    mechanism_summary = pd.DataFrame(
        summary_rows,
        columns=[
            "mechanism",
            "event_count",
            "mean_car_value",
            "min_car_value",
            "max_car_value",
            "successful_event_count",
            "failed_event_count",
        ],
    )
    mechanism_summary.to_csv(MECHANISM_SUMMARY_FILE, index=False)

    return MECHANISM_SUMMARY_FILE


def get_car_direction(row):
    if row["status"] != "success" or pd.isna(row["car_value"]):
        return "N/A"
    if row["car_value"] > 0:
        return "Positive"
    if row["car_value"] < 0:
        return "Negative"
    return "Neutral"


def write_dashboard_data():
    event_results = pd.read_csv(RESULTS_FILE)
    event_results["car_value"] = pd.to_numeric(
        event_results["car_value"],
        errors="coerce",
    )
    event_results["car_percent"] = event_results["car_value"] * 100
    event_results["car_direction"] = event_results.apply(get_car_direction, axis=1)

    success_mask = event_results["status"] == "success"
    event_results["report_path"] = ""
    event_results["figure_path"] = ""
    event_results["event_window_path"] = ""
    event_results.loc[success_mask, "report_path"] = (
        "reports/" + event_results.loc[success_mask, "event_id"] + "_report.md"
    )
    event_results.loc[success_mask, "figure_path"] = (
        "figures/"
        + event_results.loc[success_mask, "event_id"]
        + "_abnormal_returns.png"
    )
    event_results.loc[success_mask, "event_window_path"] = (
        "results/event_windows/"
        + event_results.loc[success_mask, "event_id"]
        + "_event_window_data.csv"
    )

    dashboard_data = event_results[
        [
            "event_id",
            "event_name",
            "event_date",
            "mechanism",
            "event_type",
            "asset",
            "benchmark",
            "car_value",
            "car_percent",
            "car_direction",
            "status",
            "report_path",
            "figure_path",
            "event_window_path",
        ]
    ]
    dashboard_data.to_csv(DASHBOARD_DATA_FILE, index=False)

    return DASHBOARD_DATA_FILE


def format_event_summary(row):
    if row is None:
        return "N/A"
    return (
        f"{row['event_name']} ({row['event_id']}): "
        f"{row['car_percent']:.2f}% benchmark-adjusted abnormal CAR"
    )


def write_executive_summary():
    event_results = pd.read_csv(RESULTS_FILE)
    mechanism_summary = pd.read_csv(MECHANISM_SUMMARY_FILE)

    event_results["car_value"] = pd.to_numeric(
        event_results["car_value"],
        errors="coerce",
    )
    event_results["car_percent"] = event_results["car_value"] * 100

    total_events = len(event_results)
    successful_events = event_results[event_results["status"] == "success"].copy()
    failed_events = event_results[event_results["status"] == "failed"].copy()

    strongest_positive = None
    positive_events = successful_events[successful_events["car_value"] > 0]
    if not positive_events.empty:
        strongest_positive = positive_events.loc[positive_events["car_value"].idxmax()]

    strongest_negative = None
    negative_events = successful_events[successful_events["car_value"] < 0]
    if not negative_events.empty:
        strongest_negative = negative_events.loc[negative_events["car_value"].idxmin()]

    mechanism_table_lines = [
        "| Mechanism | Events | Successful | Failed | Mean CAR | Min CAR | Max CAR |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for _, row in mechanism_summary.iterrows():
        mechanism_table_lines.append(
            "| "
            + " | ".join(
                [
                    str(row["mechanism"]),
                    str(row["event_count"]),
                    str(row["successful_event_count"]),
                    str(row["failed_event_count"]),
                    f"{row['mean_car_value']:.4f}",
                    f"{row['min_car_value']:.4f}",
                    f"{row['max_car_value']:.4f}",
                ]
            )
            + " |"
        )
    mechanism_table = "\n".join(mechanism_table_lines)

    summary = f"""# Taiwan Geopolitical Risk Event Study Engine - Executive Summary

## Overview

This batch run analyzed Taiwan-related geopolitical and strategic-importance events using the current event-study engine.

| Metric | Count |
|---|---:|
| Events analyzed | {total_events} |
| Successful events | {len(successful_events)} |
| Failed events | {len(failed_events)} |

## Strongest Event Results

- Strongest positive event: {format_event_summary(strongest_positive)}
- Strongest negative event: {format_event_summary(strongest_negative)}

## Mechanism-Level Summary

{mechanism_table}

## Short Interpretation

The current results summarize benchmark-adjusted abnormal CAR by event and mechanism. Positive values indicate that the selected asset outperformed its benchmark during the event window, while negative values indicate underperformance relative to the benchmark. These outputs are intended to support analytical review, dashboard development, and business-facing discussion.

## Important Note

This summary is for academic and educational analytics purposes only. It is not investment advice, policy advice, or an official publication.
"""

    EXECUTIVE_SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)
    EXECUTIVE_SUMMARY_FILE.write_text(summary)

    return EXECUTIVE_SUMMARY_FILE
