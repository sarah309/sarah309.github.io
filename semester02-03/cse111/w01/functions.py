#built in function
print()
int()

#Library / Module Functions

#Object Methods

import math

x = 4
print(math.sqrt(x))

my_sentence = 'The following questions are available'
print(my_sentence.upper())

print()

#Optional Arguments - range()

for i in range(4, 10, 2):
    print(i)

x = 123.45678
print(round(x, 2))


#Named parameters - print sep=

my_sentence = 'The following questions are available'
print(my_sentence.upper(), end = '--------------------')
print(my_sentence.lower())

print(1, 2, 3, 4, 5, sep= '------------------')

#datetime module

from datetime import datetime

now = datetime.now()

print(datetime.date(now))
print(f'{datetime.date(now): %Y %m %d %H:%M}')

#Write to a file

with open('testfileoutput1.txt', 'wt') as filehandle: #w will overwrite, a will add onto file
    for i in range(10):
        now = datetime.now()
        print(f'Current time: {now}', file=filehandle)