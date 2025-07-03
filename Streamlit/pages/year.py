import streamlit as st
from main import data

st.subheader("Average scores by year")
year_avg = data.groupby('Year').mean(numeric_only=True)
st.line_chart(year_avg)



year = data['Year'].unique()
st.subheader("Choose a year  to view ")

selected_year = st.selectbox("Select years", year)
group_students = data[data['Group'] == selected_year]['Student'].unique()

year_data = data[(data['Year'] == selected_year)]
subject_avg = year_data[['Math', 'Science', 'History', 'Geography', 'English']].mean()
st.bar_chart(subject_avg)

button = st.button("See Code")
if button:
    st.image("year.py.png")