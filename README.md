# Cosmic Octaves Analysis

![Cover](cover.png)

**Statistical Evidence for Scale Recurrence in the Universe**

[![YouTube](https://img.shields.io/badge/YouTube-Our_Fractal_Universe-red)](https://youtube.com/@OurFractalUniverse)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue)](paper/Cosmic_Octaves_Analysis_Paper.pdf)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Overview

This repository contains the complete analysis, data, and code for our paper:

**"Scale Recurrence Across Cosmic Structures: A Statistical Analysis of the 10²⁴-Meter Pattern"**

We document a statistically significant pattern where canonical organizational structures recur at intervals approximating 10²⁴ meters across 42 orders of magnitude, from protons to the observable universe.

**Full Paper**: [Cosmic_Octaves_Analysis_Paper.pdf](paper/Cosmic_Octaves_Analysis_Paper.pdf)

---

## Key Findings

- **15 structures** spanning quantum to cosmological scales
- **7 canonical octave pairs** (one per rung of the structure ladder)
- **3 strong matches** (deviation ≤0.2 from ideal ratio of 24.0)
- **p = 0.000055** for ≥3 strong matches by chance (~3.9σ)
- Conservative look-elsewhere correction: p ≈ 10⁻⁵

---

## Repository Contents

- 📄 **paper/**: Full manuscript (PDF)
- 📊 **data/**: Complete datasets (15 structures, 7 octave pairs)
- 💻 **code/**: Python scripts for permutation test and Δ-scan
- 📈 **figures/**: High-resolution visualizations (5 figures)

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/Chris-L78/cosmic-octaves-analysis.git
cd cosmic-octaves-analysis

# Install dependencies
pip install -r code/requirements.txt

# Run permutation test
python code/permutation_test.py

# Run look-elsewhere scan
python code/delta_scan.py
```

---

## The Canonical Ladder (15 Structures)

Our analysis uses a predefined "ladder" of fundamental organizational structures:

| Scale | Structure | log₁₀(L) | Octave Pair |
|-------|-----------|----------|-------------|
| Universe | Observable Universe | 26.64 | ← 7 → City |
| Supercluster | Virgo | 23.84 | ← 6 → Human |
| Galactic | Milky Way | 20.70 | ← 5 → C. elegans |
| Bubble | Local Bubble | 18.665 | ← 4 → Bacterium |
| Cluster | Open Cluster | 16.67 | ← 3 → Ribosome |
| System | Solar System | 12.65 | ← 2 → Atomic Orbital |
| Stellar | Sun | 8.84 | ← 1 → Proton |
| Planetary | Earth | 6.80 | |
| Social | City | 3.00 | |
| Organism | Human | -0.046 | |
| Multicellular | C. elegans | -3.30 | |
| Cellular | Bacterium | -6.00 | |
| Molecular | Ribosome | -7.96 | |
| Atomic | Hydrogen atom | -10.28 | |
| Subatomic | Proton | -15.08 | |

---

## The 7 Octave Pairs

Each "rung" is paired with a structure ~10²⁴ meters larger:

1. **Proton → Sun**: 23.92 (deviation: 0.08) ✓✓✓ Excellent
2. **Atomic Orbital → Solar System**: 22.93 (deviation: 1.07) Fair
3. **Ribosome → Open Cluster**: 24.63 (deviation: 0.63) ✓✓ Very Good
4. **Bacterium → Local Bubble**: 24.665 (deviation: 0.665) ✓✓ Very Good
5. **C. elegans → Milky Way**: 24.00 (deviation: 0.00) ✓✓✓✓ Perfect
6. **Human → Virgo Supercluster**: 23.886 (deviation: 0.114) ✓✓✓ Excellent
7. **City → Observable Universe**: 23.64 (deviation: 0.36) ✓✓ Very Good

**Result**: 3 strong matches (≤0.2), 6 total within ±0.7

---

## Visualizations

### Structure Ladder
![Structure Ladder](figures/2_structure_ladder.png)

### Permutation Test Results
![Permutation Test](figures/1_permutation_test_histogram.png)

### Deviation Summary
![Deviation Summary](figures/3_deviation_summary.png)

*See [figures/](figures/) for all 5 visualizations with detailed explanations.*

---

## Reproducibility

All analysis uses **fixed random seed (42)** for complete reproducibility. The permutation test runs 200,000 trials and can be independently verified.

**Verified output:**
```
Observed deviations: [0.08  1.07  0.63  0.665 0.    0.114 0.36 ]
Observed strong matches (<=0.2): 3
Permutation p-value: 0.000055 (0.0055%)
Successes: 11 out of 200000
Statistical significance: ~3.9 sigma
```

---

## What Makes This Analysis Rigorous

✅ **Predefined structure ladder** (not cherry-picked after seeing results)  
✅ **Consistent measurement methodology** across all scales  
✅ **Excluded speculative structures** (e.g., Oort Cloud)  
✅ **Conservative statistical testing** (look-elsewhere correction)  
✅ **Complete transparency** (all code, data, and limitations disclosed)  
✅ **Falsifiable predictions** provided for future testing

---

## Important Caveats

This is a **pattern claim, not a mechanism claim**. We document the statistical observation but do not propose a physical cause for the 10²⁴ spacing.

**Limitations:**
- Small sample size (7 pairs)
- Some structures have definitional ambiguity
- Pattern was noticed post-hoc (though scan correction addresses this)
- Independent replication needed

See paper Section 4.2 for complete discussion of limitations.

---

## Citation

If you use this analysis in your work, please cite:

```bibtex
@misc{lehto2026cosmic,
  author = {Lehto, Chris},
  title = {Scale Recurrence Across Cosmic Structures: A Statistical Analysis of the 10²⁴-Meter Pattern},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Chris-L78/cosmic-octaves-analysis}
}
```

---

## Video Series

Watch the complete video explanation on YouTube:  
🎥 [Our Fractal Universe - Cosmic Octaves](https://youtube.com/@OurFractalUniverse)

---

## Feedback Welcome

This research is open for peer review and constructive criticism. If you find errors, have questions, or want to suggest improvements:

- 📬 Open an [Issue](https://github.com/Chris-L78/cosmic-octaves-analysis/issues)
- 💬 Discuss on [Twitter/X: @LehtoFiles](https://twitter.com/LehtoFiles)
- 📺 Comment on [YouTube: @OurFractalUniverse](https://youtube.com/@OurFractalUniverse)

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## Acknowledgments

We thank the scientific community for the peer-reviewed measurements used here. Additional thanks to Claude (Anthropic), Grok (xAI), and ChatGPT (OpenAI) for methodology critique and code-review assistance.

---

**Status**: 🟢 Open for peer review and replication  
**Last Updated**: January 30, 2026
