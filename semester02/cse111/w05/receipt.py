import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}

    try:
        with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[key_column_index]
                products_dict[key] = row
        return products_dict
    
    except FileNotFoundError as file_not_found:
        print(f'Error: missing file\n{file_not_found}')

def main():
    products_dict = read_dictionary('products.csv', 0)

    print('Inkom Emporium\n')

    subtotal = 0
    sales_tax_rate = 0.06
    total_items = 0
    ordered_items = []

    current_date_and_time = datetime.now()
    
    try:
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                total_items += quantity
                product_details = products_dict[product_number]
                product_name = product_details[1]
                product_price = float(product_details[2])
                if current_date_and_time.weekday() in [1, 2]:
                    product_price *= 0.9
                item_total = product_price * quantity
                subtotal += item_total
                ordered_items.append(f'{product_name}: {quantity} @ {product_price:.2f}')
        
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        for item in ordered_items:
            print(item)
        print()

        print(f'Number of Items: {total_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')

        print('\nThank you for shopping at the Inkom Emporium.')
        print(f'{current_date_and_time:%A %I:%M %p}')

    except FileNotFoundError as file_not_found:
        print(f'Error: missing file\n{file_not_found}')
    except KeyError as key_error:
        print(f'Error: unknown product ID in the request.csv file\n{key_error}')

if __name__ == '__main__':
    main()