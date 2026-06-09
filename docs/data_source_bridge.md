# Data Source Bridge

> Academic Research Notice:
> This document is provided for educational and research reference purposes only.
> It may contain preliminary analysis, working assumptions, draft frameworks, or evolving interpretations.
> It should not be treated as a peer-reviewed publication.

## 1. Purpose

Repo 2 reuses cleaned market data produced during Repo 1.

Repo 1 created the cleaned market dataset manually.
Repo 2 standardizes it as the engine input file.

## 2. Source File

Original cleaned file:

data/processed/market.csv

Standardized engine input:

data/market_data.csv

## 3. Why This Matters

Repo 2 is not starting from raw data collection yet.

The current version focuses on automating the event-study workflow after market data has already been cleaned.

This allows the engine to focus on:
- reading event inputs
- selecting asset and benchmark columns
- calculating returns
- calculating abnormal returns
- calculating CAR
- generating outputs

## 4. Future Version

A future version may automate raw data downloading directly from market data sources.

For now, data/market_data.csv is treated as the standardized input contract for the engine.
