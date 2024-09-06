def process_number(number):
    if number > 15:
        difference = number - 15
        result = 2 * difference
    else:
        difference = 15 - number
        result = 4 * difference

    print(f"The result is: {result}")


number = float(input("Enter a number: "))

process_number(number)
