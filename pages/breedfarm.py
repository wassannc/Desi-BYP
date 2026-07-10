import streamlit as st
from odk import get_form_data
from config import PROJECTS, FORMS

def show_breedfarm():

    st.title("Breed Farm Assessment")

    df = get_form_data(
        PROJECTS["Survey"]["project_id"],
        FORMS["breedfarm"]
    )

    st.dataframe(df)
