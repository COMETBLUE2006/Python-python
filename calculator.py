import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Invalid input"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'sin' for sine")
    print("Enter 'cos' for cosine")
    print("Enter 'tan' for tangent")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "sin", "cos", "tan"):
        if user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter the angle in degrees: "))
        if user_input == "add":
            print("Result: " + str(add(num1, num2)))
        elif user_input == "subtract":
            print("Result: " + str(subtract(num1, num2)))
        elif user_input == "multiply":
            print("Result: " + str(multiply(num1, num2)))
        elif user_input == "divide":
            print("Result: " + str(divide(num1, num2)))
        elif user_input == "sqrt":
            print("Result: " + str(square_root(num1)))
        elif user_input == "sin":
            print("Result: " + str(sin(num1)))
        elif user_input == "cos":
            print("Result: " + str(cos(num1)))
        elif user_input == "tan":
            print("Result: " + str(tan(num1)))
    else:
        print("Invalid input")