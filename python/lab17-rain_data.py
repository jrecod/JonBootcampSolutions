import requests
import re
from datetime import datetime
import math

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/sylvan.rain')
# print(response.text)


# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date)
# # access the properties of that object
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00

# # turn the datetime object back into a string
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

response_list = re.findall(r'\d+-\w+-\d+\s+\d+', response.text)
new_list = []
rain_list = []

for response in response_list:
    #print(response)
    response = response.split()
    rain_list.append(int(response[1]))
    new_list.append(response)
for combo in new_list:
    combo[1] = int(combo[1])

def find_mean(new_list):
    total_sum = 0
    for combo in new_list:
        total_sum += combo[1]
    # print(total_sum)
    # print(len(new_list))
    return total_sum/len(new_list)
# find the variance
def find_variance(new_list, mean):
    total = 0
    for ele in new_list:
        total += (ele[1] - mean) ** 2
    return total / len(new_list)

# find the raniest day
def wettest_day(new_list):
    most_rain_date = new_list[rain_list.index(max(rain_list))][0]
    most_rain = max(rain_list)
    return most_rain_date, most_rain

mean = find_mean(new_list)
variance = find_variance(new_list, mean)
standard_deviation = math.sqrt(variance)
most_rain_date, most_rain = wettest_day(new_list)


print(f'Version 2, 1. The mean is {round(mean, 4)} tips')
print(f'Version 2, 2. The variance is {variance}')
print(f'Version 2, 3. The day that had the most rain was {most_rain_date} with {most_rain} tips')