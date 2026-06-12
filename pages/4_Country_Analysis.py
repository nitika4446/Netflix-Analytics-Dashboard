import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.title("🌍 Country Analysis")

df = load_data()

countries = []

for item in df["country"]:
    countries.extend(str(item).split(","))

country_df = (
    pd.Series(countries)
    .str.strip()
    .value_counts()
    .head(20)
    .reset_index()
)

country_df.columns = ["Country", "Count"]

fig = px.bar(
    country_df,
    x="Country",
    y="Count",
    title="Top Content Producing Countries"
)

st.plotly_chart(fig, use_container_width=True)