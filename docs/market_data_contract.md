# Market Data Contract

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

This document defines the expected market data structure for the Taiwan Geopolitical Risk Event Study Engine.

The engine needs standardized market data so that event-study calculations can run automatically.

## 2. Expected File

The engine expects market data at:

data/market_data.csv

## 3. Required Columns

| Column | Meaning | Example | Required |
|---|---|---|---|
| date | Trading date in YYYY-MM-DD format | 2022-08-02 | Yes |
| TSMC | TSMC adjusted closing price | 500.00 | Yes |
| SOX | Semiconductor benchmark index price | 3000.00 | Yes |
| TWSE | Taiwan market index price | 15000.00 | Recommended |
| NASDAQ | U.S. technology benchmark price | 12000.00 | Recommended |

## 4. Design Logic

Each row should represent one trading day.

Each asset or benchmark should be stored as one column.

This wide format allows the engine to select the asset and benchmark based on events/events.csv.

Example:
- If asset = TSMC and benchmark = SOX, the engine uses the TSMC and SOX columns.
- If asset = TWSE and benchmark = NASDAQ, the engine uses the TWSE and NASDAQ columns.

## 5. Data Quality Rules

The file should:
- have one row per trading day
- use YYYY-MM-DD dates
- contain no duplicate dates
- contain numeric price values
- include enough dates before and after the event window
- be sorted from oldest to newest date

## 6. Future Expansion

Future versions may add:
- USD/TWD
- sector ETFs
- volatility index
- trading volume
- alternative Taiwan firms
