#!/usr/bin/env python3
"""
Big Data Landscape — 2026
Style: Helvetica Neue, larger fonts, cleaned labels,
       section titles above coloured bands,
       bubble-area note in upper-left.
       Y-axis extended to 100 M PB to show LHC raw data on-scale.
       Annotation boxes repositioned to avoid axis/overlap clashes.
       White space at top reduced — axes fill more of the figure.
       All text sizes increased.
       Google Web Index moved right; SKA moved down.
       White-box annotation text at fontsize 16.
       Netflix label moved up and right.
       Background white.
       LHC Grid labels repositioned for clarity.
       Spam, YouTube, LHC Grid Streaming labels rearranged.

Requirements:
    pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# ═══════════════════════════════════════════════════════════════════
# 0.  Font detection & global style
# ═══════════════════════════════════════════════════════════════════
_available = {f.name for f in font_manager.fontManager.ttflist}
_font = next(
    (f for f in ['Helvetica Neue', 'Helvetica', 'Arial'] if f in _available),
    'DejaVu Sans',
)
print(f"Using font: {_font}")

plt.rcParams.update({
    'font.family':    _font,
    'font.size':       14,
    'axes.linewidth':  0.8,
})

BACKGROUND = 'white'

# ═══════════════════════════════════════════════════════════════════
# 1.  Data  (x_pos, PB_value, label_text, hex_colour, ann_x, ann_y)
#
#     x_pos   : arbitrary horizontal position (axis range 0 – 12.5)
#     PB_value: data volume in PB  (log10 is taken internally)
#     ann_x/y : text-box anchor in the same data-coordinate space
#
#     *** Changes in this version marked with  # <-- MOVED ***
# ═══════════════════════════════════════════════════════════════════
DATA = [

    # ── STREAMING ──────────────────────────────────────────────────
    (
        1.60, 54_750,
        "Netflix\n~150 M hrs/day streaming\n(1 GB/hr)  →  ~55 k PB/y",
        '#E50914',
        2.60, 6.40,
    ),
    (
        0.55, 10_300,
        "Global E-mail\n~376 B e-mails/day  (75 KB)\n→  ~10.3 k PB/y",
        '#8E44AD',
        1.50, 3.80,
    ),
    (
        1.10, 580,
        "Spam\n~320 B messages/day  (5 KB)\n→  ~580 PB/y",
        '#27AE60',
        0.50, 1.80,          # <-- MOVED: shifted left and below — clear of YouTube
    ),
    (
        2.45, 365,
        "YouTube Uploads\n~1 M hrs/day  (1 GB/hr)\n→  ~365 PB/y",
        '#CC0000',
        2.50, 1.50,          # <-- MOVED: pulled down below the cluster of bubbles
    ),
    (
        3.00, 800,
        "LHC Grid Data Streaming\n~80 GB/s inter-site\n→  ~800 PB/y  (2026)",
        '#003082',
        1.60, 4.80,          # <-- MOVED: up and left — sits above the cluster, arrow points down-right to bubble
    ),

    # ── STORAGE ────────────────────────────────────────────────────
    (
        5.50, 1_800_000,
        "AWS S3\n~1 800 EB total stored\n(~280 T objects,  2026 est.)",
        '#FF9900',
        6.90, 6.25,
    ),
    (
        4.15, 163,
        "Google Web Index\n~65 B pages  (2.5 MB avg)\n→  ~163 PB",
        '#34A853',
        5.30, 1.50,
    ),
    (
        4.85, 3_260,
        "Dropbox\n~130 M new free (2 GB)\n+ 2 M new paid (1.5 TB)\n→  ~3 260 PB/y",
        '#007EE5',
        3.70, 4.10,
    ),
    (
        6.30, 600_000,
        "Azure Blob Storage\n~600 EB total stored\n(2026 projection)",
        '#0089D6',
        7.55, 5.35,
    ),
    (
        6.75, 2_500,
        "LHC Grid Total Stored\n~2 500 PB  (disk + tape)\nall runs,  all tiers  (2026)",
        '#1A5276',
        5.60, 4.80,
    ),

    # ── PRODUCTION — HEP + ASTRONOMY ───────────────────────────────
    (
        7.70, 15,
        "Vera Rubin Obs.\n~15 PB/y\n(sky surveys, 2025+)",
        '#9B59B6',
        7.20, 2.20,
    ),
    (
        8.20, 30,
        "SKA (Partial Array)\n~30 PB/y\n(since 2025)",
        '#E67E22',
        9.40, 1.20,
    ),
    (
        8.85, 300,
        "LHC Run 3\nReal Data\n~300 PB/y",
        '#2980B9',
        7.70, 3.10,
    ),
    (
        9.45, 500,
        "LHC Run 3\nMonte Carlo\n~500 PB/y",
        '#4CAF50',
        9.95, 3.90,
    ),
    (
        10.10, 1_500,
        "HL-LHC Real Data\n~1 500 PB/y\n(projected, 2029+)",
        '#1ABC9C',
        11.10, 3.75,
    ),
    (
        10.80, 900,
        "HL-LHC Monte Carlo\n~900 PB/y\n(projected, 2029+)",
        '#2ECC71',
        11.35, 2.35,
    ),

    # ── LHC RAW (no trigger) — on-scale ────────────────────────────
    (
        9.10, 1e8,
        "LHC Run 3 Raw Data\n(no trigger selection)\n~10⁸ PB/y  [hypothetical]",
        '#7F8C8D',
        11.00, 8.40,
    ),
]

# ═══════════════════════════════════════════════════════════════════
# 2.  Figure & axes
# ═══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(22, 14))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(BACKGROUND)

fig.subplots_adjust(
    top    = 0.88,
    bottom = 0.08,
    left   = 0.09,
    right  = 0.98,
)

# ── Coloured background bands ──────────────────────────────────────
BANDS = [
    (-0.30,  3.30, '#4472C4'),   # Streaming
    ( 3.30,  7.25, '#C0504D'),   # Storage
    ( 7.25, 12.50, '#70AD47'),   # Production
]
for x0, x1, col in BANDS:
    ax.axvspan(x0, x1, color=col, alpha=0.09, zorder=0)

# ── Dashed dividers between bands ─────────────────────────────────
for xd in [3.30, 7.25]:
    ax.axvline(xd, color='#BBBBBB', lw=0.9, ls='--', alpha=0.50, zorder=1)

# ═══════════════════════════════════════════════════════════════════
# 3.  Bubbles  (area ∝ (log10(PB) × K)²)
# ═══════════════════════════════════════════════════════════════════
K = 30

for x, pb, ann, color, ann_x, ann_y in DATA:
    y = np.log10(pb)

    # ── Draw bubble ──
    ax.scatter(
        x, y,
        s          = (y * K) ** 2,
        c          = color,
        alpha      = 0.62,
        edgecolors = 'white',
        linewidths = 1.8,
        zorder     = 5,
    )

    # ── Annotate with arrow ──
    ax.annotate(
        ann,
        xy         = (x, y),
        xytext     = (ann_x, ann_y),
        ha         = 'center',
        va         = 'center',
        fontsize   = 16,
        color      = '#1A1A1A',
        arrowprops = dict(
            arrowstyle      = '-|>',
            color           = '#555555',
            lw              = 0.85,
            mutation_scale  = 10,
            connectionstyle = 'arc3,rad=0.05',
        ),
        bbox = dict(
            boxstyle  = 'round,pad=0.45',
            facecolor = 'white',
            edgecolor = '#CCCCCC',
            alpha     = 0.92,
            linewidth = 0.70,
        ),
        zorder = 10,
    )

# ═══════════════════════════════════════════════════════════════════
# 4.  Axis configuration
#     Y range: 0.55 → 9.20  (covers 10 PB up to ~1.6 × 10⁹ PB)
# ═══════════════════════════════════════════════════════════════════
XLIM = (-0.30, 12.50)
YLIM = ( 0.55,  9.20)
ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)

# ── Y-axis major ticks (one per decade) ───────────────────────────
ax.set_yticks(range(1, 10))
ax.set_yticklabels(
    [
        '10 PB',
        '100 PB',
        '1 k PB',
        '10 k PB',
        '100 k PB',
        '1 M PB',
        '10 M PB',
        '100 M PB',
        '1 B PB',
    ],
    fontsize = 15,
)

# ── Y-axis minor ticks (2–9 within each decade) ───────────────────
y_minor = [
    np.log10(m * 10**e)
    for e in range(1, 10)
    for m in range(2, 10)
]
ax.set_yticks(y_minor, minor=True)
ax.tick_params(axis='y', which='major', length=6, width=0.8)
ax.tick_params(axis='y', which='minor', length=3, width=0.6)

# ── Gridlines ─────────────────────────────────────────────────────
ax.yaxis.grid(True, which='major', ls='--', lw=0.5,
              color='gray', alpha=0.40, zorder=2)
ax.yaxis.grid(True, which='minor', ls=':',  lw=0.3,
              color='gray', alpha=0.22, zorder=2)
ax.set_axisbelow(True)

# ── Hide un-needed spines and x-ticks ────────────────────────────
ax.set_xticks([])
ax.spines[['top', 'right', 'bottom']].set_visible(False)

# ── Y-axis label ──────────────────────────────────────────────────
ax.set_ylabel(
    'Data Volume  (PB / year  or  total PB)',
    fontsize  = 17,
    labelpad  = 10,
)

# ── X-axis label (black, non-italic, title-case) ─────────────────
ax.set_xlabel(
    'Data Source Category',
    fontsize  = 17,
    labelpad  = 10,
    color     = 'black',
    fontstyle = 'normal',
)

# ═══════════════════════════════════════════════════════════════════
# 5.  Section titles ABOVE the coloured bands
# ═══════════════════════════════════════════════════════════════════
_xleft  = XLIM[0]
_xwidth = XLIM[1] - XLIM[0]

SECTIONS = [
    ('Streaming',  1.500, '#2453A2'),
    ('Storage',    5.275, '#A12F2E'),
    ('Production', 9.875, '#4A7A2A'),
]
for label, x_data_mid, col in SECTIONS:
    x_norm = (x_data_mid - _xleft) / _xwidth
    ax.text(
        x_norm, 1.03,
        label,
        transform  = ax.transAxes,
        ha         = 'center',
        va         = 'bottom',
        fontsize   = 21,
        fontweight = 'bold',
        color      = col,
        clip_on    = False,
    )

# ═══════════════════════════════════════════════════════════════════
# 6.  Main figure title
# ═══════════════════════════════════════════════════════════════════
fig.suptitle(
    'Big Data Landscape — 2026',
    fontsize   = 27,
    fontweight = 'bold',
    y          = 0.99,
    color      = '#1A1A2E',
)

# ═══════════════════════════════════════════════════════════════════
# 7.  Bubble-area note in upper-left
# ═══════════════════════════════════════════════════════════════════
ax.text(
    0.005, 0.975,
    'Bubble area  ∝  log₁₀(data volume in PB)',
    transform = ax.transAxes,
    ha        = 'left',
    va        = 'top',
    fontsize  = 13,
    color     = '#444444',
    bbox      = dict(
        boxstyle  = 'round,pad=0.42',
        facecolor = 'white',
        edgecolor = '#CCCCCC',
        alpha     = 0.92,
        linewidth = 0.70,
    ),
    zorder = 10,
)

# ═══════════════════════════════════════════════════════════════════
# 8.  Footnote / data sources
# ═══════════════════════════════════════════════════════════════════
ax.text(
    0.01, 0.005,
    "2026 estimates.  "
    "Sources: Netflix Q1 2026 investor report · "
    "Statista e-mail volume statistics (2024–26) · "
    "AWS re:Invent 2025 projections · "
    "LHC Grid (WLCG) resource pledges & data transfer statistics (CERN, 2024–2026) · "
    "Rubin Obs. LSST DM plan · "
    "SKA-Mid SDP specifications · "
    "HL-LHC Computing TDR (CERN-LHCC-2020-015).",
    transform = ax.transAxes,
    fontsize  = 8.5,
    color     = '#999999',
    va        = 'bottom',
)

# ═══════════════════════════════════════════════════════════════════
# 9.  Save & show
# ═══════════════════════════════════════════════════════════════════
plt.savefig('big_data_landscape_2026.pdf',
            bbox_inches='tight')
plt.savefig('big_data_landscape_2026.png',
            dpi=200,
            bbox_inches='tight',
            facecolor=BACKGROUND)

plt.show()
