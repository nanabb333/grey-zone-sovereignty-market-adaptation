# Research Design Revision V2

> Academic Research Notice:
> This document provides dissertation-ready revision text for the research design chapter.
> It does not add new event-study calculations or causal claims.

## Proposed Section: Event-Level Coding Variables

In addition to event category and mechanism, the revised event dataset introduces three interpretive coding variables: `surprise_score`, `event_family`, and `event_repetition_level`. These variables are designed to make the dissertation's adaptation argument more transparent and to address the rival explanation that muted market reactions may reflect anticipation or prior pricing rather than investor adaptation.

The first added variable is `surprise_score`. This variable codes whether an event was high, medium, or low surprise relative to information available before the event date. A high-surprise event is one whose timing, occurrence, scale, or market relevance was not clearly expected before Day 0. A medium-surprise event was plausible or partially discussed before Day 0, but still contained meaningful uncertainty. A low-surprise event was scheduled, heavily signaled, or part of an established repeated pattern. The purpose of `surprise_score` is to distinguish events that likely introduced new information from events that may have been partly priced before the observed event window.

This variable is especially important because surprise is conceptually distinct from objective severity. A military exercise may be objectively serious but low surprise if investors expected a PRC response after a scheduled political trigger. Conversely, a policy announcement may have lower objective security risk but still be medium or high surprise if the content or scale of the announcement was not anticipated. The dissertation therefore treats surprise as an information variable rather than a severity variable.

The second added variable is `event_family`. This variable groups events according to their substantive type, such as `Military_Exercise`, `Diplomatic_Shock`, `Economic_Coercion`, `Export_Control`, `Strategic_Investment`, `Political_Signaling`, and `Legal_Judicial_Signaling`. The purpose of this variable is to clarify which events are comparable to one another. Adaptation is most plausible when investors encounter repeated events from the same family. For example, repeated PLA exercises around Taiwan are more directly comparable to one another than a PLA exercise and a TSMC investment announcement.

The third added variable is `event_repetition_level`. This variable codes the degree to which an event belongs to a recurring pattern within the sample. A level of 1 indicates a first or relatively novel event. A level of 2 indicates that a similar prior event exists but the pattern is not yet routinized. A level of 3 indicates a repeated event family with a recognizable market or policy pattern. A level of 4 indicates a highly repeated grey-zone signaling pattern. The purpose of this variable is to operationalize the recurrence dimension of the dissertation's theory.

These variables are not intended to prove adaptation. They are intended to make the adaptation claim more disciplined. If repeated low-surprise events generate muted reactions, the result may reflect anticipation or prior pricing rather than adaptation. If repeated events generate muted reactions even when surprise is not low, the adaptation interpretation becomes more plausible. Similarly, if repeated event families continue to generate large negative abnormal returns, then the adaptation interpretation is weakened.

The coding is transparent and interpretive. Each event receives a short rationale explaining the surprise assignment, event-family assignment, and repetition level. The coding does not rely on the observed CAR itself. This is important because using market outcomes to code surprise would make the argument circular. Instead, the coding is based on the event's public visibility, prior warning signals, scheduled or unscheduled character, and relationship to earlier events in the sample.

This operationalization has limitations. It does not directly observe investor beliefs, analyst expectations, or trading-desk information. It also cannot fully determine whether repricing occurred before the event window. The variables should therefore be interpreted as structured qualitative controls rather than precise measures of market expectations. Their main value is to clarify the difference between adaptation, anticipation, and surprise so that the dissertation does not overstate the causal meaning of observed abnormal returns.

## Dissertation Integration Note

This section can be inserted after the existing event classification discussion or within the variables and operationalization section of Chapter 4. It should be paired with the upgraded dataset:

```text
data/events_v2.csv
```

