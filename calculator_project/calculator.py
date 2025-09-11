"""
Calculator Program
Performs addition, subtraction, multiplication, and division
User chooses operation by selecting 1, 2, 3, or 4
"""

def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function"""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("           CALCULATOR MENU")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")
    print("="*50)

def main():
    """Main calculator program"""
    print("Welcome to the Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            elif choice in ['1', '2', '3', '4']:
                print(f"\nYou selected: {choice}")
                
                # Get two numbers from user
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Error: Please enter valid numbers!")
                    continue
                
                # Perform the selected operation
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                    
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                    
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                    
                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):  # Error message
                        print(f"\n{result}")
                    else:
                        print(f"\n{num1} ÷ {num2} = {result}")
                
                # Ask if user wants to continue
                continue_calc = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
                if continue_calc not in ['y', 'yes']:
                    print("Thank you for using the calculator. Goodbye!")
                    break
                    
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()