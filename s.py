import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Headers for spoofing user-agent
def get_headers():
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    ]
    return {"User-Agent": random.choice(user_agents)}

# Scraper Function
def scrape_amazon(category, pages=2):
    products = []
    base_url = f"https://www.amazon.in/s?k=laptops&ref=nb_sb_noss"

    for page in range(1, pages + 1):
        url = f"{base_url}&page={page}"
        headers = get_headers()
        print(f"Fetching Page {page}...")

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}, status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        print(f"Found {len(results)} products on page {page}")

        for item in results:
            try:
                name = item.h2.text.strip()
                price = item.find('span', 'a-price-whole')
                price = price.text.strip().replace(',', '') if price else '0'

                rating = item.find('span', class_='a-icon-alt')
                rating = rating.text.split()[0] if rating else '0'

                products.append({
                    'name': name,
                    'price': float(price),
                    'rating': float(rating)
                })
            except Exception as e:
                print(f"Error: {e}")
                continue

        time.sleep(random.randint(2, 4))  # delay between requests

    return products

# Save to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Analyze the data
def analyze_data(filename):
    df = pd.read_csv(filename)

    print("\nTop 5 Products by Rating:")
    top_products = df.sort_values(by='rating', ascending=False).head(5)
    print(top_products[['name', 'price', 'rating']])

    print("\nPrice Statistics:")
    print(f"Min Price: ₹{df['price'].min():,.2f}")
    print(f"Max Price: ₹{df['price'].max():,.2f}")
    print(f"Average Price: ₹{df['price'].mean():,.2f}")

# Main runner
if __name__ == "__main__":
    category = "laptop"
    data = scrape_amazon(category, pages=2)
    if data:
        save_to_csv(data, f"{category}.csv")
        analyze_data(f"{category}.csv")
    else:
        print("No data found.")
