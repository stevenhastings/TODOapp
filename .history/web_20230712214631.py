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
todos = funcs.get_todo_list()
for index, task in enumerate(todos, start=1):
    st.write(f'{index}. {task}')

# Checkbox - Show/Hide Todo List
if st.checkbox('Show/Hide Todo List'):
    for index, task in enumerate(todos, start=1):
        st.write(f'{index}. {task}')

# Button - Remove Task
if st.button('Remove Task'):
    task_index = st.number_input('Enter the task number to remove:', min_value=1, max_value=len(todos), value=1)
    confirm_remove = st.button('Confirm')
    if confirm_remove:
        task_removed = funcs.remove_todo_index(task_index - 1)
        if task_removed:
            st.write(f'Task {task_index} removed successfully!')
        else:
            st.write(f'Invalid task number.')

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
