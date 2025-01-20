# Python

def print_error_message(message, error):
    print(f'{message}, Error is: {error}')
    print('Please input a valid age')


# Read input - handle exceptions

def receive_age():
    done = False
    while not done:
        try:
            age = int(input('Please input your age (0-125): '))
            if -1 < age < 126:
                done = True
            else:
                print('Please input a valid age')
        except ValueError as ve:
            print_error_message('Invalid age', ve)
        except KeyboardInterrupt as ki:
            print_error_message('Nice try, input valid age', ki)
        except EOFError as ee:
            print_error_message('You\'re pretty smart, but need valid age', ee)
        except AssertionError as ae:
            pass
        finally:
            print('This is the finally block')
    return age

# Other exceptions - type error and divide by zero

def test_exceptions():
    try:
        my_data = [1, 2, 3, 4, 5]
        print(my_data[6])
        my_friends = {'Bob': 2910401345, 'Shannon': 1023948031}
        print(my_friends['Billy'])
        number = 13 / 0
    except IndexError as ie:
        print_error_message('Bad Index', ie)
    except KeyError as ke:
        print_error_message('Bad Key', ke)


def main():
    age = receive_age()
    print(f'Your age is: {age}')

main()