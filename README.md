# E-commerce Sales Analytics | MySQL, Python

## Project Overview

This project focuses on analyzing an online retail dataset to identify sales trends, customer purchasing patterns, top-selling products, and country-wise sales performance.

MySQL was used for data storage and SQL analysis, while Python (Pandas and Matplotlib) was used to retrieve data, generate reports, and create visualizations.

## Project Objectives

- Analyze monthly sales and order trends.
- Identify top-selling products.
- Understand customer purchasing patterns.
- Compare sales performance across countries.
- Generate automated reports and visualizations.

## Tools & Technologies

- MySQL
- Python
- Pandas
- SQLAlchemy
- Matplotlib
- Excel / CSV

## Dataset

- Dataset: Online Retail
- Original records: 541,909
- Cleaned records: 535,187
- Contains invoice details, products, quantities, prices, customer IDs, dates, and countries.

**Dataset files:**
- `Online Retail.xlsx` – Original dataset.
- `online_retail_sample.csv` – 10,000-row sample provided for demonstration.

The full cleaned dataset is not included in this repository due to its file size. It is available locally for the complete analysis.

## Data Cleaning

The dataset was cleaned using Python and Pandas.

- Removed duplicate records.
- Handled missing product descriptions.
- Converted date and numeric columns into appropriate data types.
- Created a new Sales column using Quantity × UnitPrice.

## Project Analysis

1. Monthly Sales Trend
2. Country-wise Sales Analysis
3. Top 10 Products by Sales
4. Top 10 Products by Quantity Sold
5. Top 10 Customers by Spending
6. Monthly Order Volume

## Key Insights

- November 2011 recorded the highest monthly sales of 1,456,145.80.
- The United Kingdom was the leading market, with sales of 8,167,128.18 in the initial country-wise sales analysis.
- DOTCOM POSTAGE recorded the highest sales value among the listed stock codes.
- PAPER CRAFT, LITTLE BIRDIE was the most purchased product, with 80,995 units.
- Customer 14646 was the highest-spending customer, with total spending of 280,206.02.

## Python Automation

Python connects to the MySQL database and generates:

- Monthly sales report (CSV)
- Monthly sales trend chart (PNG)
- Country-wise sales report (CSV)
- Country-wise sales chart (PNG)
- Top products sales report (CSV)

## Project Structure

```text
Ecommerce-Sales-Analytics/
│
├── Dataset/
│   ├── README.md
│   ├── Online Retail.xlsx
│   └── online_retail_sample.csv
│
├── Python/
│   ├── README.md
│   ├── data_inspection.py
│   ├── import_to_mysql.py
│   └── ecommerce_analysis.py
│
├── SQL/
│   ├── README.md
│   └── ecommerce_analysis.sql
│
├── Reports/
│   ├── README.md
│   ├── monthly_sales_report.csv
│   ├── monthly_sales_trend.png
│   ├── country_sales_report.csv
│   ├── country_sales_chart.png
│   └── product_sales_report.csv
│
└── README.md
```

## How to Run the Project

1. Install Python and MySQL.
2. Install the required Python libraries: Pandas, SQLAlchemy, PyMySQL, OpenPyXL, and Matplotlib.
3. Create a MySQL database named `ecommerce_analytics`.
4. Update the database connection details in the Python scripts with your own credentials.
5. Run `data_inspection.py` to inspect the dataset.
6. Run `import_to_mysql.py` to import the cleaned dataset into MySQL.
7. Execute the SQL queries in `ecommerce_analysis.sql`.
8. Run `ecommerce_analysis.py` to generate reports and charts.

Use the full cleaned dataset for reproducing the original analysis results. The GitHub sample can be used for demonstration.

## Conclusion

This project demonstrates practical skills in data cleaning, SQL querying, Python automation, data analysis, and visualization to generate meaningful business insights from retail data.
