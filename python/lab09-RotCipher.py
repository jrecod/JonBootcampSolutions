def rot13(phrase):
    a = 'abcdefghijklmnopqrstuvwxyz'
    out_phrase = ''

    for char in phrase:
        out_phrase += a[(a.find(char)+13)%len(a)]
    return out_phrase

phrase = input('Please enter a phrase you would like to have ciphered: ')
print(rot13(phrase))

#add another function that asks for that takes input for rotation amount