password = input("Enter password: ")
tries = 0

while password != "superstructure":
    
    print("Wrong password!")
    password = input("Enter password: ")

print("Correct password!")