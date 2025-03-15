#                         1. Distribution of Age
import pandas as pd 
df = pd.read_csv("HR-Employee-Attrition.csv")
#df = pd.read_csv("HR-Employee-Attrition-Updated.csv")

import matplotlib.pyplot as plt
import seaborn as sns
'''
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], kde=True, bins=15, color='skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig("visualization_3/Distribution_of_Age.png", format='png')
plt.show()
'''
#                       2  Employee Count by Department
'''
department_counts = df['Department'].value_counts()
department_counts.plot(kind='bar', color='coral', figsize=(8, 5))
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)  # Rotate x-axis labels by 45 degrees
plt.savefig("visualization_3/Employee_Count_by_Department.png", format='png')
plt.show()
'''

#                     3. Attrition Rate by Department
'''
plt.figure(figsize=(8, 5))
sns.countplot(x='Department', hue='Attrition', data=df, palette='Set2')
plt.title('Attrition Rate by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.savefig("visualization_3/Attrition_Rate_by_Department.png", format='png')
plt.show()
'''
'''
Yes, in the Attrition column of your dataset, "Yes" typically indicates employees
who have left the company, while "No" represents those who are still with the company.
'''

#                          4. Monthly Income Distribution
'''
plt.figure(figsize=(8, 5))
sns.histplot(df['MonthlyIncome'], bins=30, color='lightgreen')
plt.title('Distribution of Monthly Income')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.savefig("visualization_3/Monthly_Income_Distribution.png", format='png')
plt.show()
'''

#                          5. Job Satisfaction by Attrition

'''
plt.figure(figsize=(8, 5))
sns.barplot(x='Attrition', y='JobSatisfaction', data=df, palette='pastel')
plt.title('Average Job Satisfaction by Attrition (Bar Plot)')
plt.xlabel('Attrition')
plt.ylabel('Average Job Satisfaction')
plt.savefig("visualization_3/Job_Satisfaction_by_Attrition_bar.png", format='png')
plt.show()
'''

#                         6. Marital Status and Attrition
'''
plt.figure(figsize=(8, 5))
sns.countplot(x='MaritalStatus', hue='Attrition', data=df, palette='Blues')
plt.title('Attrition by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.savefig("visualization_3/Marital_Status_and_Attrition.png", format='png')
plt.show()
'''

#                        7. Years at Company Distribution
'''
plt.figure(figsize=(8,5))
sns.histplot(df['YearsAtCompany'],bins = 20,kde = True,color = 'purple')
plt.title('Distribution of Years at Company')
plt.xlabel('Years at company')
plt.ylabel('frequency')
plt.savefig("visualization_3/Years_at_Company_Distribution.png",format = 'png')
plt.show()
'''

#                     8. Work-Life Balance by Attrition
'''
plt.figure(figsize=(8, 5))
sns.boxplot(x='Attrition', y='WorkLifeBalance', data=df, palette='pastel')
plt.title('Work-Life Balance by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Work-Life Balance')
plt.savefig("visualization_3/Work-Life Balance by Attrition.png",format = 'png')
plt.show()
'''
#                     9. Job Role and Monthly Income
'''
plt.figure(figsize=(10, 6))
sns.boxplot(x='JobRole', y='MonthlyIncome', data=df, palette='viridis')
plt.title('Monthly Income by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Monthly Income')
plt.xticks(rotation=45)
plt.savefig("visualization_3/Job_Role_and_Monthly_Income.png",format = 'png')
plt.show()
'''

#                     10. Education Level Distribution
'''
plt.figure(figsize=(8, 5))
sns.countplot(x='Education', data=df, palette='magma')
plt.title('Distribution of Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.savefig("visualization_3/Education_Level_Distribution.png",format = 'png')
plt.show()
'''

#                     11. Attrition Rate by Education Level
'''
plt.figure(figsize=(8, 5))
sns.countplot(x='Education', hue='Attrition', data=df, palette='cool')
plt.title('Attrition Rate by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.savefig("visualization_3/Attrition_Rate_by_Education_Level.png",format = 'png')
plt.show()
'''

#                     12. Income vs. Job Satisfaction
'''
plt.figure(figsize=(8, 5))
sns.scatterplot(x='MonthlyIncome', y='JobSatisfaction', hue='Attrition', data=df, palette='Set1')
plt.title('Monthly Income vs. Job Satisfaction')
plt.xlabel('Monthly Income')
plt.ylabel('Job Satisfaction')
plt.savefig("visualization_3/Income_vs_Job_Satisfaction.png",format = 'png')
plt.show()
'''

#                    13. Years with Current Manager vs. Attrition
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.boxplot([df[df['Attrition'] == 'Yes']['YearsWithCurrManager'], 
             df[df['Attrition'] == 'No']['YearsWithCurrManager']], 
            labels=['Yes', 'No'])
plt.title('Years with Current Manager by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Years with Current Manager')
plt.savefig("visualization_3/Years_with_Current_Manager_vs_Attrition.png",format = 'png')
plt.show()
'''

#                    14. Distance from Home vs. Attrition
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Plot for employees who left
plt.hist(df[df['Attrition'] == 'Yes']['DistanceFromHome'], bins=15, alpha=0.6, color='salmon', label='Yes (Left)')

# Plot for employees who stayed
plt.hist(df[df['Attrition'] == 'No']['DistanceFromHome'], bins=15, alpha=0.6, color='lightblue', label='No (Stayed)')

plt.title('Distance from Home Distribution by Attrition')
plt.xlabel('Distance from Home')
plt.ylabel('Frequency')
plt.legend()
plt.savefig("visualization_3/ Distance from Home_vs_Attrition.png",format = 'png')
plt.show()
'''

#                     15. Performance Rating Distribution
'''
plt.figure(figsize=(8, 5))
performance_counts = df['PerformanceRating'].value_counts()
plt.bar(performance_counts.index, performance_counts.values, color='purple')
plt.title('Distribution of Performance Ratings')
plt.xlabel('Performance Rating')
plt.ylabel('Count')
plt.savefig("visualization_3/Performance_Rating_Distribution.png",format = 'png')
plt.show()


plt.figure(figsize=(8, 5))
sns.countplot(x='PerformanceRating', data=df, palette='viridis')
plt.title('Distribution of Performance Ratings')
plt.xlabel('Performance Rating')
plt.ylabel('Count')
plt.savefig("visualization_3/Performance_Rating_Distribution_1.png",format = 'png')
plt.show()
'''

#                       16. Attrition by Work-Life Balance
'''
plt.figure(figsize=(8, 5))
sns.countplot(x='WorkLifeBalance', hue='Attrition', data=df, palette='YlGnBu')
plt.title('Attrition by Work-Life Balance')
plt.xlabel('Work-Life Balance')
plt.ylabel('Count')
plt.savefig("visualization_3/Attrition_by_Work-Life_Balance.png",format = 'png')
plt.show()
'''

#                      17. Monthly Income by Department
'''
import matplotlib.pyplot as plt

# Calculate the mean Monthly Income for each Department
dept_income = df.groupby('Department')['MonthlyIncome'].mean()

plt.figure(figsize=(10, 6))
dept_income.plot(kind='bar', color='skyblue')
plt.title('Average Monthly Income by Department')
plt.xlabel('Department')
plt.ylabel('Average Monthly Income')
plt.xticks(rotation=45)
plt.savefig("visualization_3/Average_Monthly_Income_by_Department.png", format='png')
plt.show()
'''

#                       18. Total Working Years by Job Role
'''
# Calculate the mean Total Working Years for each Job Role
job_working_years = df.groupby('JobRole')['TotalWorkingYears'].mean()

plt.figure(figsize=(10, 6))
job_working_years.plot(kind='bar', color='lightcoral')
plt.title('Average Total Working Years by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Average Total Working Years')
plt.xticks(rotation=45)
plt.savefig("visualization_3/Average_Total_Working_Years_by_Job_Role.png", format='png')
plt.show()
'''













