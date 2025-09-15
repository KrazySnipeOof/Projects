import sys

s = input('Input a string ')

def right_justify(s):
    string_space = 70 - len(s)
    new_str = ' ' * string_space + s
    return new_str

# Call the function and print the result
#result = right_justify(s)
print(right_justify(s))
