import sys

upTo = int(input('Input a number: '))


def fizzBuzz(upTo):
    if upTo % 3 and upTo % 5 == 0:
       return print('FizzBuz')
        
    elif upTo % 3 == 0:
       return print('Fizz')
    elif upTo % 5 ==0:
        print('Buzz')
    else:
     print(f'The number {upTo} is not divisible by 3 nor 5')
   


print(fizzBuzz(upTo))