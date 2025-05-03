#####------------- mupix_evaluation_tracker.py

import pandas as pd

# Create a list of excerpts and tools
excerpts = [f"excerpt{str(i).zfill(2)}" for i in range(1, 2)] #1, 11
tools = ["soundslice", "newzik", "photoscore", "playscore2"]

# Create a DataFrame to track comparisons
data = []
for tool in tools:
    for ex in excerpts:
        row = {
            "Tool": tool,
            "Excerpt": ex,
            "Ground Truth Path": f"./ground_truth/{ex}.xml",
            "OMR Output Path": f"./omr_outputs/{tool}/{ex}.xml",
            "Mupix Result Path": f"./mupix_results/{tool.lower()}_{ex}.json",
            "Command": f"mupix -pT compare ./ground_truth/{ex}.xml ./omr_outputs/{tool}/{ex}.xml > ./mupix_results/{tool.lower()}_{ex}.json"
        }
        data.append(row)

df = pd.DataFrame(data)

# Export to CSV instead of Excel
csv_path = "mupix_evaluation_tracker.csv"
df.to_csv(csv_path, index=False)

print(f"Saved tracker to: {csv_path}")

