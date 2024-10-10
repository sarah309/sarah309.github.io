my_data = [324, 1, 45, 21, 59, -110, 'bob']

my_data.append(999)
print(my_data)

my_data.insert(3, 100)
print(my_data)

my_element = my_data.pop()
print(my_data)
print(my_element)
my_element2 = my_data.remove(1)
print(my_element2)
print(my_data)

my_index = my_data.index('bob')
print(my_index)

print(my_data[3])

for data in my_data:
    print(data)

for index in range(len(my_data)):
    print(my_data[index])


my_compound = [[1, 2], [3, 9], [99, -11], [23, 44]]

for compound in my_compound:
    print(compound[1])


print(my_compound[2][0])

for i in range(len(my_compound)):
    for j in range(len(my_compound[i])):
        print(my_compound[i][j])