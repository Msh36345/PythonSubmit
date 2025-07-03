import streamlit as st
from main import data

st.subheader("Average scores per subject")
subject_avg = data.drop(columns=['Group', 'Student']).groupby('Year').mean()
st.line_chart(subject_avg)