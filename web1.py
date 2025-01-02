import streamlit as st
import os

# Title of the website
st.title("Plant-Based Cellulose Research")

# Introduction section
st.header("Introduction")
st.write("""This website focuses on the benefits of plant-based cellulose for cattle, goats, and sheep. ....""")
st.write(""" As a researcher focused on plant-based cellulose products, my work explores innovative ways to harness cellulose for sustainable agricultural practices. Cellulose, a major component of plant cell walls, can be transformed into various products that enhance animal nutrition and health.
By developing cellulose-based feed additives, we can improve digestibility and nutrient absorption in livestock such as cattle, sheep, and poultry. These products can serve as a valuable source of energy and fiber, promoting better growth rates and overall health in animals.
Furthermore, cellulose products can help mitigate environmental impacts by reducing methane emissions during digestion, a significant concern in ruminant livestock. By incorporating cellulose into animal diets, we can enhance feed efficiency, leading to lower feed costs and improved economic viability for farmers.
Additionally, cellulose-based materials can be utilized in bedding and housing, contributing to better animal welfare by providing a comfortable and hygienic environment. This holistic approach not only supports animal health but also aligns with sustainable farming practices, ultimately benefiting the agricultural ecosystem. Through this research, the aim is to contribute to the development of innovative cellulose products, fostering a more sustainable future for animal agriculture.""")

# Health Benefits section
st.header("Health Benefits")
st.write("""
- Improves digestion in ruminants
- Enhances nutrient absorption
- Supports overall health and well-being
""")

# Gallery section
st.header("Gallery of Products Made from Plant Cellulose")

# List of images with relative paths
image_files = ["image/FEED_GRAIN.jpg"]  # Use relative path

# Display images in the gallery
for image_path in image_files:
    if os.path.exists(image_path):
        st.image(image_path, caption=image_path.split("/")[-1], use_container_width=True)  # Use the new parameter
    else:
        st.error(f"Image file not found: {image_path}")

# Contact section
st.header("Contact")
st.write("For further information, contact RONI SAHA at ronisaha2025@gmail.com")
