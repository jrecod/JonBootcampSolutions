import random

eyes = [':', ';', '8', '=']
nose = ['-', '^', ' ']
mouth = [']', '}', '[', '{', '(', ')', '@', '3', 'D']

emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)

print(emoticon)