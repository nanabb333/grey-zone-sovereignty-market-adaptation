# Repetition Figure Interpretation

> Academic Research Notice:
> This document interprets a descriptive dissertation figure.
> It does not make causal claims and should not be read as proof of investor adaptation.

## Figure Description

Figure file:

```text
figures/repetition_vs_car.png
```

The figure plots `event_repetition_level` against 3-day cumulative abnormal returns for TWSE and TSMC. Each point represents an event in the upgraded event dataset. The points are colored by `surprise_score`, and a mean line summarizes average CAR by repetition level. The figure is designed as a first descriptive diagnostic for the dissertation's adaptation argument.

The x-axis measures event repetition from 1 to 4:

- 1: first or relatively novel event
- 2: similar prior event exists
- 3: repeated event family with recognizable pattern
- 4: highly repeated or expected grey-zone signaling pattern

The y-axis reports 3-day cumulative abnormal return. TWSE and TSMC are shown separately because the broader Taiwan market and Taiwan's strategic semiconductor firm may react differently to the same political event.

## Observed Pattern

The pattern is mixed rather than monotonic. Events with repetition level 4 show positive average 3-day abnormal returns for both TWSE and TSMC. This is substantively important because level 4 events are mostly repeated military-signaling events, the type of case most relevant to the adaptation argument.

However, repetition level 3 does not show the same pattern. Level 3 events show negative average 3-day abnormal returns, especially for TSMC. This means the figure does not show a simple linear relationship in which market reactions become steadily more positive as repetition increases.

The descriptive mean 3-day CAR pattern is:

| Repetition Level | TWSE Mean 3-Day CAR | TSMC Mean 3-Day CAR |
| --- | ---: | ---: |
| 1 | -0.026 | 1.384 |
| 2 | 0.565 | 1.619 |
| 3 | -0.982 | -2.881 |
| 4 | 0.455 | 1.141 |

## Why The Pattern May Be Consistent With Adaptation

The figure may be consistent with adaptation because the most repeated event category does not produce uniformly negative abnormal returns. If investors learn from repeated Taiwan-related shocks, later grey-zone events may be interpreted as familiar signaling rather than as immediate escalation. In that case, repeated military exercises and patrols may generate weaker negative reactions than a simple risk-damage model would predict.

Joint Sword-2024B is the key illustrative case. It is a risk event and a repeated military exercise, yet it is associated with positive short-window abnormal returns. This does not establish adaptation, but it gives the adaptation framework empirical relevance. It suggests that event repetition and investor interpretation should be considered alongside objective event severity.

## Why The Figure Does Not Prove Adaptation

The figure does not prove adaptation for three reasons.

First, event repetition is not the same as investor learning. Repetition is an observable event characteristic, while adaptation is an unobserved investor process. The figure shows a relationship between repeated event categories and CAR patterns, not direct evidence of investor beliefs.

Second, the pattern is not monotonic. Repetition level 3 is negative on average, while repetition level 4 is positive. This weakens any simple claim that more repetition automatically produces less negative market reaction.

Third, the sample is small. A few events can strongly influence average CARs at each repetition level. The figure should therefore be interpreted as a descriptive diagnostic rather than a statistical test.

## Alternative Explanations

### Anticipation

Repeated events are easier to anticipate. If investors expected later military demonstrations before Day 0, muted or positive abnormal returns may reflect anticipation rather than adaptation.

### Prior Pricing

Related to anticipation, markets may have repriced before the event window. If relevant information entered prices earlier, the observed event-window CAR may understate the true market impact of the event.

### Sample Limitations

The number of events at each repetition level is limited. Event categories also differ in content, timing, and market environment. Some positive returns may reflect broader technology-sector conditions, semiconductor-sector momentum, or benchmark choice rather than adaptation.

## Dissertation Interpretation

The appropriate dissertation claim is:

```text
The repetition figure is consistent with the possibility of investor adaptation, especially for highly repeated grey-zone military events, but it does not prove adaptation. Anticipation, prior pricing, and sample limitations remain important rival explanations.
```

