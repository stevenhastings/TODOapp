import streamlit as st
import funcs

# Initialize session state
if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None

# Title
st.title('My To-Do List App')

# Text Input
todo = st.text_input('Enter a new task:')
st.write('You entered:', todo)

# Button - Add Task
if st.button('Add Task'):
    try:
        funcs.add_todo(todo)
        st.write(f'Task "{todo}" added successfully!')
    except Exception as e:
        st.write(f'Error adding task: {str(e)}')

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
    st.session_state.edit_mode = True

if st.session_state.edit_mode:
    selected_index = st.number_input('Enter the number of the task to edit:', min_value=1, max_value=len(todos), value=st.session_state.selected_index or 1, step=1)
    st.session_state.selected_index = selected_index
    if st.button('Select Task'):
        st.session_state.edit_mode = False

if st.session_state.edit_mode:
    selected_index = st.session_state.selected_index
    if selected_index:
        edit_todo = todos[selected_index - 1].strip()
        updated_todo = st.text_input('Enter the updated task:', value=edit_todo, key=f"edit-{selected_index}")
        if st.button('Update'):
            try:
                funcs.edit_todo(selected_index - 1, str(updated_todo))  # Convert to string
                st.write(f'Task "{edit_todo}" updated to "{updated_todo}" successfully!')
                st.session_state.edit_mode = False
                st.session_state.selected_index = None
            except Exception as e:
                st.write(f'Error updating task: {str(e)}')

# Date Input - Due Date
import datetime
due_date = st.date_input('Due Date', datetime.date.today())

# Button - Clear Todos
if st.button('Clear Todos'):
    st.warning('Are you sure you want to clear all todos?')
    if st.button('Confirm'):
        try:
            funcs.clear_todos()
            st.success('Todos cleared successfully!')
        except Exception as e:
            st.write(f'Error clearing todos: {str(e)}')

# Button - Exit
if st.button('Exit'):
    st.warning('Are you sure you want to exit?')
    if st.button('Confirm'):
        st.balloons()
        st.stop()


