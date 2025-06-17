import streamlit as st
from blog_writer import generate_blog
from scraper import get_best_sellers
from seo_keywords import get_keywords

st.title("SEO Blog Generator")

category = st.text_input("Enter a product category (e.g., Smartphones, Laptops)")

if st.button("Generate Blog"):
    if category:
        products = get_best_sellers()
        product = products[0]  # Take the first trending product
        keywords = get_keywords(product)
        blog = generate_blog(product, keywords)
        st.write(blog)
    else:
        st.warning("Please enter a product category")
