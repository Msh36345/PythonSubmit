import streamlit as st
from main import data

groups = data['Group'].unique()

st.subheader("Choose a group and a student to view all subjects over years")

selected_group = st.selectbox("Select group", groups)
group_students = data[data['Group'] == selected_group]['Student'].unique()
selected_student = st.selectbox("Select student", group_students)

student_data = data[(data['Group'] == selected_group) & (data['Student'] == selected_student)]
st.line_chart(student_data.set_index('Year')[['Math', 'Science', 'History', 'Geography', 'English']])