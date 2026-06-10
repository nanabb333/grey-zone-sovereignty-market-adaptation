# Adaptation vs Anticipation

## Public Summary

Adaptation and anticipation are different explanations that can produce similar observed market patterns.

### Adaptation

Adaptation means investors learn from repeated Taiwan-related shocks and begin to interpret some recurring events as familiar, contained, or less informative than earlier shocks.

### Anticipation

Anticipation means investors expected an event before the event date and priced it before the measured event window.

## Why The Distinction Matters

Muted or positive abnormal returns after a repeated event may be consistent with adaptation.

But the same pattern may also reflect anticipation or prior pricing.

This is why the project adds:

- `surprise_score`
- `surprise_rationale`
- `event_family`
- `event_repetition_level`

These variables help clarify whether an event was repeated, expected, novel, or likely to contain new information.

## Preferred Claim

The project should say:

```text
The findings are consistent with adaptation, but they do not prove adaptation.
```

It should not say:

```text
The findings prove that investors adapted.
```

## Deeper Documents

- [Adaptation vs Anticipation](../adaptation_vs_anticipation.md)
- [Surprise Variable Framework](../surprise_variable_framework.md)
- [Repetition Figure Interpretation](../repetition_figure_interpretation.md)
