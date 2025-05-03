##############-------evaluate_omr_performance.py

import json
import os
import pandas as pd

# Path to your results folder
results_folder = './mupix_results'

# List of tools and excerpts
tools = ["newzik", "photoscore", "playscore2", "soundslice"]
excerpts = [f"excerpt{str(i).zfill(2)}" for i in range(1, 11)]

# Initialize list for DataFrame rows
data = []

for excerpt in excerpts:
    row = {"Excerpt": excerpt}
    for tool in tools:
        filename = f"{tool}_{excerpt}.json"
        filepath = os.path.join(results_folder, filename)

        if not os.path.exists(filepath):
            print(f" Missing file: {filename}")
            row[tool] = None
            continue

        with open(filepath, 'r') as f:
            content = f.read().strip()
            if not content:
                print(f" Empty file: {filename}")
                row[tool] = None
                continue
            try:
                data_json = json.loads(content)
            except json.JSONDecodeError:
                print(f" Invalid JSON in file: {filename}")
                row[tool] = None
                continue

        # Sum up discrepancies
        total_diff = 0
        for category in data_json:
            if isinstance(data_json[category], dict) and 'discrepancies' in data_json[category]:
                total_diff += data_json[category]['discrepancies']
        row[tool] = total_diff
    data.append(row)

# Convert to DataFrame
df = pd.DataFrame(data)

# Print summary
print("\n=== Mupix Discrepancy Summary ===")
print(df.to_string(index=False))

# Save to CSV
df.to_csv("mupix_summary.csv", index=False)
print("\n Results saved to mupix_summary.csv")




