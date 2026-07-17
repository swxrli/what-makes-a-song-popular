import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="What Makes a Song Popular?",
    page_icon="🎵",
    layout="wide"
)

# Page title
st.title("🎵 What Makes a Song Popular?")

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Sidebar
st.sidebar.title("🎛 Dashboard Controls")

st.sidebar.markdown("Use the filters below to explore the dataset.")

genres = sorted(df["track_genre"].unique())

selected_genre = st.sidebar.selectbox(
    "Select a Genre",
    ["All"] + genres
)

if selected_genre != "All":
    df = df[df["track_genre"] == selected_genre]

# Display basic information
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎵 Songs", f"{len(df):,}")

with col2:
    st.metric("📊 Features", df.shape[1])

with col3:
    st.metric(
        "⭐ Avg Popularity",
        f"{df['popularity'].mean():.2f}"
    )


left, right = st.columns(2)

with left:
    st.header("Popularity Distribution")
    st.bar_chart(df["popularity"].value_counts().sort_index())

with right:
    st.header("Top 10 Genres by Average Popularity")

    genre_popularity = (
        df.groupby("track_genre")["popularity"]
          .mean()
          .sort_values(ascending=False)
          .head(10)
    )

    st.bar_chart(genre_popularity)

st.subheader("First 5 Rows")

st.dataframe(df.head())


st.header("Correlation Heatmap")

st.image(
    "visuals/correlation_heatmap.png",
    caption="Correlation between Spotify audio features"
)

st.header("Feature Correlation Ranking")

st.image(
    "visuals/popularity_correlation_ranking.png",
    caption="Correlation of each feature with popularity"
)


st.header("💡 Key Insights")

st.info(
    f"""
- Dataset currently contains **{len(df):,} songs**.
- Average popularity is **{df['popularity'].mean():.2f}**.
- Average danceability is **{df['danceability'].mean():.2f}**.
- Average energy is **{df['energy'].mean():.2f}**.
"""
)