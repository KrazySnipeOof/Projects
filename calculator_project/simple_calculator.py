"""
Simple Calculator Program
User chooses operation by selecting 1, 2, 3, or 4
"""
print("1. Addition")
print("2. Subtraction") 
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        
    elif choice == '3':
        result = num1 * num2
        print(f"{num1} × {num2} = {result}")
        
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"{num1} ÷ {num2} = {result}")
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")