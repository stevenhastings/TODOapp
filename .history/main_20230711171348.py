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
            todo = input(user_prompt)
            print(f"Removed {todo} from the list of todos on {datetime.today()}.")

        case "show" | "list" | "display":
            print("Here are your todos:")
            file = open("todos.txt", "r")
            print(file.read())
            file.close()
    
        case "clear":
            print("Cleared all todos.")
            file = open("todos.txt", "w")
            file.write("")
            file.close()
        
        case "edit" | "change":
            todo = input(f"{user_prompt} to edit: ")
            

            print(f"Edited {todo} on {datetime.today()}.")
        
        case "complete" | "done":
    
        case _:
            print("Sorry, I don't understand that.")

        