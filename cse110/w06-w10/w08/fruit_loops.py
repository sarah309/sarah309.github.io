'''
Part 1

word = 'fruit loops'

for letter in word:
    if letter == 'o':
        print(letter.capitalize())
    else:
        print(letter)

Part 2

word = 'fruit loops'
favorite_letter = input('What is your favorite letter? ')
for letter in word:
    if letter == favorite_letter:
        print(letter.capitalize(), end='')
    else:
        print(letter, end='')

Part 3

word = 'fruit loops'
favorite_letter = input('What is your favorite letter? ')
for letter in word:
    if letter == favorite_letter:
        print('_', end='')
    else:
        print(letter, end='')

Stretch

'''

print()
number = int(input('Please enter a number: '))
quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
new_quote = ''
count = 0
for letter in quote:
    count += 1
    if count % number == 0:
        print(letter.capitalize(), end='')
    else:
        print(letter, end='')
print(new_quote)
print()

another_number = input('Would you like to enter another number? ')
print()

while another_number.lower() == 'yes':
    number = int(input('Please enter a number: '))
    new_quote = ''
    count = 0
    for letter in quote:
        count += 1
        if count % number == 0:
            print(letter.capitalize(), end='')
        else:
            print(letter, end='')
    print(new_quote)
    print()
    another_number = input('Would you like to enter another number? ')
    print()
if another_number.lower() != 'yes':
    print('Goodbye')
    print()