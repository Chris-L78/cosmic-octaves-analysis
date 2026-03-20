#!/usr/bin/env python3
"""
Cross-Scale Lifespan Regression Analysis
=========================================
Video 7: "Can Mouse Metabolism Predict the Lifespan of a Galaxy?"
Our Fractal Universe — Chris Lehto

Fits a log-log regression through Cell, Human, and Sun data points,
then predicts the Milky Way galaxy lifespan as an out-of-sample test.

All numbers are calculator-verified. Fixed seed for reproducibility.

Usage:
    python cross_scale_regression.py

References:
    Kleiber M. (1932) Hilgardia 6:315-353
    West GB, Brown JH, Enquist BJ (1997) Science 276:122-126
    Sackmann IJ et al. (1993) ApJ 418:457
    Adams FC, Laughlin G (1997) Rev Mod Phys 69:337
    de Magalhães JP et al. (2009) AnAge Database
    McMillan PJ (2011) MNRAS 414:2446
"""

import numpy as np
from scipy import stats
import json
import os

np.random.seed(42)

print("=" * 70)
print("CROSS-SCALE LIFESPAN REGRESSION")
print("Video 7 — Our Fractal Universe")
print("=" * 70)

# ============================================================
# DATA POINTS (3 training + 1 prediction target)
# ============================================================

training = {
    "Cell": {
        "mass_kg": 1e-12,
        "lifespan_years": 14 / 365.25,  # 14 days → years
        "source": "Typical mammalian cell turnover ~14 days (Sender et al. 2016)"
    },
    "Human": {
        "mass_kg": 70,
        "lifespan_years": 80,
        "source": "Global average human lifespan (WHO 2023)"
    },
    "Sun": {
        "mass_kg": 1.989e30,
        "lifespan_years": 1e10,
        "source": "Main-sequence lifetime (Sackmann et al. 1993, ApJ 418:457)"
    }
}

prediction_targets = {
    "Milky_Way": {
        "mass_kg": 1.5e42,
        "observed_range_years": [1e13, 1e14],
        "source": "Total mass incl. dark matter (McMillan 2011); "
                  "Star formation era (Adams & Laughlin 1997)"
    },
    "Universe": {
        "mass_kg": 1e53,
        "observed_active_lifespan_years": 1e14,
        "source": "Observable universe total mass; "
                  "Star formation era ~100 trillion yr (Adams & Laughlin 1997)"
    }
}

# Extract arrays
names = list(training.keys())
log_mass = np.array([np.log10(training[n]["mass_kg"]) for n in names])
log_life = np.array([np.log10(training[n]["lifespan_years"]) for n in names])

print("\n--- Training Data ---")
print(f"{'Name':<10} {'Mass (kg)':<15} {'Lifespan (yr)':<18} {'log₁₀(M)':<10} {'log₁₀(T)':<10}")
print("-" * 70)
for i, n in enumerate(names):
    m = training[n]["mass_kg"]
    t = training[n]["lifespan_years"]
    print(f"{n:<10} {m:<15.3e} {t:<18.6f} {log_mass[i]:<10.3f} {log_life[i]:<10.4f}")

# ============================================================
# LINEAR REGRESSION: log₁₀(T) = a + b × log₁₀(M)
# ============================================================

result = stats.linregress(log_mass, log_life)
slope = result.slope
intercept = result.intercept
r_sq = result.rvalue ** 2
se = result.stderr

print("\n--- Regression Results ---")
print(f"Slope (b):        {slope:.4f} ± {se:.4f}")
print(f"Intercept (a):    {intercept:.4f}")
print(f"R²:               {r_sq:.4f}")
print(f"Degrees of freedom: {len(names) - 2}")
print(f"\nEquation: log₁₀(T) = {intercept:.4f} + {slope:.4f} × log₁₀(M)")
print(f"Power law: T ∝ M^{slope:.4f}")

# ============================================================
# COMPARISON WITH BIOLOGICAL SCALING
# ============================================================

kleiber = 0.25
anage_low, anage_high = 0.20, 0.27

print("\n--- Comparison with Biological Scaling ---")
print(f"Kleiber theoretical (West et al. 1997):  {kleiber}")
print(f"AnAge mammals empirical range:           {anage_low} – {anage_high}")
print(f"Cross-scale fit:                         {slope:.4f} ± {se:.4f}")
print(f"Difference from Kleiber:                 {abs(slope - kleiber):.4f}")
print(f"Sigma from Kleiber:                      {abs(slope - kleiber)/se:.1f}σ")

# ============================================================
# MILKY WAY PREDICTION (out-of-sample)
# ============================================================

mw = prediction_targets["Milky_Way"]
mw_logM = np.log10(mw["mass_kg"])
mw_logT_pred = intercept + slope * mw_logM
mw_T_pred = 10 ** mw_logT_pred

print("\n--- Milky Way Galaxy Prediction ---")
print(f"Mass:              {mw['mass_kg']:.2e} kg  (log₁₀ = {mw_logM:.2f})")
print(f"Predicted:         10^{mw_logT_pred:.2f} = {mw_T_pred:.2e} years")
print(f"                   ≈ {mw_T_pred/1e12:.1f} trillion years")
print(f"Observed range:    {mw['observed_range_years'][0]:.0e} – {mw['observed_range_years'][1]:.0e} years")
print(f"Factor from lower: {mw_T_pred / mw['observed_range_years'][0]:.1f}×")

# ============================================================
# UNIVERSE PREDICTION (known overshoot)
# ============================================================

uni = prediction_targets["Universe"]
uni_logM = np.log10(uni["mass_kg"])
uni_logT_pred = intercept + slope * uni_logM
uni_T_pred = 10 ** uni_logT_pred

print("\n--- Universe Prediction (Known Overshoot) ---")
print(f"Mass:              {uni['mass_kg']:.0e} kg  (log₁₀ = {uni_logM:.1f})")
print(f"Predicted:         10^{uni_logT_pred:.1f} = {uni_T_pred:.1e} years")
print(f"Active lifespan:   {uni['observed_active_lifespan_years']:.0e} years")
print(f"Overshoot:         ~{uni_T_pred / uni['observed_active_lifespan_years']:.0f}× (2 orders of magnitude)")
print(f"NOTE: Current age 13.8 Gyr ≠ lifespan. Age is ~0.01% of the active lifespan.")

# ============================================================
# SAVE RESULTS
# ============================================================

results = {
    "regression": {
        "slope": round(slope, 4),
        "slope_stderr": round(se, 4),
        "intercept": round(intercept, 4),
        "r_squared": round(r_sq, 4),
        "n_points": 3,
        "degrees_of_freedom": 1,
        "equation": f"log10(T) = {intercept:.4f} + {slope:.4f} * log10(M)"
    },
    "kleiber_comparison": {
        "kleiber_theoretical": kleiber,
        "anage_mammals_range": [anage_low, anage_high],
        "cross_scale_slope": round(slope, 4),
        "sigma_from_kleiber": round(abs(slope - kleiber) / se, 1)
    },
    "galaxy_prediction": {
        "milky_way_mass_kg": mw["mass_kg"],
        "predicted_log10_years": round(mw_logT_pred, 2),
        "predicted_years": float(f"{mw_T_pred:.2e}"),
        "observed_range_years": mw["observed_range_years"],
        "factor_from_lower_bound": round(mw_T_pred / mw["observed_range_years"][0], 1)
    },
    "universe_prediction": {
        "mass_kg": uni["mass_kg"],
        "predicted_log10_years": round(uni_logT_pred, 1),
        "predicted_years": float(f"{uni_T_pred:.1e}"),
        "active_lifespan_years": uni["observed_active_lifespan_years"],
        "overshoot_factor": round(uni_T_pred / uni["observed_active_lifespan_years"])
    },
    "training_data": {
        n: {
            "mass_kg": training[n]["mass_kg"],
            "lifespan_years": training[n]["lifespan_years"],
            "source": training[n]["source"]
        }
        for n in names
    }
}

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "cross_scale_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to: data/cross_scale_results.json")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  Slope:       {slope:.4f} ± {se:.4f}  (Kleiber predicts 0.25)")
print(f"  R²:          {r_sq:.4f}")
print(f"  Galaxy pred: {mw_T_pred/1e12:.1f} trillion yr  (observed: 10–100 T)")
print(f"  Factor off:  {mw_T_pred/mw['observed_range_years'][0]:.1f}×")
print("=" * 70)
