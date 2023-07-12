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
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
    st.write('You are active!')
else:
    st.write('You are inactive!')

# Select Box
occupation = st.selectbox('Your Occupation', ['Programmer', 'Data Scientist', 'Doctor', 'Businessman'])
st.write('You selected: ', occupation)

# Multi Select
location = st.multiselect('Where do you work?', ('London', 'New York', 'Accra', 'Kiev', 'Nepal'))
st.write('You selected: ', len(location), 'locations')

# Slider
level = st.slider('What is your level?', 1, 5)
    