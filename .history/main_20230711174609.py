from datetime import datetime


user_prompt = "Enter a todo: "

while True:
    user_action = input("Would you like to add/remove/show/clear/edit/complete todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    match user_action:
    
        case "add":
            todo = input(user_prompt) + "\n"
            print(f"Added {todo} to the list of todos on {datetime.today()}.")

            file = open("todos.txt", "a")
            file.write(f"{todo} @ {datetime.today()}\n\n")
            file.close()

        case "remove" | "delete" | "del":
            todo = input(f"{user_prompt} to remove: ")

            file = open("todos.txt", "r")
            todos = file.readlines()
            
            try:
                todos.remove(todo)
                print(f"Removed {todo} from the list of todos.")
            
            except ValueError:
                print(f"{todo} was not found in the list of todos.")
            
            file.close()
            

    
        case "show" | "list" | "display":
            print("Here are your todos:")

            file = open("todos.txt", "r")
            todos = file.readlines()
            
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
            
            file.close()
    
        case "clear":
            input("Are you sure you want to clear all todos? Press enter to continue...")

            file = open("todos.txt", "r+")
            todos = file.readlines()
            todos.clear()
            file.close()
            print("All todos have been cleared.")
        
        case "edit" | "change":
            todo = input(f"Enter a todo to edit: ")
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            new_todo = []

            try:
                for item in todos:
                    if item == todo:
                        
                        new_todo.append(input(f"Enter a new todo for {todo}: "))
                    else:
                        new_todo.append(item)
                
                for index, item in enumerate(new_todo):
                    row = f"{index + 1}. {item}"
                    new_todo[index] = row

                print(f"Updated {todo} to {new_todo}.")

            except ValueError:
                print(f"{todo} was not found in the list of todos.")
        
        case "complete" | "done":
            todo = input(f"{user_prompt} to complete: ")
            file = open("todos.txt", "r")
            todos = file.readlines()

            try:
                todos.remove(todo)
                print(f"Completed {todo} at {datetime.today()}.")
            except ValueError:
                print(f"{todo} was not found in the list of todos.")
            
            file.close()
    
        case _:
            print("Sorry, I don't understand that.")

        