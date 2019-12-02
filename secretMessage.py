alphabet = 'abcdefghjiklmnopqurstuvwxyz'
key = 3
#secret key

character = input ('Please enter a letter: ')

position = alphabet.find(character)
print(position)

newPosition = (position + key) % 26
print(newPosition)



