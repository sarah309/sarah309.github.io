print ()
first = input ('What is your first name? ')
print()
last = input ('What is your last name? ')
print()
#print('Your name is ' + last + ', ' + first + ' ' + last + '.') 
#line 6 gets same result, but line 7 is easier to read
output = f'Your name is {last}, {first} {last}.'
print(output)