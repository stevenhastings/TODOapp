import streamlit as st
import funcs

todos = funcs.read_todos()

# Title
st.title('My To-Do List App')
st.subheader('Organize and keep track of your tasks!')
st.write("""This is a data-driven web app built with Streamlit. 
         It uses a SQLite database to store your tasks.
          Feel free to add, delete, and clear tasks.""")

# Text Input
todo = st.text_input('Enter a new task:')
st.write('You entered:', todo)

# Button
if st.button('Add Task'):
    st.write(f'Task "{todo}" added successfully!')

for todo in todos:
    st.checkbox(todo['task'])

# Display Todo List
st.subheader('Todo List:')
todos = [1, 2, 3]  # Replace with your actual todo list
for index, task in enumerate(todos, start=1):
    st.write(f'{index}. {task}')

# Checkbox
if st.checkbox('Show/Hide Todo List'):
    for index, task in enumerate(todos, start=1):
        st.write(f'{index}. {task}')

# Radio Button
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
    st.write('You are active!')
else:
    st.write('You are inactive!')

# Select Box
occupation = st.selectbox('Your Occupation', ['Programmer', 'Data Scientist', 'Doctor', 'Businessman'])
st.write('You selected:', occupation)

# Slider
level = st.slider('What is your level?', 1, 5)

# Date Input
import datetime
due_date = st.date_input('Due Date', datetime.date.today())

# Button to Clear Todos
if st.button('Clear Todos'):
    st.warning('Are you sure you want to clear all todos?')
    if st.button('Confirm'):
        st.success('Todos cleared successfully!')

# Button to Exit
if st.button('Exit'):
    st.warning('Are you sure you want to exit?')
    if st.button('Confirm'):
        st.balloons()
        st.stop()
