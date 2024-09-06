def reverse_number(number):
    reversed_number = 0

    number = abs(number)
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number

number = int(input("Enter a number: "))


reversed_num = reverse_number(number)

print(f"The reverse of {number} is {reversed_num}.")
