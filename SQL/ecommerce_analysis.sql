CREATE DATABASE IF NOT EXISTS ecommerce_analytics;

USE ecommerce_analytics;

SELECT DATABASE();

USE ecommerce_analytics;

CREATE TABLE online_retail (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID DECIMAL(10,1) NULL,
    Country VARCHAR(100),
    Sales DECIMAL(12,2)
);

SHOW TABLES;

DESCRIBE online_retail;

USE ecommerce_analytics;

SELECT COUNT(*) AS total_records
FROM ecommerce_analytics.online_retail;

SELECT *
FROM ecommerce_analytics.online_retail
LIMIT 10;

SELECT ROUND(SUM(Sales), 2) AS total_sales
FROM ecommerce_analytics.online_retail;


USE ecommerce_analytics;

SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS month,
    ROUND(SUM(Sales), 2) AS monthly_sales
FROM online_retail
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY month;


SELECT
    Country,
    ROUND(SUM(Sales), 2) AS total_sales
FROM online_retail
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    StockCode,
    Description,
    ROUND(SUM(Sales), 2) AS total_sales
FROM online_retail
GROUP BY StockCode, Description
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    StockCode,
    Description,
    SUM(Quantity) AS total_quantity
FROM online_retail
WHERE Quantity > 0
  AND StockCode NOT IN ('DOT', 'POST')
GROUP BY StockCode, Description
ORDER BY total_quantity DESC
LIMIT 10;


SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_spent
FROM online_retail
WHERE CustomerID IS NOT NULL
  AND Quantity > 0
  AND UnitPrice > 0
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;


SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    ROUND(SUM(Sales), 2) AS total_sales
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    DATE_FORMAT(InvoiceDate, '%Y-%m') AS month,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
GROUP BY DATE_FORMAT(InvoiceDate, '%Y-%m')
ORDER BY month;
