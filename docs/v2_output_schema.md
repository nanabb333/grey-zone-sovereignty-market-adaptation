# V2 Output Schema

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

V2 will move Repo 2 from single-event processing to multi-event processing.

The main event-level output will remain:

```text
results/event_results.csv
```

In V1, this file contains one event.

In V2, this file should contain one row per processed event.

The output table should support:

- analytics
- validation
- comparison across events
- future dashboards
- future agent workflows

## 2. Required Columns

These columns should appear in every V2 event-level output row over time.

Current implemented V2 uses a smaller schema. See Section 9 for the implemented schema and future recommended schema.

| Column | Meaning | Example |
|---|---|---|
| event_id | Unique event identifier | E001 |
| event_name | Event name | Pelosi Visit |
| event_date | Original event date from `events/events.csv` | 2022-08-02 |
| matched_trading_date | Trading date used by the engine | 2022-08-02 |
| mechanism | High-level theoretical mechanism | Risk |
| event_type | Specific event classification | Diplomatic Shock |
| asset | Asset being analyzed | TSMC |
| benchmark | Benchmark used for abnormal returns | SOX |
| event_window_start | Event-window start from input | -7 |
| event_window_end | Event-window end from input | 7 |
| trading_days_in_window | Number of trading rows in the event window | 15 |
| status | Processing status | success |

## 3. Optional Columns

These columns are not strictly required for calculation, but they improve interpretation, validation, and future dashboard use.

| Column | Meaning | Example |
|---|---|---|
| event_sequence | Order of event in input file | 1 |
| event_year | Year of event | 2022 |
| window_rule | How event windows are interpreted | trading_day |
| return_unit | Unit used for return outputs | decimal |
| notes | Human-readable processing note | Processed successfully |
| validation_flag | Indicates whether the event needs review | pass |
| overlap_flag | Indicates overlapping event windows | review |

## 4. Raw CAR Fields

Raw CAR measures the selected asset's own cumulative return during the event window.

Raw CAR is not implemented yet in the current V2 engine. It remains a planned output enhancement.

Recommended raw CAR fields:

| Column | Meaning |
|---|---|
| raw_car | Cumulative raw asset return over the event window |
| raw_car_pct | Raw CAR expressed as a percentage |
| asset_day0_return | Asset return on the matched trading date |
| cumulative_asset_return_path | Optional path to event-window cumulative raw return data |

Future V2.x should include `raw_car` even if abnormal CAR remains the primary event-study metric.

This allows direct validation against Repo 1 outputs such as the Pelosi raw cumulative TSMC return.

## 5. Abnormal CAR Fields

Abnormal CAR measures asset performance relative to the selected benchmark.

Recommended abnormal CAR fields:

| Column | Meaning |
|---|---|
| abnormal_car | Sum of abnormal returns over the event window |
| abnormal_car_pct | Abnormal CAR expressed as a percentage |
| asset_day0_return | Asset return on matched trading date |
| benchmark_day0_return | Benchmark return on matched trading date |
| day0_abnormal_return | Asset day 0 return minus benchmark day 0 return |

For TSMC, the default benchmark is SOX.

For TWSE, the default benchmark is NASDAQ.

## 6. Validation Fields

Validation fields help explain whether each output row is trustworthy and comparable to Repo 1.

Recommended validation fields:

| Column | Meaning | Example |
|---|---|---|
| status | Processing status | success |
| validation_flag | Summary validation label | pass |
| validation_notes | Human-readable validation note | Event processed with expected columns |
| event_date_matched | Whether event date matched a trading date directly | Yes |
| days_to_matched_trading_date | Days between event date and matched trading date | 0 |
| expected_asset_column_found | Whether asset column exists | Yes |
| expected_benchmark_column_found | Whether benchmark column exists | Yes |
| event_window_complete | Whether the full event window was available | Yes |
| trading_days_in_window | Number of trading rows in event window | 15 |
| unit_check | Confirms decimal or percentage-point output | decimal |
| metric_definition | Metric used for primary CAR | benchmark_adjusted |

Suggested `status` values:

```text
success
missing_asset_column
missing_benchmark_column
event_date_out_of_range
empty_event_window
insufficient_data
failed
```

Suggested `validation_flag` values:

```text
pass
review
fail
```

## 7. Report Paths

Each event should have its own report.

Recommended report fields:

| Column | Meaning | Example |
|---|---|---|
| report_path | Path to generated Markdown report | reports/E001_report.md |
| report_generated | Whether report was generated | Yes |

## 8. Figure Paths

Each event should have its own abnormal-return figure.

Recommended figure fields:

| Column | Meaning | Example |
|---|---|---|
| figure_path | Path to abnormal-return figure | figures/E001_abnormal_returns.png |
| figure_generated | Whether figure was generated | Yes |

Optional future figure fields:

| Column | Meaning |
|---|---|
| raw_return_figure_path | Path to raw return figure |
| cumulative_return_figure_path | Path to cumulative return figure |

## 9. Current Implemented V2 Event-Level Schema

Current implemented columns for `results/event_results.csv`:

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
car_value
status
error_message
```

Current `car_value` meaning:

```text
benchmark-adjusted abnormal CAR
```

Current active event-window output:

```text
results/event_windows/{event_id}_event_window_data.csv
```

Deprecated V1-style event-window output:

```text
results/event_window_data.csv
```

## 10. Recommended Future V2 Event-Level Schema

Recommended future columns for dashboard and agent-readiness:

```text
event_id
event_name
event_date
matched_trading_date
mechanism
event_type
asset
benchmark
event_window_start
event_window_end
window_rule
trading_days_in_window
asset_day0_return
benchmark_day0_return
day0_abnormal_return
raw_car
raw_car_pct
abnormal_car
abnormal_car_pct
return_unit
event_window_data_path
figure_path
figure_generated
report_path
report_generated
status
validation_flag
validation_notes
event_date_matched
days_to_matched_trading_date
expected_asset_column_found
expected_benchmark_column_found
event_window_complete
metric_definition
notes
```

## 11. Example Rows

The examples below show what a single row should look like for three events.

Values marked `TBD` should be calculated by the V2 engine.

### Pelosi Visit

| Column | Example Value |
|---|---|
| event_id | E001 |
| event_name | Pelosi Visit |
| event_date | 2022-08-02 |
| matched_trading_date | 2022-08-02 |
| mechanism | Risk |
| event_type | Diplomatic Shock |
| asset | TSMC |
| benchmark | SOX |
| event_window_start | -7 |
| event_window_end | 7 |
| window_rule | trading_day |
| trading_days_in_window | 15 |
| asset_day0_return | TBD |
| benchmark_day0_return | TBD |
| day0_abnormal_return | TBD |
| raw_car | TBD |
| raw_car_pct | TBD |
| abnormal_car | TBD |
| abnormal_car_pct | TBD |
| return_unit | decimal |
| event_window_data_path | results/event_windows/E001_event_window_data.csv |
| figure_path | figures/E001_abnormal_returns.png |
| figure_generated | Yes |
| report_path | reports/E001_report.md |
| report_generated | Yes |
| status | success |
| validation_flag | pass |
| validation_notes | Compare raw_car to Repo 1 raw Pelosi output and abnormal_car to Repo 1 abnormal CAR output |
| event_date_matched | Yes |
| days_to_matched_trading_date | 0 |
| expected_asset_column_found | Yes |
| expected_benchmark_column_found | Yes |
| event_window_complete | Yes |
| metric_definition | benchmark_adjusted |
| notes | V2 validation anchor event |

### Joint Sword 2023

| Column | Example Value |
|---|---|
| event_id | E002 |
| event_name | Joint Sword 2023 |
| event_date | 2023-04-08 |
| matched_trading_date | 2023-04-10 |
| mechanism | Risk |
| event_type | Military Demonstration |
| asset | TSMC |
| benchmark | SOX |
| event_window_start | -7 |
| event_window_end | 7 |
| window_rule | trading_day |
| trading_days_in_window | 15 |
| asset_day0_return | TBD |
| benchmark_day0_return | TBD |
| day0_abnormal_return | TBD |
| raw_car | TBD |
| raw_car_pct | TBD |
| abnormal_car | TBD |
| abnormal_car_pct | TBD |
| return_unit | decimal |
| event_window_data_path | results/event_windows/E002_event_window_data.csv |
| figure_path | figures/E002_abnormal_returns.png |
| figure_generated | Yes |
| report_path | reports/E002_report.md |
| report_generated | Yes |
| status | success |
| validation_flag | review |
| validation_notes | Event date falls on a non-trading day; matched to next available trading day |
| event_date_matched | No |
| days_to_matched_trading_date | 2 |
| expected_asset_column_found | Yes |
| expected_benchmark_column_found | Yes |
| event_window_complete | Yes |
| metric_definition | benchmark_adjusted |
| notes | Weekend event requires trading-date matching |

### Joint Sword 2024A

| Column | Example Value |
|---|---|
| event_id | E003 |
| event_name | Joint Sword 2024A |
| event_date | 2024-05-23 |
| matched_trading_date | 2024-05-23 |
| mechanism | Risk |
| event_type | Military Demonstration |
| asset | TSMC |
| benchmark | SOX |
| event_window_start | -7 |
| event_window_end | 7 |
| window_rule | trading_day |
| trading_days_in_window | 15 |
| asset_day0_return | TBD |
| benchmark_day0_return | TBD |
| day0_abnormal_return | TBD |
| raw_car | TBD |
| raw_car_pct | TBD |
| abnormal_car | TBD |
| abnormal_car_pct | TBD |
| return_unit | decimal |
| event_window_data_path | results/event_windows/E003_event_window_data.csv |
| figure_path | figures/E003_abnormal_returns.png |
| figure_generated | Yes |
| report_path | reports/E003_report.md |
| report_generated | Yes |
| status | success |
| validation_flag | pass |
| validation_notes | Event date matches trading date directly |
| event_date_matched | Yes |
| days_to_matched_trading_date | 0 |
| expected_asset_column_found | Yes |
| expected_benchmark_column_found | Yes |
| event_window_complete | Yes |
| metric_definition | benchmark_adjusted |
| notes | Suitable for cross-event comparison with Joint Sword 2023 |

## 12. Design Recommendation

The V2 output table should avoid a single ambiguous `car_value` field.

Recommended:

```text
raw_car
abnormal_car
```

This will make validation easier, improve dashboard readiness, and prevent confusion between descriptive returns and event-study abnormal returns.
