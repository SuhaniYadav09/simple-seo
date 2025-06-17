import requests
from bs4 import BeautifulSoup

def get_best_sellers():
    url = "https://www.amazon.com/Best-Sellers/zgbs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = [item.text.strip() for item in soup.select(".p13n-sc-truncate")]
    return products[:5]

if __name__ == "__main__":
    print(get_best_sellers())
