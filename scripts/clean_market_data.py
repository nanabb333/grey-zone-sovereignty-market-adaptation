import pandas as pd
from pathlib import Path


# Define the raw input file paths.
TWSE_RAW_FILE = Path("data/raw/twse_twii_yahoo.csv")
TSMC_RAW_FILE = Path("data/raw/tsmc_2330tw_yahoo.csv")
NASDAQ_RAW_FILE = Path("data/raw/nasdaq_ixic_yahoo.csv")
NVIDIA_RAW_FILE = Path("data/raw/nvidia_nvda_yahoo.csv")
SOX_RAW_FILE = Path("data/raw/sox_yahoo.csv")
# Define the cleaned output file path.
OUTPUT_FILE = Path("data/processed/market.csv")


def load_yahoo_close(path, close_column_name):
    # Read a Yahoo Finance CSV file.
    data = pd.read_csv(path)

    # Convert Yahoo's Date column into a standardized date column.
    data["date"] = pd.to_datetime(data["Date"])

    # Keep only the standardized date and closing price columns.
    data = data[["date", "Close"]]

    # Rename the closing price column to the project-specific variable name.
    data = data.rename(columns={"Close": close_column_name})

    # Return the cleaned two-column dataset.
    return data


def main():
    # Create the processed data directory before writing outputs.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Load and clean the TWSE Index raw data.
    twse = load_yahoo_close(TWSE_RAW_FILE, "twse_close")

    # Load and clean the TSMC raw data.
    tsmc = load_yahoo_close(TSMC_RAW_FILE, "tsmc_close")

    # Load and clean the NASDAQ Composite raw data.
    nasdaq = load_yahoo_close(NASDAQ_RAW_FILE, "nasdaq_close")

    # Load and clean the NVIDIA raw data.
    nvidia = load_yahoo_close(NVIDIA_RAW_FILE, "nvidia_close")

    # Load and clean the Philadelphia Semiconductor Index raw data.
    sox = load_yahoo_close(SOX_RAW_FILE, "sox_close")

    # Merge TWSE and TSMC data on the standardized date column.
    market = twse.merge(tsmc, on="date", how="outer")

    # Merge NASDAQ data into the combined market dataset.
    market = market.merge(nasdaq, on="date", how="outer")

    # Merge NVIDIA data into the combined market dataset.
    market = market.merge(nvidia, on="date", how="outer")

    # Merge SOX data into the combined market dataset.
    market = market.merge(sox, on="date", how="outer")

    # Sort observations chronologically.
    market = market.sort_values("date")

    # Format dates as YYYY-MM-DD strings for clean CSV output.
    market["date"] = market["date"].dt.strftime("%Y-%m-%d")

    # Keep only the required final columns.
    market = market[
        [
            "date",
            "twse_close",
            "tsmc_close",
            "nasdaq_close",
            "nvidia_close",
            "sox_close",
        ]
    ]

    # Save the cleaned market dataset.
    market.to_csv(OUTPUT_FILE, index=False)

    # Print the cleaned dataset date range.
    print(f"Date range: {market['date'].min()} to {market['date'].max()}")

    # Print the cleaned dataset row count.
    print(f"Row count: {len(market)}")

    # Print missing-value counts for each output column.
    print("Missing value counts:")
    print(market.isna().sum())


# Run the cleaning workflow when the script is executed directly.
if __name__ == "__main__":
    main()
