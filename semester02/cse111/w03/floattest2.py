for i in range(11):
    value = i/10
    print(f'{value:.17f}')
    #if value == 0.7:
    if abs (value - 0.7) < 0.00001:
        print('The value is .7')