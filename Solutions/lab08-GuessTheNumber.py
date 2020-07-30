import random

answer = random.randint(1,10)
atempt = 0
guess = int(input ('Guess the right number between 1 and 10: '))
atempt += 1 

while guess != answer:
    if guess < answer:
        print('The number is higher. Try agian.')
        guess = int(input ('Guess the right number between 1 and 10: '))
        atempt += 1 
    else:
        print('The number is lower. Try again.')
        guess = int(input ('Guess the right number between 1 and 10: '))
        atempt += 1 

print ('You got it! It took you ' + str(atempt) + ' tries to figure it out!')


