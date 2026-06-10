# Figure Production Readiness

> Academic Research Notice:
> This document classifies which dissertation figures can be generated from existing repository data.
> It does not create new figures or perform new calculations.

## Ready Now

| Figure | Data Source | Reason |
| --- | --- | --- |
| Risk vs Strategic Importance CAR Comparison | `results/event_abnormal_return_summary.csv` | Event-level CAR outputs already exist and include the `mechanism` field needed to compare Risk and Strategic_Importance events. |
| Key Figure: Average CAR by Event Type | `figures/average_car_by_event_type.png` | Already generated and embedded in the README. |
| Event-Level CAR Scatter | `figures/event_level_car_scatter.png` | Already generated and available for results discussion. |
| Event Coding Summary Table | `data/events_v2.csv` | Surprise, event family, and repetition fields are now coded for all existing events. |

## Need Additional Processing

| Figure | Additional Processing Needed | Reason |
| --- | --- | --- |
| Event Repetition vs CAR | Merge `data/events_v2.csv` with `results/event_abnormal_return_summary.csv` | Repetition coding and CAR results exist in separate files and need to be joined by event name/date. |
| Surprise Score vs CAR | Merge `data/events_v2.csv` with `results/event_abnormal_return_summary.csv` | Surprise coding exists, but no figure currently compares surprise categories with abnormal returns. |
| Event Family Distribution | Count `event_family` values in `data/events_v2.csv` | The data are ready, but the figure has not yet been generated. |
| Adaptation vs Anticipation Diagnostic Table | Combine `surprise_score`, `event_repetition_level`, and CAR direction | Requires a derived table, not new data collection. |

## Not Currently Feasible

| Figure | Missing Evidence | Reason |
| --- | --- | --- |
| Direct Investor Adaptation Measure | Direct investor belief data, analyst expectations, trading-desk evidence, or survey data | The repository observes market outcomes, not investor beliefs directly. |
| Prior Pricing Timeline | Systematic pre-event news intensity or market expectation data | The current dataset codes surprise qualitatively but does not measure pre-event information flow quantitatively. |
| Causal Adaptation Effect Plot | Stronger identification strategy and larger sample | The current project is exploratory and descriptive, not a causal design. |
| Forecasting-Based Market Reaction Figure | Forecast model and out-of-sample predictions | Forecasting is outside the dissertation's current scope and should not be added for this project. |

## Recommended Immediate Figure

The highest-value next figure is:

```text
Event Repetition vs CAR
```

This figure would directly support the adaptation discussion while remaining descriptive. It should be presented as suggestive evidence, not as proof of adaptation.

