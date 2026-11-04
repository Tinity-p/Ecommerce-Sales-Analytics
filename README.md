# E-commerce Sales Analytics | MySQL, Python

## Project Overview
This project focuses on analyzing an online retail dataset to identify sales trends, customer purchasing patterns, top-selling products, and country-wise sales performance.

MySQL was used for data storage and SQL analysis, while Python (Pandas and Matplotlib) was used to retrieve data, generate reports, and create visualizations.

## Tools & Technologies
- MySQL
- Python
- Pandas
- SQLAlchemy
- Matplotlib
- Excel / CSV

## Dataset
- Online Retail dataset
- Original records: 541,909
- Cleaned records: 535,187
- Contains invoice details, products, quantities, prices, customer IDs, dates, and countries.

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
Python connects to the MySQL database and automatically generates:
- Monthly sales report (CSV)
- Monthly sales trend chart (PNG)
- Country-wise sales report (CSV)
- Country-wise sales chart (PNG)
- Top products sales report (CSV)

## Project Structure
```text
ecommerce-analytics/
│
├── Dataset/
│   ├── Online Retail.xlsx
│   └── online_retail_cleaned.csv
├── SQL/
│   └── ecommerce_analysis.sql
│
├── Python/
│   ├── data_inspection.py
│   ├── import_to_mysql.py
│   └── ecommerce_analysis.py
│
├── Reports/
│   ├── monthly_sales_report.csv
│   ├── monthly_sales_trend.png
│   ├── country_sales_report.csv
│   ├── country_sales_chart.png
│   └── product_sales_report.csv
│
└── README.md
```

## Conclusion
This project demonstrates practical skills in data cleaning, SQL querying, Python automation, data analysis, and visualization to generate meaningful business insights from retail data.