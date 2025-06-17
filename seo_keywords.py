def get_keywords(product_name):
    return [product_name.lower(), "trending", "best-selling", "popular"]

if __name__ == "__main__":
    print(get_keywords("Wireless Headphones"))
