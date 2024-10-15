# Read data using strip and split into list
import csv

# Read data using csv reader into list
def read_data(filename):
    cities_list = []
    with open(filename, 'rt') as filehandle:
        next(filehandle)
        for line in filehandle:
            # Running with line.strip removes extra line between data
            line = line.strip()
            # Prints as list
            cities_info = line.split(',')
            cities_list.append(cities_info)
    return(cities_list)

NAME_INDEX = 0
COUNTRY_INDEX = 1
POPULATION_INDEX = 2

# Read data using csv read into dictionary (same output as read_data function, but much shorter code with csv)
def read_data_into_dictionary(filename):
    cities_dictionary = {}
    with open(filename, 'rt') as filehandle:
        reader = csv.reader(filehandle)
        next(reader)
        for line in reader:
            #print(line)
            city_name = line[0]
            print(city_name)
            cities_dictionary[city_name] = [line[COUNTRY_INDEX], line[POPULATION_INDEX]]
    return cities_dictionary

def main():
    filename = 'favoritecities4.csv'

    cities_list = read_data(filename)
    # print(cities_list)
    for city_info in cities_list:
        print(city_info)
    read_data(filename)
    print(cities_list[4][0])
    read_data_into_dictionary(filename)

main()