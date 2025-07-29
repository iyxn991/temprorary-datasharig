import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_amazon():
    print("Scraping Amazon...")
    base_url = "https://www.amazon.in/s?k={category}&page={page}"
    categories = ["laptop", "mobile", "camera", "headphones", "smartwatch", "tablet"]
    all_data = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/58.0.3029.110 Safari/537.3"
    }

    for category in categories:
        for page in range(1, 3):  # Scrape first 2 pages per category
            url = base_url.format(category=category, page=page)
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to retrieve page {page} for category {category}")
                continue
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", {"data-component-type": "s-search-result"})
            for product in products:
                name_tag = product.h2
                if not name_tag:
                    continue
                product_name = name_tag.text.strip()

                brand_name = product_name.split()[0] if product_name else ""

                price_whole = product.find("span", {"class": "a-price-whole"})
                price_fraction = product.find("span", {"class": "a-price-fraction"})
                if price_whole:
                    price = price_whole.text.replace(",", "")
                    if price_fraction:
                        price += price_fraction.text
                    try:
                        price = float(price)
                    except:
                        price = None
                else:
                    price = None

                rating_tag = product.find("span", {"class": "a-icon-alt"})
                rating = rating_tag.text.strip() if rating_tag else ""

                all_data.append({
                    "product_name": product_name,
                    "brand_name": brand_name,
                    "price": price,
                    "rating_or_reviews": rating,
                    "website_name": "amazon",
                    "category": category
                })
            time.sleep(1)  # polite delay

    df = pd.DataFrame(all_data)
    df.to_csv("data/amazon.csv", index=False)
    print("Amazon data saved to data/amazon.csv")

if __name__ == "__main__":
    scrape_amazon()
