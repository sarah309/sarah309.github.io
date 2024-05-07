print()
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')
print()
print('The ID Card is: ')
print('-------------------------------------------')
#output = f'{last_name.upper}, {first_name.upper}'
output = (last_name.upper() + ', ' + first_name.upper())
print(output)
#output = f'{job_title.capitalize}'
output = (job_title.title())
print(output)
#output = f'ID: {id_number}'
output = ('ID: ' + id_number)
print(output)
print()
#output = f'{email_address.lower}'
output = (email_address.lower())
print(output)
#output = f'{phone_number}'
output = (phone_number)
print(output)
print('-------------------------------------------')