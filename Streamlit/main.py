import streamlit as st
import pandas as pd

data = pd.read_csv('school_scores.csv')
st.write(data)