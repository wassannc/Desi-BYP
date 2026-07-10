import streamlit as st

st.set_page_config(
    page_title="Desi Backyard Poultry",
    page_icon="🐔",
    layout="wide"
)

st.title("🐔 Desi Backyard Poultry")

menu = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "🗂 MIS Data"
    ]
)

if menu == "📊 Dashboard":

    st.header("Dashboard")

    st.info("Dashboard is under development.")

elif menu == "🗂 MIS Data":

    st.header("Breed Farm Assessment")

    st.write("Loading data...")
