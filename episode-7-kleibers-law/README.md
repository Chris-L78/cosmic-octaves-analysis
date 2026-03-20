# Video 7 — Cross-Scale Lifespan Regression

**"Can Mouse Metabolism Predict the Lifespan of a Galaxy?"**
Our Fractal Universe — Chris Lehto

📺 [Watch the video](https://youtube.com/@OurFractalUniverse)

---

## Overview

In 1932, Max Kleiber discovered that animal lifespans follow a power law: T ∝ M^0.25. Bigger animal → slower metabolism per kilogram → longer life.

We take three data points — a mammalian cell, a human, and the Sun — spanning **42 orders of magnitude in mass**, and fit a log-log regression. The slope comes back at **0.272 ± 0.011**, matching Kleiber's biological prediction within 2 standard errors.

We then use that line to predict the lifespan of the **Milky Way galaxy** — a data point the regression has never seen.

**It lands within a factor of 1.4.**

---

## Key Results

| Metric | Value |
|--------|-------|
| Regression slope | 0.272 ± 0.011 |
| Kleiber theoretical | 0.25 |
| R² | 0.998 |
| Milky Way prediction | ~14 trillion years |
| Milky Way observed range | 10–100 trillion years |
| Factor off (lower bound) | 1.4× |
| Universe prediction | ~10^16 years (overshoots by ~100×) |

---

## Repository Contents

```
video7_cross_scale_lifespan/
├── README.md                           ← You are here
├── code/
│   ├── cross_scale_regression.py       ← Main 3-point regression + galaxy prediction
│   ├── sensitivity_cell_lifespan.py    ← Cell lifespan variation (3d to 300d)
│   ├── within_class_inversion.py       ← Dogs/Stars/Galaxies inversion pattern
│   ├── energy_density_comparison.py    ← Sun vs Human W/kg calculation
│   ├── generate_figures.py             ← Generates all 5 figures
│   └── requirements.txt
├── data/
│   ├── training_data.csv               ← Cell, Human, Sun (with sources)
│   ├── prediction_targets.csv          ← Milky Way + Universe predictions
│   ├── within_class_inversion.csv      ← Full inversion dataset
│   ├── energy_density.csv              ← W/kg comparison data
│   ├── cross_scale_results.json        ← Generated regression output
│   └── sensitivity_analysis.csv        ← Generated sensitivity results
└── figures/
    ├── 1_cross_scale_regression.png    ← Main log-log plot with galaxy prediction
    ├── 2_sensitivity_analysis.png      ← Robustness across cell lifespan choices
    ├── 3_three_slope_comparison.png    ← AnAge vs Kleiber vs cross-scale slopes
    ├── 4_energy_density.png            ← Sun vs Human energy density
    └── 5_inversion_comparison.png      ← 4-panel within/cross-class inversions
```

---

## Quick Start

```bash
cd video7_cross_scale_lifespan
pip install -r code/requirements.txt

# Run the main analysis
python code/cross_scale_regression.py

# Run sensitivity tests
python code/sensitivity_cell_lifespan.py

# Explore the within-class inversion pattern
python code/within_class_inversion.py

# Energy density comparison
python code/energy_density_comparison.py

# Generate all figures
python code/generate_figures.py
```

All scripts use **fixed random seed (42)** for exact reproducibility.

---

## The Honest Problems

1. **n = 3.** Two points define a line perfectly; three gives one degree of freedom. R² = 0.998 with n = 3 is suggestive, not overwhelming.

2. **Slope is at the high end.** Our 0.272 exceeds the AnAge mammal empirical range (~0.20–0.27) slightly. It's in the biological neighborhood, not a perfect match.

3. **Universe prediction overshoots by ~100×.** The line predicts ~10^16 years for the universe; the active lifespan (star formation era) is ~10^14. Two orders of magnitude off across 55 orders of magnitude of mass.

4. **Within-class scaling inverts.** Massive stars die faster, not slower. Massive galaxies go "red and dead" earliest. This within-class inversion is real and must be accounted for in any scaling framework.

---

## Verified Numbers

All numerical claims in the video are calculator-confirmed:

| Claim | Verified Value |
|-------|----------------|
| Cell lifespan (14d) | 0.03833 years |
| Regression slope | 0.2721 |
| Slope std error | 0.0110 |
| R² | 0.9984 |
| MW prediction | 10^13.14 = 1.39 × 10^13 years |
| Factor from observed | 1.4× |
| Sun energy density | 0.000192 W/kg |
| Human energy density | 1.14 W/kg |
| Human/Sun ratio | 5,938× (~6,000×) |
| 60 M☉ star lifespan | ~3 million years |
| Within-star effective exponent | ~−2 |
| Neuron outlier ratio | 482× above prediction |

---

## References

- Kleiber M. (1932) "Body Size and Metabolism." *Hilgardia* 6:315–353
- West GB, Brown JH, Enquist BJ (1997) "A General Model for the Origin of Allometric Scaling Laws in Biology." *Science* 276:122–126
- Lindstedt SL, Calder WA (1981) "Body Size, Physiological Time, and Longevity of Homeothermic Animals." *Q Rev Biol* 56:1–16
- Sackmann IJ, Boothroyd AI, Kraemer KE (1993) "Our Sun. III. Present and Future." *ApJ* 418:457
- Adams FC, Laughlin G (1997) "A Dying Universe: The Long-Term Fate and Evolution of Astrophysical Objects." *Rev Mod Phys* 69:337
- de Magalhães JP et al. (2009) "The Human Ageing Genomic Resources: AnAge Database"
- McMillan PJ (2011) "Mass Models of the Milky Way." *MNRAS* 414:2446
- Sender R et al. (2016) "Revised Estimates for the Number of Human and Bacteria Cells." *Cell* 164:337
- Thomas D et al. (2005) "Ages and Metallicities of Cluster and Field Ellipticals." *ApJ* 621:673
- Weisz DR et al. (2011) "The Star Formation Histories of Local Group Dwarf Galaxies." *ApJ* 739:5
- Kraus C et al. (2013) "The Size–Life Span Trade-Off Decomposed: Why Large Dogs Die Young." *Am Nat* 181:492–505
- Hansen CJ, Kawaler SD, Trimble V (2004) *Stellar Interiors: Physical Principles, Structure, and Evolution.* Springer
- Tye SHH, Luu HN, Qiu YC (2025) "A New Cosmological Model: Big Crunch." *JCAP*

---

## License

MIT — see [LICENSE](../LICENSE)

## Connection to Cosmic Octaves

This analysis extends the spatial scaling patterns documented in the main [cosmic-octaves-analysis](../README.md) into the **temporal domain**. Where the spatial analysis found structures recurring at 10^24 meter intervals (p = 0.000055), this analysis finds that the *lifespans* of those structures follow a single power law consistent with biological metabolic scaling.

If you find an error, please [open an issue](https://github.com/Chris-L78/cosmic-octaves-analysis/issues).
