#ask for name
name = input('What is your name?: ')

#ask for age
age = int(input('How old are you?: '))

#ask for cityS
city = input('Where do you live?: ')


#ask for hobbies
hobby = input('What things do you enjoy?: ')


#create output text
string = 'Your name is {}, you are {} years old. You live in {} and you enjoy. {}'

output = string.format(name, age, city, hobby)


#print output to screen
print(output)