import sys

def area(L, W):
    areas = L * W
    return areas

def perimeter(L, W):
    perimeters = L + W + L + W 
    return perimeters

def volume(L, W, H):
    volumes = L * W * H
    return volumes

def surfaceArea(L, W, H):
    surfaceAreas = (L * W * 2) + (L * H * 2) + (W * H * 2)
    return surfaceAreas

L = int(input('Input the Length: '))
W = int(input('Input the width: '))
H = int(input('Input the Height: '))

solve = input('Input which function to solve? (area, perimeter, volume, or surface area): ')

if solve.lower() == 'area':
    print(f'The area is: {area(L, W)}')
elif solve.lower() == 'perimeter':
    print(f'The perimeter is: {perimeter(L, W)}')
elif solve.lower() == 'volume':
    print(f'The volume is: {volume(L, W, H)}')
elif solve.lower() == 'surface area':
    print(f'The surface area is: {surfaceArea(L, W, H)}')
else:
    print('Invalid input, please check your input and try again.')