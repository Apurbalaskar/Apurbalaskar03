import math


def calculate_volume_of_sphere(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


radius = 6  # in cm


volume = calculate_volume_of_sphere(radius)


print(f"The volume of the sphere with radius {radius} cm is {volume:.2f} cubic centimeters.")
