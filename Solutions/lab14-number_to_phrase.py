num = int(input('Please enter a number to be converted into words: '))

d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 
      6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'elevin',
      12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen',
      17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'
      }

d2 = { 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 
       7 : 'seventy', 8 : 'eighty', 9 : 'ninety' }

d3 = { 1 : 'one hundred', 2 : 'two hundred', 3 : 'three hundred', 4: 'four hundred', 5 : 'five hundred', 6 : 'six', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety' }


if num < 20:
    print (d[num])
elif num >= 20 and num <= 99:
    print (f'{d2[num//10]} {d[num%10]}')
elif num//10%10 == 1:
    print(f'{d3[num//100]} {d[num%100]}')
elif num >=100:
    print (f'{d3[num//100]} {d2[(num//10)%10]} {d[num%10]}')

# print(num % 10)
# print((num//10)%10)