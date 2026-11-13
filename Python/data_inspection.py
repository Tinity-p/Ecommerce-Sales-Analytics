
import pandas as pd

file_path = "../Dataset/online_retail_sample.csv"
df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])

print("CLEANED DATASET SUMMARY")
print("-----------------------")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))

print("\nTotal sales value:", round(df["Sales"].sum(), 2))
print("Unique invoices:", df["InvoiceNo"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique countries:", df["Country"].nunique())

print("\nNegative quantity rows:", (df["Quantity"] < 0).sum())
print("Zero or negative price rows:", (df["UnitPrice"] <= 0).sum())

print("\nTop 5 countries by sales:")
print(
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
