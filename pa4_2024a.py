# pa4 atkins - 0
from datetime import date
import collections

def read_wage_date(file):
    emp_list = []
    wage_list = []
    
    with open (file, 'r') as infile:
        for x in infile:
            emp, wage = x.strip().split(',')
            emp_list.append(emp)
            wage_list.append(float(wage))
            
    infile.close()
    print('The file has been read successfully.\n')
    
            
    return emp_list, wage_list

def show_by_name(emp, wage):
    print('XXXX Manufacturing')
    print(date.today())
    print('\nEmployee Report\n')
    
    ttl = 0
    if len(emp) == len(wage):
        for x in range(len(emp)):
            print(f'{emp[x]:<25}\t${wage[x]:>7.2f}')
            ttl += wage[x]
            

        print(f'\nTotal employees:  {len(emp)} / Average wage: ${(ttl/len(emp)):.2f}')
        
    else:
        print('Error. Uneven amount of values.')
        

def show_by_rate(emp, wage):
    
    zipd = sorted(list(zip(wage, emp)))
    
    print('\nXXXX Manufacturing')
    print(date.today())
    print('Wage Report\n')
    
    for x in zipd:
        print(f'{x[1]:<25}\t${x[0]:>7.2f}')
    
def show_less18(emp, wage):
    print('XXXX Manufacturing')
    print(date.today())
    print('\nEmployees Earning < $18\n')

    for x in range(len(wage)):
        if wage[x] < 18:
            print(f'{emp[x]:<25}\t${wage[x]:>7.2f}')

def count(wage):
    counted = collections.Counter(wage)
    
    print(f'\nHourly rates with highest number of employees: {counted.most_common(3)}')

def main():
    emp, wage = read_wage_date('PA4_wages.txt')
    
    cont = 'y'
    while cont != 'e':
        print('''
              -------------------------------------------
                            Options Menu
                     
               1 - Employees & Hourly Rate
               2 - Employees by hourly rate (low-to-high)
               3 - Employees making less than $18/hr
               4 - Most common hourly rate
               
               E - Exit
              -------------------------------------------
            ''')
        
        cont = input('Type in your selection: ').lower()
        
        if cont == '1':
            show_by_name(emp, wage)
        elif cont == '2':
            show_by_rate(emp, wage)
        elif cont == '3':
            show_less18(emp, wage)
        elif cont == '4':
            count(wage)
        elif cont != 'e':
            print('Please enter a valid menu option.')

main()
