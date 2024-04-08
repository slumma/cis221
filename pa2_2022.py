## Programmer name: Sam Ogden
## Purpose: Identify valid inputs and create outputs by utilizing calculations
## My submission of this program indicates that I have neither received nor given unauthorized 
## assistance in writing this program. All coding is my own work.

# Introduction statements
print('-- Custom Print Quote --')
print('\nEnter the following information to create a quote:')

# gather valid user inputs by using string testing methods
prod_name = input('\nProduct name: ')
if all(prod_name.isalpha() or prod_name.isspace() for prod_name in prod_name):
    pass
else:
    print('Product name must contain only letters and spaces.')
    quit()
    
order_quan = input('Quantity: ')
if order_quan.isdigit():
    pass
else:
    print('Quantity size must be numeric.')
    quit()
    
unit_cost = input(f'{prod_name.title()} unit cost: ')
if unit_cost.replace('.','').replace('$','').isdigit():
    pass
else:
    print('Unit Cost must be numeric.')
    quit()
    
num_colors = input('How many colors will be printed? ')
if num_colors.isdigit():
    pass
else:
    print('Number of colors must be numeric.')
    quit()

#seperator
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')

# ignore '$' from unit cost input

unit_cost = unit_cost.replace('$','')

# convert strings to floats/ints

num_colors = int(num_colors)
order_quan = int(order_quan)
unit_cost = float(unit_cost)


#calculations
mat_cost=(unit_cost * order_quan)
if mat_cost > 350:
    disc_amt = mat_cost * 0.12
    disc_ttl = mat_cost - disc_amt
else:
    disc_ttl = 0
    disc_amt = 0

set_charge = 18.00 * num_colors

cust_ttl = 1.24 * (mat_cost - disc_amt + set_charge)

# print outputs
order_num = prod_name[:4]
print(f'Your order confrimation code is: {order_num}-{num_colors}')

print(f'Product type: {prod_name.title()}')
print(f'\nMaterials cost\t\t$ {mat_cost:9,.2f}')

if mat_cost > 350:
    print(f'  Minus Discount\t$ {disc_amt:9,.2f}')

if mat_cost>350:
    print(f'Discounted total\t$ {disc_ttl:9,.2f}')
    
print(f'{num_colors} color setup\t\t$ {set_charge:9,.2f}')
print(f'Customer total\t\t$ {cust_ttl:9,.2f}')
