def find_largest_element(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


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


largest = find_largest_element(numbers)

if largest is not None:
    print(f"The largest element in the list is: {largest}")
else:
    print("The list is empty, no largest element.")
