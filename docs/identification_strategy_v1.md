# Identification Strategy V1

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## Purpose

This memo assesses whether the observed market reactions are truly Taiwan-specific geopolitical effects.

The current analysis uses raw TWSE and TSMC returns around selected events. That is useful for early exploration, but it cannot yet isolate the effect of Taiwan-specific geopolitical risk.

---

## 1. Current Identification Problem

Raw returns cannot isolate geopolitical effects because market prices move for many reasons at the same time.

For example, a positive TSMC return after a military exercise could mean:

1. Investors were not worried about the exercise.
2. The risk was already priced in.
3. The market adapted to repeated PLA exercises.
4. Global semiconductor stocks were rising for unrelated reasons.
5. AI-related optimism outweighed geopolitical concerns.

The current event-window method shows what happened around the event date, but it does not prove why it happened.

Current limitation:

```text
Observed return = Taiwan geopolitical effect + global market effect + semiconductor sector effect + firm-specific effect + noise
```

The project needs benchmark controls to separate Taiwan-specific reactions from broader market movements.

---

## 2. Alternative Explanations

### Global Technology Rally

If global technology stocks are rising during the same event window, positive TWSE or TSMC returns may reflect global tech momentum rather than low geopolitical concern.

### AI Boom

TSMC may rise during geopolitical-risk windows if investors focus on AI demand, advanced chips, or NVIDIA-related growth. This could offset negative geopolitical pressure.

### U.S. Market Conditions

U.S. monetary policy, inflation news, earnings expectations, and risk appetite can affect global equity markets. TWSE and TSMC may move with U.S. markets even when Taiwan-specific risk is elevated.

### Semiconductor Sector Trends

TSMC may track the global semiconductor cycle. If semiconductor stocks are broadly rising, a positive TSMC return does not necessarily mean Taiwan geopolitical risk had no effect.

---

## 3. Proposed Benchmark Variables

| Benchmark | Suggested Variable | Why It Matters |
| --- | --- | --- |
| NASDAQ Composite | `nasdaq_close` | Captures global technology-market conditions and U.S. risk appetite. |
| NVIDIA | `nvidia_close` | Captures AI and advanced-chip momentum that may affect TSMC. |
| Philadelphia Semiconductor Index (SOX) | `sox_close` | Captures global semiconductor-sector trends. |

Possible ticker symbols:

| Benchmark | Possible Ticker |
| --- | --- |
| NASDAQ Composite | `^IXIC` |
| NVIDIA | `NVDA` |
| Philadelphia Semiconductor Index | `^SOX` |

These benchmark variables should be added to the market dataset before making stronger causal claims.

---

## 4. Event Study Upgrade Plan

The next version should calculate abnormal returns.

Basic abnormal-return approach:

```text
Abnormal return = Taiwan asset return - benchmark return
```

Possible models:

| Model | Formula | Use |
| --- | --- | --- |
| Simple benchmark model | `TSMC return - SOX return` | Separates TSMC from global semiconductor movement. |
| Technology benchmark model | `TSMC return - NASDAQ return` | Separates TSMC from broad technology-market movement. |
| AI momentum model | `TSMC return - NVIDIA return` | Tests whether TSMC movement is driven by AI-sector momentum. |
| Market model | `TSMC return = alpha + beta * benchmark return + error` | Estimates expected return using pre-event data, then measures abnormal return. |

Recommended event-study steps:

1. Add NASDAQ, NVIDIA, and SOX data to `data/market.csv`.
2. Calculate daily returns for all variables.
3. Estimate expected returns using a pre-event estimation window.
4. Calculate abnormal returns during the event window.
5. Calculate cumulative abnormal returns.
6. Compare raw returns with abnormal returns.

Recommended windows:

| Window | Purpose |
| --- | --- |
| `-1/+1` | Immediate reaction. |
| `-3/+3` | Short delayed reaction. |
| `-7/+7` | Broader event-window effect. |
| `-60/-10` | Possible estimation window for market-model expected returns. |

---

## 5. Research Implications

Benchmark controls may change the interpretation of the adaptation model.

Current finding:
Joint Sword-2024A and Joint Sword-2024B show positive raw window returns.

Possible interpretations after benchmark controls:

| If Benchmark-Adjusted Returns Show... | Interpretation |
| --- | --- |
| Positive abnormal returns | Markets may genuinely have adapted, or investors viewed the events as contained. |
| Near-zero abnormal returns | Raw positive returns were likely driven by broader market momentum. |
| Negative abnormal returns | Geopolitical risk may have hurt Taiwan assets, but the effect was hidden by a global tech or AI rally. |

This means the adaptation model should remain provisional.

The revised theory should distinguish:

1. Raw market movement.
2. Benchmark-adjusted Taiwan-specific movement.
3. Semiconductor-sector movement.
4. AI-sector movement.
5. Geopolitical-risk perception.

## Bottom Line

The current raw-return analysis is useful for discovery, but it is not yet enough for causal identification.

To argue that market reactions are Taiwan-specific geopolitical effects, the project needs benchmark-adjusted abnormal returns using NASDAQ, NVIDIA, and SOX controls.

