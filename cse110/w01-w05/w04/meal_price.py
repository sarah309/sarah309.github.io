print()
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))
tip = float(input("Tip amount (every penny is appreciated!): "))
subtotal = float(tip) + (float(child_meal) * float(number_children)) + (float(adult_meal) * float(number_adults))
formatted_subtotal = f"{subtotal:.2f}"
print()
print(f"Subtotal: ${formatted_subtotal}")
sales_tax = (float(tax) / 100) * float(subtotal)
formatted_sales_tax = f"{sales_tax:.2f}"
print(f"Sales Tax: ${formatted_sales_tax}")
total = float(sales_tax) + float(subtotal)
formatted_total = f"{total:.2f}"
print(f"Total: ${formatted_total}")
print()
payment = float(input("What is the payment amount? "))
change = (float(payment) - float(total))
formatted_change = f"{change:.2f}"
print(f"Change: ${formatted_change}")
print()