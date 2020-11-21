import re
import requests
import math

response = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt')
response.encoding = 'utf-8'
text = response.text
# count all the characters.

def character_count(text):
    characters = re.findall(r'[a-zA-Z]', text)
    return len(characters)
# count all the one or more non-whitespace characters
def word_count(text):
    word = re.findall(r'[\S+]', text)
    return len(word)
# count the sentence by finding all the punctuation.
def sentence_count(text):
    sentence = re.findall('[\.!?]', text)
    return len(sentence)

ari = 4.71*(character_count(text)/word_count(text)) + .5*(word_count(text)/sentence_count(text)) - 21.43

# print(character_count(text))
# print(sentence_count(text))
# print(word_count(text))

rounded = math.ceil(ari)
if rounded > 14:
    rounded = 14
# print(rounded)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
print("The ARI for The Raven, by Edgar Allan Poe is", rounded,". This coresponds to a", ari_scale[rounded]['grade_level'], "level of difficulty. That is suitable for an average person", ari_scale[rounded]['ages'], "years old." )