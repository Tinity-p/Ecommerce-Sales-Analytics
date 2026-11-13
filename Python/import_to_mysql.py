
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# MySQL connection settings
DB_USER = "root"
DB_PASSWORD = "your_password"  # Enter your own MySQL password
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "ecommerce_analytics"

# CSV file location
CSV_FILE = "../Dataset/online_retail_sample.csv"

# Connect to MySQL
connection_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

engine = create_engine(connection_url)

try:
    # Check the connection before changing any data
    with engine.connect() as conn:
        print("Connected to MySQL successfully!")

    # Remove the incomplete import so we can start cleanly
    confirm = input(
        "This will clear the existing online_retail rows "
        "before reimporting the CSV. Type REIMPORT to continue: "
    )

    if confirm != "REIMPORT":
        print("Import cancelled. Existing rows were not changed.")
    else:
        with engine.begin() as conn:
            conn.execute(text("TRUNCATE TABLE online_retail"))

        total_rows = 0

        # Load the CSV in manageable batches
        for batch in pd.read_csv(
            CSV_FILE,
            chunksize=5000,
            parse_dates=["InvoiceDate"]
        ):
            batch.to_sql(
                name="online_retail",
                con=engine,
                if_exists="append",
                index=False,
                chunksize=500,
                method=None
            )

            total_rows += len(batch)
            print(f"Imported {total_rows:,} rows")

        # Verify the final count
        with engine.connect() as conn:
            count = conn.execute(
                text("SELECT COUNT(*) FROM online_retail")
            ).scalar_one()

        print(f"\nImport completed! Database rows: {count:,}")

finally:
    engine.dispose()
