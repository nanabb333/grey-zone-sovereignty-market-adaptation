# Grey-Zone Sovereignty and Market Adaptation: Financial Responses to Taiwan-Related Geopolitical Shocks

**Author:** Tina Chen

## Abstract

This project examines why some Taiwan-related geopolitical shocks fail to generate persistent financial-market damage despite elevated objective risk. It develops a grey-zone sovereignty framework, arguing that Taiwan's unresolved sovereignty status generates recurring geopolitical and geoeconomic shocks. Market reactions are shaped by investor interpretation, including threat, opportunity, adaptation, and surprise. The empirical strategy is an exploratory event study of abnormal returns for the Taiwan Stock Exchange Weighted Index (TWSE) and Taiwan Semiconductor Manufacturing Company (TSMC) around Taiwan-related events from 2022 to 2025.

## Project Status

This is a research portfolio repository for an exploratory event-study project. The findings should be interpreted as descriptive and theory-building rather than definitive causal proof.

## Research Question

Why do some Taiwan-related geopolitical shocks produce negative financial-market reactions while others generate muted or even positive abnormal returns?

## Theory Summary

The project argues that Taiwan-related geopolitical risk should not be understood as an automatic risk-damage mechanism. Taiwan's unresolved sovereignty status produces repeated grey-zone crises, military signaling, diplomatic disputes, and geoeconomic policy shocks. Investors interpret these events through multiple frames: direct threat, strategic opportunity, market adaptation, and surprise. Because markets learn from repeated episodes and distinguish between different kinds of Taiwan-related shocks, similar levels of objective risk can produce different financial responses.

## Hypotheses

- **H1: Risk events** are expected to generate negative abnormal returns on average because they increase perceived military, diplomatic, or sanctions-related threat.
- **H2: Strategic_Importance events** are expected to generate positive abnormal returns on average because they reinforce Taiwan's centrality in semiconductor supply chains and allied industrial strategy.
- **H3: Repeated grey-zone events** are expected to produce weaker or more variable negative reactions as investors adapt to recurring Taiwan Strait risk.
- **H4: Surprise matters:** events that deviate from investor expectations are expected to produce stronger abnormal returns than events that are already anticipated.

## Data and Method

The empirical strategy is an exploratory event study. The project analyzes abnormal returns for TWSE and TSMC around Taiwan-related events from 2022 to 2025. Events are classified as either `Risk` or `Strategic_Importance`. TWSE abnormal returns are benchmark-adjusted against NASDAQ, while TSMC abnormal returns are benchmark-adjusted against the Philadelphia Semiconductor Index.

Daily market data are collected with `yfinance`. The analysis calculates daily returns, benchmark-adjusted abnormal returns, and cumulative abnormal returns (CARs) over short event windows. The project emphasizes transparent coding choices and interpretable results rather than complex forecasting or causal-identification machinery.

## Repository Structure

```text
.
├── README.md
├── paper/
│   └── Grey-Zone-Sovereignty-and-Market-Adaptation.pdf
├── data/
│   ├── raw/
│   ├── processed/
│   └── events/
├── docs/
├── scripts/
│   ├── download_market_data.py
│   ├── clean_market_data.py
│   ├── calculate_abnormal_returns.py
│   └── generate_figures.py
├── figures/
├── notes/
│   └── drafts/
├── output/
├── results/
│   └── summary_results.md
├── requirements.txt
└── .gitignore
```

## Full Dissertation

The full dissertation manuscript is available at:

[Grey-Zone-Sovereignty-and-Market-Adaptation.pdf](paper/Grey-Zone-Sovereignty-and-Market-Adaptation.pdf)

## Main Findings

- Risk events are negative on average.
- Strategic-importance events are positive on average.
- However, individual cases vary substantially.
- Some risk events, such as Joint Sword-2024B, generate positive abnormal returns.
- This supports a conditional interpretation of geopolitical risk rather than an automatic risk-damage model.

## Key Figure

![Average cumulative abnormal returns by event type](figures/average_car_by_event_type.png)

## Results Outputs

- `figures/average_car_by_event_type.png`: summarizes average cumulative abnormal returns by event classification.
- `figures/event_level_car_scatter.png`: shows event-level variation in TWSE and TSMC cumulative abnormal returns.
- `results/event_abnormal_return_summary.csv`: reports event-window abnormal-return and CAR results used in the analysis.

## Limitations

This is an exploratory event study with a small number of Taiwan-related events. Event classification requires interpretive judgment, and some shocks overlap with broader market conditions, earnings expectations, or global technology-sector movements. The benchmark-adjusted abnormal-return approach improves comparability, but it does not fully isolate causality. The findings should therefore be read as evidence of conditional market interpretation and adaptation, not as definitive proof of a single causal mechanism.

## How to Reproduce the Analysis

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download market data:

   ```bash
   python scripts/download_market_data.py
   ```

4. Clean the market data:

   ```bash
   python scripts/clean_market_data.py
   ```

5. Calculate abnormal returns and event-window results:

   ```bash
   python scripts/calculate_abnormal_returns.py
   ```

6. Generate figures:

   ```bash
   python scripts/generate_figures.py
   ```

The main processed datasets are written to `data/processed/`, event coding files are stored in `data/events/`, figures are written to `figures/`, and summary tables are written to `results/`.

## Paper

The completed dissertation paper is stored at:

```text
paper/Grey-Zone-Sovereignty-and-Market-Adaptation.pdf
```

## License

This project is for academic and research use. Reuse and adaptation permitted with attribution.
