import pandas as pd 
#df = pd.read_csv("HR-Employee-Attrition.csv")
#df = pd.read_csv("HR-Employee-Attrition-Updated.csv")
df = pd.read_csv("HR-Employee-Attrition-Updated_1.csv")
#print(df.head()) 

#                    1.  dropna                    #
'''
# 1. dropna(): Removes rows with any missing values.
df.dropna(inplace = True)

df.dropna(subset=['Department'], inplace=True)  # Drops rows where 'Column_Name' has NaN

df.dropna(axis=1, inplace=True)  # Drops columns with any NaN values
'''
#                    2.  fillna /bfill/ffill                   #
'''
df.fillna(0, inplace=True)  #  fillna(): Replaces missing values with a specified value (e.g., 0).

# 4. bfill()/ffill(): Fills missing values by propagating the next or previous value.
df.bfill(inplace=True)  # Backward fill
df.ffill(inplace=True)  # Forward fill
'''

#                    3.  interpolate                   #

'''
df.interpolate(method='linear', inplace=True)   # linear interpolation

df.interpolate(method='polynomial', order=2, inplace=True)  # Quadratic interpolation
'''
'''

Linear interpolation assumes that the missing value lies on a straight line
between two known data points. This method is simple and works best when the 
data is generally linear (i.e., follows a straight-line pattern between points).

Polynomial interpolation fits a polynomial curve through known data points 
and uses that curve to estimate missing values. This method is 
more complex and can capture non-linear trends.

'''

#                    4.  Filtering and Subsetting Data                   #
'''
filtered_df = df.query("Age > 30 and Department == 'Sales'")  # query(): Filters data based on conditions.
print(filtered_df.to_string())

subset_df = df.loc[df['EnvironmentSatisfaction'] > 3, ['EmployeeNumber', 'EnvironmentSatisfaction']]
print(subset_df)
# Selects rows with 'JobSatisfaction' greater than 3, showing only 'EmployeeNumber' and 'JobSatisfaction' columns.

subset_df1 = df.iloc[0:5, 0:3]
print(subset_df1)
# Selects the first 5 rows and the first 3 columns based on their positions.

filtered_df1 = df[df['Department'].isin(['Sales', 'HR'])]
print(filtered_df1)
# Filters rows where 'Department' is either 'Sales' or 'HR'.

filtered_df2 = df[df['MonthlyIncome'].between(3000, 6000)]
print(filtered_df2)
# Filters rows where 'MonthlyIncome' is between 3000 and 6000, inclusive.

df_dropped = df.drop(columns=['abhckbkbk'])
# Removes the column 'EmployeeCount' from the DataFrame.
'''

#                    5. Cleaning Data Types                  #
'''
df['Age'] = df['Age'].astype(int)
# Converts the 'Age' column to integer data type

# Remove any leading or trailing spaces in the 'Department' column, if they exist
df['Department'] = df['Department'].str.strip()
df['Department'] = df['Department'].replace({'Sales': 'Sales & Marketing'})
df['Department'] = df['Department'].replace({'Sales & Marketing': 'Sales'})
# Save the updated DataFrame to a new CSV file (you can use the same filename if you want to overwrite)
df.to_csv("HR-Employee-Attrition.csv", index=False)
'''

#                    6. Renaming and Formatting                  #
'''
df.rename(columns={'EmployeeNumber': 'Emp_ID'}, inplace=True)
# Renames the 'EmployeeNumber' column to 'Emp_ID'.

df['Department'] = df['Department'].str.strip()
# Removes extra spaces around text in the 'Department' column.

df['Department'] = df['Department'].str.upper()
# Converts all text in the 'Department' column to uppercase

df['Department'] = df['Department'].str.lower()
# Converts all text in the 'Department' column to lowercase.

df.to_csv("HR-Employee-Attrition.csv", index=False)   # if u want to save changes run this along with query which u want to perform 
'''

#                    7. Handling Duplicates                  #
'''
duplicates = df.duplicated()
print(duplicates)

df_unique = df.drop_duplicates(subset=['EmployeeNumber'])
print(df_unique)
# Removes duplicate rows based on the 'EmployeeNumber' column.
'''

#                    8. Custom Function Application                 #
'''
df['Age_Group'] = df['Age'].apply(lambda x: 'Senior' if x > 50 else 'Junior')
# Creates a new column 'Age_Group' where 'Age' > 50 is labeled 'Senior,' otherwise 'Junior'.

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Gender'] = df['Gender'].map({ 0: 'Male',1:'Female'})
# Maps 'Male' to 0 and 'Female' to 1 in the 'Gender' column.

#df.to_csv("HR-Employee-Attrition.csv", index=False)  if u want to save changes then run this code along with query 
'''

#                    9. Handling Outliers                #
'''
df['MonthlyIncome'] = df['MonthlyIncome'].clip(lower=3000, upper=15000)
# Caps 'MonthlyIncome' values below 3000 to 3000 and above 15000 to 15000.

# Create a temporary view with the clipped 'MonthlyIncome' column
temp_income = df['MonthlyIncome'].clip(lower=3000, upper=15000)

# Display EmployeeNumber and the clipped MonthlyIncome
print(df[['EmployeeNumber']].assign(ClippedMonthlyIncome=temp_income).head(10))
'''
'''
Any value in MonthlyIncome below 3000 is set to 3000.
Any value in MonthlyIncome above 15000 is set to 15000.
'''




#                    10. encoding                   #
'''
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load the dataset
df = pd.read_csv("HR-Employee-Attrition.csv")

# Initialize label encoder
label_encoder = LabelEncoder()

# Label encoding for binary categorical columns (create new columns without deleting originals)
df['Gender_encoded'] = label_encoder.fit_transform(df['Gender'])
df['OverTime_encoded'] = label_encoder.fit_transform(df['OverTime'])
print(df[['Gender', 'Gender_encoded', 'OverTime', 'OverTime_encoded']].head())

# One-hot encoding for other categorical columns, keeping original columns
columns_to_encode = ['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'MaritalStatus']

# Generate one-hot encoded columns for specified columns
encoded_df = pd.get_dummies(df[columns_to_encode], prefix=['BT', 'Dept', 'Edu', 'Job', 'Marital'])

# Concatenate the new encoded columns with the original DataFrame
df = pd.concat([df, encoded_df], axis=1)

# Convert any boolean columns to integers explicitly
df[encoded_df.columns] = df[encoded_df.columns].astype(int)

from sklearn.preprocessing import LabelEncoder

# Encoding the OverTime column
label_encoder = LabelEncoder()
df['OverTime_encoded'] = label_encoder.fit_transform(df['OverTime'])

# Save DataFrame to CSV
df.to_csv("HR-Employee-Attrition-Updated.csv", index=False)

# Check the dataset after encoding
print(df.head())
'''


'''
import pandas as pd
from sklearn.preprocessing import StandardScaler


# 1. Convert Attrition to a binary column, while keeping the original
df['Attrition_Binary'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# 2. Scale numerical features, keeping both original and scaled versions
numerical_cols = ['MonthlyIncome', 'DailyRate', 'DistanceFromHome', 'YearsAtCompany', 
                  'TotalWorkingYears', 'YearsWithCurrManager', 'YearsSinceLastPromotion']
scaler = StandardScaler()

# Create scaled versions of the numerical columns with a suffix
scaled_cols = [col + '_Scaled' for col in numerical_cols]
df[scaled_cols] = scaler.fit_transform(df[numerical_cols])

# 3. Create TenureOutsideCompany, representing experience outside the current company
df['TenureOutsideCompany'] = df['TotalWorkingYears'] - df['YearsAtCompany']
df['TenureOutsideCompany'] = df['TenureOutsideCompany'].apply(lambda x: max(0, x))  # Ensure no negative values

# 4. Add a flag for employees with long time since last promotion, retain original
df['LongTimeSinceLastPromotion'] = df['YearsSinceLastPromotion'].apply(lambda x: 1 if x > 5 else 0)

# 5. Create an interaction feature between OverTime and Attrition
df['OverTime_Attrition'] = df['OverTime_encoded'] * df['Attrition_Binary']

# 6. Create an age group column without modifying original Age column
df['Age_Group_Binned'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 60], 
                                labels=['Junior', 'Mid-Level', 'Senior', 'Veteran'])

# 7. Check for target variable imbalance (just prints, no modification)
attrition_counts = df['Attrition_Binary'].value_counts(normalize=True)
print("Attrition Class Distribution:\n", attrition_counts)

# Save updated DataFrame
df.to_csv("HR-Employee-Attrition-Updated.csv", index=False)

# Display the first few rows to verify changes
print(df.head())
'''


'''
import pandas as pd

pd.set_option('display.max_rows', None)  # This will display all rows
pd.set_option('display.max_columns', None)  # This will display all columns

# Now print the null value summary
print(df.isnull().sum())
'''

'''
# Check for age values outside the bin range
print(df[df['Age'] < 18])  # Ages less than 18
print(df[df['Age'] > 60])  # Ages greater than 60
'''

'''
df['Age'] = df['Age'].fillna(df['Age'].median())  # Replace missing Age with the median
# Re-run the binning of the 'Age' column to categorize into groups
df['Age_Group_Binned'] = pd.cut(df['Age'], bins=[17, 25, 35, 45, 61],
                                labels=['Junior', 'Mid-Level', 'Senior', 'Veteran'])
df.to_csv("HR-Employee-Attrition-Updated.csv", index=False)
'''

'''
# Check for rows with NaN in 'Age_Group_Binned'
missing_age_group_rows = df[df['Age_Group_Binned'].isna()]

# Display the rows with missing Age_Group_Binned
print(missing_age_group_rows)
'''
'''
# Drop unnecessary columns
df_cleaned = df.drop(columns=[
    'EmployeeCount',            # Identifier column, won't contribute to prediction
    'EmployeeNumber',           # Identifier column, won't contribute to prediction
    'Over18',                   # Constant value column, doesn't vary
    'StandardHours',            # Constant value column, doesn't vary
    'Gender',                   # Already encoded as Gender_encoded
    'OverTime',                 # Already encoded as OverTime_encoded
    'Attrition',                # Target column should not be in X features
    'Age_Group',                # Categorical column already processed
    'Age_Group_Binned',         # Categorical column already processed
    'TenureOutsideCompany',     # This might be redundant if 'TotalWorkingYears' is used
    'LongTimeSinceLastPromotion' # If this is derived from other features
])
df_cleaned.to_csv("HR-Employee-Attrition-Updated_1.csv", index=False)
# Check cleaned dataframe columns
print(df_cleaned.columns)
# Save the cleaned dataframe to a new CSV file
'''

# Drop text-based columns (columns that are categorical and not encoded yet)
df_cleaned = df.drop(columns=[
    'BusinessTravel',  # Text column, needs encoding
    'Department',      # Text column, needs encoding
    'Education',       # Text column, needs encoding
    'EducationField',  # Text column, needs encoding
    'JobRole',         # Text column, needs encoding
    'MaritalStatus',   # Text column, needs encoding
])

# Save the cleaned dataframe
df_cleaned.to_csv("HR-Employee-Attrition-Updated_1.csv", index=False)


