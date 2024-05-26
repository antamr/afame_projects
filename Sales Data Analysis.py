#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Load the data set
import pandas as pd
df = pd.read_excel("C:/Users/ALEN/Downloads/ECOMM DATA.xlsx")
df
df.head()


# In[17]:


# Calculate total sales revenue
total_revenue = df['Sales'].sum()
print("Total Sales Revenue: $", total_revenue)


# In[21]:


import matplotlib.pyplot as plt

# Convert the 'Date' column to datetime format
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Group sales data by date and calculate total sales for each date
daily_sales = df.groupby('Ship Date')['Sales'].sum()

# Plot the sales trends over time
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-')
plt.title('Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Total Sales Revenue')
plt.grid(True)
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:/Users/ALEN/Downloads/ECOMM DATA.xlsx")
df
# Group data by product and calculate total sales quantity or revenue for each product
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

# Select top N best-selling products (change N as needed)
top_n = 10
best_selling_products = product_sales.head(top_n)

# Plot bar chart for best-selling products
plt.figure(figsize=(10, 6))
best_selling_products.plot(kind='bar', color='skyblue')
plt.title('Top {} Best-Selling Products'.format(top_n))
plt.xlabel('Product')
plt.ylabel('Total Sales Quantity')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

