import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_flipkart():
    print("Scraping Flipkart...")
    # Mapping of categories to their Flipkart Electronics dropdown URLs
    category_urls = {
        "laptop": "https://www.flipkart.com/computers/laptops/pr?sid=6bo,b5g",
        "mobile": "https://www.flipkart.com/mobiles/pr?sid=tyy,4io",
        "camera": "https://www.flipkart.com/cameras/pr?sid=jek,p31",
        "headphones": "https://www.flipkart.com/headphones/pr?sid=0pm,ajp",
        "smartwatch": "https://www.flipkart.com/smart-watches/pr?sid=ajy,abm",
        "tablet": "https://www.flipkart.com/tablets/pr?sid=tyy,hry"
    }
    all_data = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/58.0.3029.110 Safari/537.3"
    }

    for category, url in category_urls.items():
        for page in range(1, 3):  # Scrape first 2 pages per category
            page_url = f"{url}&page={page}"
            response = requests.get(page_url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to retrieve page {page} for category {category}")
                continue
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", {"class": "_1AtVbE"})
            for product in products:
                name_tag = product.find("div", {"class": "_4rR01T"})
                if not name_tag:
                    continue
                product_name = name_tag.text.strip()

                brand_name = product_name.split()[0] if product_name else ""

                price_tag = product.find("div", {"class": "_30jeq3 _1_WHN1"})
                price = price_tag.text.strip().replace("₹", "").replace(",", "") if price_tag else None
                price = float(price) if price and price.isdigit() else None

                rating_tag = product.find("div", {"class": "_3LWZlK"})
                rating = rating_tag.text.strip() if rating_tag else ""

                all_data.append({
                    "product_name": product_name,
                    "brand_name": brand_name,
                    "price": price,
                    "rating_or_reviews": rating,
                    "website_name": "flipkart",
                    "category": category
                })
            time.sleep(1)  # polite delay


    df = pd.DataFrame(all_data)
    df.to_csv("data/flipkart.csv", index=False)
    print("Flipkart data saved to data/flipkart.csv")

if __name__ == "__main__":
    scrape_flipkart()
