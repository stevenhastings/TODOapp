user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Would you like to add/remove/show/clear todos? ").lower()

    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
            