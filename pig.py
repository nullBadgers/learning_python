# get sentence from user

original = input("Please enter a sentence: ").lower().strip()

# split sentence into words

words = original.split()

# loop through words and covert to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        cons = word[vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

print(new_words)

# if it starts with a vowel, just add 'yay'
# otherwise, move the first consonent cluster to end and add 'ay'

# stick words back together

output = " ".join(new_words)

# output final string

print(output)