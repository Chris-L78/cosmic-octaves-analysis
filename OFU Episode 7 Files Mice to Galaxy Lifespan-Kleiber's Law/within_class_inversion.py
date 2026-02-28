#!/usr/bin/env python3
"""
Within-Class vs Cross-Class Scaling Inversion Analysis
=======================================================
Video 7: "Can Mouse Metabolism Predict the Lifespan of a Galaxy?"
Our Fractal Universe — Chris Lehto

Demonstrates that within each class of objects, the mass-lifespan
relationship INVERTS relative to the cross-class trend:
  - Within dogs:     bigger → shorter life (Great Dane vs Chihuahua)
  - Across species:  bigger → longer life (mouse vs elephant)
  - Within stars:    bigger → shorter life (O-star vs M-dwarf)
  - Across scales:   bigger → longer life (cell → human → Sun → galaxy)
  - Within galaxies: bigger → shorter active lifespan (elliptical vs dwarf)

This pattern recurs independently across three unrelated systems.

Usage:
    python within_class_inversion.py

References:
    Kraus C et al. (2013) Am Nat 181:492-505 [dog breed lifespan scaling]
    Lindstedt SL, Calder WA (1981) Q Rev Biol 56:1 [biological time scaling]
    Hansen CJ et al. (2004) Stellar Interiors, Springer [stellar mass-luminosity]
    Thomas D et al. (2005) ApJ 621:673 [elliptical formation timescales]
    Weisz DR et al. (2011) ApJ 739:5 [dwarf galaxy star formation histories]
"""

import numpy as np

print("=" * 70)
print("WITHIN-CLASS vs CROSS-CLASS SCALING INVERSIONS")
print("Video 7 — Our Fractal Universe")
print("=" * 70)

# ============================================================
# 1. DOG BREED INVERSION
# ============================================================

print("\n--- 1. Within Dogs (bigger → shorter) ---")
dogs = [
    ("Chihuahua",     2,   15),
    ("Beagle",        10,  12),
    ("Labrador",      30,  11),
    ("Great Dane",    60,   8),
]
print(f"{'Breed':<15} {'Mass (kg)':<12} {'Lifespan (yr)'}")
print("-" * 40)
for name, m, t in dogs:
    print(f"{name:<15} {m:<12} {t}")

log_m_dogs = np.log10([d[1] for d in dogs])
log_t_dogs = np.log10([d[2] for d in dogs])
dog_slope = np.polyfit(log_m_dogs, log_t_dogs, 1)[0]
print(f"\nWithin-dog slope: {dog_slope:.2f} (NEGATIVE = bigger → shorter)")

# ============================================================
# 2. ACROSS-SPECIES (bigger → longer)
# ============================================================

print("\n--- 2. Across Species (bigger → longer) ---")
species = [
    ("Mouse",          0.02,    4),
    ("Rat",            0.3,     3),
    ("Cat",            4,      15),
    ("Dog (avg)",     20,      12),
    ("Human",         70,      80),
    ("Elephant",    5000,      65),
    ("Bowhead whale", 100000, 211),
]
print(f"{'Species':<18} {'Mass (kg)':<12} {'Lifespan (yr)'}")
print("-" * 45)
for name, m, t in species:
    print(f"{name:<18} {m:<12.1f} {t}")

log_m_sp = np.log10([s[1] for s in species])
log_t_sp = np.log10([s[2] for s in species])
sp_slope = np.polyfit(log_m_sp, log_t_sp, 1)[0]
print(f"\nAcross-species slope: {sp_slope:.3f} (POSITIVE = bigger → longer)")

# ============================================================
# 3. WITHIN STARS (bigger → shorter)
# ============================================================

print("\n--- 3. Within Stars (bigger → shorter) ---")
print("Main-sequence lifetime: T ∝ M / L ∝ M / M^3.5 ∝ M^(-2.5)")
print("(Effective exponent ~-2 for massive stars due to L-M flattening)")
stars = [
    ("Red dwarf (0.1 M☉)",    0.1,   1e13),     # 10 trillion years
    ("K-dwarf (0.7 M☉)",      0.7,   4.5e10),   # 45 billion years
    ("Sun (1.0 M☉)",          1.0,   1e10),      # 10 billion years
    ("A-star (2.0 M☉)",       2.0,   1.5e9),     # 1.5 billion years
    ("B-star (10 M☉)",       10.0,   2e7),       # 20 million years
    ("O-star (60 M☉)",       60.0,   3e6),       # 3 million years
]
print(f"{'Star type':<25} {'Mass (M☉)':<12} {'Lifespan (yr)':<18} {'Notes'}")
print("-" * 75)
for name, m, t in stars:
    note = "← Our star" if m == 1.0 else ""
    print(f"{name:<25} {m:<12.1f} {t:<18.1e} {note}")

log_m_st = np.log10([s[1] for s in stars])
log_t_st = np.log10([s[2] for s in stars])
st_slope = np.polyfit(log_m_st, log_t_st, 1)[0]
print(f"\nWithin-star slope: {st_slope:.2f} (NEGATIVE = bigger → shorter)")

# Verify the 60× mass → 3 Myr claim
ratio_60 = stars[-1][2] / stars[3-1][2]  # O-star / Sun
print(f"\nVerification: 60 M☉ star / Sun lifespan = {stars[-1][2]/stars[2][2]:.0e}")
print(f"60× more massive → {stars[2][2]/stars[-1][2]:.0f}× shorter lifespan")

# ============================================================
# 4. WITHIN GALAXIES (bigger → shorter active lifespan)
# ============================================================

print("\n--- 4. Within Galaxies (bigger → shorter active lifespan) ---")
galaxies = [
    ("Dwarf irregular",  1e8,   "Still forming stars now; will continue for trillions of years"),
    ("Milky Way-type",   1e11,  "Star formation declining; ~10-100 trillion yr active lifespan"),
    ("Giant elliptical", 1e13,  "Formed most stars in first 1-2 Gyr; now 'red and dead'"),
]
print(f"{'Galaxy type':<20} {'Stellar mass (M☉)':<20} {'Activity'}")
print("-" * 85)
for name, m, note in galaxies:
    print(f"{name:<20} {m:<20.0e} {note}")

print("\nPattern: Most massive galaxies exhausted their gas earliest → shortest ACTIVE lifespan")
print("Source: Thomas et al. (2005) ApJ 621:673; Weisz et al. (2011) ApJ 739:5")

# ============================================================
# 5. CROSS-CLASS (bigger → longer)
# ============================================================

print("\n--- 5. Cross-Scale Trend (bigger → longer) ---")
cross = [
    ("Cell",       1e-12,    14/365.25),
    ("Human",      70,       80),
    ("Sun",        1.989e30, 1e10),
    ("Milky Way",  1.5e42,   1.39e13),  # predicted
]
print(f"{'Object':<12} {'Mass (kg)':<15} {'Lifespan (yr)':<18} {'Note'}")
print("-" * 60)
for name, m, t in cross:
    note = "(predicted)" if name == "Milky Way" else ""
    print(f"{name:<12} {m:<15.2e} {t:<18.2e} {note}")

print(f"\nCross-scale slope: 0.272 (POSITIVE = bigger → longer)")

# ============================================================
# SUMMARY: THE PATTERN
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY: THREE INDEPENDENT INVERSIONS")
print("=" * 70)
print(f"""
  System       | Within-class              | Cross-class
  -------------|---------------------------|---------------------------
  Biology      | Dogs: bigger → shorter    | Species: bigger → longer
               | (slope ≈ {dog_slope:.2f})           | (slope ≈ {sp_slope:.2f})
  -------------|---------------------------|---------------------------
  Stars        | Massive → shorter         | Cell→Human→Sun: longer
               | (slope ≈ {st_slope:.2f})           | (slope ≈ 0.272)
  -------------|---------------------------|---------------------------
  Galaxies     | Massive → red and dead    | Small→MW→Universe: longer
               | (qualitative)             | (slope ≈ 0.272)

Three unrelated systems. Same structural pattern.
Within each class: bigger → shorter.
Across classes: bigger → longer.
""")
