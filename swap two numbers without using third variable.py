def swap_numbers(a, b):

    a = a + b
    b = a - b
    a = a - b
    return a, b


a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))


print(f"Before swapping: a = {a}, b = {b}")


a, b = swap_numbers(a, b)


print(f"After swapping: a = {a}, b = {b}")
