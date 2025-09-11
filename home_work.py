"""
Write a program in python to compute the volume and circumference of a sphere. The user
will ask for the radius as the input
"""
import math

# Get radius from user
radius = float(input("Enter the radius of the sphere: "))

volume = (4/3) * math.pi * (radius ** 3)

circumference = 2 * math.pi * radius

print(f"\nSphere Calculations:")
print(f"Radius: {radius}")
print(f"Volume: {volume:.2f} cubic units")
print(f"Circumference: {circumference:.2f} units")
