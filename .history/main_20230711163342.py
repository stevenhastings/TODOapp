user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Would you like to add/remove/show/clear todos? ").lower()

    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
            print(f"Added {todo} to the list of todos.")
        case "remove":
            todo = input(f"{user_prompt} to remove: ")
            try:
                todos.remove(todo)
                print(f"Removed {todo} from the list of todos.")
            except ValueError:
                print(f"{todo} was not found in the list of todos.")