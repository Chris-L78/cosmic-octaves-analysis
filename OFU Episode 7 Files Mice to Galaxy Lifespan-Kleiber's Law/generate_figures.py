#!/usr/bin/env python3
"""
Generate All Figures for Video 7
=================================
Video 7: "Can Mouse Metabolism Predict the Lifespan of a Galaxy?"
Our Fractal Universe — Chris Lehto

Generates publication-quality figures:
  1. Main log-log regression plot with galaxy prediction
  2. Sensitivity analysis chart
  3. Three-slope comparison (AnAge / Kleiber / Cross-scale)
  4. Within-class inversion comparison
  5. Energy density comparison bar chart

Usage:
    python generate_figures.py

Saves to: ../figures/
"""

import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Output directory
fig_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(fig_dir, exist_ok=True)

# Common style
plt.rcParams.update({
    'figure.facecolor': '#0d1b2a',
    'axes.facecolor': '#0d1b2a',
    'axes.edgecolor': '#4cc9f0',
    'axes.labelcolor': '#e0e0e0',
    'text.color': '#e0e0e0',
    'xtick.color': '#e0e0e0',
    'ytick.color': '#e0e0e0',
    'grid.color': '#1b3a5c',
    'grid.alpha': 0.5,
    'font.size': 12,
})

CYAN = '#4cc9f0'
GOLD = '#e8a838'
GREEN = '#51cf66'
RED = '#ff6b6b'
WHITE = '#e0e0e0'

# ============================================================
# DATA
# ============================================================

training_names = ["Cell", "Human", "Sun"]
training_logM = np.array([np.log10(1e-12), np.log10(70), np.log10(1.989e30)])
training_logT = np.array([np.log10(14/365.25), np.log10(80), np.log10(1e10)])

reg = stats.linregress(training_logM, training_logT)
slope, intercept = reg.slope, reg.intercept

mw_logM = np.log10(1.5e42)
mw_logT = intercept + slope * mw_logM

# ============================================================
# FIGURE 1: Main Log-Log Regression
# ============================================================

fig, ax = plt.subplots(figsize=(12, 8))

x_line = np.linspace(-15, 45, 100)
y_line = intercept + slope * x_line
ax.plot(x_line, y_line, color=GOLD, linewidth=2, alpha=0.7, label=f'Fit: slope = {slope:.3f}')

# Training points
ax.scatter(training_logM, training_logT, color=CYAN, s=150, zorder=5, edgecolors='white', linewidths=1.5)
for name, x, y in zip(training_names, training_logM, training_logT):
    ax.annotate(name, (x, y), textcoords="offset points", xytext=(12, 12),
                fontsize=13, fontweight='bold', color=CYAN)

# Galaxy prediction
ax.scatter([mw_logM], [mw_logT], color=GREEN, s=200, zorder=5, marker='*',
           edgecolors='white', linewidths=1.5)
ax.annotate("Milky Way\n(predicted)", (mw_logM, mw_logT),
            textcoords="offset points", xytext=(12, -20),
            fontsize=13, fontweight='bold', color=GREEN)

# Observed range for MW
ax.axhspan(np.log10(1e13), np.log10(1e14), alpha=0.15, color=GREEN,
           label='MW observed range (10¹³–10¹⁴ yr)')

ax.set_xlabel("log₁₀(Mass / kg)", fontsize=14)
ax.set_ylabel("log₁₀(Lifespan / years)", fontsize=14)
ax.set_title("Cross-Scale Lifespan Regression", fontsize=16, fontweight='bold', color=GOLD)
ax.legend(loc='upper left', fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xlim(-15, 45)
ax.set_ylim(-2, 18)

# Equation box
eq_text = f"log₁₀(T) = {intercept:.3f} + {slope:.3f} × log₁₀(M)\nR² = {reg.rvalue**2:.4f}"
ax.text(0.97, 0.03, eq_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='#1b3a5c', alpha=0.8), color=GOLD)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "1_cross_scale_regression.png"), dpi=200, bbox_inches='tight')
plt.close()
print("✓ Figure 1: Cross-scale regression")

# ============================================================
# FIGURE 2: Sensitivity Analysis
# ============================================================

cell_days = [3, 14, 28, 120, 300]
cell_labels = ["3d (gut)", "14d (baseline)", "28d (skin)", "120d (RBC)", "300d (liver)"]
slopes_sens = []
preds_sens = []

for d in cell_days:
    logM = np.array([np.log10(1e-12), np.log10(70), np.log10(1.989e30)])
    logT = np.array([np.log10(d/365.25), np.log10(80), np.log10(1e10)])
    r = stats.linregress(logM, logT)
    slopes_sens.append(r.slope)
    preds_sens.append(r.intercept + r.slope * mw_logM)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Slopes
colors_s = [RED if i != 1 else CYAN for i in range(len(cell_days))]
ax1.barh(range(len(cell_days)), slopes_sens, color=colors_s, alpha=0.8)
ax1.axvline(x=0.25, color=GOLD, linestyle='--', linewidth=2, label='Kleiber (0.25)')
ax1.set_yticks(range(len(cell_days)))
ax1.set_yticklabels(cell_labels)
ax1.set_xlabel("Slope", fontsize=12)
ax1.set_title("Slope Sensitivity", fontsize=14, fontweight='bold', color=GOLD)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3, axis='x')
for i, v in enumerate(slopes_sens):
    ax1.text(v + 0.003, i, f"{v:.3f}", va='center', fontsize=10, color=WHITE)

# Predictions
colors_p = [RED if i != 1 else GREEN for i in range(len(cell_days))]
ax2.barh(range(len(cell_days)), preds_sens, color=colors_p, alpha=0.8)
ax2.axvspan(13, 14, alpha=0.2, color=GREEN, label='MW observed (10¹³–10¹⁴)')
ax2.set_yticks(range(len(cell_days)))
ax2.set_yticklabels(cell_labels)
ax2.set_xlabel("MW Predicted Lifespan (log₁₀ years)", fontsize=12)
ax2.set_title("Galaxy Prediction Sensitivity", fontsize=14, fontweight='bold', color=GOLD)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, axis='x')
for i, v in enumerate(preds_sens):
    ax2.text(v + 0.05, i, f"10^{v:.1f}", va='center', fontsize=10, color=WHITE)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "2_sensitivity_analysis.png"), dpi=200, bbox_inches='tight')
plt.close()
print("✓ Figure 2: Sensitivity analysis")

# ============================================================
# FIGURE 3: Three-Slope Comparison
# ============================================================

fig, ax = plt.subplots(figsize=(10, 6))

x_plot = np.linspace(-15, 35, 100)

# AnAge mammals
anage_slope = 0.22
anage_int = 1.17  # approximate from existing data
ax.plot(x_plot, anage_int + anage_slope * x_plot, color=RED, linewidth=2,
        linestyle='--', alpha=0.7, label=f'AnAge mammals: ~{anage_slope}')

# Kleiber theoretical
kleiber_int = intercept + (slope - 0.25) * np.mean(training_logM)  # adjusted to pass near same region
ax.plot(x_plot, kleiber_int + 0.25 * x_plot, color=GOLD, linewidth=2,
        linestyle='-.', alpha=0.7, label='Kleiber theory: 0.25')

# Cross-scale fit
ax.plot(x_plot, intercept + slope * x_plot, color=CYAN, linewidth=2.5,
        label=f'Cross-scale fit: {slope:.3f}')

ax.scatter(training_logM, training_logT, color=CYAN, s=120, zorder=5, edgecolors='white')

ax.set_xlabel("log₁₀(Mass / kg)", fontsize=14)
ax.set_ylabel("log₁₀(Lifespan / years)", fontsize=14)
ax.set_title("Three Power Laws in the Same Neighborhood", fontsize=16,
             fontweight='bold', color=GOLD)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xlim(-15, 35)
ax.set_ylim(-3, 12)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "3_three_slope_comparison.png"), dpi=200, bbox_inches='tight')
plt.close()
print("✓ Figure 3: Three-slope comparison")

# ============================================================
# FIGURE 4: Energy Density Comparison
# ============================================================

fig, ax = plt.subplots(figsize=(10, 5))

objects = ["Sun", "Human"]
densities = [0.000192, 1.14]
colors_e = [GOLD, CYAN]

bars = ax.barh(objects, densities, color=colors_e, alpha=0.9, height=0.5)

ax.set_xlabel("Energy Density (W/kg)", fontsize=14)
ax.set_title("Energy Density: You vs The Sun", fontsize=16, fontweight='bold', color=GOLD)
ax.set_xscale('log')
ax.grid(True, alpha=0.3, axis='x')

ax.text(densities[0] * 3, 0, f"{densities[0]:.4f} W/kg", va='center', fontsize=13, color=GOLD,
        fontweight='bold')
ax.text(densities[1] * 1.5, 1, f"{densities[1]:.2f} W/kg", va='center', fontsize=13, color=CYAN,
        fontweight='bold')

ax.text(0.97, 0.95, f"Human is ~{densities[1]/densities[0]:,.0f}× more\nenergy-dense than the Sun",
        transform=ax.transAxes, fontsize=14, va='top', ha='right',
        bbox=dict(boxstyle='round', facecolor='#1b3a5c', alpha=0.8), color=GREEN,
        fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "4_energy_density.png"), dpi=200, bbox_inches='tight')
plt.close()
print("✓ Figure 4: Energy density comparison")

# ============================================================
# FIGURE 5: Within-Class Inversion Summary
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Within dogs
ax = axes[0, 0]
dogs_m = [2, 10, 30, 60]
dogs_t = [15, 12, 11, 8]
ax.scatter(dogs_m, dogs_t, color=RED, s=100, zorder=5)
ax.plot(dogs_m, dogs_t, color=RED, alpha=0.7)
ax.set_xlabel("Mass (kg)")
ax.set_ylabel("Lifespan (years)")
ax.set_title("Within Dogs: Bigger → Shorter", color=RED, fontweight='bold')
ax.grid(True, alpha=0.3)
labels = ["Chihuahua", "Beagle", "Lab", "Great Dane"]
for i, lab in enumerate(labels):
    ax.annotate(lab, (dogs_m[i], dogs_t[i]), textcoords="offset points",
                xytext=(5, 8), fontsize=9, color=WHITE)

# Panel 2: Across species
ax = axes[0, 1]
sp_m = [0.02, 4, 70, 5000, 100000]
sp_t = [4, 15, 80, 65, 211]
ax.scatter(sp_m, sp_t, color=GREEN, s=100, zorder=5)
ax.plot(sp_m, sp_t, color=GREEN, alpha=0.7)
ax.set_xscale('log')
ax.set_xlabel("Mass (kg)")
ax.set_ylabel("Lifespan (years)")
ax.set_title("Across Species: Bigger → Longer", color=GREEN, fontweight='bold')
ax.grid(True, alpha=0.3)
labels2 = ["Mouse", "Cat", "Human", "Elephant", "Bowhead"]
for i, lab in enumerate(labels2):
    ax.annotate(lab, (sp_m[i], sp_t[i]), textcoords="offset points",
                xytext=(5, 8), fontsize=9, color=WHITE)

# Panel 3: Within stars
ax = axes[1, 0]
st_m = [0.1, 0.7, 1.0, 2.0, 10, 60]
st_t = [1e13, 4.5e10, 1e10, 1.5e9, 2e7, 3e6]
ax.scatter(st_m, st_t, color=RED, s=100, zorder=5)
ax.plot(st_m, st_t, color=RED, alpha=0.7)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Mass (M☉)")
ax.set_ylabel("Lifespan (years)")
ax.set_title("Within Stars: Bigger → Shorter", color=RED, fontweight='bold')
ax.grid(True, alpha=0.3)
labels3 = ["Red dwarf", "K-dwarf", "Sun", "A-star", "B-star", "O-star"]
for i, lab in enumerate(labels3):
    ax.annotate(lab, (st_m[i], st_t[i]), textcoords="offset points",
                xytext=(5, 8), fontsize=9, color=WHITE)

# Panel 4: Cross-scale
ax = axes[1, 1]
cs_m = [1e-12, 70, 1.989e30, 1.5e42]
cs_t = [14/365.25, 80, 1e10, 1.39e13]
cs_labels = ["Cell", "Human", "Sun", "Milky Way"]
ax.scatter(cs_m[:3], cs_t[:3], color=GREEN, s=100, zorder=5)
ax.scatter([cs_m[3]], [cs_t[3]], color=GREEN, s=200, zorder=5, marker='*')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Mass (kg)")
ax.set_ylabel("Lifespan (years)")
ax.set_title("Across Scales: Bigger → Longer", color=GREEN, fontweight='bold')
ax.grid(True, alpha=0.3)
for i, lab in enumerate(cs_labels):
    ax.annotate(lab, (cs_m[i], cs_t[i]), textcoords="offset points",
                xytext=(8, 8), fontsize=9, color=WHITE, fontweight='bold')

fig.suptitle("Within-Class vs Cross-Class Scaling Inversions",
             fontsize=18, fontweight='bold', color=GOLD, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "5_inversion_comparison.png"), dpi=200, bbox_inches='tight')
plt.close()
print("✓ Figure 5: Inversion comparison")

print(f"\nAll figures saved to: {fig_dir}/")
print("Done!")
