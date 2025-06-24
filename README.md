# hps1
Age at Diagnosis vs Pulmonary Fibrosis Onset
# HPS1 Pulmonary Fibrosis Analysis

This repository contains synthetic, literature-informed analyses for pulmonary fibrosis (PF) in Hermansky–Pudlak Syndrome Type 1 (HPS1) patients. It includes statistical evaluation and visualizations to support translational research and registry development.

## Contents

- `hps1_fvc_analysis_script.py`: Python script that:
  - Simulates a patient dataset based on real clinical study summaries (Gochuico 2012, Vicary 2016, El-Chemaly 2018)
  - Plots age at diagnosis vs PF onset
  - Performs ANOVA and Tukey HSD post-hoc test for FVC (%) across treatment groups
  - Exports CSV of significant pairwise comparisons
  - Generates high-quality publication-style plots

Disclaimer
All data in this repository is modelled from literature research and used solely for educational, visual, and analytic purposes. No real patient data is included.

- `tukey_posthoc_results.csv`: Post-hoc test results showing which treatments significantly affect pulmonary function (FVC%).

- `fvc_by_treatment_boxplot.png`: Box plot with individual patient FVCs by treatment.

- `fvc_by_treatment_ci.png`: Point plot with 95% confidence intervals of FVC per treatment group.

- `diagnosis_vs_pf_onset.png`: Scatter plot of age at diagnosis vs. PF onset age.

## Dependencies

- Python 3.x  
- `pandas`, `matplotlib`, `seaborn`, `statsmodels`

Install via:
```bash
pip install pandas matplotlib seaborn statsmodels
