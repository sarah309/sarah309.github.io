# Python

import math

def calculate_square_area(side_length):
    area = side_length ** 2
    return area

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # square_areas = list(map(calculate_square_area, data))
    square_areas = list(map(lambda side_length : side_length ** 2, data))

    print(square_areas)

    circle_areas = list(map(lambda radius : math.pi * radius ** 2, data))
    print(circle_areas)

    even_numbers = list(filter(lambda x : not x % 2, data))
    print(even_numbers)

main()