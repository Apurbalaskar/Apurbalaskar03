def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))


simple_interest = calculate_simple_interest(principal, rate, time)


print(f"The Simple Interest for a principal of {principal} at a rate of {rate}% for {time} years is {simple_interest:.2f}.")
