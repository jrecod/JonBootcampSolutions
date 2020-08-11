import requests
import string


def clean_text(dirty_text):
    '''
    1. Remove all new line characters from the text
    2. Remove all punctuation from text
    3. Make the text lowercase
    4. Convert the text into a list of words
    Return a list of lower case words with no punctuation or whitespace
    
    How now, Brown Cow? = ['how', 'now', 'brown', 'cow]
    '''
    book = dirty_text
    deleted_char = ':;1234567890!@#$%^&*()-_=+[]/?.," '
    replaced_char = ' ' * len(deleted_char)
    table = str.maketrans(deleted_char, replaced_char)
    stripped_book = book.translate(table)
    clean_text = stripped_book.lower().split()
    return clean_text
    

def wordfreq(words):
    wordfreq = {}
    for w in words:
        if w in wordfreq:
            wordfreq[w] += 1
        else:
            wordfreq[w] = 1
    return wordfreq
response = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt')
words = clean_text(response.text)
# print(words)
counts = wordfreq(words)

words = list(counts.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])