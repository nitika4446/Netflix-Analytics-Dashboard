import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("⭐ Ratings Insights")

df = load_data()

rating_data = (
    df["rating"]
    .value_counts()
    .reset_index()
)

fig = px.bar(
    rating_data,
    x="rating",
    y="count",
    title="Rating Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(
    rating_data.head(10),
    names="rating",
    values="count",
    title="Top Ratings"
)

st.plotly_chart(fig2, use_container_width=True)