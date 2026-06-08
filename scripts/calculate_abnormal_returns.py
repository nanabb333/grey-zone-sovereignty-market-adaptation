from pathlib import Path

import pandas as pd


# Define project paths.
MARKET_FILE = Path("data/processed/market.csv")
EVENT_FILE = Path("data/events/event_sample.csv")
ABNORMAL_RETURN_FILE = Path("data/processed/market_abnormal_returns.csv")
EVENT_RESULT_FILE = Path("results/event_abnormal_return_summary.csv")

# Define the event windows used in the dissertation analysis.
EVENT_WINDOWS = [1, 3, 7]


def load_market_data():
    # Load the cleaned market dataset.
    market = pd.read_csv(MARKET_FILE)

    # Convert dates to datetime so that sorting and matching work correctly.
    market["date"] = pd.to_datetime(market["date"])

    # Sort chronologically before calculating returns.
    market = market.sort_values("date").reset_index(drop=True)

    return market


def calculate_daily_abnormal_returns(market):
    # Calculate daily percent returns for Taiwan and benchmark markets.
    market["twse_return"] = market["twse_close"].pct_change(fill_method=None) * 100
    market["tsmc_return"] = market["tsmc_close"].pct_change(fill_method=None) * 100
    market["nasdaq_return"] = market["nasdaq_close"].pct_change(fill_method=None) * 100
    market["sox_return"] = market["sox_close"].pct_change(fill_method=None) * 100

    # TWSE abnormal returns are benchmark-adjusted against NASDAQ.
    market["twse_abnormal_return"] = (
        market["twse_return"] - market["nasdaq_return"]
    )

    # TSMC abnormal returns are benchmark-adjusted against the SOX index.
    market["tsmc_abnormal_return"] = market["tsmc_return"] - market["sox_return"]

    return market


def load_events():
    # Load the event sample used for the event-window calculations.
    events = pd.read_csv(EVENT_FILE)

    # Keep only the final event-study sample if an inclusion flag is present.
    if "include_in_event_study" in events.columns:
        events = events[events["include_in_event_study"] == "Yes"].copy()

    # Accept either date naming convention.
    if "event_date" not in events.columns and "date" in events.columns:
        events = events.rename(columns={"date": "event_date"})

    # Standardize event dates.
    events["event_date"] = pd.to_datetime(events["event_date"])

    return events


def find_event_row(market, event_date):
    # Match the event to the nearest available trading day on or after the event date.
    possible_rows = market.index[market["date"] >= event_date]

    if len(possible_rows) == 0:
        return None

    return possible_rows[0]


def calculate_event_summary(market, events):
    event_rows = []

    for _, event in events.iterrows():
        event_index = find_event_row(market, event["event_date"])

        # Skip events outside the available market-data range.
        if event_index is None:
            continue

        market_row = market.loc[event_index]

        result = {
            "event_name": event["event_name"],
            "event_date": event["event_date"].strftime("%Y-%m-%d"),
            "mechanism": event["mechanism"],
            "matched_trading_date": market_row["date"].strftime("%Y-%m-%d"),
            "twse_day0_ar": market_row["twse_abnormal_return"],
            "tsmc_day0_ar": market_row["tsmc_abnormal_return"],
        }

        # Calculate forward CAR windows using trading-day rows.
        for window in EVENT_WINDOWS:
            window_rows = market.iloc[event_index:event_index + window + 1]

            result[f"twse_car_{window}"] = window_rows[
                "twse_abnormal_return"
            ].sum()
            result[f"tsmc_car_{window}"] = window_rows[
                "tsmc_abnormal_return"
            ].sum()

        event_rows.append(result)

    return pd.DataFrame(event_rows)


def main():
    # Create output folders.
    ABNORMAL_RETURN_FILE.parent.mkdir(parents=True, exist_ok=True)
    EVENT_RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Calculate daily abnormal returns.
    market = load_market_data()
    market = calculate_daily_abnormal_returns(market)

    # Save the full abnormal-return dataset.
    market_to_save = market.copy()
    market_to_save["date"] = market_to_save["date"].dt.strftime("%Y-%m-%d")
    market_to_save.to_csv(ABNORMAL_RETURN_FILE, index=False)

    # Calculate and save event-window summaries.
    events = load_events()
    event_summary = calculate_event_summary(market, events)
    event_summary.to_csv(EVENT_RESULT_FILE, index=False)

    print(f"Saved daily abnormal returns to {ABNORMAL_RETURN_FILE}")
    print(f"Saved event summary to {EVENT_RESULT_FILE}")
    print()
    print("Average event-window results by mechanism:")
    print(event_summary.groupby("mechanism").mean(numeric_only=True))


if __name__ == "__main__":
    main()
