print()
first_number = input('What is the first number? ')
second_number = input('What is the second number? ')
if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')
if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')
if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')
print()
animal = input('What is your favorite animal? ')
if animal.lower() == 'cow':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')
    animal = input("So what do you think my favorite animal is? I'll give you a hint...gentle giant: ")
    if animal.lower() == 'cow':
        print('You guessed it!')
    else:
        print("Oof, the correct answer is cow. Was my hint not obvious?")