# Grading

# prompt user to enter score and convert the string number to an integer number
score = int(input("Enter your score: "))



# compare the score to the grade
if score >= 90 and score <= 100:
    result = f'You got an A'
elif score >= 80 and score <= 89:
    result = f'You got a B'
elif score >= 70 and score <= 79:
    result = f'You got a C'
elif score >= 60 and score <= 69:
    result = f'You got a D'
else:
    result = f'You got a F'

# display the result
print(result)
