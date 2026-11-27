# Data Directory & Provenance Index — Fuel&Go (Assignment 02)

This directory stores verified numerical datasets for reproducible Python figure generation (`scripts/plots/`).

## Dataset Inventory

### 1. `data/ev_market_summary_verified.csv`
- **Purpose**: Verified 2024 global and regional EV market context metrics for Chapter 2 (`Figure 2.1`).
- **Coverage Period**: 2024 (published in IEA *Global EV Outlook 2025*).
- **Units & Exact IEA Definitions**:
  - `million_vehicles`: Millions of passenger electric cars (BEV + PHEV) sold globally in 2024 (`more_than` 17 million).
  - `percent`: Global electric car share of new car sales (`more_than` 20%) and year-over-year sales growth vs. 2023 (`more_than` 25%).
  - `chargers_per_10_evs`: Public charging points per 10 electric cars in China (`more_than` 1.0 public charger per 10 electric cars; deterministic reciprocal upper bound `< 10` electric cars per public charger — **not** an exact measured value of 10).
  - `evs_per_charger`: Average electric cars per public charging point in the European Union (`average_approx` 13 electric cars per public charger).
- **Verified Primary Source (`iea2025gev`)**:
  - International Energy Agency (IEA), *Global EV Outlook 2025*, directly inspected on 2026-11-27:
    - Executive Summary: `https://www.iea.org/reports/global-ev-outlook-2025/executive-summary`
    - Electric Vehicle Charging: `https://www.iea.org/reports/global-ev-outlook-2025/electric-vehicle-charging`
- **Unverified / Excluded Rows (`UNVERIFIED_EXCLUDED`)**:
  - The two Israel 2024–2025 rows (`bev_share_of_new_car_sales`) originate from unverified secondary press summaries without a directly inspected Israel Central Bureau of Statistics (CBS) primary source. They are **UNVERIFIED** and **strictly excluded** from all empirical claims, charts, and calculations. Do **not** plot or cite these rows unless an official CBS primary dataset is directly inspected and archived first.
- **Charting Rules for `design` (`Figure 2.1`)**:
  - Filter strictly to `source_key == "iea2025gev"` (5 rows).
  - Do **not** plot vehicle sales (millions) and percentages on a shared numerical axis; use separate clearly labeled panels or KPI cards.
  - Preserve `"more than"` (`>`) and `"on average"` (`~`) uncertainty qualifiers on every label.
  - Do **not** plot China's `"more than 1 public charger per 10 electric cars"` (`< 10` EVs/charger) as an exact measured bar of `10`.
