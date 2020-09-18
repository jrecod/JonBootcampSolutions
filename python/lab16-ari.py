import re
import requests

response = requests.get('http://www.gutenberg.org/cache/epub/17192/pg17192.txt')

res = len(re.findall(r'\w+', response))

print(str(res))

# how many characters.
z  
# how many words.

# how many sentences.
