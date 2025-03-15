import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
team_performance = pd.read_csv("Team_Performance_cleaned.csv")
#                     1. Match Winner Distribution (Bar Plot)
'''
plt.figure(figsize=(10, 6))
match_winner_count = team_performance['Match_Winner'].value_counts()
sns.barplot(x = match_winner_count.index ,y = match_winner_count.values,palette = "viridis")
plt.title('Distribution of Match Winners', fontsize=16)
plt.xlabel('Team', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.savefig("Visualization_4_Team_Performance/Match_Winner_Distribution.png")
plt.show()
'''

#                         2. Win Type Distribution (Pie Chart)
'''
plt.figure(figsize=(8, 8))
win_type_counts = team_performance['Win_Type'].value_counts()
plt.pie(win_type_counts, labels=win_type_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set3", len(win_type_counts)))
plt.title('Distribution of Win Types', fontsize=16)
plt.savefig("Visualization_4_Team_Performance/Win_Type_Distribution.png")
plt.show()
'''

#                        3. Toss Decision vs Match Winner (Bar Plot)
'''
plt.figure(figsize=(10, 6))
toss_decision_match_winner = team_performance.groupby(['Toss_Decision', 'Match_Winner']).size().unstack()
toss_decision_match_winner.plot(kind='bar', stacked=True, figsize=(10, 6), color=sns.color_palette("Set2"))
plt.title('Toss Decision vs Match Winner', fontsize=16)
plt.xlabel('Toss Decision', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.savefig("Visualization_4_Team_Performance/Toss_Decision_vs_Match_Winner.png")
plt.show()
'''

#                      4. Powerplay Score Distribution (Box Plot)

'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
team_performance = pd.read_csv('Team_Performance_cleaned.csv')

# Step 1: Split the 'Teams' column into two separate columns: 'Team_1' and 'Team_2'
team_performance[['Team_1', 'Team_2']] = team_performance['Teams'].str.split(' vs ', expand=True)

# Step 2: Melt the DataFrame to get 'Team_1' and 'Team_2' in a single column
melted_teams = team_performance.melt(id_vars=['Powerplay_Scores'], 
                                     value_vars=['Team_1', 'Team_2'], 
                                     var_name='Team_Position', 
                                     value_name='Team')

# Step 3: Group by 'Team' and sum the Powerplay scores
team_powerplay_scores = melted_teams.groupby('Team')['Powerplay_Scores'].sum().sort_values(ascending=False)

# Step 4: Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=team_powerplay_scores.index, y=team_powerplay_scores.values, palette="Set1")
plt.title('Total Powerplay Scores by Team', fontsize=16)
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Total Powerplay Scores', fontsize=12)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.savefig("Visualization_4_Team_Performance/Total_Powerplay_Scores_by_Team.png")
plt.show()
'''

#                            5. Match Margin (Histogram)
'''
plt.figure(figsize=(10, 6))
sns.histplot(team_performance['Win_Margin'], bins=15, kde=True, color='blue')
plt.title('Distribution of Match Winning Margin', fontsize=16)
plt.xlabel('Winning Margin (Runs/Wickets)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("Visualization_4_Team_Performance/Match_Margin_Distribution.png")
plt.show()
'''

#                             6. First vs Second Innings Score Comparison (Line Plot)
'''
plt.figure(figsize=(10, 6))
sns.lineplot(data=team_performance[['First_Innings_Score', 'Second_Innings_Score']], dashes=False)
plt.title('First vs Second Innings Score Comparison', fontsize=16)
plt.xlabel('Match Number', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.legend(['First Innings', 'Second Innings'])
plt.savefig("Visualization_4_Team_Performance/First_vs_Second_Innings_Score.png")
plt.show()
'''

#                            7. Top Players by Player of Match Awards (Bar Plot)
'''
plt.figure(figsize=(10, 6))
top_players = team_performance['Player_of_Match'].value_counts().head(10)
sns.barplot(x=top_players.index, y=top_players.values, palette="magma")
plt.title('Top Players by Player of the Match Awards', fontsize=16)
plt.xlabel('Player Name', fontsize=12)
plt.ylabel('Number of Awards', fontsize=12)
plt.xticks(rotation=90)
plt.savefig("Visualization_4_Team_Performance/Top_Players_by_Awards.png")
plt.show()
'''

#                               8. Venue vs Match Winner (Bar Plot)
'''
plt.figure(figsize=(12, 6))
venue_match_winner = team_performance.groupby(['Venue', 'Match_Winner']).size().unstack()
venue_match_winner.plot(kind='bar', stacked=True, figsize=(12, 6), color=sns.color_palette("coolwarm"))
plt.title('Venue vs Match Winner', fontsize=16)
plt.xlabel('Venue', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.xticks(rotation=90)
plt.savefig("Visualization_4_Team_Performance/Venue_vs_Match_Winner.png")
plt.show()
'''
'''
# Group by Venue and Match_Winner to find the count of wins at each venue for each team
venue_match_winner = team_performance.groupby(['Venue', 'Match_Winner']).size().unstack().fillna(0)

# Most Wins at Each Venue
most_wins = venue_match_winner.idxmax(axis=1)  # Team with most wins at each venue
most_wins_count = venue_match_winner.max(axis=1)  # Number of wins for that team

# Most Losses at Each Venue
# Losses will be all matches - wins
venue_match_loser = venue_match_winner.apply(lambda x: x.sum() - x.max(), axis=1)

# Extract teams with most losses at each venue
# If you have more than one team with the same loss count, you can handle it accordingly, here I will just pick the first
most_losses = venue_match_winner.apply(lambda x: x.idxmin(), axis=1)

# Display the results
result_df = pd.DataFrame({
    'Most Wins': most_wins,
    'Wins Count': most_wins_count,
    'Most Losses': most_losses,
    'Losses Count': venue_match_loser
})

# Display the result to confirm
print(result_df)

# Visualization for Most Wins per Venue
plt.figure(figsize=(12, 6))
sns.countplot(data=team_performance, x='Venue', hue='Match_Winner', palette="coolwarm")
plt.title('Most Wins per Venue', fontsize=16)
plt.xlabel('Venue', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()  # To avoid overlap of labels
plt.savefig("Visualization_4_Team_Performance/Most_Wins_Per_Venue.png")
plt.show()

# Visualization for Most Losses per Venue
# Plot a separate bar for losses
plt.figure(figsize=(12, 6))
sns.countplot(data=team_performance, x='Venue', hue='Match_Winner', palette="coolwarm", dodge=True)
plt.title('Most Losses per Venue', fontsize=16)
plt.xlabel('Venue', fontsize=12)
plt.ylabel('Number of Losses', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Visualization_4_Team_Performance/Most_Losses_Per_Venue.png")
plt.show()
'''

