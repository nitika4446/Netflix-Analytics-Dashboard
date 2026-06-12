import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.title("⏱ Watch Time Insights")

df = load_data()

movies = df[df["type"] == "Movie"].copy()

movies["duration"] = (
    movies["duration"]
    .str.replace(" min", "")
)

movies["duration"] = pd.to_numeric(
    movies["duration"],
    errors="coerce"
)

fig = px.histogram(
    movies,
    x="duration",
    nbins=30,
    title="Movie Duration Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(
    movies,
    y="duration",
    title="Duration Spread"
)

st.plotly_chart(fig2, use_container_width=True)