import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "netflix_titles.csv"
    )

    df.fillna("Unknown", inplace=True)

    return df