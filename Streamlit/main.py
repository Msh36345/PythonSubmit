import streamlit as st
import pandas as pd

data = pd.read_csv('school_scores.csv')

st.write("# Data Student")
st.write(data)

button = st.button("See Code")
if button:
    st.image("main.py.png")