# Stage 1 + Stage 2 Calculator

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Performing calculation
if operator == '+':
    result = num1 + num2
    print("Result =", result)

elif operator == '-':
    result = num1 - num2
    print("Result =", result)

elif operator == '*':
    result = num1 * num2
    print("Result =", result)

elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
        print("Result =", result)

else:
    print("Invalid operator. Please use +, -, *, or /.")
    result = None

# Stage 2: Check if result is positive, negative, or zero
if result is not None:
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
