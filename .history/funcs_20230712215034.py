from datetime import datetime

user_prompt = "Enter a todo: "
current_date = datetime.today().strftime('%Y-%m-%d')

def read_todos():
    """
    read_todos : _read_todos 

    Returns
    -------
    list
        The list of todos.

    """

    try:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        return todos
    
    except IOError:
        print("An error occurred while reading the todos file.")
        return []

def write_todos(todos):
    """
    write_todos : _write_todos

    Parameters
    ----------
    todos : list
        The list of todos to write.

    """

    with open("todos.txt", "w") as file:
        file.writelines(todos)

def add_todo(todo):
    """
    add_todo : Adds a todo to the todo list. 

    Parameters
    ----------
    todo : str
        The todo to add.

    """

    todos = read_todos()
    todos.append(f"{todo} @ {current_date}\n")
    write_todos(todos)

def remove_todo_index(index):
    """
    remove_todo_index: Removes a todo from the todo list based on its index.

    Parameters
    ----------
    index : int
        The index of the todo to remove.

    Returns
    -------
    bool
        True if the todo was removed, False otherwise.
    """

    todos = read_todos()
    todos[index] = f""


def edit_todo(index, updated_todo):
    """
    edit_todo : Edits a todo in the todo list.

    Parameters
    ----------
    index : int, optional
        The index of the todo to edit.
    updated_todo : str
        The updated todo.

    """
    todos = read_todos()
    todos[index] = f"{updated_todo.strip()} @ {datetime.today().strftime('%Y-%m-%d')}\n"
    write_todos(todos)

def clear_todos():
    """
    clear_todos: Clears all todos from the todo list.
    
    """

    write_todos([])

def get_todo_list():
    """
    get_todo_list: Gets the list of todos.

    Returns
    -------
    list
        The list of todos.

    """

    todos = read_todos()
    return [todo.strip() for todo in todos]
