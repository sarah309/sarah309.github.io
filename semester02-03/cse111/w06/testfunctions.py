# Python

import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_square_area(side_length):
    area = side_length ** 2
    return area

def calculate_areas(area_function, value):
    area = area_function(value)
    return area

def main():
    for i in range(20):
        circle_area = calculate_areas(calculate_circle_area, i)
        square_area = calculate_areas(calculate_square_area, i)
        print(f'Value: {i}, The square area is: {square_area}, circle area is: {circle_area:.2f}')


# calculate_circle_area(10)
main()