def average_of_numbers(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def input_numbers():
    user_numbers = []
    while True:
        entry = input("Enter a number (or type 'done' to finish): ")
        if entry.lower() == 'done':
            break
        try:
            number = float(entry)
            user_numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
    return user_numbers


numbers = input_numbers()


average = average_of_numbers(numbers)


print(f"The average of the entered numbers is: {average}")
