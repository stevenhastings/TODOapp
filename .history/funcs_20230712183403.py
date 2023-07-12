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
    todos = read_todos()
    try:
        todos.remove(todo + "\n")
        write_todos(todos)
        return True
    except ValueError:
        return False

def clear_todos():
    write_todos([])

def get_todo_list():
    todos = read_todos()
    return [todo.strip() for todo in todos]
