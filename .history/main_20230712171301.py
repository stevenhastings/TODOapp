from datetime import datetime

user_prompt = "Enter a todo: "
current_date = datetime.today().strftime('%Y-%m-%d')

def read_todos():
    """
    Reads the todos file and returns a list of todos.
    If the file does not exist, an empty list is returned.
    
    Returns:
        list: A list of todos.
    
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
    Writes the todos to the todos file.
    
    Args:
        todos (list): A list of todos.
    
    """
    
    with open("todos.txt", "w") as file:
        file.writelines(todos)

def add_todo():
    """
    Adds a todo to the todos file.
    
    """

    todo = input(user_prompt)
    with open("todos.txt", "a") as file:
        file.write(f"{todo} @ {current_date}\n")
    print(f"Added {todo} to the list of todos.")

def remove_todo():
    """
    Removes a todo from the todos file.
    
    """
    todos = read_todos()
    todo = input(f"{user_prompt} to remove: ")
    try:
        todos.remove(todo + "\n")
        print(f"Removed {todo} from the list of todos.")
        write_todos(todos)
    except ValueError:
        print(f"{todo} was not found in the list of todos.")

def delete_all_todos():
    """
    Deletes all todos from the todos file.
    
    """
    input("Are you sure you want to delete all todos? Press enter to continue...")
    write_todos([])
    print("All todos have been deleted.")

def show_todos():
    """
    Shows all todos in the todos file.
    
    """
    print("Here are your todos:")
    todos = read_todos()
    if len(todos) == 0:
        print("Your todo list is empty.")
        return
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo.strip()}")

def clear_todos():
    """
    Clears all todos from the todos file.
    
    """
    input("Are you sure you want to clear all todos? Press enter to continue...")
    write_todos([])
    print("All todos have been cleared.")

def edit_todo():
    """
    Edits a todo in the todos file.

    """
    todos = read_todos()
    print("Here are your todos:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo.strip()}")
    try:
        number = int(input("Enter the number of the todo to edit: ")) - 1
        if number < 0 or number >= len(todos):
            print("Invalid todo number.")
            return
        question = input(f"Are you sure you want to edit {todos[number].strip()}? (y/n) ").lower()
        if question == "n":
            return
        elif question == "y":
            new_todo = input(f"{user_prompt} to replace {todos[number].strip()}: ")
        todos[number] = new_todo + " " + current_date + "\n"
        write_todos(todos)
        print(f"Updated {todos[number].strip()} to {new_todo}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def complete_todo():
    todo = input(f"{user_prompt} to complete: ")
    todos = read_todos()
    try:
        todos.remove(todo + "\n")
        print(f"Completed {todo} at {datetime.today()}.")
        write_todos(todos)
    except ValueError:
        print(f"{todo} was not found in the list of todos.")

while True:
    user_action = input("Would you like to add/remove/show/clear/edit/complete todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    match user_action:
        case "add":
            add_todo()
        
        case "remove" | "delete" | "del":
            remove_todo()
        
        case "delete all todos":
            delete_all_todos()
        
        case "show" | "list" | "display":
            show_todos()
        
        case "clear":
            clear_todos()
        
        case "edit" | "change":
            edit_todo()
        
        case "complete" | "done":
            complete_todo()
        
        case _:
            print("Sorry, I don't understand that.")



        