import pandas as pd 
                                     # read csv file
'''
df = pd.read_csv("sales.csv")
print(df.to_string())
'''
                                    #  convert csv to excel
'''
df_1 = pd.read_csv("sales.csv")
df_1.to_excel('sales_1.xlsx',index = False)      
'''
                                      # drop duplicates

'''
df = pd.read_csv("sales.csv")
df_1 = df[df.duplicated()]
print(df_1)
df = df.drop_duplicates()
df.to_csv("sales.csv",index= False)
'''
                                         #   Date format 


'''
lambda creates a simple, inline function to transform each date string.
pd.to_datetime() converts the date string to a datetime object, allowing for date manipulations.
strftime() converts the datetime object back to a string in the specified format (here, YYYY/MM/DD).
'''

'''
import pandas as pd
df = pd.read_csv("sales.csv")
# This locates all rows where the 'Date' column has missing values
missing_dates = df[df['Date'].isna()]
print(missing_dates)
df['Date'] = df['Date'].apply(lambda x: pd.to_datetime(x, dayfirst=False).strftime('%Y-%m-%d'))
df.to_csv('sales.csv', index=False)
'''



                                 # remove specifc column based on condition  
'''
df = pd.read_csv('sales.csv')
df = df[df['Date'] != '2024-04-01']   # Remove rows where the date is '2024-04-01'
df.to_csv('sales.csv',index=False)     #Save the updated DataFrame back to the CSV
'''

'''
df = pd.read_csv("sales.csv")                                        # handling negative values
df['Units Sold'] = df['Units Sold'].abs()  # Convert negative 'Units Sold' to positive
df['Sales Amount'] = df['Sales Amount'].abs()  # Convert negative 'Sales Amount' to positive

df.loc[df['Units Sold'] < 1, 'Units Sold'] = 100
df.loc[df['Sales Amount'] < 1, 'Sales Amount'] = 100

df.to_csv("sales.csv",index = False)
'''

'''
df = pd.read_csv("sales.csv")
df = df.dropna(subset = ['Sales','Amount'],how='all')
df.to_csv('cleaned_data.csv',index=False)
'''
                                        # filling missing value from amounts,cold_count

import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('sales.csv')

'''
# Step 1: Fill Units Sold and Sales Amount using mean/median
df['Units Sold'] = df['Units Sold'].fillna(df['Units Sold'].mean().astype(int))
df['Sales Amount'] = df['Sales Amount'].fillna(df['Sales Amount'].mean().astype(int))
df.to_csv('sales.csv',index =False)
'''
                                             # filling missing value for category/and products
'''
Grouping and Mode Calculation: Use df.groupby('Category')['Product'].agg(lambda x: x.mode()[0] if not x.mode().empty else None) 
to group products by category and find the most frequent product (mode) for each category.

Filling Missing Values: Apply df.apply(lambda row: category_mode[row['Category']] 
if pd.isna(row['Product']) else row['Product'], axis=1) to fill missing product values with the mode based on their category.

axis=1: Indicates that the function should be applied to each row.

pd.isna(): Checks if a value is NaN (missing) to decide whether to fill it or keep the existing value.

'''
'''
import pandas as pd

# Load the dataset
df = pd.read_csv('sales.csv')

# Step 1: Group products by category and find the most frequent product (mode) for each category
category_mode = df.groupby('Category')['Product'].agg(lambda x: x.mode()[0] if not x.mode().empty else None)

# Step 2: Fill missing products based on the most frequent product in their category
df['Product'] = df.apply(lambda row: category_mode[row['Category']] if pd.isna(row['Product']) else row['Product'], axis=1)

# Save the updated DataFrame back to the CSV
df.to_csv('sales.csv', index=False)

print("Missing Product values filled based on the most frequent product in each Category.")


import pandas as pd

# Load the dataset
df = pd.read_csv('sales_1.csv')

# Step 1: Group products by category and find the most frequent category for each product
product_mode = df.groupby('Product')['Category'].agg(lambda x: x.mode()[0] if not x.mode().empty else None)

# Step 2: Fill missing categories based on the most frequent category for each product
df['Category'] = df.apply(lambda row: product_mode[row['Product']] if pd.isna(row['Category']) else row['Category'], axis=1)

# Save the updated DataFrame back to the CSV
df.to_csv('sales.csv', index=False)

print("Missing Category values filled based on the most frequent category for each Product.")
'''
#                                 finding any null values after updation  

'''
import pandas as pd

# Load the dataset
df = pd.read_csv('sales.csv')

# After processing (filling missing values as needed)
# ...

# Step 1: Identify rows with any missing values
missing_rows = df[df.isnull().any(axis=1)]

# Step 2: Display the rows with missing values
if not missing_rows.empty:
    print("Rows with missing values:")
    print(missing_rows)
else:
    print("No missing values found in the dataset.")

# Optional: To get a summary of missing values per column
missing_summary = df.isnull().sum()
print("\nSummary of missing values per column:")
print(missing_summary[missing_summary > 0])

'''

import pandas as pd

# Load the Excel file
excel_file = 'sales_1.xlsx'

# Read the data into a DataFrame
df = pd.read_excel(excel_file)

# Save the DataFrame to a CSV file
csv_file = 'sales_raw.csv'
df.to_csv(csv_file, index=False)

print(f"Excel file '{excel_file}' has been converted to CSV as '{csv_file}'.")

