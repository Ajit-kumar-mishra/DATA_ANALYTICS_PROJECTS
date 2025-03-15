import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import text

# Define your database credentials

# Define your database credentials
user = 'postgres'
password = 'ajit12345'
host = 'localhost'
port = '5432'
database = 'CustomerAnalyticsDB '

# Create the connection string
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"

# Connect to the database using SQLAlchemy
engine = create_engine(connection_string)

# Define the table names
tables = ['customers_table', 'orders_table', 'products_table', 'orderdetails_table', 'reviews_table']

# Read each table into a DataFrame
dataframes = {}
for table in tables:
    dataframes[table] = pd.read_sql(f"SELECT * FROM {table}", engine)

# Access each DataFrame by table name
customers_df = dataframes['customers_table']
orders_df = dataframes['orders_table']
products_df = dataframes['products_table']
orderdetails_df = dataframes['orderdetails_table']
reviews_df = dataframes['reviews_table']

# Now you can work with the DataFrames as needed
#print(customers_df.head())  # Shows the first 5 rows of the customers_table DataFrame
'''
print(customers_df.head())
print(orders_df.head())
print(products_df.head())
print(orderdetails_df.head())
print(reviews_df.head())
'''

'''
# Save each DataFrame to a CSV file
customers_df.to_csv('customers_table.csv', index=False)
orders_df.to_csv('orders_table.csv', index=False)
products_df.to_csv('products_table.csv', index=False)
orderdetails_df.to_csv('orderdetails_table.csv', index=False)
reviews_df.to_csv('reviews_table.csv', index=False)
'''
def execute_query(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return pd.DataFrame(result.fetchall(), columns=result.keys())
'''
# Example SQL query to count male customers
query = "SELECT COUNT(*) FROM customers_table WHERE gender = 'Male';"
male_count = execute_query(query)
print(male_count)
'''

'''
query = "select product_name,category from products_table where category = 'Electronics'"
x = execute_query(query)
print(x)
'''

'''
query = """
SELECT 
    customers_table.customer_id,
    customers_table.first_name,
    customers_table.last_name,
    products_table.product_id,
    products_table.product_name
FROM 
    customers_table
JOIN 
    orders_table ON customers_table.customer_id = orders_table.customer_id
JOIN 
    orderdetails_table ON orders_table.order_id = orderdetails_table.order_id
JOIN 
    products_table ON orderdetails_table.product_id = products_table.product_id
ORDER BY 
    customers_table.customer_id, products_table.product_id;
"""
x = execute_query(query)
print(x.to_string())
'''

                     ###########  cleaning data with pandas     ###########

'''
# Handling Missing Values
customers_df.dropna(inplace=True)  # Remove rows with missing values
# Remove duplicates
customers_df.drop_duplicates(inplace=True)
# Renaming columns (if needed)
#customers_df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)



# Fill missing values without using inplace=True
customers_df['age'] = customers_df['age'].fillna(customers_df['age'].median())  # Replace NaN with median age
customers_df['area'] = customers_df['area'].fillna('Unknown')  # Fill missing cities with 'Unknown'

# Fill missing values using forward fill
customers_df.ffill(inplace=True)  # Forward fill

# Fill missing values using backward fill
customers_df.bfill(inplace=True)  # Backward fill
'''

'''
customers_df['join_date'] = pd.to_datetime(customers_df['join_date'])  # Convert to datetime
customers_df['customer_id'] = customers_df['customer_id'].astype(int)  # Ensure customer_id is int
customers_df['email'] = customers_df['email'].str.strip()
# Example to check for valid email format
import re


customers_df.drop(columns=['unnecessary_column'], inplace=True, errors='ignore')
customers_df.drop_duplicates(subset=['email'], inplace=True)  # Keep unique emails
customers_df['age_category'] = pd.cut(customers_df['age'], bins=[0, 18, 35, 60, 100], labels=['Teen', 'Young Adult', 'Adult', 'Senior'])
'''
'''
#customers_df.rename(columns={'first_name': 'FirstName', 'last_name': 'LastName'},inplace=True)
customers_df.rename(columns={'FirstName':'first_name','LastName': 'last_name'},inplace=True)
'''
# Save cleaned DataFrame to CSV
#customers_df.to_csv('customers_table.csv', index=False)

                            #### Matplotlib  ###

import matplotlib.pyplot as plt
'''
# Histogram for age distribution
plt.figure(figsize=(8, 6))
plt.hist(customers_df['age'], bins=15, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.title('Age Distribution of Customers')
plt.savefig('age_distribution.png', format='png', dpi=300)
plt.show()


# Bar chart for gender distribution
gender_counts = customers_df['gender'].value_counts()

plt.figure(figsize=(6, 6))
gender_counts.plot(kind='bar', color=['lightblue', 'salmon'])
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.title('Gender Distribution of Customers')
plt.savefig('Gender_Distribution_of_Customers.png', format='png', dpi=300)
plt.show()


# Assuming 'category' column exists in products_table and is linked via orderdetails_table
sales_by_category = orderdetails_df.merge(products_df, on='product_id').groupby('category')['quantity'].sum()

# Bar chart for sales by category
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar', color='orange')
plt.xlabel('Product Category')
plt.ylabel('Total Quantity Sold')
plt.title('Sales by Product Category')
plt.xticks(rotation=45)
plt.savefig('Sales by Product Category.png', format='png', dpi=300)
plt.show()


# Number of orders per customer
orders_per_customer = orders_df['customer_id'].value_counts()

# Histogram for customer order frequency
plt.figure(figsize=(8, 6))
plt.hist(orders_per_customer, bins=20, color='lightcoral', edgecolor='black')
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.title('Distribution of Orders per Customer')
plt.savefig('Distribution of Orders per Customer.png', format='png', dpi=300)
plt.show()


# Histogram for rating distribution
plt.figure(figsize=(8, 6))
plt.hist(reviews_df['rating'], bins=5, color='gold', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.title('Distribution of Product Ratings')
plt.savefig('Distribution of Product Ratings.png', format='png', dpi=300)
plt.show()

'''
'''
import matplotlib.pyplot as plt

# Merge customers and orders data to include customer gender in the analysis
customer_orders = orders_df.merge(customers_df[['customer_id', 'gender']], on='customer_id')

# Count the number of orders placed by each gender
gender_purchase_count = customer_orders.groupby('gender').size()

# Plot a bar chart to show purchase count by gender
plt.figure(figsize=(8, 6))
gender_purchase_count.plot(kind='bar', color=['lightblue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Number of Products Purchased')
plt.title('Product Purchases by Gender')
plt.xticks(rotation=0)
plt.savefig('Purchases_by_Gender.png', format='png', dpi=300)
plt.show()


import matplotlib.pyplot as plt

# Merge customers and orders data to include customer gender in the analysis
customer_orders = orders_df.merge(customers_df[['customer_id', 'state_name']], on='customer_id')

# Count the number of orders placed by each gender
gender_purchase_count = customer_orders.groupby('state_name').size().sort_values(ascending=False).head(5)

# Plot a bar chart to show purchase count by gender
plt.figure(figsize=(8, 6))
gender_purchase_count.plot(kind='bar', color=['lightblue', 'pink'])
plt.xlabel('stae_name')
plt.ylabel('Number of Products Purchased')
plt.title('Product Purchases by state')
plt.xticks(rotation=0)
plt.savefig('Purchases_by_state.png', format='png', dpi=300)
plt.show()


# Assuming there's a 'quantity' column in products_df that indicates product stock
products_by_category_count = products_df.groupby('category')['product_name'].size().sort_values(ascending=False)
#products_by_category = products_df.groupby('category').size().sort_values(ascending=False)
# Plotting the total quantity by category
plt.figure(figsize=(10, 6))
products_by_category_count.plot(kind='bar', color='lightcoral')
plt.xlabel('Product Category')
plt.ylabel('Total Quantity of Products')
plt.title('Total Quantity by Product Category')
plt.xticks(rotation=45)
plt.savefig('Total_Quantity_by_Category.png', format='png', dpi=300)
plt.show()


# Ensure there's a 'price' column in the products_df DataFrame
# Sorting the products by price
most_expensive = products_df.nlargest(5, 'price')  # Change 'price' to your actual column name for price
least_expensive = products_df.nsmallest(5, 'price')  # Change 'price' to your actual column name for price

# Display the most and least expensive products
print("Most Expensive Products:")
print(most_expensive[['product_name', 'price']])  # Adjust if there are additional columns of interest

print("\nLeast Expensive Products:")
print(least_expensive[['product_name', 'price']])  # Adjust if there are additional columns of interest
'''
'''
import pandas as pd
import matplotlib.pyplot as plt

# Get the most expensive products
most_expensive = products_df.nlargest(5, 'price')[['product_name', 'price']]

# Get the least expensive products
least_expensive = products_df.nsmallest(5, 'price')[['product_name', 'price']]

# Combine the two DataFrames
combined_df = pd.concat([most_expensive, least_expensive])

# Resetting index for better plotting
combined_df.reset_index(drop=True, inplace=True)

# Plotting the combined data
plt.figure(figsize=(12, 6))
plt.bar(combined_df['product_name'], combined_df['price'], color=['gold'] * 5 + ['lightblue'] * 5)
plt.title('Most and Least Expensive Products')
plt.xlabel('Product Name')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Save the plot as a PNG file
plt.savefig('Most_and_Least_Expensive_Products.png', format='png', dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Get the least expensive products (top 5)
least_expensive = products_df.nsmallest(5, 'price')[['product_name', 'price']]

# Plotting the least expensive products
plt.figure(figsize=(12, 6))
plt.bar(least_expensive['product_name'], least_expensive['price'], color='lightblue')

# Adding labels and title
plt.title('Least Expensive Products')
plt.xlabel('Product Name')
plt.ylabel('Price')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adding grid lines for better readability
plt.grid(axis='y')

# Save the plot as a PNG file
plt.savefig('Least_Expensive_Products.png', format='png', dpi=300)

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Assuming reviews_df is already defined and contains the reviews_table data
# Here we are assuming there's a 'product_id' and 'rating' column in the reviews_df

# Group by 'product_id' and calculate the average rating for each product
average_ratings = reviews_df.groupby('product_id')['rating'].mean()

# Get the top 5 products with the highest average rating
top_rated_products = average_ratings.nlargest(5)

# Reset index for better plotting
top_rated_products = top_rated_products.reset_index()

# Assuming there's a products_df DataFrame to get product names
# Merge with products_df to get product names
top_rated_products = top_rated_products.merge(products_df[['product_id', 'product_name']], on='product_id')

# Plotting the top rated products
plt.figure(figsize=(10, 6))
plt.bar(top_rated_products['product_name'], top_rated_products['rating'], color='lightgreen')
plt.title('Top 5 Highest Rated Products')
plt.xlabel('Product Name')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Save the plot as a PNG file
plt.savefig('Top_5_Highest_Rated_Products.png', format='png', dpi=300)
plt.show()

# Display the top rated products DataFrame
print(top_rated_products)
'''


                           ######### multiple joins problems ###########

'''
query = """
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(od.totalprice) AS total_purchase_amount,
    CASE 
        WHEN SUM(od.totalprice) >= 1000 THEN 'High'
        WHEN SUM(od.totalprice) BETWEEN 500 AND 999 THEN 'Medium'
        ELSE 'Low'
    END AS customer_segment
FROM 
    customers_table AS c
JOIN 
    orders_table AS o ON c.customer_id = o.customer_id
JOIN 
    orderdetails_table AS od ON o.order_id = od.order_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    c.customer_id ASC;
"""

customer_segment_df = execute_query(query)
print(customer_segment_df.to_string())

import matplotlib.pyplot as plt
import pandas as pd

# Check data types
print(customer_segment_df.dtypes)

# Convert 'total_purchase_amount' to numeric
customer_segment_df['total_purchase_amount'] = pd.to_numeric(customer_segment_df['total_purchase_amount'], errors='coerce')

# Drop NaN values if any
customer_segment_df = customer_segment_df.dropna(subset=['total_purchase_amount'])

# Sort the DataFrame by total_purchase_amount and get the top 5 customers
top_customers = customer_segment_df.nlargest(5, 'total_purchase_amount')

# Plotting the top 5 customers and their purchase amounts
plt.figure(figsize=(10, 6))
plt.bar(top_customers['first_name'] + ' ' + top_customers['last_name'], top_customers['total_purchase_amount'], color='skyblue')
plt.xlabel('Customer Name')
plt.ylabel('Total Purchase Amount')
plt.title('Top 5 Customers by Total Purchase Amount')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Save the plot as a PNG file
plt.savefig('Top_5_Customers_by_Purchase_Amount.png', format='png', dpi=300)
plt.show()
'''