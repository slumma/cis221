## Programmer Name: Sam Ogden
## Purpose: Calculate the total net pay using the users inputs 

# My submission of this program indicates that I have neither received nor given 
# unauthorized assistance in writing this program. All coding is my own work.

# State variables and input statements 
emp_name = str(input('Enter employee\'s name (first and last): '))
num_hrs = eval(input('Enter number of hours worked this week: '))
hr_pay = eval(input('Enter hourly rate: '))
fed_tax = float(input('Enter federal tax withholding rate: '))
st_tax = float(input('Enter state tax withholding rate: '))
cash = '$'

print('''
''')

# Calculations of income and tax deductions
gross_pay = num_hrs * hr_pay
fed_deduc = gross_pay * fed_tax
st_deduc = gross_pay * st_tax
ttl_deduc = st_deduc + fed_deduc
net_pay = gross_pay - ttl_deduc

# Outputs with context
print('Employee Name:', emp_name)
print()

print('Hours:', num_hrs)
print(f"Hourly Rate: ${hr_pay:>10.2f}")
print(f"Gross Pay:   ${gross_pay:>10,.2f}")
print()

print('Deductions:')
print(f'\tFederal Withholding {fed_tax: .1%}: {cash:>8} {fed_deduc:>1,.2f}')
print(f'\tState Withholding {st_tax: .1%}: {cash:>11} {st_deduc:>1,.2f}')
print(f'\tTotal Deductions: {cash:>18} {ttl_deduc:>1,.2f}')
print(f'Net pay: {cash:>35} {net_pay:>1,.2f}')


