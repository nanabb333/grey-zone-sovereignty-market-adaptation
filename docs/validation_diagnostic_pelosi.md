# Pelosi Visit Validation Diagnostic

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Repo 1 Result

The reported Repo 1 Pelosi Visit TSMC value of approximately +2.59% comes from the raw return event-window output in `output/pelosi_event_window_v2.csv`.

That file shows a final `tsmc_cumulative_return` of `2.5948103792414967` on `2022-08-11`.

This calculation used:

- asset: TSMC
- return type: raw TSMC percentage return, not benchmark-adjusted abnormal return
- event date: `2022-08-02`
- event window: 15 trading rows, from `2022-07-22` to `2022-08-11`
- market data source: the cleaned Repo 1 market dataset, represented in the current repo as `data/processed/market.csv`

Repo 1 also contains abnormal-return CAR outputs. In `data/processed/market_abnormal_returns_legacy.csv`, Pelosi Visit TSMC `tsmc_car_7` is `0.2341829569712628`, or about +0.234 percentage points. That value uses TSMC abnormal return versus SOX, not raw TSMC return.

## Repo 2 Result

Repo 2 currently reports:

- event: Pelosi Visit
- event date: `2022-08-02`
- asset: `TSMC`
- benchmark: `SOX`
- event window: `[-7, +7]`
- CAR value: `0.0044332006595363405`

Repo 2 uses `data/market_data.csv`, which was standardized from `data/processed/market.csv`.

Repo 2 calculates:

```text
asset_return = TSMC daily percentage change
benchmark_return = SOX daily percentage change
abnormal_return = asset_return - benchmark_return
CAR = sum(abnormal_return)
```

Repo 2 stores returns in decimal units, so `0.0044332006595363405` is approximately +0.443%.

Repo 2's current event-window data contains 11 trading rows:

```text
2022-07-26
2022-07-27
2022-07-28
2022-07-29
2022-08-01
2022-08-02
2022-08-03
2022-08-04
2022-08-05
2022-08-08
2022-08-09
```

## Difference

The Repo 1 `+2.59%` value and the Repo 2 `0.0044332006595363405` value are not the same metric.

Repo 1 `+2.59%` is a raw cumulative TSMC return across a 15-trading-day window.

Repo 2 `0.0044332006595363405` is a SOX-adjusted abnormal-return CAR across an 11-trading-day window.

The standardized market columns match:

| Repo 1 Column | Repo 2 Column |
|---|---|
| `tsmc_close` | `TSMC` |
| `sox_close` | `SOX` |
| `twse_close` | `TWSE` |
| `nasdaq_close` | `NASDAQ` |

The underlying prices around the Pelosi Visit match between `data/processed/market.csv` and `data/market_data.csv`.

## Possible Causes

1. Metric mismatch

Repo 1's approximately +2.59% figure is raw cumulative TSMC return. Repo 2 is calculating benchmark-adjusted abnormal return.

2. Window mismatch

Repo 1 raw Pelosi output uses 15 trading rows from `2022-07-22` to `2022-08-11`.

Repo 2 currently interprets `[-7, +7]` as calendar days around the event date, producing 11 trading rows from `2022-07-26` to `2022-08-09`.

3. Unit mismatch

Repo 1 stores returns as percentage points, for example `2.5948103792414967`.

Repo 2 stores returns as decimals, for example `0.0044332006595363405`, which equals about `0.443%`.

4. Repo 1 contains multiple Pelosi result definitions

The repo contains at least three Pelosi-related calculations:

| File | Pelosi TSMC Result | Meaning |
|---|---:|---|
| `output/pelosi_event_window_v2.csv` | `2.5948103792414967` | raw cumulative TSMC return over 15 trading rows |
| `data/processed/market_abnormal_returns_legacy.csv` | `0.2341829569712628` | SOX-adjusted TSMC abnormal CAR over a legacy two-sided window |
| `results/event_abnormal_return_summary.csv` | `1.8572276153865368` | SOX-adjusted TSMC abnormal CAR over a forward window |

## Most Likely Cause

The most likely cause is not a data error.

The most likely cause is that Repo 2 is comparing its current benchmark-adjusted abnormal-return CAR against Repo 1's raw cumulative TSMC return.

The second major cause is window construction. Repo 1's raw Pelosi calculation used trading-day indexing, while Repo 2 currently uses calendar-date filtering.

## Recommended Fix

Before changing code, choose the validation target for Repo 2.

Recommended target:

Repo 2 should reproduce Repo 1's abnormal-return event-study result, not the raw cumulative TSMC return, because Repo 2 is intended to be an event-study engine.

To align Repo 2 with the Repo 1 event-study method, update the specification later so that:

- TSMC abnormal returns are benchmark-adjusted against SOX
- TWSE abnormal returns are benchmark-adjusted against NASDAQ
- `[-7, +7]` means 7 trading rows before the matched event trading day through 7 trading rows after it
- CAR outputs are clearly labeled as decimal or percentage-point values
- validation compares Repo 2 against the correct Repo 1 abnormal-return file, not the raw cumulative-return file

If the immediate goal is instead to reproduce the `+2.59%` Pelosi value, Repo 2 would need a separate raw cumulative return mode. That should be documented as a different metric from abnormal-return CAR.
