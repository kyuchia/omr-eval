###############-------evaluate_omr_performance.py

import json
import os
import pandas as pd

# Paths
results_folder = './mupix_results'
output_folder = './evaluation'
os.makedirs(output_folder, exist_ok=True)

# Predefined export paths
summary_csv = os.path.join(output_folder, "omr_category_summary.csv")
skipped_csv = os.path.join(output_folder, "omr_skipped_files.csv")

# List of tools and excerpts
tools = ["newzik", "photoscore", "playscore2", "soundslice"]
excerpts = [f"excerpt{str(i).zfill(2)}" for i in range(1, 11)]

# Containers for data
data = []
all_categories = set()
skipped_entries = []

for excerpt in excerpts:
    row = {"Excerpt": excerpt}
    for tool in tools:
        filename = f"{tool}_{excerpt}.json"
        filepath = os.path.join(results_folder, filename)

        # File missing
        if not os.path.exists(filepath):
            msg = f"{tool}_{excerpt} → Missing file"
            print("⚠️", msg)
            skipped_entries.append({"Tool": tool, "Excerpt": excerpt, "Reason": "Missing file"})
            row[tool] = None
            continue

        # File present, try reading JSON
        with open(filepath, 'r') as f:
            try:
                data_json = json.load(f)
            except json.JSONDecodeError:
                msg = f"{tool}_{excerpt} → Invalid JSON"
                print("⚠️", msg)
                skipped_entries.append({"Tool": tool, "Excerpt": excerpt, "Reason": "Invalid JSON"})
                row[tool] = None
                continue

        tool_total_wrong = 0

        for category, entries in data_json.items():
            if isinstance(entries, list):
                wrong = sum(entry.get('wrong', 0) for entry in entries)
                right = sum(entry.get('right', 0) for entry in entries)
                row[f"{tool}_{category}_wrong"] = wrong
                row[f"{tool}_{category}_right"] = right
                tool_total_wrong += wrong
                all_categories.add(category)

        row[tool] = tool_total_wrong
    data.append(row)

# Create summary DataFrame
df = pd.DataFrame(data)

# Output to terminal
print("\n=== OMR Discrepancy Summary by Tool and Category ===")
print(df.to_string(index=False))

# Save to CSV
df.to_csv(summary_csv, index=False)
print(f"\nResults saved to {summary_csv}")

# Save skipped entries to CSV
if skipped_entries:
    skipped_df = pd.DataFrame(skipped_entries)
    skipped_df.to_csv(skipped_csv, index=False)
    print(f"Skipped file log saved to {skipped_csv}")
else:
    print("No skipped or invalid files.")
