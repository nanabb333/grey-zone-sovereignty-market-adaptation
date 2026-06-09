import csv
from pathlib import Path

from abnormal_returns import calculate_abnormal_returns
from car_calculator import calculate_car
from data_loader import load_market_data
from figure_generator import generate_event_figure
from report_generator import generate_event_report
from results_writer import (
    initialize_event_results,
    save_event_results,
    save_failed_event_result,
    write_dashboard_data,
    write_executive_summary,
    write_mechanism_summary,
    write_run_summary,
)
from returns_calculator import calculate_returns


EVENTS_FILE = Path("events/events.csv")

METADATA_FIELDS = [
    "event_id",
    "event_name",
    "event_date",
    "mechanism",
    "event_type",
    "asset",
    "benchmark",
    "event_window_start",
    "event_window_end",
]

ENGINE_STEPS = [
    "Load market data",
    "Clean and align data",
    "Calculate returns",
    "Calculate abnormal returns",
    "Calculate CAR",
    "Save results",
    "Generate figure",
    "Generate report",
]


def print_event_metadata(event):
    print("Event Metadata")
    print("--------------")
    for field in METADATA_FIELDS:
        print(f"{field}: {event[field]}")


def print_engine_steps():
    print()
    print("Planned Engine Steps")
    print("--------------------")
    for step_number, step in enumerate(ENGINE_STEPS, start=1):
        print(f"{step_number}. {step}")


def print_market_data_success(market_data, asset, benchmark):
    print()
    print("Market Data")
    print("-----------")
    print("market data loaded successfully")
    print(f"rows loaded: {len(market_data)}")
    print(f"asset column used: {asset}")
    print(f"benchmark column used: {benchmark}")


def print_returns_success(market_data):
    print()
    print("Returns")
    print("-------")
    print("returns calculated successfully")
    print(f"rows after return calculation: {len(market_data)}")
    print("new columns created: asset_return, benchmark_return")


def print_abnormal_returns_success(abnormal_returns_data):
    print()
    print("Abnormal Returns")
    print("----------------")
    print("abnormal returns calculated successfully")
    print("new column created: abnormal_return")
    print(f"number of rows available: {len(abnormal_returns_data)}")


def print_car_success(car_value, event_window_data, window_start, window_end):
    print()
    print("CAR")
    print("---")
    print("CAR calculated successfully")
    print(f"event window start: {window_start}")
    print(f"event window end: {window_end}")
    print(f"number of trading rows in event window: {len(event_window_data)}")
    print(f"CAR value: {car_value}")


def print_results_success(event_results_path, event_window_data_path):
    print()
    print("Results")
    print("-------")
    print("event results saved successfully")
    print(f"event results path: {event_results_path}")
    print("event window data saved successfully")
    print(f"event window data path: {event_window_data_path}")


def print_figure_success(figure_path):
    print()
    print("Figures")
    print("-------")
    print("figure generated successfully")
    print(f"figure path: {figure_path}")


def print_report_success(report_path):
    print()
    print("Report")
    print("------")
    print("report generated successfully")
    print(f"report path: {report_path}")


# Single-Event Processor area
def process_one_event(event):
    asset = event["asset"]
    benchmark = event["benchmark"]
    event_date = event["event_date"]
    event_window_start = event["event_window_start"]
    event_window_end = event["event_window_end"]
    market_data = load_market_data(asset, benchmark)
    returns_data = calculate_returns(market_data, asset, benchmark)
    abnormal_returns_data = calculate_abnormal_returns(returns_data)
    car_value, event_window_data = calculate_car(
        abnormal_returns_data,
        event_date,
        event_window_start,
        event_window_end,
    )
    event_results_path, event_window_data_path = save_event_results(
        event,
        car_value,
        event_window_data,
    )
    figure_path = generate_event_figure(event, event_window_data)
    report_path = generate_event_report(
        event,
        car_value,
        event_results_path,
        event_window_data_path,
        figure_path,
    )

    print_event_metadata(event)
    print_market_data_success(market_data, asset, benchmark)
    print_returns_success(returns_data)
    print_abnormal_returns_success(abnormal_returns_data)
    print_car_success(
        car_value,
        event_window_data,
        event_window_start,
        event_window_end,
    )
    print_results_success(event_results_path, event_window_data_path)
    print_figure_success(figure_path)
    print_report_success(report_path)
    print_engine_steps()

    return {
        "event": event,
        "car_value": car_value,
        "event_window_data": event_window_data,
        "event_results_path": event_results_path,
        "event_window_data_path": event_window_data_path,
        "figure_path": figure_path,
        "report_path": report_path,
    }


# Run-Level Controller area
def read_events(events_file):
    with events_file.open(newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def main():
    events = read_events(EVENTS_FILE)
    initialize_event_results()

    print(f"Events loaded: {len(events)}")

    for event in events:
        print()
        print(f"Processing {event['event_id']}: {event['event_name']}")
        try:
            process_one_event(event)
        except Exception as error:
            error_message = str(error)
            print(
                f"Failed {event['event_id']}: {event['event_name']} - "
                f"{error_message}"
            )
            save_failed_event_result(event, error_message)

    mechanism_summary_path = write_mechanism_summary()
    dashboard_data_path = write_dashboard_data()
    executive_summary_path = write_executive_summary()
    run_summary_path = write_run_summary()
    print()
    print(f"Mechanism summary saved to {mechanism_summary_path}")
    print(f"Dashboard data saved to {dashboard_data_path}")
    print(f"Executive summary saved to {executive_summary_path}")
    print(f"Run summary saved to {run_summary_path}")


if __name__ == "__main__":
    main()
