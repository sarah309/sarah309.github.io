import math

pi = math.pi

def calculate_circle_area(radius):
    area = pi * radius ** 2
    return area

def main():
    circle_area = calculate_circle_area(10)
    print(f'\nArea of the circle: {circle_area:.2f} units^2\n')

main()