import streamlit as st

# Title
st.title('My To-Do List App')

# Text Input
todo = st.text_input('Enter a new task:')
st.write('You entered: ', todo)

# Button
if st.button('Add Task'):
    st.write('Task added successfully!')

# Checkbox
if st.checkbox('Show/Hide'):
    st.write('Showing or Hiding Widget')

# Radio Button