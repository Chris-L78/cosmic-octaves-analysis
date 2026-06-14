# Book verification scripts

Standalone scripts and figures referenced from the printed appendices of
*Our Fractal Universe: The Math Behind the Pattern* (Appendix K, Duty Cycles).

The canonical, fully-annotated analysis lives in the Jupyter notebook
[`notebooks/Appendix_K_Sleep_Duty_Cycles.ipynb`](../../notebooks/Appendix_K_Sleep_Duty_Cycles.ipynb).
The files here are the script-and-figure form the book cites directly.

```
issue34_scripts/sleep_duty_cycles.py   16-level duty-cycle table, mammalian
                                        sleep-mass power law, global
                                        period-vs-mass fit, generates the 3 plots
issue34_plots/                          duty_fraction_vs_mass.png
                                        cycle_period_vs_mass.png
                                        cross_scale_comparison.png
issue35_scripts/regime_scaling.py       biological vs cosmic regime fits and the
                                        z-test from Appendix K Section 6.3
```

Requirements: `numpy`, `scipy`, `matplotlib` (see `../../code/requirements.txt`).
Run either script directly, e.g. `python issue34_scripts/sleep_duty_cycles.py`.
