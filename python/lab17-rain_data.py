import requests
import re
from datetime import datetime
import math

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/sylvan.rain')
# print(response.text)


# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')
#print(date)
# access the properties of that object
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

response_list = re.findall(r'\d+-\w+-\d+\s+\d+', response.text)
new_list = []
for response in response_list:
    #print(response)
    response = response.split()
    new_list.append(response)
# print(new_list)

total_sum = 0
for ele in new_list:
    total_sum += int(ele[1])
print(total_sum)
print(len(new_list))
mean = total_sum/len(new_list)
print(mean)
#find the varience
for 


