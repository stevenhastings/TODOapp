from funcs import perform_action

while True:
    user_action = input("Would you like to add/remove/show/clear/edit/complete todos? ").lower()
    user_action = user_action.strip()
    
    if user_action == "exit":
        break
    
    perform_action(user_action)

        