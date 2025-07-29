import streamlit as st
import pandas as pd
import requests

API_BASE_URL = "http://localhost:5000/api/products"

def fetch_data(website, category=None):
    url = f"{API_BASE_URL}/{website}"
    params = {}
    if category:
        params['category'] = category
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error("Failed to fetch data from API")
        return pd.DataFrame()

def main():
    st.title("E-commerce Product Data Preview")

    websites = ["flipkart", "amazon", "site3", "site4", "site5", "site6"]
    website = st.selectbox("Select Website", websites)

    categories = ["All", "laptop", "mobile", "camera", "headphones", "smartwatch"]
    category = st.selectbox("Select Category", categories)

    if category == "All":
        category = None

    data = fetch_data(website, category)

    if not data.empty:
        st.dataframe(data)

        csv = data.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=f"{website}_data.csv",
            mime="text/csv",
        )
    else:
        st.write("No data available for the selected filters.")

if __name__ == "__main__":
    main()
