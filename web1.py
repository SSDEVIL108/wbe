import streamlit as st
import os

# Title of the website
st.title("Plant-Based Cellulose Research")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Home", "Health Benefits", "Gallery", "Contact"])

if page == "Home":
    # Introduction section
    st.header("Introduction")
    st.write("""This website focuses on the benefits of plant-based cellulose for cattle, goats, and sheep. ....""")
    # Additional content...

elif page == "Health Benefits":
    # Benefits section
    st.header("Health Benefits")
    st.write("""
    - Improves digestion in ruminants
    - Enhances nutrient absorption
    - Supports overall health and well-being
    """)

elif page == "Gallery":
    # Gallery section
    st.header("Gallery of Products Made from Plant Cellulose")
    # Image display logic...

elif page == "Contact":
    # Contact section
    st.header("Contact")
    st.write("For further information, contact RONI SAHA at ronisaha2025@gmail.com")
