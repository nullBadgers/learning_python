alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 3

new_message = " "

message = input("Enter message: ").strip()

for character in message:
    position  = alphabet.find(character)
    new_position = (position + key) % 26
    new_character = alphabet[new_position]
    print("New character is:", new_character)

