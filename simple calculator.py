def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."


print("Select operation:")
print("1. Addition (add)")
print("2. Subtraction (subtract)")
print("3. Multiplication (multiply)")
print("4. Division (divide)")

operation = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = calculator(operation, num1, num2)


print(f"The result of the operation is: {result}")
