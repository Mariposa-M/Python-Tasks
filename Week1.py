# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

def calculator(value1, value2, operator):
    if (operator == "+"):
        calculation = int(value1) + int(value2)
    elif (operator == "-"):
        calculation = int(value1) - int(value2)
    elif (operator == "*"):
        calculation = int(value1) * int(value2)
    elif (operator == "/"):
        calculation = int(value1) / int(value2)
    else: 
        print('Please enter a valid operator')
    return calculation

print('Welcome to this Simple Calculator')
print('Please make sure you\'re not adding zero as second value in division')
value1 = input('Enter the first value: ')
value2 = input('Enter the second value: ')
operator = input('Enter the operator: + Or - Or * Or /: ')
print(calculator(value1, value2, operator))
