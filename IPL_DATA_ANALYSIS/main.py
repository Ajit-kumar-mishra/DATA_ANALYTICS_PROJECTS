import pandas as pd
import numpy as np
#                     IPL_BallByBall2008_2024(Updated)      
'''
ball_data = pd.read_csv("IPL_DATASET_2008_24/IPL_BallByBall2008_2024(Updated).csv", low_memory=False)

#print(ball_data.head())

print(ball_data.isnull().sum())

# Replace missing values based on column context
ball_data['type of extras'].fillna("None", inplace=True)
ball_data['wicket_type'].fillna("Not Out", inplace=True)
ball_data['fielders_involved'].fillna("None", inplace=True)
ball_data['Player Out'].fillna("None", inplace=True)

# Drop duplicate rows, if any
ball_data.drop_duplicates(inplace=True)

# Save the cleaned DataFrame to a new CSV file
ball_data.to_csv("IPL_BallByBall_Cleaned.csv", index=False)
'''

'''
ball_data_1 = pd.read_csv("IPL_BallByBall_Cleaned.csv", low_memory=False)

print(ball_data_1.isnull().sum())
ball_data_1.drop_duplicates(inplace=True)
print(ball_data_1.dtypes)
'''

#                           ipl_teams_2024_info
'''
team_info = pd.read_csv("IPL_DATASET_2008_24/ipl_teams_2024_info.csv")
print(team_info.head())

# Check for missing values
print(team_info.isnull().sum())

team_info.to_csv("IPL_Team_2024_Cleaned.csv",index = False)
'''

#                           Players_Info_2024
'''
player_data = pd.read_csv("IPL_DATASET_2008_24/Players_Info_2024.csv")
#print(player_data.head())

print(player_data.isnull().sum())
missing_dob = player_data[player_data['Date of Birth'].isnull()]
#print(missing_dob)

# Assuming 'player_data_cleaned' is your dataframe with missing data already handled
player_data.loc[player_data['Player Name'] == 'Jake Fraser-McGurk', 'Date of Birth'] = '11-Apr-2002'

# Verify if the date was updated correctly
print(player_data[player_data['Player Name'] == 'Jake Fraser-McGurk'])

player_data.to_csv("Player_info_2024_cleaned.csv",index = False)
'''

'''
player_data_1 = pd.read_csv("Player_info_2024_cleaned.csv")
print(player_data_1.head())

player_data_1['Date of Birth'] = pd.to_datetime(player_data_1['Date of Birth'], errors='coerce')

player_data_1['IPL Debut'].fillna("Not Available", inplace=True)
player_data_1.to_csv("Player_info_2024_cleaned.csv",index = False)

print(player_data_1.isnull().sum())
'''

#                           team_performance_dataset_2008to2024
'''
match_data = pd.read_csv("IPL_DATASET_2008_24/team_performance_dataset_2008to2024.csv")
print(match_data.head())

print(match_data.isnull().sum())

# Fill columns with specific placeholders
match_data['Win_Type'].fillna('Not Available', inplace=True)
match_data['Win_Margin'].fillna(0, inplace=True)
match_data['Second_Innings_Score'].fillna(0, inplace=True)
match_data['Player_of_Match'].fillna('Not Assigned', inplace=True)

# Drop rows where Match_ID or Date is missing
match_data.dropna(subset=['Match_ID', 'Date'], inplace=True)

match_data.to_csv("Team_Performance_cleaned.csv",index = False)
'''

'''
match_data_1 = pd.read_csv("Team_Performance_cleaned.csv")
# Verify that no missing values remain
print(match_data_1.isnull().sum())
'''