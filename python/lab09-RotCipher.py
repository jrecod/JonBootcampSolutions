def rot13(phrase):
    a = 'abcdefghijklmnopqrstuvwxyz'
    out_phrase = ''

    for char in phrase:
        out_phrase += a[(a.find(char)+(rotation))%len(a)]
    return out_phrase

phrase = input('Please enter a phrase you would like to have ciphered: ')
rotation = int(input('Please enter the amount of times you would like to rotate: '))
print(rot13(phrase))

#add another function that asks for that takes input for rotation amount