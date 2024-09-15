print()
print('Please rate the following from 1 to 10')
print()
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? ' ))


if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            loan = True
        else:
            loan = False
    else:
        loan = False
if loan_size < 5:
    if credit_history < 4:
        loan = False
    elif income >= 7 or down_payment >= 7:
        loan = True
    elif income >= 4 and down_payment >= 4:
        loan = True
    else:
        loan = False
print()
if loan == True:
    print('You qualify for a loan!')
if loan == False:
    print('You do not qualify for a loan.')
print()