import psycopg2
import pandas as pd
from database.db_connect import get_db_connection

def insert_data(table_name, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    for _, row in data.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (product_name, brand_name, price, rating_or_reviews, website_name, category)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (row['product_name'], row['brand_name'], row['price'], row['rating_or_reviews'], row['website_name'], row['category']))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    # Example: Load CSV files from data/ directory and insert into DB
    websites = ['flipkart', 'amazon', 'site3', 'site4', 'site5', 'site6']
    for site in websites:
        try:
            df = pd.read_csv(f"data/{site}.csv")
            insert_data(site, df)
            print(f"Inserted data for {site}")
        except FileNotFoundError:
            print(f"No data file found for {site}, skipping.")

if __name__ == "__main__":
    main()
