from datetime import datetime


user_prompt = "Enter a todo: "

while True:
    user_action = input("Would you like to add/remove/show/clear/edit/complete todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    match user_action:
    
        case "add":
            todo = input(user_prompt)

            file = open("todos.txt", "a")
            file.write(f"{todo} @ {datetime.today()}\n")
            file.close()
        
            print(f"Added {todo} to the list of todos.")

        case "remove" | "delete" | "del":
            
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            try:
                todo = input(f"{user_prompt} to remove: ")
                todos.remove(todo + "\n")
                print(f"Removed {todo} from the list of todos.")
            except ValueError:
                print(f"{todo} was not found in the list of todos.")

        case "Deleta all todos" | "delete all todos" | "delete all":
            input("Are you sure you want to delete all todos? Press enter to continue...")

            file = open("todos.txt", "w")
            file.write("")
            file.close()
            
            print("All todos have been deleted.")

        case "show" | "list" | "display":
            print("Here are your todos:")

            file = open("todos.txt", "r")
            todos = file.readlines()
            
            if len(todos) == 0:
                print("Your todo list is empty.")
                continue

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

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input(f"Enter the number of the todo to edit: {            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")}"))
            number -= 1
            question = input(f"Are you sure you want to edit {todos[number]}? (y/n) ").lower()
            
            if question == "n":
                continue
            elif question == "y":
                new_todo = input(f"{user_prompt} to replace {todos[number]}: ")
            
            todos[number] = new_todo + "\n"

            print(f"Updated {todo} to {new_todo}.")
        
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

        