def calculate_rectangle_area(width, height):
    ''' Calculate the area of a rectangle with 
    the given width and height'''
    area = width * height
    return area

def calculate_square_area(size):
    ''' Calculate the area of a square with the given size'''
    area = calculate_rectangle_area(size, size)
    return area

def main():
    main_width = 5
    main_height = 2
    main_size = 7
    area_of_rectangle = calculate_rectangle_area(main_width, main_height)
    area_of_square = calculate_square_area(main_size)
    print(f'\nThe area of the rectangle is: {area_of_rectangle:.0f} units^2')
    print(f'The area of the square is: {area_of_square:.0f} units^2\n')

main()