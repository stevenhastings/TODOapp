import streamlit as st
import funcs

# Set page title and favicon
st.set_page_config(page_title="My Todo List App", page_icon="📝")

# Apply custom theme
st.markdown(
    """
    <style>
        .streamlit-container {
            max-width: 800px;
            padding: 2rem;
        }
        .streamlit-button.primary-button {
            background-color: #FF5722;
            color: white;
        }
        .title-wrapper {
            margin-bottom: 2rem;
        }
        .footer {
            font-size: 14px;
            color: gray;
            text-align: center;
            margin-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title('My Todo List App')

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
    st.write(f'{index}. {task.strip()}')

# Checkbox - Show/Hide Todo List
if st.checkbox('Show/Hide Todo List'):
    for index, task in enumerate(todos, start=1):
        st.write(f'{index}. {task.strip()}')

# Date Input - Due Date
import datetime
due_date = st.date_input('Due Date', datetime.date.today())

# Button - Remove Task
if st.button('Remove Task'):
    selected_index = st.number_input('Enter the number of the task to remove:', min_value=1, max_value=len(todos), step=1)
    if st.button('Remove', key='remove_button'):
        if selected_index:
            try:
                removed_task = todos[selected_index - 1].strip()
                funcs.remove_todo_index(selected_index - 1)
                st.write(f'Task "{removed_task}" removed successfully!')
            except IndexError:
                st.write('Invalid task number.')
        else:
            st.write('Please select a task number.')

# Button - Clear Todos
if st.button('Clear Todos'):
    st.warning('Are you sure you want to clear all todos?')
    if st.button('Confirm', key='clear_button'):
        funcs.clear_todos()
        st.success('Todos cleared successfully!')

# Button - Exit
if st.button('Exit'):
    st.warning('Are you sure you want to exit?')
    if st.button('Confirm', key='exit_button'):
        st.balloons()
        st.stop()

# Footer
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<p class="footer">Thanks for using My Todo List App!</p>', unsafe_allow_html=True)
