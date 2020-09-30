import random

eyes = [':', ';', '8', '=']
nose = ['-', '^', ' ']
mouth = [']', '}', '[', '{', '(', ')', '@', '3', 'D']


i = 0
while i < 5:
    emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    i += 1
    print(emoticon)


vert_eyes_list = ['-', 'O', 'o', '0', 'X', 'x', '~', '*']
vert_mouth_list = ['_', '.', '>', 'u']
sides_list = [
    ['[', ']'],
    ['(', ')'],
    ['{', '}'],
    ['<([', '])>'],
]


sides = random.choice(sides_list)
vert_eyes = random.choice(vert_eyes_list)
vert_mouth = random.choice(vert_mouth_list)

vert_emoticon = sides[0] + vert_eyes + vert_mouth + vert_eyes + sides[1]

print(vert_emoticon)