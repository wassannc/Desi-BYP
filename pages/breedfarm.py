import streamlit as st
from odk import get_form_data
from config import PROJECTS, FORMS

def show_breedfarm():

    st.header("🗂 MIS Data")

    st.subheader("Breed Farm Assessment")

    project = "Survey"

    df = get_form_data(
        PROJECTS[project]["project_id"],
        FORMS["breedfarm"]
    )

    st.dataframe(df)

    st.write("Records :", len(df))
