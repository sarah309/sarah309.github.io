# Basic function

def print_hello():
    print('Hello, World!')

print_hello()  # Call the function to print the message

print('Statement 1')
print_hello()
print('Statement 2')



# Receives parameters

def can_you_vote(name, age):
    if age >= 18:
        print(f'{name}, you can vote.')
    else:
        print(f'{name}, you cannot vote.')

print()
can_you_vote('John', 19)
can_you_vote(age = 91, name = 'Betty')

# can_you_vote('19, John Doe) does not work because John cannot be greater than 18


# Default values/Optional Parameters

def add_numbers(n1, n2, n3, n4=None, n5=None): #'string' would not work if n4 and n5 were set to 0
    total = n1 + n2 + n3 + n4 + n5
    return total

total = add_numbers(18, 19, 20, 21, 22)
print(f'The total is {total}.')
string = add_numbers("Betty", "Bobby", "Billy", "Brian", "Bekah")
print(string)


# Returns a value (Calculate)

