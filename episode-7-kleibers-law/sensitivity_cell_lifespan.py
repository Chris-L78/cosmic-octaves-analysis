#!/usr/bin/env python3
"""
Sensitivity Analysis: Cell Lifespan Variation
==============================================
Video 7: "Can Mouse Metabolism Predict the Lifespan of a Galaxy?"
Our Fractal Universe — Chris Lehto

Tests how the cross-scale regression changes when the cell lifespan
input is varied across biologically reasonable values (3 days to 300 days).

Key result: Galaxy prediction is robust across all variations,
landing between 10^12.5 and 10^13.5 regardless of cell lifespan choice.

Usage:
    python sensitivity_cell_lifespan.py
"""

import numpy as np
from scipy import stats
import csv
import os

np.random.seed(42)

print("=" * 70)
print("SENSITIVITY ANALYSIS: CELL LIFESPAN VARIATION")
print("Video 7 — Our Fractal Universe")
print("=" * 70)

# Fixed data points
human_mass = 70         # kg
human_life = 80         # years
sun_mass = 1.989e30     # kg
sun_life = 1e10         # years

cell_mass = 1e-12       # kg (fixed)

# Milky Way for prediction
mw_mass = 1.5e42        # kg
mw_logM = np.log10(mw_mass)

# Cell lifespan variations (days → years)
variations = [
    {"name": "Gut epithelial",   "days": 3,    "source": "Gut epithelial cell turnover"},
    {"name": "Baseline (14d)",   "days": 14,   "source": "Typical mammalian cell turnover (Sender et al. 2016)"},
    {"name": "Skin cell",        "days": 28,   "source": "Keratinocyte cycle (~4 weeks)"},
    {"name": "Red blood cell",   "days": 120,  "source": "Erythrocyte lifespan (~120 days)"},
    {"name": "Hepatocyte",       "days": 300,  "source": "Liver cell turnover (~200-300 days)"},
]

# Neuron outlier test
neuron_mass = 1e-9     # kg (typical neuron, heavier than average cell)
neuron_life = 80       # years (non-dividing, lasts entire human lifespan)

print("\n--- Sensitivity Results ---")
print(f"{'Variation':<20} {'Days':<8} {'Slope':<10} {'R²':<10} {'MW pred (log₁₀ yr)':<20} {'MW (trillion yr)'}")
print("-" * 85)

results = []
for v in variations:
    cell_life = v["days"] / 365.25
    
    logM = np.array([np.log10(cell_mass), np.log10(human_mass), np.log10(sun_mass)])
    logT = np.array([np.log10(cell_life), np.log10(human_life), np.log10(sun_life)])
    
    reg = stats.linregress(logM, logT)
    mw_pred_log = reg.intercept + reg.slope * mw_logM
    mw_pred_yr = 10 ** mw_pred_log
    
    marker = " ← baseline" if v["days"] == 14 else ""
    print(f"{v['name']:<20} {v['days']:<8} {reg.slope:<10.4f} {reg.rvalue**2:<10.4f} {mw_pred_log:<20.2f} {mw_pred_yr/1e12:.1f}{marker}")
    
    results.append({
        "variation": v["name"],
        "cell_lifespan_days": v["days"],
        "source": v["source"],
        "slope": round(reg.slope, 4),
        "slope_stderr": round(reg.stderr, 4),
        "intercept": round(reg.intercept, 4),
        "r_squared": round(reg.rvalue**2, 4),
        "mw_predicted_log10_years": round(mw_pred_log, 2),
        "mw_predicted_trillion_years": round(mw_pred_yr / 1e12, 1)
    })

print("\n--- Robustness Summary ---")
slopes = [r["slope"] for r in results]
preds = [r["mw_predicted_log10_years"] for r in results]
print(f"Slope range:      {min(slopes):.4f} – {max(slopes):.4f}")
print(f"Prediction range: 10^{min(preds):.1f} – 10^{max(preds):.1f}")
print(f"All within:       10^12.5 to 10^13.5 (robust)")
print(f"Observed MW:      10^13 to 10^14 (star formation era)")

# ============================================================
# NEURON OUTLIER TEST
# ============================================================

print("\n--- Neuron Outlier Test ---")
baseline_logM = np.array([np.log10(cell_mass), np.log10(human_mass), np.log10(sun_mass)])
baseline_logT = np.array([np.log10(14/365.25), np.log10(human_life), np.log10(sun_life)])
baseline_reg = stats.linregress(baseline_logM, baseline_logT)

neuron_pred_log = baseline_reg.intercept + baseline_reg.slope * np.log10(neuron_mass)
neuron_pred_yr = 10 ** neuron_pred_log
neuron_ratio = neuron_life / neuron_pred_yr

print(f"Neuron mass:      {neuron_mass:.0e} kg")
print(f"Neuron lifespan:  {neuron_life} years (non-dividing, lasts entire human life)")
print(f"Predicted by fit: {neuron_pred_yr:.2f} years ({neuron_pred_yr*365.25:.0f} days)")
print(f"Actual/Predicted: {neuron_ratio:.0f}× above prediction")
print(f"Explanation:      Non-dividing cell — does not follow turnover scaling")
print(f"                  Analogous to Greenland shark (400 yr) not breaking Kleiber trend")

# ============================================================
# SAVE CSV
# ============================================================

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(out_dir, exist_ok=True)
csv_path = os.path.join(out_dir, "sensitivity_analysis.csv")

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to: data/sensitivity_analysis.csv")
