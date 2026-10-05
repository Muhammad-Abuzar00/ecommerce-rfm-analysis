"""Shared chart style for every notebook in this project.

Keeping the theme, palette and save settings in one place means the charts
look like they belong to the same report.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import FuncFormatter

# Palette: one main colour, one highlight, one neutral for context.
BLUE = "#2a78d6"
ORANGE = "#eb6834"
GREY = "#b9b8b2"
DARK_BLUE = "#184f95"
TEXT = "#0b0b0b"
TEXT_MUTED = "#52514e"

# Single-hue sequential ramp for heatmaps (light = low, dark = high).
BLUE_RAMP = LinearSegmentedColormap.from_list(
    "blue_ramp", ["#f4f8fd", "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
)

IMAGES = Path(__file__).resolve().parent.parent / "images"


def set_style():
    """Apply the project-wide seaborn/matplotlib theme."""
    sns.set_theme(style="whitegrid", font_scale=1.05)
    plt.rcParams.update({
        "figure.figsize": (11, 5.5),
        "figure.dpi": 100,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.titlepad": 12,
        "axes.labelsize": 11,
        "axes.labelcolor": TEXT_MUTED,
        "axes.edgecolor": "#d9d8d4",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.color": "#ecebe8",
        "grid.linewidth": 0.8,
        "xtick.color": TEXT_MUTED,
        "ytick.color": TEXT_MUTED,
        "text.color": TEXT,
        "legend.frameon": False,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
    })


def titles(ax, title, subtitle=None):
    """Bold headline that states the insight, with an optional muted line under it."""
    if subtitle:
        ax.set_title(title, pad=28)
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=10.5,
                color=TEXT_MUTED, va="bottom", ha="left")
    else:
        ax.set_title(title)


def save_fig(fig, name):
    """Save a figure to images/ as a 300 dpi PNG."""
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / f"{name}.png"
    fig.savefig(path, dpi=300)
    print(f"saved {path.name}")


def gbp(x, _pos=None):
    """Axis formatter: 1500000 -> £1.5M, 25000 -> £25k."""
    if abs(x) >= 1e6:
        return f"£{x / 1e6:.1f}M"
    if abs(x) >= 1e3:
        return f"£{x / 1e3:.0f}k"
    return f"£{x:.0f}"


GBP = FuncFormatter(gbp)
