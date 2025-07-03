import streamlit as st
from main import data

st.subheader("Average scores by year")
year_avg = data.groupby('Year').mean(numeric_only=True)
st.line_chart(year_avg)