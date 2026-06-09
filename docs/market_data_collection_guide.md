# Market Data Collection Guide

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

This guide defines how to collect the first market dataset for event-study analysis.

The dataset should measure Taiwan equity, semiconductor, and currency reactions around events in `data/events_v1.csv`.

Recommended event windows:

- `-1/+1`
- `-3/+3`
- `-7/+7`

## Date Range Needed

Initial full range:

`1995-07-14` to `2025-05-26`

This covers the earliest event in `data/events_v1.csv` plus a 7-day pre-window and the latest event plus a 7-day post-window.

If a source does not provide full historical coverage, collect the available range and document the gap.

## Variables

| Variable | Ticker / Code | Data Source | Download Method | CSV Format |
| --- | --- | --- | --- | --- |
| TWSE Index | `^TWII` on Yahoo Finance; TAIEX on TWSE | Yahoo Finance for easy download; Taiwan Stock Exchange for official reference | Manual CSV download from Yahoo Finance historical data, or later scripted download with `yfinance` if allowed | `date,twse_close` |
| TSMC stock price | `2330.TW` on Yahoo Finance; `2330` on TWSE | Yahoo Finance for easy adjusted historical prices; Taiwan Stock Exchange for official local-market data | Manual CSV download from Yahoo Finance historical data, or TWSE daily trading data export | `date,tsmc_close` |
| USD/TWD exchange rate | `TWD=X` on Yahoo Finance; `DEXTAUS` on FRED | FRED for Federal Reserve H.10 daily exchange-rate series; Yahoo Finance as alternate market source | Manual CSV download from FRED or Yahoo Finance; later API collection if allowed | `date,usd_twd` |

## Why Each Variable Matters

| Variable | Why It Matters |
| --- | --- |
| `twse_close` | Captures broad Taiwan equity-market reaction to geopolitical risk. |
| `tsmc_close` | Captures semiconductor-sector reaction through Taiwan's most strategically important firm. |
| `usd_twd` | Captures Taiwan dollar pressure and possible risk-off movement into U.S. dollars. |

## Target Combined CSV

Final market dataset should use this structure:

```csv
date,twse_close,tsmc_close,usd_twd
YYYY-MM-DD,,,
```

Optional future columns:

```csv
nasdaq_close,nvidia_close
```

## Event Window Notes

| Window | Purpose |
| --- | --- |
| `-1/+1` | Measures immediate market reaction around the event date. |
| `-3/+3` | Captures short delays, weekend effects, and multi-day adjustment. |
| `-7/+7` | Captures broader reaction around major crises, military exercises, or policy shocks. |

## Collection Notes

1. Do not mix adjusted and unadjusted prices without documenting the choice.
2. Use closing prices for the first version.
3. If an event occurs on a non-trading day, use the nearest trading day and record the adjustment.
4. Keep raw downloaded files separate from cleaned data.
5. Do not calculate returns until the raw market dataset is complete.

## Source Links

- Yahoo Finance TAIEX symbol: `^TWII`
- Yahoo Finance TSMC Taiwan symbol: `2330.TW`
- Yahoo Finance USD/TWD symbol: `TWD=X`
- FRED USD/TWD series: `DEXTAUS`
- Taiwan Stock Exchange index and listed-company data pages

