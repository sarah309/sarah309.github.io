
# Dictionary
def test_dictionary():
    my_friends = {'Bob': 5551212, 'Billy': 1234567, 'Jenny': 8675309}
    # Print dictionary
    print(my_friends)

    # Print names
    print(my_friends.keys())

    # Print numbers
    print(my_friends.values())

    # Print dictionary
    print(my_friends.items())

    for key in my_friends.keys():
        # Prints the value (number) at each key (name)
        print(my_friends[key])

    for value in my_friends.values():
        # can print value
        print(value)
        # print(my_friends[value])
        # above comment crashes because cannot find key from value (reverse lookup)

    print(my_friends['Jenny'])

    for key, value in my_friends.items():
        print(key, value)

# print
    # Appends Betty
    my_friends['Betty'] = 9876543
    print(my_friends)

    # Because Bob already exists, this new value overrides existing value for Bob
    my_friends['Bob'] = 8887777
    print(my_friends)

    # Saves value of Jenny if you call old_girlfriend, although will not show up in dictionary my_friends
    old_girlfriend = my_friends.pop('Jenny')
    print(old_girlfriend)
    print(my_friends)

    # Removes Billy forever
    my_friends.pop('Billy')

    my_friends['Bubba'] = 876039
    print(my_friends)

    if 'Carl' in my_friends:
        print(my_friends['Carl'])
    else:
        my_friends['Carl'] = 9001212

    if 'Bubba' in my_friends:
        print(my_friends['Bubba'])

    print(my_friends)

    periodic_table = {'Ag', ['Silver', 23.234]}


def main():
    test_dictionary()

main()