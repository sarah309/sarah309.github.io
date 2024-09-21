from datetime import datetime

print()

weekday = datetime.now().weekday()

subtotal = float(input('What is the subtotal of your purchase? '))

print()

if (weekday == 2 or weekday == 3) and subtotal >= 50:
    #print("Today is a Wednesday or Thursday")
    discount = subtotal * .1
    print(f'Your discount is ${discount:.2f}')
    before_tax = subtotal - discount
    sales_tax = 0.06 * before_tax
    print(f'Your sales tax is ${sales_tax:.2f}\n')
    total = before_tax + sales_tax
    print(f'Your total is ${total:.2f}')

else:
    print('You do not qualify for a discount')
    before_tax = subtotal
    sales_tax = 0.06 * before_tax
    print(f'Your sales tax is ${sales_tax:.2f}\n')
    total = before_tax + sales_tax
    print(f'Your total is ${total:.2f}')
print()