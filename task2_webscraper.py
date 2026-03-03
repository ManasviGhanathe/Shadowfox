import sys
print(sys.executable)
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

print("Status Code:", response.status_code)

# Convert HTML into readable format
soup = BeautifulSoup(response.text, "html.parser")

# Find all book sections
books = soup.find_all("article", class_="product_pod")

print("Total books found:", len(books))
print("Website parsed successfully")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    print(title)
    print("Price:", price)
    print("-" * 40)