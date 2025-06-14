# 🛒 Amazon Product Scraper

A Python-based web scraping project that extracts product data (name, price, rating) from Amazon India and performs basic analysis to identify top-rated and best-priced items.

---

## 🔍 Features

- 🔎 Scrapes product **name, price, and rating** from Amazon
- 📦 Saves data to a CSV file
- 📊 Analyzes and prints:
  - Top 5 products by rating
  - Minimum, maximum, and average prices
- 🔁 Scrapes **2 pages** of product listings (~40 products)

---

## 🛠 Tech Stack

- **Python 3**
- **Requests** – Fetch HTML content
- **BeautifulSoup** – Parse and extract product data
- **Pandas** – Store and analyze structured data

---

## 📊 Output 
Example:
Top 5 Products by Rating:

name	price	rating
HP i5 13th Gen Laptop	₹60,990	5.0
DELL i3 12th Gen Laptop	₹34,490	5.0
Apple MacBook Air M2 (2022)	₹78,900	4.8

Price Statistics:
Min Price: ₹12,493.00
Max Price: ₹1,09,199.00
Average Price: ₹50,525.89

