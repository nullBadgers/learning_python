#get user email address and strip away the blank spaces

email = input('What is your email address?: ').strip()


#slice username

user = email[:email.index('@')]


#slice domain name

domain = email[email.index('@') +1 :]


#format message

output = 'Your username is {} and your domain is {}'.format(user, domain)


#display output

print(output)