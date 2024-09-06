import cmath


def find_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c


    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2



a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))


if a == 0:
    print("Coefficient 'a' should not be zero for a quadratic equation.")
else:

    root1, root2 = find_roots(a, b, c)


    print(f"The roots of the quadratic equation are: {root1} and {root2}")
