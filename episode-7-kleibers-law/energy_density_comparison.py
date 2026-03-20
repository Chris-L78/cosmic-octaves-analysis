#!/usr/bin/env python3
"""
Energy Density Comparison: Stars vs Biology
=============================================
Video 7: "Can Mouse Metabolism Predict the Lifespan of a Galaxy?"
Our Fractal Universe — Chris Lehto

Calculates the per-kilogram energy output of the Sun vs a human,
demonstrating that biological organisms are far more energetically
intense than stellar objects per unit mass.

Key result: Humans are ~6,000× more energy-dense than the Sun.

Usage:
    python energy_density_comparison.py

References:
    IAU 2015 nominal solar luminosity: L☉ = 3.828 × 10²⁶ W
    IAU 2015 nominal solar mass: M☉ = 1.989 × 10³⁰ kg
    Human BMR ~80 W at 70 kg (Mifflin-St Jeor / Harris-Benedict)
"""

import numpy as np

print("=" * 70)
print("ENERGY DENSITY: SUN vs HUMAN")
print("Video 7 — Our Fractal Universe")
print("=" * 70)

# ============================================================
# SUN
# ============================================================

sun_luminosity_W = 3.828e26   # Watts (IAU 2015 nominal)
sun_mass_kg = 1.989e30        # kg
sun_W_per_kg = sun_luminosity_W / sun_mass_kg

print("\n--- Sun ---")
print(f"Luminosity:       {sun_luminosity_W:.3e} W")
print(f"Mass:             {sun_mass_kg:.3e} kg")
print(f"Energy density:   {sun_W_per_kg:.6f} W/kg")
print(f"                  ≈ 0.0002 W/kg")
print(f"                  ≈ 0.2 milliwatts per kilogram")

# ============================================================
# HUMAN
# ============================================================

human_bmr_W = 80          # Watts (typical adult at rest)
human_mass_kg = 70         # kg
human_W_per_kg = human_bmr_W / human_mass_kg

print("\n--- Human ---")
print(f"BMR:              ~{human_bmr_W} W (at rest)")
print(f"Mass:             {human_mass_kg} kg")
print(f"Energy density:   {human_W_per_kg:.2f} W/kg")

# ============================================================
# COMPARISON
# ============================================================

ratio = human_W_per_kg / sun_W_per_kg

print("\n--- Comparison ---")
print(f"Human / Sun:      {ratio:,.0f}×")
print(f"You are nearly {ratio/1000:.0f},000× more energetically intense than the Sun")
print(f"per kilogram of matter.")

print(f"""
Context:
  The Sun's total energy output is enormous: {sun_luminosity_W:.1e} watts.
  But spread over {sun_mass_kg:.1e} kg of mass, it's actually very gentle.
  
  A human body, despite being {human_mass_kg} kg, runs at {human_bmr_W} watts —
  more than a standard light bulb.
  
  The Sun wins by being {sun_mass_kg/human_mass_kg:.0e}× more massive, not more intense.
""")

# ============================================================
# OTHER OBJECTS FOR CONTEXT
# ============================================================

print("--- Extended Comparison ---")
objects = [
    ("Laptop charger",   65,       2.0,        "65W / ~2 kg"),
    ("Human (resting)",  80,       70,         "BMR at rest"),
    ("Human (running)",  1200,     70,         "During intense exercise"),
    ("Sun",              3.828e26, 1.989e30,   "IAU 2015 nominal values"),
    ("Red dwarf (0.1 M☉)", 3.828e26 * 0.001, 1.989e30 * 0.1, "L ≈ 0.001 L☉"),
    ("Blue giant (60 M☉)", 3.828e26 * 7e5, 1.989e30 * 60,    "L ≈ 700,000 L☉"),
]

print(f"{'Object':<25} {'Power (W)':<15} {'Mass (kg)':<15} {'W/kg':<12} {'× Sun'}")
print("-" * 80)
for name, power, mass, note in objects:
    w_per_kg = power / mass
    x_sun = w_per_kg / sun_W_per_kg
    print(f"{name:<25} {power:<15.3e} {mass:<15.3e} {w_per_kg:<12.4f} {x_sun:<.0f}×")

print(f"""
Key insight from the script:
  "So why does this comparatively GENTLE object have a birth,
   life stages, and a death?"
  
  Stars are less energetically intense per kg than you are.
  Yet they exhibit: birth (protostellar collapse), life stages
  (main sequence → giant → dwarf), and death (supernova/white dwarf).
  
  The question is: why do their durations follow the same
  mathematical form (power law) as biological lifespans?
""")
