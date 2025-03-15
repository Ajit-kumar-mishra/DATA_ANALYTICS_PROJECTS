# Import required libraries
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
team_info = pd.read_csv("IPL_Team_2024_Cleaned.csv")

# Create folder if it doesn't exist
folder_name = "Visualization_2_IPL_Team_2024"
os.makedirs(folder_name, exist_ok=True)

# Clean and process data for visualization
team_info['Number of IPL Titles'] = team_info['Number of IPL Titles'].str.extract(r'(\d+)').astype(int)

# Plot data
plt.figure(figsize=(12, 6))
sns.barplot(data=team_info, x='Team Full Name', y='Number of IPL Titles', palette='viridis')
plt.title('Number of IPL Titles by Team', fontsize=16)
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save plot
plt.savefig(os.path.join(folder_name, "IPL_Titles_per_Team.png"))

# Show plot
plt.show()
