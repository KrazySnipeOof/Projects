"""
Check if a number is divisible by both 3 and 7
"""

number = int(input("Enter a number: "))

divisible_by_3 = number % 3 == 0
divisible_by_7 = number % 7 == 0
divisible_by_both = divisible_by_3 and divisible_by_7

print(f"\nNumber: {number}")
print(f"Divisible by 3? {'YES' if divisible_by_3 else 'NO'}")
print(f"Divisible by 7? {'YES' if divisible_by_7 else 'NO'}")
print(f"Divisible by BOTH 3 and 7? {'YES' if divisible_by_both else 'NO'}")

if divisible_by_both:
    print(f"\n✓ {number} is divisible by both 3 and 7!")
    print(f"  {number} ÷ 3 = {number // 3}")
    print(f"  {number} ÷ 7 = {number // 7}")
else:
    print(f"\n✗ {number} is NOT divisible by both 3 and 7")
