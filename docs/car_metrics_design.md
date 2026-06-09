# CAR Metrics Design

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

Repo 2 should support two related but distinct event-study metrics:

1. Raw CAR
2. Benchmark-adjusted CAR

This distinction matters because Repo 1 contains both raw event-window return outputs and benchmark-adjusted abnormal-return outputs. Repo 2 needs to label each metric clearly so validation compares like with like.

## 2. Raw CAR

Raw CAR measures the cumulative return of the selected asset during the event window without subtracting a benchmark.

For the selected asset:

```text
asset_return = daily percentage change in asset price
raw_car = cumulative asset return during the event window
```

Raw CAR answers:

```text
How much did the asset move during the event window?
```

For example, the Repo 1 Pelosi Visit value of approximately `+2.59%` is a raw cumulative TSMC return across the Pelosi event window.

## 3. Abnormal CAR

Abnormal CAR measures the cumulative benchmark-adjusted return of the selected asset during the event window.

For the selected asset and benchmark:

```text
asset_return = daily percentage change in asset price
benchmark_return = daily percentage change in benchmark price
abnormal_return = asset_return - benchmark_return
abnormal_car = sum of abnormal_return during the event window
```

Abnormal CAR answers:

```text
How much did the asset move relative to the benchmark during the event window?
```

For TSMC, Repo 1 generally used SOX as the benchmark. For TWSE, Repo 1 generally used NASDAQ as the benchmark.

## 4. Why Both Are Useful

Raw CAR is useful because it shows the asset's direct market movement. It is easy to explain and matches the intuitive question: did TSMC go up or down around the event?

Abnormal CAR is useful because it separates event-specific movement from broader market or sector movement. This is closer to the event-study logic from Repo 1.

Together, the two metrics help the analyst distinguish:

- whether the asset rose or fell in absolute terms
- whether the asset outperformed or underperformed its benchmark
- whether a positive raw return was simply part of a broader market rise
- whether a negative raw return was less severe than the benchmark decline

## 5. Repo 1 and Repo 2 Mapping

| Source | Metric | Meaning |
|---|---|---|
| `output/pelosi_event_window_v2.csv` | Raw CAR | Raw cumulative TSMC return over the Pelosi event window |
| `data/processed/market_abnormal_returns_legacy.csv` | Abnormal CAR | Benchmark-adjusted TWSE and TSMC CAR outputs |
| `results/event_abnormal_return_summary.csv` | Abnormal CAR | Benchmark-adjusted event-study summary outputs |
| Current Repo 2 engine | Abnormal CAR | TSMC return minus SOX return, summed over the event window |

Repo 2 currently calculates abnormal CAR only.

Repo 2 does not yet calculate raw CAR as a separate named output.

## 6. Recommendation for V2 Outputs

V2 should output both metrics for every event:

| Output Column | Meaning |
|---|---|
| `raw_car` | Cumulative raw asset return during the event window |
| `abnormal_car` | Cumulative benchmark-adjusted abnormal return during the event window |
| `asset_return` | Daily raw asset return |
| `benchmark_return` | Daily raw benchmark return |
| `abnormal_return` | Daily asset return minus benchmark return |

The event-level results file should include:

```text
event_id
event_name
event_date
mechanism
event_type
asset
benchmark
event_window_start
event_window_end
trading_days_in_window
raw_car
abnormal_car
```

The event-window data file should include:

```text
date
asset_return
benchmark_return
abnormal_return
```

Optionally, V2 can also include a cumulative raw return column and cumulative abnormal return column in the event-window data:

```text
cumulative_asset_return
cumulative_abnormal_return
```

## 7. Validation Recommendation

For validation against Repo 1:

- compare Repo 2 `raw_car` to Repo 1 raw cumulative return outputs
- compare Repo 2 `abnormal_car` to Repo 1 benchmark-adjusted CAR outputs
- keep units explicit: decimal values versus percentage-point values
- use the same event-window rule before comparing values

The recommended V2 default is:

```text
Primary event-study metric: abnormal_car
Supporting descriptive metric: raw_car
```

This keeps Repo 2 aligned with the event-study methodology while still allowing direct comparison to Repo 1's raw Pelosi output.
