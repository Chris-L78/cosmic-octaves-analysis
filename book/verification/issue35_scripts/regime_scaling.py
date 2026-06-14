#!/usr/bin/env python3
"""
Appendix K -- Regime Scaling Analysis (cycle period vs system mass)

Reproduces the per-regime power-law fits and the statistical test reported in
Appendix K, Section 6.3 ("Are the biological and cosmic regimes different?").

The global fit across all 16 levels (cycle_period ~ M^0.34, R^2 ~ 0.72) is
produced by ../issue34_scripts/sleep_duty_cycles.py. This script isolates the
biological and cosmic sub-regimes and tests whether their period-mass slopes
differ.

Regimes (mass, period values identical to sleep_duty_cycles.py / Appendix A):
  - Biological: Ribosome, Bacterium, C. elegans, Human        (4 points)
  - Cosmic:     Earth through Observable Universe              (8 points)

The quantum levels (Proton, Atom) are excluded: same mass, different physics
(strong vs electromagnetic binding), so they do not belong to a mass-scaling
regime. The social levels (City, Nation) are too few to fit independently.

Expected output (matches Appendix K Section 6.3):
  Biological slope: 0.128 +/- 0.051
  Cosmic slope:     0.353 +/- 0.125
  z = -1.67, p = 0.095 (two-tailed) -- marginal, not significant at 95%

Usage:
    python regime_scaling.py
"""

import numpy as np
from scipy import stats

# (name, mass_kg, cycle_period_s)
BIOLOGICAL = [
    ("Ribosome",            2.50e-21, 60.0),
    ("Bacterium (E. coli)", 1.00e-15, 7200.0),
    ("C. elegans",          1.00e-9,  36000.0),
    ("Human",               70.0,     86400.0),
]

COSMIC = [
    ("Earth",               5.97e24,  86400.0),
    ("Sun",                 1.99e30,  3.47e8),
    ("Solar System",        2.00e30,  2.0e15),
    ("Open Cluster",        5.00e32,  3.15e15),
    ("Local Bubble",        1.00e34,  3.5e13),
    ("Milky Way",           1.50e42,  3.15e15),
    ("Virgo Supercluster",  1.00e45,  3.15e16),
    ("Observable Universe", 1.50e53,  4.35e17),
]


def fit_regime(data):
    """OLS fit of log10(period) vs log10(mass).

    Returns (slope, standard_error_of_slope, intercept, r_squared, n).
    """
    x = np.log10([d[1] for d in data])
    y = np.log10([d[2] for d in data])
    n = len(x)
    slope, intercept = np.polyfit(x, y, 1)
    y_hat = intercept + slope * x
    resid = y - y_hat
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r_sq = 1.0 - ss_res / ss_tot if ss_tot > 0 else float('nan')
    # Standard error of the slope (OLS): sqrt( (RSS/(n-2)) / Sxx )
    s2 = ss_res / (n - 2)
    se_slope = np.sqrt(s2 / np.sum((x - x.mean()) ** 2))
    return slope, se_slope, intercept, r_sq, n


def main():
    print("=" * 72)
    print("APPENDIX K -- REGIME SCALING: cycle period vs system mass")
    print("=" * 72)

    b_slope, b_se, _, b_r2, b_n = fit_regime(BIOLOGICAL)
    c_slope, c_se, _, c_r2, c_n = fit_regime(COSMIC)

    print(f"\nBiological regime (n={b_n}): "
          f"slope = {b_slope:.3f} +/- {b_se:.3f}   (R^2 = {b_r2:.3f})")
    print(f"Cosmic regime     (n={c_n}): "
          f"slope = {c_slope:.3f} +/- {c_se:.3f}   (R^2 = {c_r2:.3f})")

    # Two-sample z-test for difference of slopes (independent regressions).
    z = (b_slope - c_slope) / np.sqrt(b_se ** 2 + c_se ** 2)
    p = 2.0 * (1.0 - stats.norm.cdf(abs(z)))

    print(f"\nDifference of slopes: z = {z:.2f}, p = {p:.3f} (two-tailed)")
    if p < 0.05:
        verdict = "significant at 95% confidence"
    elif p < 0.10:
        verdict = "MARGINAL -- not significant at 95% confidence"
    else:
        verdict = "not significant"
    print(f"Verdict: {verdict}.")
    print("\nThe biological regime has only 4 data points, limiting statistical")
    print("power; the difference is suggestive but cannot be confirmed with")
    print("current data (see Appendix K Section 6.3).")


if __name__ == '__main__':
    main()
