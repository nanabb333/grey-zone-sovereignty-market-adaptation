# Repetition Figure Methodology

> Academic Research Notice:
> This document records how the repetition figure was produced.
> The figure is descriptive and does not estimate causal effects.

## Figure File

```text
figures/repetition_vs_car.png
```

## Input Files

The figure joins two existing project files:

```text
data/events_v2.csv
results/event_abnormal_return_summary.csv
```

No new event collection, forecasting, or event-study calculation was performed.

## Variables Used

From `data/events_v2.csv`:

- `event_name`
- `date`
- `mechanism`
- `surprise_score`
- `event_family`
- `event_repetition_level`

From `results/event_abnormal_return_summary.csv`:

- `event_name`
- `event_date`
- `mechanism`
- `twse_car_3`
- `tsmc_car_3`

The figure uses 3-day cumulative abnormal returns because this window captures short-run market response while limiting some of the noise that may enter longer windows.

## Merge Process

The merge uses three identifiers:

```text
event_name
date / event_date
mechanism
```

The date variable in `data/events_v2.csv` is matched to `event_date` in `results/event_abnormal_return_summary.csv`.

All 18 events in `data/events_v2.csv` matched successfully with the event-study result file.

## Visualization Choice

The figure uses a two-panel scatter plot:

- left panel: TWSE 3-day CAR
- right panel: TSMC 3-day CAR

The x-axis is `event_repetition_level`. The y-axis is 3-day cumulative abnormal return. Points are colored by `surprise_score`. A horizontal zero line distinguishes positive and negative abnormal returns, and a mean line summarizes average CAR by repetition level.

This visualization was chosen because the dissertation's adaptation argument is about repeated shocks and changing market reaction. A scatter plot preserves individual event variation, while the mean line gives a compact descriptive summary.

## Limitations

The figure is descriptive. It does not prove investor adaptation.

Main limitations:

1. `event_repetition_level` measures observable event repetition, not investor learning directly.
2. Repetition and anticipation are closely related; repeated events may also be easier to price before Day 0.
3. The sample is small, so averages by repetition level are sensitive to individual events.
4. CARs may be influenced by broader market conditions, semiconductor-sector dynamics, or benchmark choice.
5. The figure does not measure pre-event media intensity or direct investor expectations.

## Recommended Dissertation Use

The figure is appropriate for Chapter 5 or Chapter 6 as a descriptive diagnostic. It should be introduced with cautious language:

```text
This figure examines whether repeated event families display CAR patterns consistent with adaptation. The pattern is suggestive but not causal, and anticipation remains a major rival explanation.
```

