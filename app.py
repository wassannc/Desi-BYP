import streamlit as st
from odk import get_form_data
from config import PROJECTS, FORMS

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

    df = get_form_data(
        PROJECTS["Survey"]["project_id"],
        FORMS["breedfarm"]
    )

    st.write(f"Total Records : {len(df)}")

    st.dataframe(df)
