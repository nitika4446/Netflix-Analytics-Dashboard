import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.title("🎭 Genre Analytics")

df = load_data()

genres = []

for item in df["listed_in"]:
    genres.extend(item.split(","))

genre_df = (
    pd.Series(genres)
    .str.strip()
    .value_counts()
    .reset_index()
)

genre_df.columns = ["Genre", "Count"]

fig = px.treemap(
    genre_df,
    path=["Genre"],
    values="Count",
    title="Genre Distribution"
)

st.plotly_chart(fig, use_container_width=True)