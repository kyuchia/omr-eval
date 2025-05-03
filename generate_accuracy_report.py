###############-------generate_accuracy_report.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Define input and output paths
eval_folder = "./evaluation"
os.makedirs(eval_folder, exist_ok=True)
csv_path = os.path.join(eval_folder, "omr_category_summary.csv")

# Load data
df = pd.read_csv(csv_path)

tools = ["newzik", "photoscore", "playscore2", "soundslice"]
categories = ['Notes', 'Rests', 'TimeSignatures', 'KeySignatures', 'Clefs', 'Spanners', 'Dynamics']
colors = ['#1f77b4', '#d62728', '#2ca02c', '#9467bd']

summary_data = []
total_accuracy_summary = {}

for tool in tools:
    tool_total_right = 0
    tool_total_wrong = 0
    for category in categories:
        right_col = f"{tool}_{category}_right"
        wrong_col = f"{tool}_{category}_wrong"
        if right_col in df.columns and wrong_col in df.columns:
            right = df[right_col].fillna(0).sum()
            wrong = df[wrong_col].fillna(0).sum()
            total = right + wrong
            accuracy = right / total if total > 0 else 0
            summary_data.append({
                "Tool": tool,
                "Category": category,
                "Right": right,
                "Wrong": wrong,
                "Total": total,
                "Accuracy": accuracy
            })
            tool_total_right += right
            tool_total_wrong += wrong
    total = tool_total_right + tool_total_wrong
    total_accuracy_summary[tool] = {
        "Total Right": tool_total_right,
        "Total Wrong": tool_total_wrong,
        "Total Accuracy": tool_total_right / total if total > 0 else 0
    }

category_accuracy_df = pd.DataFrame(summary_data)

# Plot 1: Accuracy by Category and Tool
plt.figure(figsize=(12, 6))
for i, tool in enumerate(tools):
    tool_data = category_accuracy_df[category_accuracy_df["Tool"] == tool]
    plt.plot(tool_data["Category"], tool_data["Accuracy"], label=tool, marker='o', color=colors[i])
plt.title("OMR Accuracy by Category and Tool", fontsize=18)
plt.ylabel("Accuracy", fontsize=14)
plt.xlabel("Category", fontsize=14)
plt.ylim(0, 1.05)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(eval_folder, "accuracy_by_category_tool.png"))
plt.close()

# Plot 2: Total Accuracy per Tool
accuracy_df = pd.DataFrame.from_dict(
    {tool: summary["Total Accuracy"] for tool, summary in total_accuracy_summary.items()},
    orient='index', columns=['Total Accuracy']
).sort_values(by='Total Accuracy', ascending=False)

plt.figure(figsize=(8, 6))
bars = plt.bar(accuracy_df.index, accuracy_df['Total Accuracy'], color=colors)
plt.title("Total Accuracy per Tool", fontsize=16)
plt.ylabel("Accuracy", fontsize=14)
plt.ylim(0, 1)
plt.grid(axis='y')
plt.xticks(rotation=45, fontsize=13)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(eval_folder, "total_accuracy_per_tool.png"))
plt.close()

# Export CSV
category_accuracy_df.to_csv(os.path.join(eval_folder, "category_accuracy_summary.csv"), index=False)

print("Plots and summary saved in ./evaluation/")
