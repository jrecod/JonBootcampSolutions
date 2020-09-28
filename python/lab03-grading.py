# Grading

# prompt user to enter score and convert the string number to an integer number
score = int(input("Enter your score: "))
qualifier = ''


# compare the score to the grade
if score >= 90 and score <= 100:
    if score % 10 <= 4:
        qualifier = '-'
    elif score % 10 >= 6:
        qualifier = '+'
    result = f'You got an A{qualifier}'
elif score >= 80 and score <= 89:
    if score % 10 <= 4:
        qualifier = '-'
    elif score % 10 >= 6:
        qualifier = '+'
    result = f'You got a B{qualifier}'
elif score >= 70 and score <= 79:
    if score % 10 <= 4:
        qualifier = '-'
    elif score % 10 >= 6:
        qualifier = '+'
    result = f'You got a C{qualifier}'
elif score >= 60 and score <= 69:
    if score % 10 <= 4:
        qualifier = '-'
    elif score % 10 >= 6:
        qualifier = '+'
    result = f'You got a D{qualifier}'
else:
    result = f'You got a F'

# display the result
print(result)
