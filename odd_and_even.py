import sys

def isOdd(num):
    if num % 2 == 1:
        return f'the {num} is odd'
    else:
        return f'the {num} is even'

def isEven(num):
    if num % 2 == 0:
        return f'the {num} is even'
    else:
        return f'the {num} is odd'

num = int(input('Insert a number: '))
type_check = input('Do you want to see if the number is odd or even? (type "odd" or "even"): ')

if type_check.lower() == 'odd':
    print(isOdd(num))
elif type_check.lower() == 'even':
    print(isEven(num))
else:
    print('Invalid input. Please type "odd" or "even"')





