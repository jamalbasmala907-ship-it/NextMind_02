"""
Master Reproducible Figure Generation Runner — Fuel&Go (Team NextMind)
Generates all verified Python vector figures for the Preliminary Design Report.
"""

from pathlib import Path
from plots.fig2_1_market_context import generate_figure as generate_fig2_1
from plots.fig5_2_telemetry_sizing import generate_figure as generate_fig5_2


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    out_2_1 = generate_fig2_1(project_root)
    print(f"[OK] Figure 2.1 generated: {out_2_1}")
    out_5_2 = generate_fig5_2(project_root)
    print(f"[OK] Figure 5.2 generated: {out_5_2}")


if __name__ == "__main__":
    main()
