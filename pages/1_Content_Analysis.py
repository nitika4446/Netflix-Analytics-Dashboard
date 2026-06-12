import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("📺 Content Analysis")

df = load_data()

content = (
    df.groupby("release_year")
    .size()
    .reset_index(name="Count")
)

fig = px.area(
    content,
    x="release_year",
    y="Count",
    title="Netflix Content Growth"
)

st.plotly_chart(fig, use_container_width=True)

movie_tv = (
    df["type"]
    .value_counts()
    .reset_index()
)

fig2 = px.bar(
    movie_tv,
    x="type",
    y="count",
    title="Movies vs TV Shows"
)

st.plotly_chart(fig2, use_container_width=True)