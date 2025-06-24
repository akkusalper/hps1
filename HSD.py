import statsmodels.stats.multicomp as mc

# Assumes `realistic_df` contains "Treatment" and "Last_Known_FVC_percent"
comp = mc.MultiComparison(realistic_df["Last_Known_FVC_percent"], realistic_df["Treatment"])
tukey_result = comp.tukeyhsd()

# Print Tukey summary table
print(tukey_result.summary())

# If you want to access each value programmatically:
tukey_df = pd.DataFrame(data=tukey_result._results_table.data[1:], columns=tukey_result._results_table.data[0])

# Save the table to CSV for GitHub-friendly use
tukey_df.to_csv("tukey_posthoc_results.csv", index=False)
