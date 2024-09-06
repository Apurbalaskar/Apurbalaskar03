def calculate_gravitational_force(m1, m2, d):
    G = 6.674 * (10 ** -11)
    force = G * (m1 * m2) / (d ** 2)
    return force

m1 = float(input("Enter the mass of the first object (in kg): "))
m2 = float(input("Enter the mass of the second object (in kg): "))
d = float(input("Enter the distance between the objects (in meters): "))


force = calculate_gravitational_force(m1, m2, d)


print(f"The gravitational force between the objects is {force:.2e} N.")
