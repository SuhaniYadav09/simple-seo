def generate_blog(product, keywords):
    blog = f"Looking for the best {product}? Our trending pick is grabbing attention! It's {', '.join(keywords)} in the market. Get yours today!"
    return blog

if __name__ == "__main__":
    product = "Wireless Headphones"
    keywords = get_keywords(product)
    print(generate_blog(product, keywords))
