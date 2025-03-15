import pandas as pd 
'''
df = pd.read_csv('sales_1.csv')
df['Date'] = pd.to_datetime((df['Date']))
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

df.to_csv('sales_1.csv',index = False)
'''

'''
import pandas as pd
df = pd.read_csv('sales_1.csv')
# Step 2: Drop the last 3 columns (Year, Month, Day)
df = df.drop(['Year', 'Month', 'Day'], axis=1)

df.to_csv('sales.csv', index=False)
'''

#                                              Line Chart of Sales Over Time
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('sales_1.csv')
'''
# Plot sales over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales Amount'], marker='^', color='b')  # marker can be o,^,s this is head point of arrow representaion
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)       # xticks(rotation = 45) means rotates the x-axis labels by 45 degrees to make them easier to read, especially if the labels are long or close together.
plt.grid(True)
plt.savefig('Sales_Amount_Over_Time.png', format='png')        # save the chart in your folder
plt.show()
#plt.clf()                                                 # Clear the figure
''' 


'''
figsize controls the overall size of the plot.
marker defines how data points are visually represented.
color sets the color of the plot elements.
rotation is used for better label readability.
grid() enhances the plot's clarity.
'''
#                                      Bar Plot of Total Sales by Category
'''
# Calculate total sales per category
category_sales = df.groupby('Category')['Sales Amount'].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(8, 6))
plt.bar(category_sales['Category'], category_sales['Sales Amount'], color='skyblue')
plt.title('Total Sales by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('Total_Sales_by_Category.png', format='png') 
plt.show()
'''

#                                        Histogram of Sales Amount Distribution
 # bins (intervals) to divide the data into for the histogram. here 20 intervals 
'''
plt.figure(figsize=(8, 6))
plt.hist(df['Sales Amount'], bins=20, color='green', edgecolor='black')      
plt.title('Distribution of Sales Amount', fontsize=16)
plt.xlabel('Sales Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('Distribution_of_Sales_Amount.png', format='png')
plt.show()
'''
#                                     Bar Plot of Total Sales by Region
'''
region_sales = df.groupby('Region')['Sales Amount'].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(8, 6))
plt.bar(region_sales['Region'], region_sales['Sales Amount'], color='orange')
plt.title('Total Sales by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('Total_Sales_by_Region.png', format='png')
plt.show()
'''
#                                          Line Chart of Units Sold Over Time
'''
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Units Sold'], marker='o', linestyle='-', color='red')
plt.title('Units Sold Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Units Sold', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Unit_sold_over_time.png', format='png')
plt.show()
'''
#                                       Scatter Plot of Units Sold vs. Sales Amount
'''
plt.figure(figsize=(8, 6))
plt.scatter(df['Units Sold'], df['Sales Amount'], color='purple', alpha=0.7)
plt.title('Units Sold vs. Sales Amount', fontsize=16)
plt.xlabel('Units Sold', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
'''

#                                       Box Plot of Sales Amount by Category
'''
categories = df['Category'].unique()
data_to_plot = [df[df['Category'] == category]['Sales Amount'] for category in categories]

# Plot boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=categories)
plt.title('Sales Amount by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig('Sales_Amount_by_Category.png', format='png')
plt.show()
'''

#                                        Bar Plot of Total Sales by Month

'''
monthly_sales = df.groupby('Month')['Sales Amount'].sum().reset_index()

# Plot bar chart
plt.figure(figsize=(8, 6))
plt.bar(monthly_sales['Month'], monthly_sales['Sales Amount'], color='teal')
plt.title('Total Sales by Month', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.grid(axis='y')
plt.xticks(monthly_sales['Month'])
plt.tight_layout()
plt.savefig('Total_Sales_by_Month.png', format='png')
plt.show()
'''



