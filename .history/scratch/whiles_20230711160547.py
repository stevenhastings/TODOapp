password = input("Enter password: ")
tries = 0

while password != "superstructure":
    print("Wrong password!")
    tries += 1
    password = input("Enter password: ")

print("Correct password!")