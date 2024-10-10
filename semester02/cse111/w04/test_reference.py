# Python

x = 10
y = x

print(x, y)

y += 20
print(x, y)

x = [1, 2, 3, 4, 5]
y = x
print(x, y)
y.append(999999)
print(x, y)

def modify_data(x, my_data):
    x += 20
    my_data.append(9999999)

def main():
    x = 10
    my_data = [1, 2, 3, 4, 5]
    modify_data(x, my_data)
    print(x, my_data)

main()