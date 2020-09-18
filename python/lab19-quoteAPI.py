import requests
import json
# V1
# response = requests.get('https://favqs.com/api/qotd')

# data = response.json()

# print(data['quote']['body'])

# print(data['quote']['author'])

# V2
while True:
    filt = input('What is your keyword: ')
    page = '1'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'filter': filt, 'page': page}

    response = requests.get('https://favqs.com/api/quotes', headers = headers)

    data = response.json()

    print(data




