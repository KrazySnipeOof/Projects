"""
Write a program in python to check if the last digit of a number is divisible by 7.
"""

number = int(input("Enter a number: "))
last_digit = number % 10
is_divisible = last_digit % 7 == 0

print(f"Number: {number}")
print(f"Last digit: {last_digit}")
print(f"Is last digit divisible by 7? {'YES' if is_divisible else 'NO'}")
