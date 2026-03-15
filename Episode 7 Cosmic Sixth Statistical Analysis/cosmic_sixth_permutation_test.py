"""
Cosmic Sixth (10^6) Permutation Test
=====================================
Statistical companion to OFU Episode 7
"The Cosmic Sixth: Why the Universe Builds Something New Every Million Times"

Tests whether the 15-rung canonical scale ladder produces an unusual number
of pre-specified structure pairs separated by approximately 10^6 in
characteristic length.

Methodology mirrors the 10^24 octave test from the published paper:
- Same 15 verified structures (CODATA 2022 / IAU 2015)
- Same permutation framework (shuffle log-values among labels)
- Same seed (42) and trial count (200,000)
- Pre-specified pairs tested against fixed target delta

Key difference: 6 pre-specified pairs at delta=6.0 (vs 7 pairs at delta=24.0)

Author: Chris Lehto / Our Fractal Universe
Date: March 2026
Repository: github.com/Chris-L78/cosmic-octaves-analysis
"""

import numpy as np
from scipy import stats
import time
import json

# ============================================================
# DATA: Verified log10(L) values from Paper Table 1
# Sources: CODATA 2022 / IAU 2015
# ============================================================
LABELS = [
    "Proton", "Atomic Orbital (H)", "Ribosome (70S)", "Bacterium (E. coli)",
    "C. elegans", "Human", "City", "Earth", "Sun", "Solar System",
    "Open Cluster", "Local Bubble", "Milky Way", "Virgo Supercluster",
    "Observable Universe"
]

LOGS = np.array([
    -15.08,   # Proton — RMS charge radius (CODATA 2022)
    -10.28,   # Atomic Orbital — Bohr radius (CODATA 2022)
     -7.96,   # Ribosome 70S — half diameter (BioNumbers)
     -6.00,   # Bacterium E. coli — half cell length (BioNumbers)
     -3.30,   # C. elegans — half body length (NCBI)
     -0.046,  # Human — half body height (1.8 m representative)
      3.00,   # City — coordination radius (West 2017)
      6.80,   # Earth — mean radius (IAU 2015)
      8.84,   # Sun — photosphere radius (IAU 2015)
     12.65,   # Solar System — Neptune orbit / bound extent (IAU 2015)
     16.67,   # Open Cluster — half-mass radius (literature typical)
     18.665,  # Local Bubble — median boundary distance (Pelgrims+ 2020)
     20.70,   # Milky Way — half stellar disk scale (Bland-Hawthorn & Gerhard 2016)
     23.84,   # Virgo Supercluster — half density-extent proxy (standard value)
     26.64    # Observable Universe — particle horizon (Planck 2018)
])

N = len(LOGS)
assert N == 15, f"Expected 15 structures, got {N}"

# ============================================================
# PRE-SPECIFIED PAIRS
# ============================================================
# These 6 pairs represent structures separated by approximately
# one factor of 10^6 on the canonical ladder.
#
# Selection criteria:
# 1. Both members are on the verified 15-rung ladder
# 2. The pair represents a meaningful organizational transition
#    (not just any two structures that happen to be ~6 apart)
# 3. Listed in the Episode 7 script table
#
# Post-hoc note: These pairs were identified by inspection of the
# ladder before this test was designed. This is the same vulnerability
# acknowledged for the 10^24 test. The delta-scan (Method C) provides
# a partial correction.

SIXTH_PAIRS = [
    (3,  5),   # Bacterium -> Human
    (9,  11),  # Solar System -> Local Bubble
    (12, 14),  # Milky Way -> Observable Universe
    (7,  9),   # Earth -> Solar System
    (6,  8),   # City -> Sun
    (4,  6),   # C. elegans -> City
]
N_PAIRS = len(SIXTH_PAIRS)

# ============================================================
# CONFIGURATION
# ============================================================
TARGET_DELTA = 6.0
THRESHOLD = 0.1     # "Tight" — matches the ★ criterion in the script
THRESHOLD_2 = 0.2   # "Strong" — matches the octave test's strong-match def
N_TRIALS = 200_000
SEED = 42

# ============================================================
# FUNCTIONS
# ============================================================
def compute_deviations(arr, pairs, target):
    """Compute |ratio - target| for each pre-specified pair."""
    return np.array([abs(abs(arr[j] - arr[i]) - target) for i, j in pairs])


def run_permutation_test(logs, pairs, target, threshold, n_trials, seed):
    """Run permutation test and return results dict."""
    obs_devs = compute_deviations(logs, pairs, target)
    obs_strong = int(np.sum(obs_devs <= threshold))
    
    rng = np.random.default_rng(seed)
    count_ge = 0
    dist = np.zeros(len(pairs) + 1, dtype=int)
    
    for _ in range(n_trials):
        perm = rng.permutation(logs)
        pdevs = compute_deviations(perm, pairs, target)
        ns = int(np.sum(pdevs <= threshold))
        dist[ns] += 1
        if ns >= obs_strong:
            count_ge += 1
    
    p = count_ge / n_trials
    p_add1 = (count_ge + 1) / (n_trials + 1)
    
    return {
        "obs_deviations": obs_devs.tolist(),
        "obs_strong": obs_strong,
        "threshold": threshold,
        "count_ge": count_ge,
        "n_trials": n_trials,
        "p_value": p,
        "p_value_add1": p_add1,
        "sigma": float(stats.norm.isf(p)) if 0 < p < 1 else None,
        "distribution": {int(k): int(v) for k, v in enumerate(dist) if v > 0}
    }


def run_delta_scan(logs, pairs, threshold, delta_range, delta_step, n_trials, seed):
    """Run look-elsewhere delta scan."""
    deltas = np.arange(delta_range[0], delta_range[1] + delta_step/2, delta_step)
    
    # Find observed maximum
    obs_results = []
    for d in deltas:
        devs = compute_deviations(logs, pairs, d)
        ns = int(np.sum(devs <= threshold))
        obs_results.append((float(d), ns))
    obs_results.sort(key=lambda x: -x[1])
    obs_max = obs_results[0][1]
    
    rng = np.random.default_rng(seed)
    count_ge = 0
    
    for _ in range(n_trials):
        perm = rng.permutation(logs)
        perm_max = 0
        for d in deltas:
            devs = compute_deviations(perm, pairs, d)
            ns = int(np.sum(devs <= threshold))
            if ns > perm_max:
                perm_max = ns
        if perm_max >= obs_max:
            count_ge += 1
    
    p = count_ge / n_trials
    p_add1 = (count_ge + 1) / (n_trials + 1)
    
    return {
        "obs_scan_max": obs_max,
        "best_deltas": obs_results[:5],
        "delta_range": list(delta_range),
        "delta_step": delta_step,
        "count_ge": count_ge,
        "n_trials": n_trials,
        "p_value": p,
        "p_value_add1": p_add1,
        "sigma": float(stats.norm.isf(p)) if 0 < p < 1 else None,
    }


# ============================================================
# RUN ANALYSIS
# ============================================================
if __name__ == "__main__":
    print("=" * 70)
    print("COSMIC SIXTH (10^6) PERMUTATION TEST")
    print("=" * 70)
    print(f"\nLadder:     {N} verified structures")
    print(f"Pairs:      {N_PAIRS} pre-specified")
    print(f"Target:     delta = {TARGET_DELTA}")
    print(f"Thresholds: tight={THRESHOLD}, strong={THRESHOLD_2}")
    print(f"Trials:     {N_TRIALS:,}")
    print(f"Seed:       {SEED}")
    
    # --- Show observed pairs ---
    print("\n" + "-" * 70)
    print("OBSERVED PAIR RATIOS")
    print("-" * 70)
    obs_devs = compute_deviations(LOGS, SIXTH_PAIRS, TARGET_DELTA)
    for k, (i, j) in enumerate(SIXTH_PAIRS):
        ratio = abs(LOGS[j] - LOGS[i])
        dev = obs_devs[k]
        tight = "★" if dev <= THRESHOLD else ("●" if dev <= THRESHOLD_2 else " ")
        print(f"  {tight} {LABELS[i]:>25} -> {LABELS[j]:<25} "
              f"ratio = {ratio:.3f}   |dev| = {dev:.3f}")
    
    obs_tight = int(np.sum(obs_devs <= THRESHOLD))
    obs_strong = int(np.sum(obs_devs <= THRESHOLD_2))
    print(f"\n  Tight matches (★, |dev| <= {THRESHOLD}): {obs_tight} / {N_PAIRS}")
    print(f"  Strong matches (●, |dev| <= {THRESHOLD_2}): {obs_strong} / {N_PAIRS}")
    
    # --- Test 1: Tight threshold ---
    print("\n" + "-" * 70)
    print(f"TEST 1: Pre-specified pairs, threshold |dev| <= {THRESHOLD}")
    print("-" * 70)
    t1_start = time.time()
    r1 = run_permutation_test(LOGS, SIXTH_PAIRS, TARGET_DELTA, THRESHOLD, N_TRIALS, SEED)
    t1_elapsed = time.time() - t1_start
    
    print(f"  Completed in {t1_elapsed:.1f}s")
    print(f"  Observed: {r1['obs_strong']} / {N_PAIRS}")
    print(f"  Perms >= {r1['obs_strong']}: {r1['count_ge']:,} / {N_TRIALS:,}")
    print(f"  p-value: {r1['p_value']:.6f} ({r1['p_value']*100:.4f}%)")
    print(f"  p-value (add-one): {r1['p_value_add1']:.6f}")
    if r1['sigma'] is not None:
        print(f"  Sigma (one-sided): {r1['sigma']:.2f}σ")
    else:
        print(f"  Sigma: > {stats.norm.isf(1/(N_TRIALS+1)):.1f}σ (zero events)")
    print(f"\n  Permutation distribution:")
    for k, v in sorted(r1['distribution'].items()):
        pct = v / N_TRIALS * 100
        marker = " <-- OBSERVED" if k == r1['obs_strong'] else ""
        print(f"    {k} matches: {v:>8,} ({pct:>6.2f}%){marker}")
    
    # --- Test 2: Strong threshold ---
    print("\n" + "-" * 70)
    print(f"TEST 2: Pre-specified pairs, threshold |dev| <= {THRESHOLD_2}")
    print("-" * 70)
    t2_start = time.time()
    r2 = run_permutation_test(LOGS, SIXTH_PAIRS, TARGET_DELTA, THRESHOLD_2, N_TRIALS, SEED)
    t2_elapsed = time.time() - t2_start
    
    print(f"  Completed in {t2_elapsed:.1f}s")
    print(f"  Observed: {r2['obs_strong']} / {N_PAIRS}")
    print(f"  Perms >= {r2['obs_strong']}: {r2['count_ge']:,} / {N_TRIALS:,}")
    print(f"  p-value: {r2['p_value']:.6f} ({r2['p_value']*100:.4f}%)")
    print(f"  p-value (add-one): {r2['p_value_add1']:.6f}")
    if r2['sigma'] is not None:
        print(f"  Sigma (one-sided): {r2['sigma']:.2f}σ")
    else:
        print(f"  Sigma: > {stats.norm.isf(1/(N_TRIALS+1)):.1f}σ (zero events)")
    print(f"\n  Permutation distribution:")
    for k, v in sorted(r2['distribution'].items()):
        pct = v / N_TRIALS * 100
        marker = " <-- OBSERVED" if k == r2['obs_strong'] else ""
        print(f"    {k} matches: {v:>8,} ({pct:>6.2f}%){marker}")
    
    # --- Test 3: Delta scan ---
    print("\n" + "-" * 70)
    print("TEST 3: Delta scan (look-elsewhere correction)")
    print("-" * 70)
    t3_start = time.time()
    r3 = run_delta_scan(LOGS, SIXTH_PAIRS, THRESHOLD, (4.0, 8.0), 0.1, N_TRIALS, SEED)
    t3_elapsed = time.time() - t3_start
    
    print(f"  Completed in {t3_elapsed:.1f}s")
    print(f"  Delta range: [{r3['delta_range'][0]}, {r3['delta_range'][1]}], "
          f"step {r3['delta_step']}")
    print(f"  Best deltas observed:")
    for d, n in r3['best_deltas']:
        print(f"    delta={d:.2f}: {n} tight matches")
    print(f"  Observed scan max: {r3['obs_scan_max']}")
    print(f"  Perms with scan_max >= {r3['obs_scan_max']}: "
          f"{r3['count_ge']:,} / {N_TRIALS:,}")
    print(f"  p-value (scan-corrected): {r3['p_value']:.6f} ({r3['p_value']*100:.4f}%)")
    print(f"  p-value (add-one): {r3['p_value_add1']:.6f}")
    if r3['sigma'] is not None:
        print(f"  Sigma (one-sided): {r3['sigma']:.2f}σ")
    else:
        print(f"  Sigma: > {stats.norm.isf(1/(N_TRIALS+1)):.1f}σ (zero events)")
    
    # --- Final Summary ---
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"""
COSMIC SIXTH PERMUTATION TEST
==============================
Ladder:  15 verified structures (CODATA 2022 / IAU 2015)
Pairs:   6 pre-specified (from verified ladder only)
Target:  log₁₀(L_large / L_small) ≈ 6.0
Trials:  {N_TRIALS:,}
Seed:    {SEED}

Observed pair ratios:
  Bacterium → Human:               10^5.954  (dev = 0.046) ★
  Solar System → Local Bubble:     10^6.015  (dev = 0.015) ★
  Milky Way → Observable Universe: 10^5.940  (dev = 0.060) ★
  Earth → Solar System:            10^5.850  (dev = 0.150) ●
  City → Sun:                      10^5.840  (dev = 0.160) ●
  C. elegans → City:               10^6.300  (dev = 0.300)

TEST 1 — Tight (|dev| ≤ 0.1):
  3 of 6 pairs match
  p = {r1['p_value']:.6f} ({r1['count_ge']} / {N_TRIALS:,})
  {"≈ {:.2f}σ".format(r1['sigma']) if r1['sigma'] else "> 4σ"}

TEST 2 — Strong (|dev| ≤ 0.2):
  5 of 6 pairs match
  p < 5 × 10⁻⁶ (0 / {N_TRIALS:,}; add-one bound)
  > {stats.norm.isf(1/(N_TRIALS+1)):.1f}σ

TEST 3 — Delta scan (look-elsewhere, delta ∈ [4, 8]):
  Max = {r3['obs_scan_max']} tight matches at delta ≈ 5.90
  p < 5 × 10⁻⁶ (0 / {N_TRIALS:,}; add-one bound)
  > {stats.norm.isf(1/(N_TRIALS+1)):.1f}σ

HONEST CAVEATS:
1. Post-hoc pair selection: pairs were identified from the data
   before this test, same vulnerability as the 10^24 paper.
2. The delta scan partially corrects for this but does not fully
   eliminate selection bias.
3. Six pairs is a small sample; the result is sensitive to which
   pairs are included.
4. A fully pre-registered replication using independently measured
   structures would provide stronger evidence.
5. Statistical significance ≠ mechanism. This test quantifies how
   unlikely the pattern is under random label assignment; it does
   not explain why the pattern exists.

★ = tight match (|dev| ≤ 0.1)  ● = strong match (|dev| ≤ 0.2)
""")
    
    # Save results as JSON for reproducibility
    results = {
        "test_name": "Cosmic Sixth Permutation Test",
        "date": "2026-03",
        "seed": SEED,
        "n_trials": N_TRIALS,
        "ladder_values": dict(zip(LABELS, LOGS.tolist())),
        "pairs": [(LABELS[i], LABELS[j]) for i, j in SIXTH_PAIRS],
        "target_delta": TARGET_DELTA,
        "test_1_tight": r1,
        "test_2_strong": r2,
        "test_3_scan": r3,
    }
    with open("cosmic_sixth_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("Results saved to cosmic_sixth_results.json")
