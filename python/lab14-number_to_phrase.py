num = int(input('Please enter a number to be converted into words: '))

d = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 
      6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven',
      12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen',
      17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'
      }

d2 = { 2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 : 'fifty', 6 : 'sixty', 
       7 : 'seventy', 8 : 'eighty', 9 : 'ninety' }

d3 = { 1 : 'one hundred', 2 : 'two hundred', 3 : 'three hundred', 4: 'four hundred', 5 : 'five hundred', 6 : 'six hundred', 7 : 'seven hundred', 8 : 'eight hundred', 9 : 'nine hundred' }

# Checks to see if the num is less than 20. Then uses d.
if num == 0:
    print('zero')
elif num < 20:
    print (d[num])
# Checks to see if the num is between 20 and 99 to decide whether or not to use teens.
elif num <= 99:
    print (f'{d2[num//10]} {d[num%10]}')
    print('1here')
# 
elif num//10%10 == 0:
    print(f'{d3[num//100]} {d[num%10]}')
    print('2here')
# Checks to see if hundred input has a teen. If so it doesn't us d2.
elif num//10%10 == 1:
    print(f'{d3[num//100]} {d[num%100]}')
    print('3here')
# Checks if it is greater than 100.
elif num >=100:
    print (f'{d3[num//100]} {d2[(num//10)%10]} {d[num%10]}')
    print('4here')

