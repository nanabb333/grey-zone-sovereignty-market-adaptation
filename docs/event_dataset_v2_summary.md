# Event Dataset V2 Summary

> Academic Research Notice:
> This document summarizes transparent coding additions to the event dataset.
> It does not report new event-study calculations or causal estimates.

## Dataset

Upgraded dataset:

```text
data/events_v2.csv
```

Source master dataset:

```text
data/events/event_sample.csv
```

## Number of Events

The upgraded dataset contains 18 existing events.

No new events were collected.

## Surprise Distribution

| Surprise Score | Number of Events |
| --- | ---: |
| High | 1 |
| Medium | 12 |
| Low | 5 |

## Event Family Distribution

| Event Family | Number of Events |
| --- | ---: |
| Military_Exercise | 8 |
| Diplomatic_Shock | 3 |
| Strategic_Investment | 3 |
| Economic_Coercion | 1 |
| Export_Control | 1 |
| Legal_Judicial_Signaling | 1 |
| Political_Signaling | 1 |

## Event Repetition Distribution

| Event Repetition Level | Number of Events |
| --- | ---: |
| 1 | 8 |
| 2 | 4 |
| 3 | 3 |
| 4 | 3 |

## Interpretation

The dataset upgrade makes the adaptation-versus-anticipation issue more explicit. The coding shows that many events are not cleanly separable into unexpected shocks or fully anticipated events. Most are coded Medium surprise because they were plausible before Day 0 but still contained new information about timing, scale, policy detail, or market relevance.

The military-exercise family is the largest event family. It also has the highest repetition levels, which makes it especially important for evaluating the adaptation argument. However, repetition does not automatically prove adaptation. Repeated military events may also be more anticipated and therefore more likely to be priced before Day 0.

## Dissertation Use

The upgraded dataset supports a more cautious dissertation claim:

```text
Market reactions are consistent with investor adaptation, but adaptation must be evaluated alongside surprise, anticipation, and event-family repetition.
```

This strengthens the dissertation by making the strongest rival explanation visible rather than implicit.

