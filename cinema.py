films = {
    "Star Trek": [15,3],
    "Home Alone":[18,3],
    "Bourne":[15,2],
    "Tarzan":[15,3],
    }

while True:
    choice = input("What do you want to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

    if age >= films[choice][0]:

        num_seats = films[choice][1]

        if num_seats > 0:
            print("Enjoy the film!")
            films[choice][1] = films[choice][1] - 1
        else:
            print("Sorry, no more tickets")
    else:
        print("Sorry no, too young.")
