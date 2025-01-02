import streamlit as st
import os

# Title of the website
st.title("Plant-Based Cellulose Research")

# Introduction section
st.header("Introduction")
st.write("""This website focuses on the benefits of plant-based cellulose for cattle, goats, and sheep. ...""")

# Benefits section
st.header("Health Benefits")
st.write("""
- Improves digestion in ruminants
- Enhances nutrient absorption
- Supports overall health and well-being
""")

# Gallery section
st.header("Gallery of Products Made from Plant Cellulose")

# List of images with relative paths
image_files = [
    "image/CATTLE_FEED.webp",  # Use relative path
    "image/POULTRY_FEED.webp",  # Use relative path
    "image/FEED_GRAIN.jpg",  # Use relative path
]

# Display images in the gallery
for image_path in image_files:
    if os.path.exists(image_path):
        st.image(image_path, caption=image_path.split("/")[-1], use_container_width=True)  # Use the new parameter
    else:
        st.error(f"Image file not found: {image_path}")

# Contact section
st.header("Contact")
st.write("For further information, contact RONI SAHA at [your_email@example.com](mailto:your_email@example.com)")
