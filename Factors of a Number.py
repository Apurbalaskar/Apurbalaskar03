def print_factors(number):
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


number = int(input("Enter a number: "))


factors = print_factors(number)

print(f"The factors of {number} are: {', '.join(map(str, factors))}.")
