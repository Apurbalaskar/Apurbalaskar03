def calculate_sum_and_average(num1, num2, num3):
    # Calculate sum
    total = num1 + num2 + num3
    # Calculate average
    average = total / 3
    return total, average


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


total, average = calculate_sum_and_average(num1, num2, num3)


print(f"Sum of the numbers: {total}")
print(f"Average of the numbers: {average}")
