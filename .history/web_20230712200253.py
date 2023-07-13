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

# Edit Todo
if st.button('Edit Todo'):
    edit_mode = True
else:
    edit_mode = False

if edit_mode:
    selected_index = st.number_input('Enter the number of the task to edit:', min_value=1, max_value=len(todos), value=None, step=1)
    if selected_index:
        edit_todo = todos[selected_index - 1].strip()
        updated_todo = st.text_input('Enter the updated task:', value=edit_todo)
        if st.button('Update'):
            funcs.edit_todo(selected_index - 1, updated_todo)
            st.write(f'Task "{edit_todo}" updated to "{updated_todo}" successfully!')
            edit_mode = False


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