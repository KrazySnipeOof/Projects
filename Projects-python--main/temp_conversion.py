import sys

temp = int(input('Insert a temperature: '))

temp_type = input('Convert to Celsius or Fahrenheit: ')

def convertToFahrenheit(temp):
    Fahrenheit = temp * (9 / 5) + 32
    return Fahrenheit

def convertToCelsius(temp):
    Celsius = (temp - 32) * (5 / 9)
    return Celsius

if temp_type == 'Fahrenheit':
    result = convertToCelsius(temp)
    print(f'The {temp} degrees Fahrenheit converted to Celsius is {round(result, 2)}')
elif temp_type == 'Celsius':
    result = convertToFahrenheit(temp)
    print(f'The {temp} degrees Celsius converted to Fahrenheit is {round(result, 2)}')
else:
    print('Error. Please insert "Celsius" or "Fahrenheit".')
