import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# MySQL connection details
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "ecommerce_analytics"

# Create MySQL connection
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Connected to MySQL successfully!")

# Monthly sales query
monthly_sales_query = """
SELECT
    DATE_FORMAT(InvoiceDate, '%%Y-%%m') AS month,
    ROUND(SUM(Sales), 2) AS monthly_sales
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%%Y-%%m')
ORDER BY month;
"""

# Load query results into a Pandas DataFrame
monthly_sales = pd.read_sql(monthly_sales_query, engine)

print("\nMonthly Sales:")
print(monthly_sales)

# Save the report as a CSV file
monthly_sales.to_csv(
    "../Reports/monthly_sales_report.csv",
    index=False
)

print("\nMonthly sales report saved successfully!")

# Create a sales trend chart
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales["month"],
    monthly_sales["monthly_sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("../Reports/monthly_sales_trend.png")

print("Sales trend chart saved successfully!")

plt.show()






# Country-wise sales query
country_sales_query = """
SELECT
    Country,
    ROUND(SUM(Sales), 2) AS total_sales
FROM online_retail
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10;
"""

# Load country sales data
country_sales = pd.read_sql(country_sales_query, engine)

print("\nTop 10 Countries by Sales:")
print(country_sales)

# Save the country sales report
country_sales.to_csv(
    "../Reports/country_sales_report.csv",
    index=False
)

print("\nCountry sales report saved successfully!")

# Create a country sales chart
plt.figure(figsize=(10, 5))
plt.bar(country_sales["Country"], country_sales["total_sales"])

plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("../Reports/country_sales_chart.png")

print("Country sales chart saved successfully!")

plt.show()




# Top 10 products by sales query
product_sales_query = """
SELECT
    StockCode,
    Description,
    ROUND(SUM(Sales), 2) AS total_sales
FROM online_retail
GROUP BY StockCode, Description
ORDER BY total_sales DESC
LIMIT 10;
"""

# Load product sales data
product_sales = pd.read_sql(product_sales_query, engine)

print("\nTop 10 Products by Sales:")
print(product_sales)

# Save the product sales report
product_sales.to_csv(
    "../Reports/product_sales_report.csv",
    index=False
)

print("\nProduct sales report saved successfully!")