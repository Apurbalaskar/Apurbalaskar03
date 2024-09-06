def multiplication_table(n, upto=10):
    print(f"Multiplication table for {n}:")
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number: "))

upto = int(input("Enter the number of terms for the table (default is 10): ") or 10)

multiplication_table(number, upto)
