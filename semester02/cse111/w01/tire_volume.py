import math #math.pi
from datetime import datetime

w = float(input('\nPlease enter the width of the tire (in mm): '))
a = float(input('Please enter the the aspect ratio of the tire: '))
d = float(input('Please enter the diameter of the tire (in inches): '))

v = ((math.pi * (w * w) * a) * ((w * a) + (2540 * d)) / (10000000000))

print(f'\nThe approximate volume of the tire is {v:.2f} liters.\n')

buy = input('\nDo you want to buy tires with the dimensions that you entered? (yes/no): ')

phone_number = None

if buy.lower() == 'yes':
    phone_number = input('\nPlease enter your phone number: ')
    print(f'\nThank you, your phone number has been stored.\n')
else:
    print('\nThank you.\n')

with open('volumes.txt', 'at') as volumes:
    date = datetime.now()
    #date = datetime.now(tz=None)
    if phone_number is not None:
        print(f'''{date:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}''', file=volumes)
    else:
        print(f'''{date:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}''', file=volumes)