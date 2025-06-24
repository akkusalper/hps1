import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset or use realistic_df if already in scope
# Example:
# realistic_df = pd.read_excel("HPS1_Realistic_Cited_Registry.xlsx")

plt.figure(figsize=(8, 6))
sns.scatterplot(
    x="Age_at_Diagnosis",
    y="PF_Onset_Age",
    hue="Study_Ref",       # e.g., Vicary, Gochuico, El-Chemaly
    style="Treatment",     # e.g., Pirfenidone, Nintedanib, None
    data=realistic_df,
    palette="deep",
    s=100,
    edgecolor='black'
)
plt.title("Age at Diagnosis vs Pulmonary Fibrosis Onset", pad=15)
plt.xlabel("Age at HPS1 Diagnosis (years)")
plt.ylabel("Pulmonary Fibrosis Onset Age (years)")
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
