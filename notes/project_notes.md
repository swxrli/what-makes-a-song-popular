# Project Notes: What Makes a Song Popular?

## Project Objective

The objective of this project was to explore a dataset of 113,999 Spotify songs and identify whether song characteristics such as danceability, energy, loudness, tempo, and genre have any relationship with popularity.

---

## Dataset Overview

- Total songs: 113,999
- Features: 20
- Missing values: None after data cleaning

---

## Analysis Performed

- Checked dataset structure and cleaned missing values.
- Identified the most frequently occurring artists.
- Explored genre distribution.
- Analyzed the relationship between audio features and popularity.
- Created a correlation heatmap.
- Ranked features by correlation with popularity.
- Compared popularity of explicit and non-explicit songs.
- Examined the distribution of popularity scores.

---

## Key Findings

### Most Frequent Artists

The dataset contains multiple songs from artists such as:

- The Beatles
- George Jones
- Stevie Wonder
- Linkin Park
- Ella Fitzgerald

This represents the composition of the dataset rather than artist popularity.

---

### Correlation Analysis

No audio feature showed a strong correlation with popularity.

The strongest positive correlations were:

- Loudness
- Explicit content
- Danceability

The strongest negative correlation was:

- Instrumentalness

Overall, all correlations were weak, suggesting that popularity depends on many factors beyond audio features.

---

### Genre Analysis

Genres with the highest average popularity included:

- Pop-film
- K-pop
- Chill
- Sad
- Grunge

This shows that some genres in the dataset have higher average popularity than others.

---

### Explicit vs Non-Explicit Songs

Average popularity:

- Explicit songs: **36.45**
- Non-explicit songs: **32.94**

Explicit songs have a slightly higher average popularity.

---

### Popularity Distribution

- **16,019 songs** have a popularity score of **0**.
- Only **2 songs** have a popularity score of **100**.

The distribution is heavily skewed toward lower popularity values.

---

## Visualizations Created

- Popularity Distribution
- Correlation Heatmap
- Feature Correlation Ranking
- Explicit vs Non-Explicit Popularity

---

## Conclusion

The analysis shows that no single audio feature can reliably explain song popularity. Although loudness, danceability, and explicit content have slightly positive relationships with popularity, the correlations are weak.

This suggests that external factors such as artist reputation, marketing, listener preferences, recommendation algorithms, and current trends likely play a much larger role in determining a song's popularity.

---

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Matplotlib
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Correlation Analysis
- Git
- GitHub