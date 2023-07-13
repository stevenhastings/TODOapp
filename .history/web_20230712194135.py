import streamlit as st
import funcs

# Title
st.title('My To-Do List App')

# Text Input
todo = st.text_input('Enter a new task:')
st.write('You entered:', todo)

# Button - Add Task
if st.button('Add Task'):
    funcs.add_todo(todo)
    st.write(f'Task "{todo}" added successfully!')

# Display Todo List
st.subheader('Todo List:')
todos = funcs.read_todos()
for index, task in enumerate(todos, start=1):
    st.write(f'{index}. {task.strip()}')

# Checkbox - Show/Hide Todo List
if st.checkbox('Show/Hide Todo List'):
    for index, task in enumerate(todos, start=1):
        st.write(f'{index}. {task.strip()}')

# Radio Button - Status
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
    st.write('You are active!')
else:
    st.write('You are inactive!')

# Date Input - Due Date
import datetime
due_date = st.date_input('Due Date', datetime.date.today())

# Button - Clear Todos
if st.button('Clear Todos'):
    st.warning('Are you sure you want to clear all todos?')
    if st.button('Confirm'):
        funcs.clear_todos()
        st.success('Todos cleared successfully!')

# Button - Exit
if st.button('Exit'):
    st.warning('Are you sure you want to exit?')
    if st.button('Confirm'):
        st.balloons()
        st.stop()

