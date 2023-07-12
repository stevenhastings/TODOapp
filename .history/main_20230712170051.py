from datetime import datetime

user_prompt = "Enter a todo: "
current_date = datetime.today().strftime('%Y-%m-%d')

while True:
    user_action = input("Would you like to add/remove/show/clear/edit/complete todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    match user_action:
        case "add":
            todo = input(user_prompt)
            
            with open("todos.txt", "a") as file:
                file.write(f"{todo} @ {current_date}\n")
            
            print(f"Added {todo} to the list of todos.")
        
        case "remove" | "delete" | "del":
            try:
                with open("todos.txt", "r") as file:
                    todos = file.readlines()

            except IOError:
                print("An error occurred while reading the todos file.")
                continue

            try:
                todo = input(f"{user_prompt} to remove: ")
                todos.remove(todo + "\n")
                print(f"Removed {todo} from the list of todos.")

                with open("todos.txt", "w") as file:
                    file.writelines(todos)

            except ValueError:
                print(f"{todo} was not found in the list of todos.")
        
        case "delete all todos":
            input("Are you sure you want to delete all todos? Press enter to continue...")

            with open("todos.txt", "w") as file:
                file.write("")
            
            print("All todos have been deleted.")
        
        case "show" | "list" | "display":
            print("Here are your todos:")

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            if len(todos) == 0:
                print("Your todo list is empty.")
                continue

            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo.strip()}")
        
        case "clear":
            input("Are you sure you want to clear all todos? Press enter to continue...")

            with open("todos.txt", "w") as file:
                file.write("")
            
            print("All todos have been cleared.")
        
        case "edit" | "change":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            print("Here are your todos:")
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo.strip()}")

            try:
                number = int(input("Enter the number of the todo to edit: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if number < 0 or number >= len(todos):
                print("Invalid todo number.")
                continue

            question = input(f"Are you sure you want to edit {todos[number].strip()}? (y/n) ").lower()

            if question == "n":
                continue
            elif question == "y":
                new_todo = input(f"{user_prompt} to replace {todos[number].strip()}: ")

            todos[number] = new_todo + " " + current_date + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Updated {todos[number].strip()} to {new_todo}.")
        
        case "complete" | "done":
            todo = input(f"{user_prompt} to complete: ")
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            try:
                todos.remove(todo + "\n")
                print(f"Completed {todo} at {datetime.today()}.")
                
                with open("todos.txt", "w") as file:
                    file.writelines(todos)

            except ValueError:
                print(f"{todo} was not found in the list of todos.")
        
        case _:
            print("Sorry, I don't understand that.")


        