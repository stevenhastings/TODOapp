from datetime import datetime

user_prompt = "Enter a todo: "
current_date = datetime.today().strftime('%Y-%m-%d')

def read_todos():
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

def remove_todo(todo):
    """
    remove_todo: Removes a todo from the todo list.

    Parameters
    ----------
    todo : str
        The todo to remove.

    Returns
    -------
    bool
        True if the todo was removed, False otherwise.
    """

    todos = read_todos()
    try:
        todos.remove(todo + "\n")
        write_todos(todos)
        return True
    except ValueError:
        return False

def edit_todo(todo, new_todo):
    """
    edit_todo: Edits a todo in the todo list.

    Parameters
    ----------
    todo : str
    new_todo : str
         
    Returns
    -------
    bool
        True if the todo was edited, False otherwise.

    """

    todos = read_todos()

    try:
        index = todos.index(todo + "\n")
        todos[index] = new_todo + " " + current_date + "\n"
        write_todos(todos)
        return True
    
    except ValueError:
        return False


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

def exit_program():
    """
    exit_program: Exits the program.
    
    """

    exit(0)

