# random password generator



import random
import string

password_characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation

password_characters = list(password_characters)

print(random.choice(password_characters))

# string to integer 
length = int(input('How long would you like your random password to be?: '))

i = 0
password = ""
while i < length :
    password += random.choice(password_characters)
    i += 1


print(password)