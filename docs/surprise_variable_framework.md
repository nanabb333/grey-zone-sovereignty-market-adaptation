# Surprise Variable Framework

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It proposes a transparent coding framework for dissertation revision.

## Purpose

This memo designs a transparent framework for coding surprise in the Taiwan-related event dataset. Surprise is important because the same objective event can produce different market reactions depending on whether investors viewed it as unexpected, partially expected, or already priced before the event date.

The purpose of this variable is not to prove causal effects. It is to make the adaptation-versus-anticipation problem more explicit and to improve the interpretability of event-study findings.

## Conceptual Definition

Surprise refers to the extent to which an event introduced new information to investors on or near the event date. A high-surprise event is less likely to have been fully priced before Day 0. A low-surprise event is more likely to have been anticipated through media coverage, official warnings, scheduled political events, or repeated historical patterns.

## Coding Levels

| Surprise Level | Prior Media Coverage | Official Warnings | Expected Likelihood | Market Expectation |
| --- | --- | --- | --- | --- |
| High | Limited or fragmented coverage before the event; little consensus that the event would occur in its realized form. | Few clear warnings or ambiguous signals. | Event timing, scale, or content appears uncertain before Day 0. | Investors likely received meaningful new information on or near Day 0. |
| Medium | Some coverage before the event, but uncertainty remains over timing, scale, or market relevance. | Warnings exist but are not specific enough to fully price the outcome. | Event is plausible but not certain. | Some prior pricing likely occurred, but Day 0 still contains information. |
| Low | Extensive pre-event coverage; event widely discussed before Day 0. | Clear official warnings, scheduled triggers, or repeated response patterns. | Event is highly expected or follows an established pattern. | Substantial prior pricing likely occurred before Day 0. |

## Coding Principles

1. Code surprise before examining the market outcome where possible.
2. Prioritize pre-event evidence over post-event interpretation.
3. Distinguish expected occurrence from expected severity. An event may be expected but still surprising in scale.
4. Treat scheduled political events differently from unscheduled market shocks.
5. Record the rationale in prose so future readers can understand the judgment.
6. Do not treat positive or negative CARs themselves as evidence of surprise.

## Coding Table Template

| Event Name | Event Date | Event Family | Surprise Score | Prior Media Coverage | Official Warnings | Expected Likelihood | Market Expectation | Surprise Rationale | Source Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Example Event | YYYY-MM-DD | Military Exercise / Diplomatic Shock / Strategic Investment | High / Medium / Low | Brief description | Brief description | Brief description | Brief description | One to three sentences explaining the coding decision. | Links or source names |

## Example Coding Logic

### Pelosi Visit

The Pelosi Visit may be coded as high or medium-high surprise depending on the coding window. The possibility of the visit was publicly discussed before the event, but uncertainty remained over whether it would occur, how Beijing would respond, and how markets would interpret the escalation. The event therefore likely contained meaningful new information even if it was not completely unforeseen.

### Joint Sword-2024B

Joint Sword-2024B is a stronger candidate for low surprise. It occurred within a repeated pattern of PLA military signaling around Taiwan and followed earlier Joint Sword episodes. If pre-event coverage and official statements indicated a likely response, then the event may have been largely anticipated even if its precise operational details remained uncertain.

## Dissertation Use

The surprise variable should be used to qualify the adaptation argument. If repeated events are low surprise and generate muted reactions, the result may reflect anticipation rather than adaptation. If repeated events generate muted reactions even when surprise is not low, the adaptation interpretation becomes more plausible.

