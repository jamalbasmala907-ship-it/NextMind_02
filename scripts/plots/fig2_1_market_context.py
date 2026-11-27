"""
Reproducible Python Plot #1 (Figure 2.1):
Global EV Adoption and Regional Public Charging Coverage (2024)

Strictly reads ONLY the 5 verified `iea2025gev` rows from:
    data/ev_market_summary_verified.csv
and STRICTLY EXCLUDES Israel rows marked UNVERIFIED_EXCLUDED.

Design (Finding 1):
  - Row 1: Three separate designed KPI cards (zero shared numerical axis) for
    2024 Global EV Sales Momentum, preserving "more than" qualifiers.
  - Row 2: Bound-aware horizontal Public Charging Density (2024) panel
    (EVs per public charger, lower = denser):
      * China: open-ended hatched upper-bounded range [0, 10) with dashed
        threshold at 10 and leftward arrow labeled "Strictly < 10 EVs/charger"
        (upper bound from > 1.0 chg per 10 EVs).
      * European Union: distinct point marker with approximate indicator
        labeled "~13 EVs/charger (average, approx.)".

Outputs vector PDF:
    figures/fig2_1_market_context.pdf
"""

from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


# Fuel&Go WCAG-hardened palette
FG_ESPRESSO = "#403011"
FG_TEAL = "#1A565E"
FG_TEAL_TINT = "#E6F0F2"
FG_ECO_GREEN = "#2F6F4E"
FG_ECO_TINT = "#E7F2EC"
FG_OLIVE = "#626C3B"
FG_PALE_SAGE = "#EAEDDE"
FG_TERRACOTTA = "#B2562F"
FG_TERRA_TINT = "#F9ECE6"
FG_AMBER = "#E8AF3B"
FG_SOFT_CREAM = "#FAF4E6"
FG_RULE_GRAY = "#D8D2C5"


def generate_figure(project_root: Path) -> Path:
    csv_path = project_root / "data" / "ev_market_summary_verified.csv"
    out_path = project_root / "figures" / "fig2_1_market_context.pdf"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)

    # STRICT PROVENANCE FILTER: ONLY verified iea2025gev rows
    verified = df[
        (df["source_key"] == "iea2025gev")
        & (df["provenance_tag"] == "Sourced Measurement")
    ].copy()

    if len(verified) != 5:
        raise ValueError(
            f"Expected exactly 5 verified iea2025gev rows, found {len(verified)}"
        )

    def get_val(metric: str) -> float:
        row = verified.loc[verified["metric"] == metric]
        if len(row) != 1:
            raise ValueError(f"Missing or duplicate metric: {metric}")
        return float(row["value"].iloc[0])

    sales_m = get_val("electric_car_sales")
    share_pct = get_val("electric_car_sales_share_of_new_cars")
    yoy_pct = get_val("electric_car_sales_yoy_growth")
    china_chg_per_10 = get_val("public_chargers_per_10_electric_cars")
    eu_evs_per_chg = get_val("electric_cars_per_public_charger")

    # Reciprocal upper bound: > 1.0 charger per 10 EVs => strictly < 10.0 EVs per charger
    china_upper_bound = 10.0 / china_chg_per_10

    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "DejaVu Sans"],
        "font.size": 10,
        "axes.titlesize": 10.5,
        "axes.labelsize": 10,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "text.color": FG_ESPRESSO,
        "axes.labelcolor": FG_ESPRESSO,
        "xtick.color": FG_ESPRESSO,
        "ytick.color": FG_ESPRESSO,
        "axes.edgecolor": FG_RULE_GRAY,
        "pdf.fonttype": 42,
    })

    fig = plt.figure(figsize=(6.65, 4.30), facecolor="white")
    gs = fig.add_gridspec(2, 1, height_ratios=[1.05, 1.35], hspace=0.34)

    # ------------------------------------------------------------------
    # ROW 1: Three Separate Designed KPI Cards (No Shared Numerical Axis)
    # ------------------------------------------------------------------
    ax_kpi = fig.add_subplot(gs[0])
    ax_kpi.set_xlim(0, 10)
    ax_kpi.set_ylim(0, 2.35)
    ax_kpi.axis("off")

    ax_kpi.text(
        0.0,
        2.22,
        "A. Global Electric Car Sales Momentum (2024) — Separate KPI Indicators",
        fontsize=10.5,
        fontweight="bold",
        color=FG_ESPRESSO,
        va="top",
    )

    cards = [
        {
            "x": 0.0,
            "accent": FG_TEAL,
            "fill": FG_TEAL_TINT,
            "kicker": "GLOBAL SALES (BEV + PHEV)",
            "value": f"More than {sales_m:.0f}M",
            "sub": "electric cars sold worldwide",
        },
        {
            "x": 3.45,
            "accent": FG_ECO_GREEN,
            "fill": FG_ECO_TINT,
            "kicker": "NEW CAR MARKET SHARE",
            "value": f"More than {share_pct:.0f}%",
            "sub": "of all global new car sales",
        },
        {
            "x": 6.90,
            "accent": FG_OLIVE,
            "fill": FG_PALE_SAGE,
            "kicker": "YEAR-OVER-YEAR GROWTH",
            "value": f"More than {yoy_pct:.0f}%",
            "sub": "sales growth vs. 2023",
        },
    ]

    card_w = 3.10
    card_h = 1.72
    card_y = 0.08

    for c in cards:
        box = FancyBboxPatch(
            (c["x"], card_y),
            card_w,
            card_h,
            boxstyle="round,pad=0.04,rounding_size=0.12",
            facecolor=c["fill"],
            edgecolor=c["accent"],
            linewidth=1.2,
        )
        ax_kpi.add_patch(box)

        # Top accent stripe (grayscale-safe solid bar)
        stripe = Rectangle(
            (c["x"] + 0.04, card_y + card_h - 0.10),
            card_w - 0.08,
            0.10,
            facecolor=c["accent"],
            edgecolor="none",
        )
        ax_kpi.add_patch(stripe)

        cx = c["x"] + card_w / 2.0
        ax_kpi.text(
            cx,
            card_y + 1.32,
            c["kicker"],
            ha="center",
            va="center",
            fontsize=9.5,
            fontweight="bold",
            color=c["accent"],
        )
        ax_kpi.text(
            cx,
            card_y + 0.80,
            c["value"],
            ha="center",
            va="center",
            fontsize=13.5,
            fontweight="bold",
            color=FG_ESPRESSO,
        )
        ax_kpi.text(
            cx,
            card_y + 0.30,
            c["sub"],
            ha="center",
            va="center",
            fontsize=9.5,
            color=FG_ESPRESSO,
        )

    # ------------------------------------------------------------------
    # ROW 2: Bound-Aware Horizontal Public Charging Density Panel (2024)
    # ------------------------------------------------------------------
    ax_chg = fig.add_subplot(gs[1])
    ax_chg.set_facecolor("white")

    y_china = 1.0
    y_eu = 0.0

    # China: open-ended hatched upper-bounded range [0, 10) (NOT a solid bar at 10.0)
    bar_h = 0.44
    china_rect = Rectangle(
        (0.0, y_china - bar_h / 2.0),
        china_upper_bound,
        bar_h,
        facecolor=FG_TERRA_TINT,
        edgecolor=FG_TERRACOTTA,
        linewidth=1.1,
        linestyle="--",
        hatch="///",
        zorder=2,
    )
    ax_chg.add_patch(china_rect)

    # Dashed vertical threshold at 10.0
    ax_chg.plot(
        [china_upper_bound, china_upper_bound],
        [y_china - 0.32, y_china + 0.32],
        color=FG_TERRACOTTA,
        linestyle="--",
        linewidth=1.8,
        zorder=4,
    )

    # Leftward arrow indicating strictly < 10
    ax_chg.annotate(
        "",
        xy=(6.6, y_china),
        xytext=(china_upper_bound, y_china),
        arrowprops=dict(
            arrowstyle="-|>,head_length=0.6,head_width=0.35",
            color=FG_TERRACOTTA,
            lw=1.8,
        ),
        zorder=5,
    )

    ax_chg.text(
        china_upper_bound + 0.35,
        y_china + 0.08,
        f"Strictly < {china_upper_bound:.0f} EVs/charger",
        va="center",
        ha="left",
        fontsize=9.8,
        fontweight="bold",
        color=FG_TERRACOTTA,
    )
    ax_chg.text(
        china_upper_bound + 0.35,
        y_china - 0.18,
        f"(upper bound from > {china_chg_per_10:.1f} chg per 10 EVs)",
        va="center",
        ha="left",
        fontsize=9.5,
        style="italic",
        color=FG_ESPRESSO,
    )

    # European Union: distinct point marker with approximate indicator
    ax_chg.plot(
        [eu_evs_per_chg - 0.6, eu_evs_per_chg + 0.6],
        [y_eu, y_eu],
        color=FG_TEAL,
        linewidth=2.0,
        linestyle=":",
        zorder=3,
    )
    ax_chg.scatter(
        [eu_evs_per_chg],
        [y_eu],
        s=95,
        marker="D",
        facecolor=FG_AMBER,
        edgecolor=FG_ESPRESSO,
        linewidth=1.3,
        zorder=5,
    )
    ax_chg.text(
        eu_evs_per_chg + 0.75,
        y_eu + 0.06,
        f"~{eu_evs_per_chg:.0f} EVs/charger",
        va="center",
        ha="left",
        fontsize=9.8,
        fontweight="bold",
        color=FG_ESPRESSO,
    )
    ax_chg.text(
        eu_evs_per_chg + 0.75,
        y_eu - 0.18,
        "(average, approx.)",
        va="center",
        ha="left",
        fontsize=9.5,
        style="italic",
        color=FG_ESPRESSO,
    )

    ax_chg.set_title(
        "B. Regional Public Charging Density (2024) — Bound-Aware Comparison",
        fontsize=10.5,
        fontweight="bold",
        loc="left",
        pad=8,
    )
    ax_chg.set_yticks([y_eu, y_china])
    ax_chg.set_yticklabels(["European Union", "China"], fontweight="bold", fontsize=10)
    ax_chg.set_xlim(0, 21.5)
    ax_chg.set_ylim(-0.55, 1.55)
    ax_chg.set_xlabel("Electric Cars per Public Charger (Lower = Denser Public Coverage)")
    ax_chg.grid(axis="x", linestyle="--", color=FG_RULE_GRAY, alpha=0.85, zorder=0)
    ax_chg.spines["top"].set_visible(False)
    ax_chg.spines["right"].set_visible(False)

    # Explicit provenance footer matching sec02_users_stakeholders.tex caption
    fig.text(
        0.5,
        0.01,
        "Provenance: [Sourced Measurement] IEA Global EV Outlook 2025 (5 verified rows; Israel rows excluded); "
        "China < 10 EVs/chg is [Calculation] from > 1.0 chg/10 EVs.",
        ha="center",
        va="bottom",
        fontsize=9.5,
        style="italic",
        color=FG_ESPRESSO,
    )

    plt.subplots_adjust(left=0.17, right=0.98, top=0.96, bottom=0.16)
    fig.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    saved = generate_figure(root)
    print(f"Generated: {saved}")
