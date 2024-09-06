def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


number = int(input("Enter a number: "))


factorial = factorial_iterative(number)


print(f"The factorial of {number} is {factorial}.")
