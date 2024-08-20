def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error, Division by zero is not allowed, Try again."
    return result

#task 2
def calculator():
    print("Select operation: ")
    print("[A]dd")
    print("[S]ubtract")
    print("[M]ultiply")
    print("[D]ivide")

while True:
    math_choice = input("Enter choice [A] to Add, [S] to Subtract, [M] to Multiply), or [D] to Divide: ").upper() 
    

    if math_choice in ['A', 'S', 'M', 'D']:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid entry. Please enter numbers only.")
            continue
            
        if math_choice == 'A':
            print(f"The result is: {add(num1, num2)}")
        elif math_choice == 'S':
            print(f"The result is: {subtract(num1, num2)}")
        elif math_choice == 'M':
            print(f"The result is: {multiply(num1, num2)}")
        elif math_choice == 'D':
            print(f"The result is: {divide(num1, num2)}")
        
    else:
        print("Invalid input. Please select [A]dd, [S]ubtract, [M]ultiply, or [D]ivide.")
        
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break


if __name__ == "__main__":
    calculator()