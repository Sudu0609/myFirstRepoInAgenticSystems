import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_and_process_data

st.title("📊 Simple Data Dashboard")

# Load data
df, posts_per_user = fetch_and_process_data()

# Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Bar Chart
st.subheader("Posts per User")
fig1, ax1 = plt.subplots()
posts_per_user.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Histogram
st.subheader("Post Length Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(df["post_length"], bins=20)
st.pyplot(fig2)