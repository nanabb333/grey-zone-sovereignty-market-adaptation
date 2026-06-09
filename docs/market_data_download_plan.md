# Market Data Download Plan

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

This plan explains how to collect the first raw market dataset for event-study analysis.

Target output later:

```csv
date,twse_close,tsmc_close,usd_twd
```

Do not calculate returns yet. First collect raw CSV files.

## Minimum Date Range

Current event range in `data/events_v1.csv`:

- Earliest event: `1995-07-21`
- Latest event: `2025-05-19`

Minimum collection range for `-7/+7` event windows:

`1995-07-14` to `2025-05-26`

This range also covers `-1/+1` and `-3/+3` windows.

## Variable 1: TWSE Index

| Item | Plan |
| --- | --- |
| Variable | `twse_close` |
| Ticker | `^TWII` on Yahoo Finance |
| Meaning | Taiwan Stock Exchange Capitalization Weighted Stock Index / TAIEX |
| Easiest Source | Yahoo Finance |
| Backup Source | Taiwan Stock Exchange / Taiwan Index Plus / commercial data vendor |

Download instructions:

1. Open Yahoo Finance.
2. Search for `^TWII`.
3. Open the Historical Data tab.
4. Set time period to `1995-07-14` through `2025-05-26`.
5. Set frequency to Daily.
6. Click Download.
7. Save the raw file as `data/raw/twse_twii_yahoo.csv`.

Yahoo Finance coverage note:

Yahoo is the easiest source, but it may not provide complete coverage back to 1995. If the download starts after the 1995-1996 Taiwan Strait Crisis, use TWSE official historical index data or a paid/vendor source for the older period.

Expected raw CSV fields from Yahoo:

```csv
Date,Open,High,Low,Close,Adj Close,Volume
```

Column needed for project:

```csv
date,twse_close
```

## Variable 2: TSMC Stock Price

| Item | Plan |
| --- | --- |
| Variable | `tsmc_close` |
| Ticker | `2330.TW` on Yahoo Finance |
| Meaning | TSMC Taiwan-listed stock price |
| Easiest Source | Yahoo Finance |
| Backup Source | Taiwan Stock Exchange / commercial data vendor |

Download instructions:

1. Open Yahoo Finance.
2. Search for `2330.TW`.
3. Open the Historical Data tab.
4. Set time period to `1995-07-14` through `2025-05-26`.
5. Set frequency to Daily.
6. Click Download.
7. Save the raw file as `data/raw/tsmc_2330tw_yahoo.csv`.

Yahoo Finance coverage note:

Yahoo Finance is probably sufficient for recent events from 2020 onward. It may not provide complete daily TSMC Taiwan-listed price data back to 1995. If early dates are missing, use TWSE official data or a commercial market-data source.

Expected raw CSV fields from Yahoo:

```csv
Date,Open,High,Low,Close,Adj Close,Volume
```

Column needed for project:

```csv
date,tsmc_close
```

## Variable 3: USD/TWD Exchange Rate

| Item | Plan |
| --- | --- |
| Variable | `usd_twd` |
| Ticker | `TWD=X` or `USDTWD=X` on Yahoo Finance |
| FRED Series | `DEXTAUS` |
| Meaning | Taiwan dollars per one U.S. dollar |
| Easiest Source | FRED |
| Backup Source | Yahoo Finance / central bank / commercial data vendor |

Recommended source:

Use FRED first for USD/TWD because it provides a clean daily series from the Federal Reserve H.10 exchange-rate release.

FRED download instructions:

1. Open the FRED page for `DEXTAUS`.
2. Set date range to `1995-07-14` through `2025-05-26`.
3. Click Download.
4. Choose CSV.
5. Save the raw file as `data/raw/usd_twd_fred_dextaus.csv`.

Yahoo Finance alternate instructions:

1. Open Yahoo Finance.
2. Search for `TWD=X` or `USDTWD=X`.
3. Open the Historical Data tab.
4. Set time period to `1995-07-14` through `2025-05-26`.
5. Set frequency to Daily.
6. Click Download.
7. Save the raw file as `data/raw/usd_twd_yahoo.csv`.

Yahoo Finance coverage note:

Yahoo Finance can provide USD/TWD historical data, but FRED is cleaner for this project because it gives a documented daily exchange-rate series. Use Yahoo only as a backup or cross-check.

Expected raw CSV fields from FRED:

```csv
observation_date,DEXTAUS
```

Column needed for project:

```csv
date,usd_twd
```

## Is Yahoo Finance Sufficient?

Short answer:

Yahoo Finance is sufficient for a first pass on recent events, especially 2020-2025.

But Yahoo Finance may not be sufficient for the full project because:

1. The project needs data back to `1995-07-14`.
2. Yahoo historical coverage can vary by instrument.
3. Yahoo notes that download availability can be limited by data licensing.
4. Early Taiwan market data may require TWSE official files or a commercial vendor.

Recommended approach:

| Period | Suggested Source |
| --- | --- |
| 1995-1996 crisis events | TWSE official data or commercial vendor; FRED for USD/TWD. |
| 2020-2025 events | Yahoo Finance is acceptable for TWSE and TSMC first pass; FRED for USD/TWD. |

## Raw File Checklist

Create this folder:

```text
data/raw/
```

Collect these raw files:

```text
data/raw/twse_twii_yahoo.csv
data/raw/tsmc_2330tw_yahoo.csv
data/raw/usd_twd_fred_dextaus.csv
```

Optional backup:

```text
data/raw/usd_twd_yahoo.csv
```

## Next Step After Download

After the raw CSV files are saved, create a cleaning script that:

1. Reads the raw files.
2. Standardizes date columns.
3. Keeps only close prices / exchange-rate values.
4. Merges all variables by date.
5. Saves the cleaned dataset as `data/market.csv`.

