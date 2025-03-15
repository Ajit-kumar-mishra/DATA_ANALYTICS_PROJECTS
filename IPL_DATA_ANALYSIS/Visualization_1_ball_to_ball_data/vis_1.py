import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ball_data_1 = pd.read_csv("IPL_BallByBall_Cleaned.csv", low_memory=False)

#                         Code 1: Distribution of Runs Scored Across Deliveries
'''
# Distribution of Runs Scored Across Deliveries
plt.figure(figsize=(10, 6))  # Set figure size
sns.histplot(ball_data_1['runs_scored'], bins=10, kde=True, color='blue')  # Histogram with KDE curve
plt.title('Distribution of Runs Scored Across Deliveries', fontsize=16)  # Add title
plt.xlabel('Runs Scored', fontsize=12)  # Label for X-axis
plt.ylabel('Frequency', fontsize=12)  # Label for Y-axis
plt.savefig("Visualization_1_ball_to_ball_data/Runs_Distribution.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                       Code 2: Extras Breakdown
'''
# Extras Breakdown (Count of Each Type)
plt.figure(figsize=(12, 6))  # Set figure size
extras_count = ball_data_1['type of extras'].value_counts()  # Count unique values in extras
sns.barplot(x=extras_count.index, y=extras_count.values, palette="muted")  # Bar plot
plt.title('Extras Breakdown', fontsize=16)  # Add title
plt.xlabel('Type of Extras', fontsize=12)  # Label for X-axis
plt.ylabel('Count', fontsize=12)  # Label for Y-axis
plt.savefig("Visualization_1_ball_to_ball_data/Extras_Breakdown.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                      Code 3: Wicket Types Distribution
'''
# Wicket Types Distribution
plt.figure(figsize=(12, 6))  # Set figure size
wicket_types = ball_data_1['wicket_type'].value_counts()  # Count unique wicket types
sns.barplot(x=wicket_types.index, y=wicket_types.values, palette="coolwarm")  # Bar plot
plt.title('Wicket Types Distribution', fontsize=16)  # Add title
plt.xlabel('Wicket Type', fontsize=12)  # Label for X-axis
plt.ylabel('Frequency', fontsize=12)  # Label for Y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.savefig("Visualization_1_ball_to_ball_data/Wicket_Types_Distribution.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                         Code 4: Runs Scored by Innings
'''
# Runs Scored in Each Innings (Average by Year)
plt.figure(figsize=(12, 6))

# Create a year column from the Date column
ball_data_1['Year'] = pd.to_datetime(ball_data_1['Date'], format='%d-%m-%Y').dt.year

# Calculate average runs scored per year for each inning
average_runs = ball_data_1.groupby(['Year', 'Innings No'])['runs_scored'].mean().reset_index()

# Plot
sns.barplot(data=average_runs, x='Year', y='runs_scored', hue='Innings No', palette="viridis")

plt.title('Average Runs Scored by Innings Across Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Runs Scored', fontsize=12)
plt.legend(title="Innings", labels=["1st Innings", "2nd Innings"])
plt.savefig("Visualization_1_ball_to_ball_data/Average_Runs_by_Innings_Year.png")  # Save the plot
plt.show()
'''

#                         Code 5: Number of Deliveries per Bowler
'''
# Number of Deliveries per Bowler
plt.figure(figsize=(12, 6))  # Set figure size
top_bowlers = ball_data_1['Bowler'].value_counts().head(10)  # Top 10 bowlers by deliveries bowled
sns.barplot(x=top_bowlers.index, y=top_bowlers.values, palette="viridis")  # Bar plot
plt.title('Top 10 Bowlers by Number of Deliveries Bowled', fontsize=16)  # Add title
plt.xlabel('Bowler', fontsize=12)  # Label for X-axis
plt.ylabel('Number of Deliveries', fontsize=12)  # Label for Y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig("Visualization_1_ball_to_ball_data/Deliveries_Per_Bowler.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                      Code 6: Runs Comparison Between Striker and Non-Striker
'''
# Runs Comparison Between Striker and Non-Striker
plt.figure(figsize=(10, 6))  # Set figure size
striker_runs = ball_data_1.groupby('Striker')['runs_scored'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=striker_runs.index, y=striker_runs.values, color='orange')  # Bar plot for striker runs
plt.title('Top 10 Strikers by Runs Scored', fontsize=16)  # Add title
plt.xlabel('Striker', fontsize=12)  # Label for X-axis
plt.ylabel('Runs Scored', fontsize=12)  # Label for Y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig("Visualization_1_ball_to_ball_data/Top_Strikers_Runs.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                       Code 7: Extras Contribution by Bowling Team
'''
# Extras Contribution by Bowling Team
plt.figure(figsize=(12, 6))  # Set figure size
team_extras = ball_data_1.groupby('Bowling team')['extras'].sum().sort_values(ascending=False)
sns.barplot(x=team_extras.index, y=team_extras.values, palette="cool")  # Bar plot for extras
plt.title('Extras Conceded by Bowling Teams', fontsize=16)  # Add title
plt.xlabel('Bowling Team', fontsize=12)  # Label for X-axis
plt.ylabel('Total Extras', fontsize=12)  # Label for Y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.savefig("Visualization_1_ball_to_ball_data/Extras_By_Team.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                       Code 8: Balls Faced by Top 10 Batsmen
'''
# Balls Faced by Top 10 Batsmen
plt.figure(figsize=(10, 6))  # Set figure size
top_batsmen = ball_data_1['Striker'].value_counts().head(10)  # Top 10 batsmen by balls faced
sns.barplot(x=top_batsmen.index, y=top_batsmen.values, palette="plasma")  # Bar plot
plt.title('Top 10 Batsmen by Balls Faced', fontsize=16)  # Add title
plt.xlabel('Batsman', fontsize=12)  # Label for X-axis
plt.ylabel('Number of Balls Faced', fontsize=12)  # Label for Y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.savefig("Visualization_1_ball_to_ball_data/Balls_Faced_By_Batsmen.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''

#                     Code 9: Distribution of Total Balls Delivered per Match
'''
# Distribution of Total Balls Delivered per Match
plt.figure(figsize=(10, 6))  # Set figure size
balls_per_match = ball_data_1.groupby('Match id').size()  # Count total balls per match
sns.histplot(balls_per_match, kde=True, color='green', bins=20)  # Histogram with KDE curve
plt.title('Distribution of Total Balls Delivered per Match', fontsize=16)  # Add title
plt.xlabel('Balls Delivered', fontsize=12)  # Label for X-axis
plt.ylabel('Frequency', fontsize=12)  # Label for Y-axis
plt.savefig("Visualization_1_ball_to_ball_data/Balls_Per_Match_Distribution.png")  # Save plot in the specified folder
plt.show()  # Display the plot
'''