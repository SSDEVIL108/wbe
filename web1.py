import streamlit as st

# Title of the website
st.title("Plant-Based Cellulose Research")

# Introduction section
st.header("Introduction")
st.write("This website focuses on the benefits of plant-based cellulose for cattle, goats, and sheep.")

# Benefits section
st.header("Health Benefits")
st.write("""
- Improves digestion in ruminants
- Enhances nutrient absorption
- Supports overall health and well-being
""")

# Research section
st.header("Research Findings")
st.write("Here you can include detailed research findings and data.")

# Gallery section
st.header("Gallery of Products Made from Plant Cellulose")

# List of images with absolute paths
image_files = [
    r"D:\web\image\cattlefeed.webp",  # Absolute path to the first image
    r"D:\web\image\poultry feed.webp",  # Corrected string syntax
    r"D:\web\image\direct pic.jpg",  # Corrected string syntax
    # Add more images as needed
]

# Display images in the gallery
for image_path in image_files:
    st.image(image_path, caption=image_path.split("\\")[-1], use_column_width=True)  # Display the image and use the file name as the caption

# Contact section
st.header("Contact")
st.write("For more information, please contact the researcher.")