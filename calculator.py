#CodSoft Task 2
"""Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result."""


num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

print("Choose an operation: ")
operator = input("(+ - * /): ")

if operator == "+":
    res = num1 + num2
    print(res)
elif operator == "-":
    res = num1 - num2
    print(res)
elif operator == "*":
    res = num1 * num2
    print(res)
elif operator == "/":
    res = num1 / num2
    print(res)
else:
    print(f"{operator} is not a valid operator")