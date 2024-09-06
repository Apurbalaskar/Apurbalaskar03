def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

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

target = float(input("Enter the number to search for: "))

index = linear_search(numbers, target)

if index != -1:
    print(f"The number {target} is found at index {index}.")
else:
    print(f"The number {target} is not found in the list.")
