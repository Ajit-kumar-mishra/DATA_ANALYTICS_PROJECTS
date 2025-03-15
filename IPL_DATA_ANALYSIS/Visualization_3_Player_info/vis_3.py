import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the player data
player_data = pd.read_csv("Player_info_2024_cleaned.csv")

#                     Code for Visualization 1: Decade-wise Player Distribution
'''
# Extract birth year from 'Date of Birth' and group by decade
player_data['Year of Birth'] = pd.to_datetime(player_data['Date of Birth'], errors='coerce').dt.year
player_data['Decade'] = (player_data['Year of Birth'] // 10) * 10

# Count players born in each decade
decade_counts = player_data['Decade'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=decade_counts.index, y=decade_counts.values, palette='viridis')
plt.title('Number of Players Born in Each Decade', fontsize=16)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Number of Players', fontsize=12)

plt.savefig("Visualization_3_Player_info\Players_by_Decade.png")
plt.show()
'''

#                     Code for Visualization 2: Distribution of Players by Role
'''
# Plotting the distribution of players by role
plt.figure(figsize=(12, 6))
sns.countplot(x='Player Role', data=player_data, palette='Set2')
plt.title('Distribution of Players by Role', fontsize=16)
plt.xlabel('Player Role', fontsize=12)
plt.ylabel('Number of Players', fontsize=12)

# Save the plot
plt.savefig("Visualization_3_Player_info\Players_by_Role.png")
plt.show()
'''

#                      Code for Visualization 3: Salary Distribution
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming player_data is already loaded

# Clean 'Player Salary' column
player_data['Player Salary'] = player_data['Player Salary'].str.replace(r'[^\d.]', '', regex=True)
player_data['Player Salary'] = pd.to_numeric(player_data['Player Salary'], errors='coerce')

# Drop rows where salary is NaN (if any) to ensure clean data
player_data = player_data.dropna(subset=['Player Salary'])

# Define salary bins (in crores) and labels
salary_bins = [0, 1, 5, 10, 20, 50, 100]  # These are in crores, adjust as needed
salary_labels = ['0-1 Cr', '1-5 Cr', '5-10 Cr', '10-20 Cr', '20-50 Cr', '50-100 Cr']

# Categorize the salary data into bins
player_data['Salary Range'] = pd.cut(player_data['Player Salary'], bins=salary_bins, labels=salary_labels, right=False)

# Plotting the frequency of players in each salary range
plt.figure(figsize=(12, 6))
sns.countplot(x='Salary Range', data=player_data, palette='viridis')

# Title and labels
plt.title('Distribution of Players by Salary Range', fontsize=16)
plt.xlabel('Salary Range (in Crores)', fontsize=12)
plt.ylabel('Number of Players', fontsize=12)

# Save the plot
plt.savefig(r"Visualization_3_Player_info\Player_Salary_Range_Distribution.png")
plt.show()
'''

#                               Code for Visualization 4: Player Nationality Distribution (Pie Chart)

'''
# Plotting the nationality distribution as a pie chart
nationality_counts = player_data['Player Nationality'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(nationality_counts, labels=nationality_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set3", len(nationality_counts)))
plt.title('Distribution of Players by Nationality', fontsize=16)

# Save the plot
plt.savefig("Visualization_3_Player_info\Players_by_Nationality.png")
plt.show()
'''