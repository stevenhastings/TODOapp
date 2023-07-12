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
    with open("todos.txt", "w") as file:
        file.writelines(todos)

def add_todo(todo):
    todos = read_todos()
    todos.append(f"{todo} @ {current_date}\n")
    write_todos(todos)

def remove_todo(todo):
    """remove_todo: Removes a todo from the todo list.

    Parameters
    ----------
    todo :

    Returns
    -------
    _type_
        _description_
    """
    todos = read_todos()
    try:
        todos.remove(todo + "\n")
        write_todos(todos)
        return True
    except ValueError:
        return False

def edit_todo(todo, new_todo):
    """edit_todo _summary_

    _extended_summary_

    Parameters
    ----------
    todo : _type_
        _description_
    new_todo : _type_
        _description_

    Returns
    -------
    _type_
        _description_
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
    """clear_todos _summary_

    _extended_summary_
    """
    write_todos([])

def get_todo_list():
    """get_todo_list _summary_

    _extended_summary_

    Returns
    -------
    _type_
        _description_
    """
    todos = read_todos()
    return [todo.strip() for todo in todos]

def exit_program():
    # Add any cleanup or finalization tasks here, if needed.
    exit(0)

