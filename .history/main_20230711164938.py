user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Would you like to add/remove/show/clear/edit todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    match user_action:
    
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
            print(f"Added {todo} to the list of todos.")
    
        case "remove" | "delete" | "del":
            todo = input(f"{user_prompt} to remove: ")
            try:
                todos.remove(todo)
                print(f"Removed {todo} from the list of todos.")
            except ValueError:
                print(f"{todo} was not found in the list of todos.")
    
        case "show" | "list" | "display":
            print("Here are your todos:")
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
    
        case "clear":
            input("Are you sure you want to clear all todos? Press enter to continue...")
            todos.clear()
            print("All todos have been cleared.")
        
        case "edit" | "change":
            todo = input(f"{user_prompt} to edit: ")
            try:
                index = todos.index(todo)
                new_todo = input(f"Enter new todo for {todo}: ")
                todos[index] = new_todo
                print(f"Updated {todo} to {new_todo}.")
            except ValueError:
                print(f"{todo} was not found in the list of todos.")
        
        case complete
    
        case _:
            print("Sorry, I don't understand that.")

        