print()
number = float(input('Please type a positive number: '))
while number <= 0:
    print('Sorry, that is not a positive number. Please try again.')
    number = float(input('Please type a positive number: '))
print (f'The number is: {number:.0f}')
print()
candy = input('May I have a piece of candy? ')
while candy.lower() == 'no':
    candy = input('May I have a piece of candy? ')
print ('Thank you.')
print()