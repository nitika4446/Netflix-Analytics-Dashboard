import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)

df = load_data()

st.title("🎬 Netflix Analytics Dashboard")
st.markdown("Analyze Netflix Content Trends, Ratings & Viewer Insights")

# ======================
# KPI SECTION
# ======================

col1, col2, col3, col5 = st.columns(4)

with col1:
    st.metric("Total Titles", len(df))

with col2:
    st.metric(
        "Movies",
        len(df[df["type"] == "Movie"])
    )

with col3:
    st.metric(
        "TV Shows",
        len(df[df["type"] == "TV Show"])
    )

with col4:
    st.metric(
        "Countries",
        df["country"].nunique()
    )

st.divider()

# ======================
# CONTENT DISTRIBUTION
# ======================

content_type = df["type"].value_counts().reset_index()
content_type.columns = ["Type", "Count"]

fig = px.pie(
    content_type,
    names="Type",
    values="Count",
    title="Movies vs TV Shows"
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# YEARLY CONTENT TREND
# ======================

year_data = (
    df.groupby("release_year")
    .size()
    .reset_index(name="Count")
)

fig2 = px.line(
    year_data,
    x="release_year",
    y="Count",
    title="Content Released Over Years"
)

st.plotly_chart(fig2, use_container_width=True)