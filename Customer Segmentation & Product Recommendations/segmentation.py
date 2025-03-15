import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy import text
import pandas as pd
from sqlalchemy import create_engine, text
from sklearn.neighbors import NearestNeighbors

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

'''
def execute_query(query):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return pd.DataFrame(result.fetchall(), columns=result.keys())
'''

                                        # first segmentation #
'''
#print(customers_df.head())
query = """
SELECT 
    o.customer_id,
    c.first_name,
    c.last_name,
    p.category,
    COUNT(od.product_id) AS purchase_count,
    SUM(od.totalprice) AS total_spent,
    MAX(o.orderdate) AS last_purchase_date
FROM 
    orders_table AS o
JOIN 
    orderdetails_table AS od ON o.order_id = od.order_id
JOIN 
    products_table AS p ON od.product_id = p.product_id
JOIN 
    customers_table AS c ON c.customer_id = o.customer_id
GROUP BY 
    o.customer_id, c.first_name, c.last_name, p.category
ORDER BY 
    o.customer_id ASC;
"""

customer_segment_df = execute_query(query)

# Display all rows in the output
pd.options.display.max_rows = len(customer_segment_df)
print(customer_segment_df)

# Save the DataFrame to a CSV file
customer_segment_df.to_csv("customer_segmentation.csv", index=False)

print("Data saved to 'customer_segmentation.csv'")
'''

'''
query = """
WITH customer_category_summary AS (
    SELECT 
        o.customer_id,
        c.first_name,
        c.last_name,
        p.category,
        COUNT(od.product_id) AS purchase_count,
        SUM(od.totalprice) AS total_spent,
        MAX(o.orderdate) AS last_purchase_date
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    JOIN 
        customers_table AS c ON c.customer_id = o.customer_id
    GROUP BY 
        o.customer_id, c.first_name, c.last_name, p.category
),

top_categories AS (
    SELECT 
        customer_id,
        category,
        purchase_count,
        RANK() OVER (PARTITION BY customer_id ORDER BY purchase_count DESC) AS category_rank
    FROM 
        customer_category_summary
)

SELECT 
    customer_id,
    category,
    purchase_count
FROM 
    top_categories
WHERE 
    category_rank = 1
ORDER BY 
    customer_id;

"""
x = execute_query(query)
print(x.to_string())
'''

'''
query= """
WITH customer_category_summary AS (
    SELECT 
        o.customer_id,
        c.first_name,
        c.last_name,
        p.category,
        COUNT(od.product_id) AS purchase_count,
        SUM(od.totalprice) AS total_spent,
        MAX(o.orderdate) AS last_purchase_date
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    JOIN 
        customers_table AS c ON c.customer_id = o.customer_id
    GROUP BY 
        o.customer_id, c.first_name, c.last_name, p.category
),

top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category,
        purchase_count,
        RANK() OVER (PARTITION BY customer_id ORDER BY purchase_count DESC) AS category_rank
    FROM 
        customer_category_summary
),

customer_top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category
    FROM 
        top_categories
    WHERE 
        category_rank = 1
),

customer_purchased_products AS (
    SELECT 
        o.customer_id,
        p.product_id,
        p.category
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
)

SELECT 
    ctc.customer_id,
    ctc.first_name,
    ctc.last_name,
    p.product_id,
    p.product_name,
    p.category
FROM 
    products_table AS p
JOIN 
    customer_top_categories AS ctc ON p.category = ctc.category
LEFT JOIN 
    customer_purchased_products AS cpp ON cpp.customer_id = ctc.customer_id AND cpp.product_id = p.product_id
WHERE 
    cpp.product_id IS NULL
ORDER BY 
    ctc.customer_id, p.category;
"""
x = execute_query(query)
print(x.to_string())
'''

'''
query="""
WITH customer_category_summary AS (
    SELECT 
        o.customer_id,
        c.first_name,
        c.last_name,
        p.category,
        COUNT(od.product_id) AS purchase_count,
        SUM(od.totalprice) AS total_spent,
        MAX(o.orderdate) AS last_purchase_date
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    JOIN 
        customers_table AS c ON c.customer_id = o.customer_id
    GROUP BY 
        o.customer_id, c.first_name, c.last_name, p.category
),

top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category,
        purchase_count,
        RANK() OVER (PARTITION BY customer_id ORDER BY purchase_count DESC) AS category_rank
    FROM 
        customer_category_summary
),

customer_top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category
    FROM 
        top_categories
    WHERE 
        category_rank = 1
),

customer_purchased_products AS (
    SELECT 
        o.customer_id,
        p.product_id,
        p.category
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
)

SELECT 
    recommendations.customer_id,
    recommendations.first_name,
    recommendations.last_name,
    recommendations.product_id,
    recommendations.product_name,
    recommendations.category
FROM 
    (
        SELECT 
            ctc.customer_id,
            ctc.first_name,
            ctc.last_name,
            p.product_id,
            p.product_name,
            p.category,
            ROW_NUMBER() OVER (PARTITION BY ctc.customer_id ORDER BY p.product_id) AS rn
        FROM 
            products_table AS p
        JOIN 
            customer_top_categories AS ctc ON p.category = ctc.category
        LEFT JOIN 
            customer_purchased_products AS cpp ON cpp.customer_id = ctc.customer_id AND cpp.product_id = p.product_id
        WHERE 
            cpp.product_id IS NULL
    ) AS recommendations
WHERE 
    recommendations.rn <= 2  -- Set the number of recommendations per customer here
ORDER BY 
    recommendations.customer_id, recommendations.category;
"""

x = execute_query(query)
print(x.to_string())
'''
                                           # first recommendation #             
'''

def execute_query(query, fetch=True, commit=False):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        if commit:
            connection.commit()  # Commit the transaction if needed
        if fetch:
            return pd.DataFrame(result.fetchall(), columns=result.keys())

query = """
WITH customer_category_summary AS (
    SELECT 
        o.customer_id,
        c.first_name,
        c.last_name,
        p.category,
        COUNT(od.product_id) AS purchase_count,
        SUM(od.totalprice) AS total_spent,
        MAX(o.orderdate) AS last_purchase_date
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    JOIN 
        customers_table AS c ON c.customer_id = o.customer_id
    GROUP BY 
        o.customer_id, c.first_name, c.last_name, p.category
),

top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category,
        purchase_count,
        RANK() OVER (PARTITION BY customer_id ORDER BY purchase_count DESC) AS category_rank
    FROM 
        customer_category_summary
),

customer_top_categories AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        category
    FROM 
        top_categories
    WHERE 
        category_rank = 1
),

customer_purchased_products AS (
    SELECT 
        o.customer_id,
        p.product_id,
        p.category
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
)

SELECT 
    recommendations.customer_id,
    recommendations.first_name,
    recommendations.last_name,
    recommendations.product_id,
    recommendations.product_name,
    recommendations.category
FROM 
    (
        SELECT 
            ctc.customer_id,
            ctc.first_name,
            ctc.last_name,
            p.product_id,
            p.product_name,
            p.category,
            ROW_NUMBER() OVER (PARTITION BY ctc.customer_id ORDER BY p.product_id) AS rn
        FROM 
            products_table AS p
        JOIN 
            customer_top_categories AS ctc ON p.category = ctc.category
        LEFT JOIN 
            customer_purchased_products AS cpp ON cpp.customer_id = ctc.customer_id AND cpp.product_id = p.product_id
        WHERE 
            cpp.product_id IS NULL
    ) AS recommendations
WHERE 
    recommendations.rn = 1  -- Set to 1 to select only one recommendation per customer
ORDER BY 
    recommendations.customer_id, recommendations.category;
"""

# Step 3: Get the recommendations
recommendations_df = execute_query(query)

# Step 4: Prepare to insert recommendations into forecasting_table
for index, row in recommendations_df.iterrows():
    insert_query = f"""
    INSERT INTO forecasting_table (customer_id, product_recommendation_history)
    VALUES ({row['customer_id']}, '{row['product_name']}')
    ON CONFLICT (customer_id) DO UPDATE 
    SET product_recommendation_history = EXCLUDED.product_recommendation_history
    WHERE forecasting_table.customer_id = {row['customer_id']};  -- Ensure only the history column is updated
    """
    execute_query(insert_query, fetch=False, commit=True)  # Add commit=True here

print("Recommendations successfully inserted into forecasting_table.")

'''

#                                       second segmentation                               #
'''
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sqlalchemy import create_engine, text

# Function to execute SQL queries
def execute_query(query, fetch=True, commit=False):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        if commit:
            connection.commit()  # Commit the transaction if needed
        if fetch:
            return pd.DataFrame(result.fetchall(), columns=result.keys())
        return None

# Load necessary tables
orderdetails_df = pd.read_sql('SELECT * FROM orderdetails_table', engine)
orders_table = pd.read_sql('SELECT * FROM orders_table', engine)
products_df = pd.read_sql('SELECT * FROM products_table', engine)

# SQL Query to Segment Customers by Top-Purchased Categories
category_segmentation_query = """
WITH customer_category_summary AS (
    SELECT 
        o.customer_id,
        p.category,
        COUNT(od.product_id) AS purchase_count
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    GROUP BY 
        o.customer_id, p.category
),

top_categories AS (
    SELECT 
        customer_id,
        category,
        RANK() OVER (PARTITION BY customer_id ORDER BY purchase_count DESC) AS category_rank
    FROM 
        customer_category_summary
)

SELECT 
    customer_id,
    category
FROM 
    top_categories
WHERE 
    category_rank = 1;
"""

# Execute the Query
customer_top_categories = pd.read_sql(category_segmentation_query, engine)

# Pivot the Data to Create a Customer-Category Matrix
customer_category_matrix = pd.pivot_table(
    data=customer_top_categories,
    index='customer_id',
    columns='category',
    aggfunc='size',
    fill_value=0
)

# Initialize KNN with appropriate parameters
knn_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5, n_jobs=-1)

# Fit the model on the customer-category matrix
knn_model.fit(customer_category_matrix)

# Function to recommend a single product based on top-purchased category
def recommend_single_product(customer_id, top_category):
    # Locate the customer in the matrix
    customer_index = customer_category_matrix.index.get_loc(customer_id)
    distances, indices = knn_model.kneighbors(customer_category_matrix.iloc[[customer_index]], n_neighbors=6)

    recommended_products = set()
    for idx in indices.flatten()[1:]:  # Skip the first index (self)
        similar_customer_id = customer_category_matrix.index[idx]
        
        # Filter products based on category and customer match
        merged_df = orderdetails_df.merge(orders_table, on='order_id')
        similar_customer_products = products_df[
            (products_df['category'] == top_category) &
            (products_df['product_id'].isin(merged_df.loc[merged_df['customer_id'] == similar_customer_id, 'product_id']))
        ]['product_id'].values

        # Get products already purchased by the target customer
        customer_products = merged_df.loc[merged_df['customer_id'] == customer_id, 'product_id'].values
        recommended_products.update(set(similar_customer_products) - set(customer_products))
    
    # Convert product_ids to product_names
    recommended_product_names = products_df[products_df['product_id'].isin(recommended_products)]['product_name'].values
    
    return list(recommended_product_names)[:1]  # Return a single recommendation

# Create the new forecasting table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS forecasting_table_2 (
    customer_id INT PRIMARY KEY,
    product_recommendation_by_categories VARCHAR(255)
);
"""
execute_query(create_table_query, fetch=False, commit=True)

# Insert recommendations into forecasting_table_2
for customer_id in customer_category_matrix.index:
    top_category = customer_top_categories.loc[customer_top_categories['customer_id'] == customer_id, 'category'].values[0]
    recommendation = recommend_single_product(customer_id, top_category)
    
    if recommendation:
        # Insert or update the recommendation in forecasting_table_2
        insert_query = f"""
        INSERT INTO forecasting_table_2 (customer_id, product_recommendation_by_categories)
        VALUES ({customer_id}, '{recommendation[0]}')
        ON CONFLICT (customer_id) DO UPDATE 
        SET product_recommendation_by_categories = EXCLUDED.product_recommendation_by_categories;
        """
        execute_query(insert_query, fetch=False, commit=True)

print("forecasting_table_2 updated with top product recommendations for each customer by category.")
'''

def execute_query(query, fetch=True, commit=False):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        if commit:
            connection.commit()  # Commit the transaction if needed
        if fetch:
            return pd.DataFrame(result.fetchall(), columns=result.keys())

# Step 1: Create a country-based product popularity table
country_popularity_query = """
WITH country_product_summary AS (
    SELECT 
        c.customer_id,  -- Added customer_id here
        c.country,
        p.product_id,
        p.category,
        COUNT(od.product_id) AS purchase_count
    FROM 
        orders_table AS o
    JOIN 
        orderdetails_table AS od ON o.order_id = od.order_id
    JOIN 
        products_table AS p ON od.product_id = p.product_id
    JOIN 
        customers_table AS c ON c.customer_id = o.customer_id
    GROUP BY 
        c.customer_id, c.country, p.product_id, p.category  -- Group by customer_id
)

SELECT 
    customer_id,  -- Select customer_id in the final output
    country,
    product_id,
    category,
    purchase_count,
    RANK() OVER (PARTITION BY country ORDER BY purchase_count DESC) AS product_rank
FROM 
    country_product_summary
ORDER BY 
    customer_id;  -- Sort by customer_id in ascending order

"""

# Execute query and store results in DataFrame
country_popularity_df = execute_query(country_popularity_query)

# Step 2: Fetch customer IDs and generate recommendations by country
recommendations_by_country = []

for _, row in country_popularity_df.iterrows():
    customer_country = row['country']
    
    # Fetch all customers for this country
    customer_query = f"SELECT customer_id FROM customers_table WHERE country = '{customer_country}'"
    customer_ids = execute_query(customer_query)['customer_id'].tolist()
    
    # Find the top-ranked product for this country
    top_products = country_popularity_df[(country_popularity_df['country'] == customer_country) & 
                                         (country_popularity_df['product_rank'] == 1)]
    
    # Retrieve product details for the top product
    top_product_id = top_products['product_id'].values[0]
    top_product_name = products_df.loc[products_df['product_id'] == top_product_id, 'product_name'].values[0]
    
    # Append a recommendation for each customer in this country
    for customer_id in customer_ids:
        recommendations_by_country.append((customer_id, top_product_name))

# Step 3: Insert recommendations into the new table forecasting_table_3
for customer_id, product_name in recommendations_by_country:
    insert_query = f"""
    INSERT INTO forecasting_table_3 (customer_id, product_recommendation_by_country)
    VALUES ({customer_id}, '{product_name}')
    ON CONFLICT (customer_id) DO UPDATE 
    SET product_recommendation_by_country = EXCLUDED.product_recommendation_by_country;
    """
    execute_query(insert_query, fetch=False, commit=True)

print("Country-based recommendations have been successfully inserted into forecasting_table_3.")
