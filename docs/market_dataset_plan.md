# Market Dataset Plan

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

The market dataset will measure how Taiwan-related geopolitical and strategic events affect financial markets.

It will support event-window analysis around each event in `data/events_v1.csv`.

## Variables to Collect

| Variable | Why It Matters | Possible Sources |
| --- | --- | --- |
| `date` | Aligns market observations with event dates. | All market data sources. |
| `twse_close` | Captures Taiwan stock market reaction. | Taiwan Stock Exchange, Yahoo Finance, Bloomberg, Refinitiv. |
| `tsmc_close` | Captures semiconductor-sector reaction through Taiwan's most important chip firm. | TWSE, Yahoo Finance, Bloomberg, Refinitiv. |
| `usd_twd` | Captures Taiwan dollar pressure against the U.S. dollar. | Central Bank of Taiwan, FRED, Bloomberg, Refinitiv. |
| `nasdaq_close` | Captures global technology-sector reaction. | Nasdaq, Yahoo Finance, Bloomberg, Refinitiv. |
| `nvidia_close` | Captures AI and advanced-chip market reaction. | Nasdaq, Yahoo Finance, Bloomberg, Refinitiv. |

## Event Windows

Use multiple windows to test whether results are sensitive to timing:

| Window | Use |
| --- | --- |
| `-1/+1` | Short-run immediate reaction. |
| `-3/+3` | Captures delayed market reaction and non-trading-day issues. |
| `-7/+7` | Captures broader adjustment around major crises or policy events. |

## Notes

1. Use closing prices for consistency.
2. If an event falls on a non-trading day, use the nearest trading day and record the adjustment.
3. Keep raw prices before calculating returns.
4. Separate Taiwan-specific reactions from global technology-market reactions.

