change = [
        #0           #1
    ['half-dollar', 50], #0
    ['quarter', 25], #1
    ['dime', 10], #2
    ('nickel', 5), #3
    ('penny', 1)
    ]


print(change[2
print(change[2][0])
change = (50, 25, 10, 5, 1)
q = 25
d = 10
n = 5
p = 1
total = float(input('What is the amount your would like change for?')) * 100

quarters = int(total // q) 
quarters_remainder = int(total % q)

dimes = (quarters_remainder // d) 
dimes_remainder = int(quarters_remainder % d)

nickels = (dimes_remainder // n) 
nickels_remainder = int(dimes_remainder % n)

pennies = (nickels_remainder // p) 


print(f'quarters {quarters}')
# print(f'pennies left over {quarters_remainder}')

print(f'dimes {dimes}')
# print(f'pennies left over {dimes_remainder}')

print(f'nickels {nickels}')
# print(f'pennies left over {nickels_remainder}')

print(f'pennies {pennies}')
