import streamlit as st
from pages.dashboard import show_dashboard
from pages.breed_farm import show_breed_farm

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Desi Backyard Poultry",
    page_icon="🐔",
    layout="wide"
)

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("🐔 Desi Backyard Poultry")
st.markdown("---")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Section",
    [
        "📊 Dashboard",
        "🗂 MIS Data"
    ]
)

# ----------------------------------------------------
# Navigation
# ----------------------------------------------------
if menu == "📊 Dashboard":
    show_dashboard()

elif menu == "🗂 MIS Data":
    show_breed_farm()
