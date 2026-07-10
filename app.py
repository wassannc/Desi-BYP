import streamlit as st
import pandas as pd
from odk import get_form_data
from utils import standardize_dataframe
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

    frames = []

    for project_name, project in PROJECTS.items():

        df = get_form_data(
            project["project_id"],
            FORMS["breedfarm"]
        )

        df = standardize_dataframe(
            df,
            project_name=project_name,
            district=project["district"]
        )

        frames.append(df)

    master_df = pd.concat(
        frames,
        ignore_index=True,
        sort=False
    )

    st.write(f"Total Records : {len(master_df)}")

    st.dataframe(master_df)
