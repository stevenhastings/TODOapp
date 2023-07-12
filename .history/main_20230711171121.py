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
            try:

        case "show" | "list" | "display":
            print("Here are your todos:")
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
    
        case "clear":
            input("Are you sure you want to clear all todos? Press enter to continue...")
            todos.clear()
            print("All todos have been cleared.")
        
        case "edit" | "change":
        
        case "complete" | "done":
    
        case _:
            print("Sorry, I don't understand that.")

        