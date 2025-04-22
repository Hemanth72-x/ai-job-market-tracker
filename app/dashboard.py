import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Job Market Tracker", layout="wide")

# Load data
df = pd.read_csv("ai_jobs.csv")

# Simulated coordinates for cities (for optional map)
city_coords = {
    "Bengaluru": [77.5946, 12.9716],
    "Hyderabad": [78.4867, 17.3850],
    "Mumbai": [72.8777, 19.0760],
    "Pune": [73.8567, 18.5204],
    "Delhi": [77.1025, 28.7041]
}

# Title
st.title("📊 AI Job Market Tracker")
st.caption("Explore AI-related job trends by title, company, location, keywords, and more.")

# Layout: 3 dropdown filters
col1, col2, col3 = st.columns(3)

with col1:
    selected_title = st.selectbox("🎯 Filter by Job Title", ["All"] + sorted(df["Title"].unique().tolist()))

with col2:
    selected_company = st.selectbox("🏢 Filter by Company", ["All"] + sorted(df["Company"].unique().tolist()))

with col3:
    selected_location = st.selectbox("📍 Filter by Location", ["All"] + sorted(df["Location"].unique().tolist()))

# Text search
search_term = st.text_input("🔎 Search in Job Descriptions")

# Apply filters
filtered_df = df.copy()

if selected_title != "All":
    filtered_df = filtered_df[filtered_df["Title"] == selected_title]

if selected_company != "All":
    filtered_df = filtered_df[filtered_df["Company"] == selected_company]

if selected_location != "All":
    filtered_df = filtered_df[filtered_df["Location"] == selected_location]

if search_term:
    filtered_df = filtered_df[filtered_df["Summary"].str.contains(search_term, case=False, na=False)]

# Show results
st.subheader(f"📄 Showing {len(filtered_df)} job(s)")
st.dataframe(filtered_df)

# Bar Charts
st.subheader("📈 Job Titles Frequency")
st.bar_chart(filtered_df["Title"].value_counts())

st.subheader("🏢 Companies Hiring")
st.bar_chart(filtered_df["Company"].value_counts())

st.subheader("📍 Locations")
st.bar_chart(filtered_df["Location"].value_counts())

# Word Cloud
st.subheader("☁️ Common Keywords in Job Descriptions")

summary_text = " ".join(filtered_df["Summary"].dropna().tolist())
if summary_text:
    wordcloud = WordCloud(width=800, height=300, background_color='white').generate(summary_text)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No job summaries to generate word cloud.")

# Map (Optional)
df["lat"] = df["Location"].map(lambda x: city_coords.get(x, [0, 0])[1])
df["lon"] = df["Location"].map(lambda x: city_coords.get(x, [0, 0])[0])

st.subheader("🗺️ Jobs by City (Simulated Map)")
st.map(df[["lat", "lon"]])