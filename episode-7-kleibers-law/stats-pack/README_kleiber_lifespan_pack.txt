Kleiber / Lifespan Scaling — Data & Stats Pack
Generated: 2026-02-13 06:35 UTC

CONTENTS
--------
1) Raw input
   - anage_data.txt
     Your AnAge export used as the primary data source.

2) Clean extracts (AnAge-only)
   - anage_vertebrates_high_acceptable_mass_longevity.csv
     All species with Adult weight (g) and Maximum longevity (yrs) present,
     filtered to Data quality in {high, acceptable}.
   - anage_mammals_high_acceptable_mass_longevity.csv
     Same filter, mammals subset.
   - anage_provenance_sample_rows.csv
     Sample rows documenting column provenance (for audit / citations).

3) Option B2 datasets (AnAge longevity + rule-based mass backfills for missing-mass invertebrate anchors)
   - anage_optionB_vertebrates_plus_key_inverts.csv
     Vertebrates AnAge-only + key invertebrate anchors (mass backfilled w/ source).
   - anage_optionB_scale_balanced_bins.csv
     Bin medians (1-dex) and counts for the above.

   - b2_dataset_species_expanded.csv
     Expanded B2 dataset used in the main writeup workstream.
   - b2_bins1_medians_expanded.csv
     1-dex bin medians used for the scale-balanced fit (expanded dataset).
   - b2_bins2_medians_expanded.csv
     2-dex bin medians used for the scale-balanced fit (expanded dataset).

4) "Max coverage" dataset (largest N available from your inputs + B2 anchors)
   - b2_max_organisms_dataset.csv
     Pooled dataset (species-level).
   - b2_max_bins1.csv
     1-dex bin medians used for scale-balanced fit.
   - b2_max_bins2.csv
     2-dex bin medians used for scale-balanced fit.

5) Historical small-set reference
   - table_1A_primary_9species.csv
     Earlier 9-species curated table (reference only).

KEY RESULTS (from this pack)
----------------------------
Model form: log10(T_years) = a + n * log10(M_kg)

A) "Max coverage" pooled OLS (species-level, dominated by dense mass ranges)
   n = 0.141236,  R^2 = 0.342,  N = 3216

B) "Max coverage" scale-balanced (bin-median OLS)
   1-dex bins: n = 0.203387, R^2 = 0.891, bins = 14
   2-dex bins: n = 0.220935, R^2 = 0.944, bins = 8

Sun extrapolation (M_sun = 1.989e30 kg) using each fitted line:
   pooled OLS:  T_sun ≈ 3.277e+05 years (dex error vs 1e10 yr = 4.484)
   1-dex bins:  T_sun ≈ 2.143e+07 years (dex error vs 1e10 yr = 2.669)
   2-dex bins:  T_sun ≈ 5.928e+07 years (dex error vs 1e10 yr = 2.227)

NOTES
-----
- The pooled OLS slope is not a good "across-scales" estimate because it is dominated by the
  most densely sampled mass ranges in the dataset.
- The bin-median (scale-balanced) fits are intended to give each mass decade comparable weight.

