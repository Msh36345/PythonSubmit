import streamlit as st
from main import data

st.subheader("Average scores by year")
year_avg = data.groupby('Year').mean(numeric_only=True)
st.line_chart(year_avg)

years = data['Year'].unique()
st.subheader("Choose a year to view")
selected_year = st.selectbox("Select year", years)

year_data = data[data['Year'] == selected_year]
subject_avg = year_data[['Math', 'Science', 'History', 'Geography', 'English']].mean()

st.subheader(f"Average subject scores for {selected_year}")
st.bar_chart(subject_avg.to_frame(name="Average"))

button = st.button("See Code")
if button:
    st.image("Subject-of-study.py.png")