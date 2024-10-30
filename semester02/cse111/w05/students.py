import csv

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
    dictionary = {}
    with open(filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        # Skip first line with next
        next(reader)
        for line in reader:
            if len(line) != 0:
                key = line[key_column_index]
                dictionary[key] = line

    return dictionary

def main():
    INUMBER_INDEX = 0
    NAME_INDEX = 1
    filename = 'students.csv'

    student_dictionary = read_dictionary(filename, INUMBER_INDEX)

    id = input('Please enter an I-Number (xxxxxxxxx): ')

    # Check if the student ID is in the dictionary.
    if id in student_dictionary:

        value = student_dictionary[id]
        name = value[NAME_INDEX]

        # Print the student's name.
        print(f"{name}")

    else:
        print("No such student")

main()