import requests
from bs4 import BeautifulSoup
import pandas as pd

# requests.get("http://example.org", proxies=proxies)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSaveAsHTML(url, path):
    # Increase timeout value (in seconds)
    timeout = 10  # Adjust as needed
    r = requests.get(url, headers=headers, timeout=timeout)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
        
def readHTMLFile(filename):
    with open(filename, "r") as f:
        html_doc = f.read()
    return html_doc

# stored_data = {'title': [], 'price': [], 'rating': []}

searchqn = input("SEARCH QUESTION: ")
searchqn_with_plus = "+".join(searchqn.split())
url = "https://stackoverflow.com/search?q=" + searchqn_with_plus
# print(url)

# OR
"""
    from urllib.parse import quote
    search_input = input("ENTER THE ITEM TO BE SEARCHED IN AMAZON: ")
    encoded_input = quote(search_input)
    url = f"https://www.amazon.in/s?k={encoded_input}&crid=NBAWX3VRB4CT&sprefix=laptops%2Caps%2C217&ref=nb_sb_noss_1"
"""

fetchAndSaveAsHTML(url, "data/stackOverflowQnScrape.html")

html_content = readHTMLFile("data/stackOverflowQnScrape.html")

soup = BeautifulSoup(html_content, 'html.parser')

"""
names of laptops:class="a-size-medium a-color-base a-text-normal"

ratings = span aria-label="3.2 out of 5 stars"  class="a-row a-size-small"

price = class="a-price"

"""
# Initialize lists to store scraped data
titles = []
prices = []
ratings = []

# Select relevant elements containing product information
answers = soup.select("div.s-prose.js-post-body")
# prices = soup.select("span.a-offscreen")
# ratings = soup.select("span.a-icon-alt")

# Loop through each product and extract its information
# for name, price, rating in zip(names, prices, ratings):
#     # Extract product title
#     title = name.string if name else "N/A"DF GHJKL;'
#     titles.append(title)
    
#     # Extract product price
#     price = price.string if price else "N/A"
#     prices.append(price)
    
#     # Extract product rating
#     rating = rating.string if rating else "N/A"
#     ratings.append(rating)

# # Create DataFrame from the collected data
# # df = pd.DataFrame({
# #     "Title": titles,
# #     "Price": prices,
# #     "Rating": ratings
# # })

# # # Save DataFrame to CSV file
# # df.to_csv("amazonscrapeddata.csv", index=False)

# print("Length of titles:", len(titles))
# print("Length of prices:", len(prices))
# print("Length of ratings:", len(ratings))
