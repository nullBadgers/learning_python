# the list
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]

while True:
    print("Hi! I am Travis")
    name = input("What is your name? ").strip().capitalize()

# this checks if the name entered exists in the list above
    if name in known_users:
        print(f"Welcome back {name}!")
        remove = input("Do you want to be removed from the Matrix (y/n)?: ").strip().lower()
# this will then ask the user if they want to be removed
        if remove == "y":
            known_users.remove(name)
            print("You've been removed from the Matrix!")
        elif remove == "n":
            print("No problem, I didn't want you to go")

# this will then ask the user if they wish to be added to the list
    else:
        print(f"Sorry, don't know who you are {name}!")
        add_me = input("Do you want to be added TO THE MATRIX? (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print(f"You are now in the Matrix {name}!")
        elif add_me == "n":
            print("No worries then")
