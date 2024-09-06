def find_largest_of_three(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest = find_largest_of_three(num1, num2, num3)

print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")
