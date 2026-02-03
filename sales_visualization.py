import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load sales data
data = pd.read_csv("sales_data.csv")
print(data)

# Step 2: Convert Date column to date format
data["Date"] = pd.to_datetime(data["Date"])

# -------------------------------
# 1. Line Chart – Sales Over Time
# -------------------------------
plt.figure()
plt.plot(data["Date"], data["Sales"])
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.show()

# --------------------------------
# 2. Bar Chart – Product-wise Sales
# --------------------------------
product_sales = data.groupby("Product")["Sales"].sum()

plt.figure()
plt.bar(product_sales.index, product_sales.values)
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Product-wise Sales")
plt.show()

# --------------------------------
# 3. Pie Chart – Sales Distribution
# --------------------------------
plt.figure()
plt.pie(product_sales.values, labels=product_sales.index, autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()
