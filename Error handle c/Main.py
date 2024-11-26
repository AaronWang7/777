try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == "/":
     
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Invalid operation. Please choose from +, -, *, /.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
