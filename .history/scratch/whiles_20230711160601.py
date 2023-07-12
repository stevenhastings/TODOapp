password = input("Enter password: ")
tries = 0

while password != "superstructure":
    if tries == 3:
        print("Too many tries, exiting...")
        break
    print("Wrong password!")
    tries += 1
    password = input("Enter password: ")

print("Correct password!")