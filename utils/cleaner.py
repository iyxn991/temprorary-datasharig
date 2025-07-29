import pandas as pd

def clean_data(df):
    # Example cleaning steps
    df = df.drop_duplicates()
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['product_name', 'price'])
    # Add more cleaning logic as needed
    return df

def main():
    # Placeholder for running cleaning on CSV files
    websites = ['flipkart', 'amazon', 'site3', 'site4', 'site5', 'site6']
    for site in websites:
        try:
            df = pd.read_csv(f"data/{site}.csv")
            cleaned_df = clean_data(df)
            cleaned_df.to_csv(f"data/{site}_cleaned.csv", index=False)
            print(f"Cleaned data saved for {site}")
        except FileNotFoundError:
            print(f"No data file found for {site}, skipping.")

if __name__ == "__main__":
    main()
