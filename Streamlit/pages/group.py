import streamlit as st
from main import data

st.subheader("Average scores by Group")
group_avg = data.groupby('Group').mean(numeric_only=True)
st.bar_chart(group_avg)

button = st.button("See Code")
if button:
    st.image("group.py.png")