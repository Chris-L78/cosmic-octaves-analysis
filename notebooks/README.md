[README.md](https://github.com/user-attachments/files/27166930/README.md)
# Mathematical Appendices — Verification Notebooks

These Jupyter notebooks reproduce all numerical claims in the *Mathematical Appendices* companion volume to the book *Our Fractal Universe: As Above, So Below* by Chris Lehto.

Each notebook is self-contained and corresponds to one appendix.

## Quick start

```bash
pip install -r requirements.txt
jupyter notebook
```

Or open any notebook directly in Jupyter, JupyterLab, VS Code, Colab, or any compatible environment.

## What each notebook contains

| Notebook | Appendix | Reproduces |
|---|---|---|
| `Appendix_A_Scale_Table.ipynb` | A | 15-structure scale table; cosmic-octave deviations; sensitivity tests (city radius, *C. elegans* selection); geometric center of the ladder; **the 200,000-trial permutation test (p = 0.000055, ≈3.9σ)**; Local Bubble population estimate (Section 5.3) |
| `Appendix_B_Mass_Radius.ipynb` | B | Mass-radius scaling exponent (n ≈ 2.9 average for accumulation); density transitions across all 15 structures; T ∝ r^0.7 derivation chain; orbital vs. accumulation classification |
| `Appendix_C_Life_Test.ipynb` | C | Nation size distribution (no characteristic length); Michod individuality scoring (16 structures); NASA-Joyce four-requirements scoring (17 structures); substrate-independence verification; worked examples |
| `Appendix_D_Kleiber_Law.ipynb` | D | Empirical Kleiber exponent (~0.20–0.22) from biological data; biology-only stellar lifetime extrapolation showing 1.9-dex shortfall at n=0.21 |
| `Appendix_E_Lifespan_Scaling.ipynb` | E | Biological regression (12 species); cross-scale regression including stellar anchor; Milky Way prediction within factor 1.4× of observed; Sun miss factor (~86×) at biological exponent; cell-lifespan and star-choice sensitivity sweeps |
| `Appendix_F_Time_Radius.ipynb` | F | 15-point time-radius regression (n = 0.78 ± 0.10, R² = 0.82); 8-point original dataset; prediction-residual table; F.14 exponent sensitivity; F.15 anchor independence |
| `Appendix_G_Energy_Power.ipynb` | G | Power densities by scale; solar input (173,000 TW); Earth magnetosphere; supercluster causal-regulation analysis; WHIM thermal energy |
| `Appendix_H_Information.ipynb` | H | Information density across DNA / brain / hard drives; thermodynamic constraints on information |
| `Appendix_K_Sleep_Duty_Cycles.ipynb` | K | Rest-activity cycles across 16 levels; mammalian power-law extrapolation failure at cosmic scales |
| `Appendix_L_Golden_Ratio_Harmonics.ipynb` | L | Dirac large-number ratios from CODATA 2022 constants; harmonic indices (h₁ = 1.640, h₂ = 1.695, h₃ = 1.716); clustering probability (~0.1%); H₀ check |

## The headline result

The book's primary statistical claim — **p = 0.000055** from a 200,000-trial permutation test on seven canonical octave pairs — is computed in `Appendix_A_Scale_Table.ipynb` (Section V) and produces the same value cited throughout the manuscript and in the parent paper at `code/permutation_test.py`. Random seed is fixed at 42 for full reproducibility.

## Notes on data sources

- **Constants:** CODATA 2022 throughout
- **Astronomical scales:** IAU 2015 nominal solar values
- **Cosmological parameters:** Planck 2018 best-fit
- **Biological cell counts:** primary literature (e.g., Sulston et al. 1983 for *C. elegans*)
- **Galactic surveys:** LAB HI (Ehlerová & Palouš 2013), outer-galaxy supershell catalog (Suad et al. 2014), MW-like simulations (Sun et al. 2024)

All numerical inputs are documented inline in each notebook.

## License

MIT — see top-level [LICENSE](../LICENSE) file.

## Citation

If you use these notebooks in your work, please cite the parent paper:

```bibtex
@misc{lehto2026cosmic,
  author = {Lehto, Chris},
  title = {Scale Recurrence Across Cosmic Structures: A Statistical Analysis of the 10²⁴-Meter Pattern},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Chris-L78/cosmic-octaves-analysis}
}
```
