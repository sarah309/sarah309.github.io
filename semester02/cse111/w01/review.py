x = 10 # Set x to 10

my_comment = '''This is a docstring or a multiline comment
that can run
across multiple lines (not a true comment)'''

print(my_comment)

# Ctrl + / comments out code

# variables have a name, type and value
# decimal numbers (1/3, 234.234, 23/8, etc.) are floats, 10 is an integer
# boolean is True or false
# string example my_name = 'Bob'
# list example my_data = [1, 2, 3, 4] my_data_names = ['Bob', 'Tara']

x = 120
print(f"{x} is the value of x")

age = input('Please input your age: ')
print(f"Your age is: {age}")

x = 0
x = x + 1
x += 1 # this is the same as above



x = 7

if x == 10:
    print(f'x is {x}')
elif x < 0:
    print('x < 0')
elif x < 4:
    print('x < 4')
elif x < 6:
    print('x < 6')
else:
    print('x is between 0 and 10')


#Logical - and and or
y = 111111111
z = 20
if y == 12 or y == 13:
    print('y is either 12 or 13')

#if put "y == 12 or 13" y for any number other than 0 would run the print


#Loops
done = False
while not done:
    age = int(input('please enter your age: '))
    if age >= 0 and age <= 120:
        done = True

my_data = [1, 79, 84, 133, 9, -34]
for data in my_data:
    print(data)
print(data)

for number in range (998, -234, -2):
    print(number)
    print(f'{number + 1}')

#Functions