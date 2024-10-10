import random

def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        number = random.uniform(0, 100)
        rounded_number = round(number, 1)
        numbers_list.append(rounded_number)



def main():
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers {numbers}')
    append_random_numbers(numbers)
    print(f'numbers {numbers}')
    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')

if __name__ == "__main__":
    main()