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

# Buttons
st.button('Simple Button')
if st.button('About'):
    st.text('Streamlit is Cool')

# Text Area
message = st.text_area('Enter your message', 'Type here...')
if st.button('Submit'):
    st.text('Your message: ' + message)

# Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# Time Input
the_time = st.time_input('The time is', datetime.time())

# Displaying JSON
st.text('Display JSON')
st.json({'name': 'John', 'age': 30})

# Display Raw Code
st.text('Display Raw Code')
st.code('import numpy as np')

# Display Raw Code
with st.echo():
    # This will also be shown
    import pandas as pd
    df = pd.DataFrame()

    