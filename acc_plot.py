# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the processed dataframe
# csv_path = "/mnt/data/omr_category_summary.csv"
# df = pd.read_csv(csv_path)

# # Define tools and categories
# tools = ["newzik", "photoscore", "playscore2", "soundslice"]
# categories = ['Notes', 'Rests', 'TimeSignatures', 'KeySignatures', 'Clefs', 'Spanners', 'Dynamics']

# # Prepare summary data
# summary_data = []
# total_accuracy_summary = {}

# for tool in tools:
#     tool_total_right = 0
#     tool_total_wrong = 0
#     for category in categories:
#         right_col = f"{tool}_{category}_right"
#         wrong_col = f"{tool}_{category}_wrong"
#         if right_col in df.columns and wrong_col in df.columns:
#             right = df[right_col].fillna(0).sum()
#             wrong = df[wrong_col].fillna(0).sum()
#             total = right + wrong
#             accuracy = right / total if total > 0 else 0
#             summary_data.append({
#                 "Tool": tool,
#                 "Category": category,
#                 "Right": right,
#                 "Wrong": wrong,
#                 "Total": total,
#                 "Accuracy": accuracy
#             })
#             tool_total_right += right
#             tool_total_wrong += wrong
#     total = tool_total_right + tool_total_wrong
#     total_accuracy_summary[tool] = {
#         "Total Right": tool_total_right,
#         "Total Wrong": tool_total_wrong,
#         "Total Accuracy": tool_total_right / total if total > 0 else 0
#     }

# # Create summary DataFrame
# category_accuracy_df = pd.DataFrame(summary_data)

# # Plot accuracy per category
# plt.figure(figsize=(12, 6))
# colors = ['#1f77b4', '#d62728', '#2ca02c', '#9467bd']  # distinct colors
# for i, tool in enumerate(tools):
#     tool_data = category_accuracy_df[category_accuracy_df["Tool"] == tool]
#     plt.plot(tool_data["Category"], tool_data["Accuracy"], label=tool, marker='o', color=colors[i])
# plt.title("OMR Accuracy by Category and Tool")
# plt.ylabel("Accuracy")
# plt.xlabel("Category")
# plt.ylim(0, 1.05)
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Create and show combined accuracy table
# total_accuracy_df = pd.DataFrame.from_dict(total_accuracy_summary, orient='index')
# combined_df = category_accuracy_df.pivot(index='Category', columns='Tool', values='Accuracy')
# combined_df.loc['Total Accuracy'] = total_accuracy_df['Total Accuracy']
# import ace_tools as tools; tools.display_dataframe_to_user(name="OMR Accuracy by Category and Tool", dataframe=combined_df.round(4))
