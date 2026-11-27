"""
Reproducible Python Plot #2 (Figure 5.2):
Analytical Telemetry Bandwidth Scaling and Illustrative Authorization Latency Budget

Strictly implements the analytical sizing model in sections/sec05_data_protocols.tex
and docs/RESEARCH_NOTES.md (Sec. 9.2):
  - Panel A: Telemetry Bandwidth Scaling (Mbps) vs Concurrent Sessions N in
    [100, 500, 1000, 2500, 5000] via B_total(N) = N * (P_bytes * 8) / (T_interval * 1e6).
      * Liquid-Fuel [Assumption: 512 B / 2 s = 2.048 kbps/session]:
        0.20, 1.02, 2.05, 5.12, 10.24 Mbps
      * EV Charging [Assumption: 768 B / 15 s = 0.4096 kbps/session]:
        0.04, 0.20, 0.41, 1.02, 2.05 Mbps
  - Panel B: Stacked Horizontal Illustrative Authorization Latency Budget (ms):
      * Fuel: 150 edge + 120 orch + 900 PSP + 1200 forecourt = 2370 ms (2.37 s)
      * EV Roaming: 150 edge + 120 orch + 900 PSP + 1800 EV roaming = 2970 ms (2.97 s)
      * Dashed vertical reference line at 1000 ms: NN/g 1.0 s UX Guidance (not an SLA)

Outputs vector PDF:
    figures/fig5_2_telemetry_sizing.pdf
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# Fuel&Go WCAG-hardened palette
FG_ESPRESSO = "#403011"
FG_TEAL = "#1A565E"
FG_TEAL_TINT = "#E6F0F2"
FG_ECO_GREEN = "#2F6F4E"
FG_ECO_TINT = "#E7F2EC"
FG_OLIVE = "#626C3B"
FG_TERRACOTTA = "#B2562F"
FG_AMBER = "#E8AF3B"
FG_TEXT_AMBER = "#8C5A00"
FG_SOFT_CREAM = "#FAF4E6"
FG_RULE_GRAY = "#D8D2C5"


def compute_bandwidth_mbps(n_sessions: np.ndarray, payload_bytes: float, interval_s: float) -> np.ndarray:
    """B_total(N) = N * (P_bytes * 8) / (T_interval * 1e6) [Mbps]."""
    return n_sessions * (payload_bytes * 8.0) / (interval_s * 1e6)


def generate_figure(project_root: Path) -> Path:
    out_path = project_root / "figures" / "fig5_2_telemetry_sizing.pdf"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Panel A calculations & verification
    n_vals = np.array([100, 500, 1000, 2500, 5000], dtype=float)
    bw_fuel = compute_bandwidth_mbps(n_vals, payload_bytes=512.0, interval_s=2.0)
    bw_ev = compute_bandwidth_mbps(n_vals, payload_bytes=768.0, interval_s=15.0)

    expected_fuel = np.array([0.2048, 1.024, 2.048, 5.12, 10.24])
    expected_ev = np.array([0.04096, 0.2048, 0.4096, 1.024, 2.048])
    assert np.allclose(bw_fuel, expected_fuel, atol=1e-6), f"Fuel BW mismatch: {bw_fuel}"
    assert np.allclose(bw_ev, expected_ev, atol=1e-6), f"EV BW mismatch: {bw_ev}"

    # Panel B latency budget (ms) & verification
    edge_ms = np.array([150.0, 150.0])
    orch_ms = np.array([120.0, 120.0])
    psp_ms = np.array([900.0, 900.0])
    op_ms = np.array([1200.0, 1800.0])  # [Fuel forecourt, EV roaming]
    totals_ms = edge_ms + orch_ms + psp_ms + op_ms
    assert np.allclose(totals_ms, np.array([2370.0, 2970.0]), atol=1e-6)

    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Calibri", "DejaVu Sans"],
        "font.size": 10,
        "axes.titlesize": 10.5,
        "axes.labelsize": 10,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.fontsize": 9.5,
        "text.color": FG_ESPRESSO,
        "axes.labelcolor": FG_ESPRESSO,
        "xtick.color": FG_ESPRESSO,
        "ytick.color": FG_ESPRESSO,
        "axes.edgecolor": FG_RULE_GRAY,
        "pdf.fonttype": 42,
    })

    fig, (ax_bw, ax_lat) = plt.subplots(
        2, 1,
        figsize=(6.45, 5.55),
        facecolor="white",
        gridspec_kw={"height_ratios": [1.22, 1.0], "hspace": 0.48},
    )

    # ------------------------------------------------------------------
    # PANEL A: Telemetry Bandwidth Scaling (Mbps) vs Concurrent Sessions N
    # ------------------------------------------------------------------
    ax_bw.set_facecolor("white")
    ax_bw.plot(
        n_vals, bw_fuel,
        color=FG_TERRACOTTA, linestyle="-", linewidth=2.0,
        marker="o", markersize=6.5, markerfacecolor=FG_TERRACOTTA, markeredgecolor="white",
        label="Liquid-Fuel [Assumption: 512 B / 2 s = 2.048 kbps/sess]",
        zorder=4,
    )
    ax_bw.plot(
        n_vals, bw_ev,
        color=FG_ECO_GREEN, linestyle="--", linewidth=2.0,
        marker="s", markersize=6.0, markerfacecolor=FG_ECO_GREEN, markeredgecolor="white",
        label="EV Charging [Assumption: 768 B / 15 s = 0.410 kbps/sess]",
        zorder=4,
    )

    for x, yf, ye in zip(n_vals, bw_fuel, bw_ev):
        ax_bw.annotate(
            f"{yf:.2f}",
            xy=(x, yf), xytext=(0, 6), textcoords="offset points",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=FG_TERRACOTTA,
        )
        ax_bw.annotate(
            f"{ye:.2f}",
            xy=(x, ye), xytext=(0, -10), textcoords="offset points",
            ha="center", va="top", fontsize=9.5, fontweight="bold", color=FG_ECO_GREEN,
        )

    ax_bw.set_title(
        "A. Analytical Telemetry Bandwidth Scaling (Mbps) vs. Concurrent Sessions",
        fontsize=10.5, fontweight="bold", loc="left", pad=8,
    )
    ax_bw.set_xlabel("Concurrent Active Sessions (N)")
    ax_bw.set_ylabel("Aggregate Bandwidth (Mbps)")
    ax_bw.set_xticks(n_vals)
    ax_bw.set_xticklabels([f"{int(n):,}" for n in n_vals])
    ax_bw.set_xlim(-180, 5380)
    ax_bw.set_ylim(-1.6, 12.2)
    ax_bw.grid(True, linestyle="--", color=FG_RULE_GRAY, alpha=0.85, zorder=0)
    ax_bw.spines["top"].set_visible(False)
    ax_bw.spines["right"].set_visible(False)
    ax_bw.legend(loc="upper left", frameon=True, facecolor=FG_SOFT_CREAM, edgecolor=FG_RULE_GRAY)

    # ------------------------------------------------------------------
    # PANEL B: Stacked Horizontal Illustrative Authorization Latency Budget (ms)
    # ------------------------------------------------------------------
    ax_lat.set_facecolor("white")
    y_pos = np.array([1.0, 0.0])  # Top = Fuel, Bottom = EV Roaming
    bar_h = 0.48

    left_orch = edge_ms
    left_psp = edge_ms + orch_ms
    left_op = edge_ms + orch_ms + psp_ms

    ax_lat.barh(
        y_pos, edge_ms, height=bar_h,
        color=FG_TEAL, edgecolor=FG_ESPRESSO, linewidth=0.7,
        label="Edge/GW (150 ms)", zorder=3,
    )
    ax_lat.barh(
        y_pos, orch_ms, left=left_orch, height=bar_h,
        color=FG_OLIVE, edgecolor=FG_ESPRESSO, linewidth=0.7, hatch="..",
        label="Orch. (120 ms)", zorder=3,
    )
    ax_lat.barh(
        y_pos, psp_ms, left=left_psp, height=bar_h,
        color=FG_AMBER, edgecolor=FG_ESPRESSO, linewidth=0.7, hatch="//",
        label="PSP Hold (900 ms)", zorder=3,
    )
    # Operator segment (Fuel forecourt = 1200 ms, EV roaming = 1800 ms)
    ax_lat.barh(
        [y_pos[0]], [op_ms[0]], left=[left_op[0]], height=bar_h,
        color=FG_TERRACOTTA, edgecolor=FG_ESPRESSO, linewidth=0.7, hatch="\\\\",
        label="Forecourt (1200 ms)", zorder=3,
    )
    ax_lat.barh(
        [y_pos[1]], [op_ms[1]], left=[left_op[1]], height=bar_h,
        color=FG_ECO_GREEN, edgecolor=FG_ESPRESSO, linewidth=0.7, hatch="xx",
        label="EV Roaming (1800 ms)", zorder=3,
    )

    # Total labels at end of each bar
    ax_lat.text(
        totals_ms[0] + 60, y_pos[0],
        f"{int(totals_ms[0]):,} ms (2.37 s)",
        va="center", ha="left", fontsize=9.5, fontweight="bold", color=FG_TERRACOTTA,
    )
    ax_lat.text(
        totals_ms[1] + 60, y_pos[1],
        f"{int(totals_ms[1]):,} ms (2.97 s)",
        va="center", ha="left", fontsize=9.5, fontweight="bold", color=FG_ECO_GREEN,
    )

    # Dashed vertical reference line at 1000 ms (NN/g 1.0 s UX Guidance)
    ax_lat.axvline(1000.0, color=FG_ESPRESSO, linestyle="--", linewidth=1.6, zorder=5)
    ax_lat.text(
        1030.0, 1.44,
        "NN/g 1.0 s UX Guidance (not an SLA)",
        va="top", ha="left", fontsize=9.5, fontweight="bold", color=FG_ESPRESSO,
        bbox=dict(boxstyle="round,pad=0.2", facecolor=FG_SOFT_CREAM, edgecolor=FG_RULE_GRAY, lw=0.7),
        zorder=6,
    )

    ax_lat.set_title(
        "B. Illustrative Authorization Latency Budget Decomposition (ms)",
        fontsize=10.5, fontweight="bold", loc="left", pad=8,
    )
    ax_lat.set_yticks(y_pos)
    ax_lat.set_yticklabels(["Liquid-Fuel\nAuth", "EV Roaming\nAuth"], fontweight="bold", fontsize=9.8)
    ax_lat.set_xlabel("End-to-End Authorization Latency (ms)")
    ax_lat.set_xlim(0, 3850)
    ax_lat.set_ylim(-0.55, 1.55)
    ax_lat.grid(axis="x", linestyle="--", color=FG_RULE_GRAY, alpha=0.85, zorder=0)
    ax_lat.spines["top"].set_visible(False)
    ax_lat.spines["right"].set_visible(False)
    ax_lat.legend(
        loc="upper center", bbox_to_anchor=(0.5, -0.32),
        ncol=3, frameon=True, facecolor=FG_SOFT_CREAM, edgecolor=FG_RULE_GRAY,
        columnspacing=0.9, handletextpad=0.4,
    )

    # Explicit provenance footer (well below legend)
    fig.text(
        0.5, 0.012,
        "[Calculation] + [Assumption] -- Analytical Sizing Model (Illustrative Inputs, Not Empirical Field Data)",
        ha="center", va="bottom", fontsize=9.5, style="italic", color=FG_ESPRESSO,
    )

    plt.subplots_adjust(left=0.14, right=0.98, top=0.94, bottom=0.22)
    fig.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    saved = generate_figure(root)
    print(f"Generated: {saved}")
