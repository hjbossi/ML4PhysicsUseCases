#!/usr/bin/env python3
"""
Streaming Data Rate vs. Latency Requirement — 2026
Updated from A3D3 Institute figure (a3d3.ai)
Bubble area ∝ ((log10(annual_PB) + 4) × K)²

Requirements:
    pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# ═══════════════════════════════════════════════════════════════════
# 0.  Font detection
# ═══════════════════════════════════════════════════════════════════
_available = {f.name for f in font_manager.fontManager.ttflist}
_font = next(
    (f for f in ['Helvetica Neue', 'Helvetica', 'Arial'] if f in _available),
    'DejaVu Sans',
)
print(f"Using font: {_font}")

plt.rcParams.update({
    'font.family':    _font,
    'font.size':       11,
    'axes.linewidth':  0.9,
})

BACKGROUND = 'white'

# ═══════════════════════════════════════════════════════════════════
# 1.  DATA
#     (name, latency_s, rate_B_s, annual_PB, colour,
#      ann_x, ann_y, ha, va)
#
#     Bubble area = ((log10(annual_PB) + 4) * K)^2  in matplotlib pt²
#     The +4 shift maps 1 TB/yr (10^-3 PB) → scale factor 1,
#     keeping all sizes positive.
# ═══════════════════════════════════════════════════════════════════
K = 18   # bubble scale factor

DATA = [
    # ── FPGA/ASIC region (latency < ~10 ms) ──────────────────────
    # name             lat     rate    PB/yr  colour     ann_x   ann_y   ha       va
    ('LHC L1T',        4e-6,   2e12,   500,   '#2166AC', 1.8e-5, 6e11,  'left',  'top'),
    ('DUNE',           5e-3,   3e10,    20,   '#FF7F0E', 2e-2,   1e10,  'left',  'top'),
    ('Neuro',          1e-4,   5e7,    0.5,   '#7B3F00', 4e-5,   1.8e8, 'right', 'bottom'),

    # ── Boundary / CPU-GPU region ─────────────────────────────────
    ('LHC HLT',        1e-1,   5e13,   300,   '#D62728', 1.8e-1, 2e13,  'left',  'top'),
    ('SKA',            5e-1,   2e12,    30,   '#6A0572', 1.8,    8e12,  'left',  'bottom'),
    ('Google Cloud',   2.0,    2e14,   1e6,   '#8C8C00', 6.0,    8e13,  'left',  'top'),
    ('LIGO O4',        1.5,    1e8,     2,    '#E377C2', 4.5e-1, 4.5e7, 'right', 'top'),
    ('Vera Rubin',     100,    4e8,     15,   '#9467BD', 300,    1.5e8, 'left',  'bottom'),
    ('IceCube',        8,      5e7,    0.5,   '#2CA02C', 25,     2.2e7, 'left',  'top'),
#     ('ZTF',            50,     2e7,     1,    '#17BECF', 150,    7e7,   'left',  'bottom'),
    ('Netflix 4K UHD', 200,    3.1e6,  0.1,   '#555555', 550,    1.3e6, 'left',  'top'),
]

# ═══════════════════════════════════════════════════════════════════
# 2.  Figure & axes
# ═══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 11))
fig.patch.set_facecolor(BACKGROUND)
ax.set_facecolor(BACKGROUND)
fig.subplots_adjust(left=0.10, right=0.97, top=0.92, bottom=0.09)

# ── Background bands ──────────────────────────────────────────────
# ax.axvspan(1e-8, 1e-2, color='#FFAAAA', alpha=0.30, zorder=0)   # FPGA/ASIC: pink
# ax.axvspan(1e-2, 1e6,  color='#AAAAEE', alpha=0.20, zorder=0)   # CPU/GPU: blue-grey
# ax.axvline(1e-2, color='#BBBBBB', lw=0.9, ls='--', alpha=0.6,  zorder=1)

# ═══════════════════════════════════════════════════════════════════
# 3.  Bubbles, stars & labels
# ═══════════════════════════════════════════════════════════════════
for name, lat, rate, pb, color, ax_, ay_, ha, va in DATA:
    log_pb = np.log10(max(pb, 1e-3))
    size   = ((log_pb + 4) * K) ** 2

    # ── Bubble ──
    ax.scatter(lat, rate,
               s=size, c=color, alpha=0.78,
               edgecolors='white', linewidths=2.0, zorder=5)
    # ── White star ──
    ax.scatter(lat, rate,
               s=80, c='white', marker='*', zorder=6)
    # ── Label (plain text, no arrow — matches original A3D3 style) ──
    ax.text(ax_, ay_, name,
            ha=ha, va=va,
            fontsize=11, fontweight='bold', color='black',
            zorder=10)

# ═══════════════════════════════════════════════════════════════════
# 4.  Reference bubbles  (upper right, in empty space)
# ═══════════════════════════════════════════════════════════════════
REF_Y  = 5e17
REFS = [
    ('1 TB/yr',  1e-3,  5e0),
    ('1 PB/yr',  1.5,   5e1),
    ('1 EB/yr',  1e6,   1.5e4),
]
for label, pb_ref, rx in REFS:
    log_ref = np.log10(pb_ref)
    size_r  = ((log_ref + 4) * K) ** 2
    ax.scatter(rx, REF_Y,
               s=size_r, c='#BBBBBB', alpha=0.55,
               edgecolors='#888888', linewidths=1.5, zorder=5)
    ax.text(rx, REF_Y * 10, label,
            ha='center', va='bottom',
            fontsize=10, color='black')

ax.text(5e0, REF_Y * 28,
        'Annual data volume reference',
        ha='center', va='bottom',
        fontsize=9, color='#999999', style='italic')

# ═══════════════════════════════════════════════════════════════════
# 5.  Axes configuration
# ═══════════════════════════════════════════════════════════════════
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1e-8, 1e6)
ax.set_ylim(5e5,  5e19)

ax.set_xlabel('Latency Requirement [s]',   fontsize=20, labelpad=8)
ax.set_ylabel('Streaming Data Rate [B/s]', fontsize=20, labelpad=8)

ax.tick_params(which='both', direction='in',
               top=True, right=True, labelsize=16)
ax.grid(True, which='major', ls='--', lw=0.5, color='gray', alpha=0.35)
ax.grid(True, which='minor', ls=':',  lw=0.3, color='gray', alpha=0.20)

# ═══════════════════════════════════════════════════════════════════
# 6.  Region labels & difficulty annotations
# ═══════════════════════════════════════════════════════════════════
# ax.text(2e-8, 2e18, 'FPGA/ASIC',
#         fontsize=13, color='#CC0000', fontweight='bold', alpha=0.85)
# ax.text(2e-2, 2e18, 'CPU/GPU',
#         fontsize=13, color='#000088', fontweight='bold', alpha=0.85)

ax.text(1.5e-7, 2e16,  'HARDER',
        fontsize=30, color='#CC0000', fontweight='bold', alpha=0.22)
ax.text(2e3,    2e6,  'EASIER',
        fontsize=30, color='#0000BB', fontweight='bold', alpha=0.22)

# # ── Bubble area note ──────────────────────────────────────────────
# ax.text(0.01, 0.975,
#         'Bubble area  ∝  log₁₀(annual data volume in PB)',
#         transform=ax.transAxes,
#         ha='left', va='top', fontsize=10, color='#555555',
#         bbox=dict(boxstyle='round,pad=0.32',
#                   facecolor='white', edgecolor='#CCCCCC',
#                   alpha=0.92, linewidth=0.7),
#         zorder=10)

# ═══════════════════════════════════════════════════════════════════
# 7.  Title & attribution
# ═══════════════════════════════════════════════════════════════════
fig.suptitle('Streaming Data Rate vs. Latency Requirement — 2026',
             fontsize=25, fontweight='bold', y=0.97, color='#1A1A2E')

ax.text(0.2, 0.005,
        'Updated from A3D3 Institute (a3d3.ai)',
        transform=ax.transAxes,
        ha='right', va='bottom', fontsize=8, color='#BBBBBB',
        style='italic')

# ═══════════════════════════════════════════════════════════════════
# 8.  Save & show
# ═══════════════════════════════════════════════════════════════════
plt.savefig('streaming_latency_2026.pdf', bbox_inches='tight')
plt.savefig('streaming_latency_2026.png', dpi=200, bbox_inches='tight',
            facecolor=BACKGROUND)
plt.show()
