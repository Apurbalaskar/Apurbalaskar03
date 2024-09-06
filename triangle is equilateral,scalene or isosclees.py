def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"
    else:
        return "Scalene"

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

triangle_type = classify_triangle(side1, side2, side3)

print(f"The triangle with sides {side1}, {side2}, and {side3} is {triangle_type}.")
