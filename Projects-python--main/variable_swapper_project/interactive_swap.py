"""
Write a program in python to swap the values of two variables. [If a=5 and b=3; after
swapping, a will become 3 and b will become 5
"""

a = input("Enter value for variable 'a': ")
b = input("Enter value for variable 'b': ")

print(f"\nBefore swapping:")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

print(f"\nAfter swapping:")
print(f"a = {a}")
print(f"b = {b}")
