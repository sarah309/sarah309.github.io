#Python

import math

def calculate_circle_area(radius):
    if radius <= 0:
        raise AssertionError
    assert radius >= 0
    area = math.pi * radius ** 2
    return area

def main():
    radius = float(input("\nEnter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle is {area:.5f} units^2.\n")

if __name__ == "__main__":
    main()