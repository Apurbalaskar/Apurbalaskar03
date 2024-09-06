def sum_of_digits(number):
    total = 0

    number = abs(number)
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = int(input("Enter a number: "))

digit_sum = sum_of_digits(number)


print(f"The sum of the digits of {number} is {digit_sum}.")
