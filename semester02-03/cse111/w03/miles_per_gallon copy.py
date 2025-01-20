# Python

# This file will calculate the miles per gallon of a trip


def calculate_miles_per_gallon(starting_mile, ending_mile, gallons_used):
    '''Calculate and return the miles per gallon (mph)
    start_milage - the starting milage on the car before the strip
    end_milage - the ending milage ont he car after the trip
    gallons - the number of gallons of gas used on the trip.
    mpg = end - start / gallons'''
    miles_traveled = ending_mile - starting_mile
    mpg = gallons_used / miles_traveled
    return mpg

def obtain_user_input():
    '''Obtain the starting mile, ending mile, and gallons used from the user and return them.'''
    starting_mile = int(input('Input car mileage before trip started: '))
    ending_mile = int(input('Input car ending mileage after the trip: '))
    gallons_used = int(input('Input the number of gallons of gas used on the trip: '))
    return ending_mile, starting_mile, gallons_used


def main():
    '''Ask the user for the needed items and call calculate_miles_per_gallong
    to get the miles per gallon (mpg)'''

    starting_mile, ending_mile, gallons_used = obtain_user_input()

    miles_per_gallon = calculate_miles_per_gallon(gallons_used, starting_mile, ending_mile)
    print(f'The miles per gallon for this trip was: {miles_per_gallon:.2f}')


if __name__ == '__main__':
    main()