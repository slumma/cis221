
#Gathering classroom data from inputs

room_num = str(input("Enter the classroom number (e.g., ZSH 0217): "))
room_cap = input("Enter the maximum number of students the room can accomodate: ")
days_avail = str(input("Enter the days the classroom is available (e.g., MW, MWF, or TTH): "))
time_start = input("Enter the start time the classroom is available (e.g., 1:00pm as 13:00): ")
time_end = input("Enter the end time the classroom is available until (e.g., 2:30pm as 14:30): ")

#Gathering course data from inputs

prof_name = input("Enter the faculty member's name: ")
course_name = str(input("Enter the course name (e.g., COB291): "))
sect_num = input("Enter the section number (e.g., 1): ")
credit_hours = input("Enter the number of credit hours (e.g., 3): ")
stu_num = input("Enter the number of students in the course (e.g., 30): ")

#Data Validation aka verifying inputs using if-else statements

if room_cap.isdigit() and int(room_cap) > 0:
    pass
else:
    room_cap = input('Invalid maximum room capacity, please try again: ')
    if room_cap.isdigit() == False or int(room_cap) <= 0:
        print('Invalid Input.')
        quit()
    else:
        pass
      
if days_avail.upper() == 'MW' or days_avail.upper() == 'MWF' or days_avail.upper() == 'TTH':
    pass
else:
    days_avail = input('Invalid days available, please try again: ')
    if days_avail.upper() == 'MW' or days_avail.upper() == 'MWF' or days_avail.upper() == 'TTH':
        pass
    else:
        print('Invalid Input.')
        quit()
    
if time_start.replace(':', '').isdigit():
    hours, minutes = time_start.split(':')
    if int(hours) >= 8:
        pass
    else:
        time_start = input('Invalid start time, please try again: ')
        hours, minutes = time_start.split(':')
        if int(hours) >= 8:
            pass
        else:
            print('Invalid Input.')
            quit()
else:
    time_start = input('Invalid start time, please try again: ')
    hours, minutes = time_start.split(':')
    if time_start.replace(':', '').isdigit() and int(hours) >= 8:
        pass
    else:
        print('Invalid Input.')
        quit()
        
if time_end.replace(':', '').isdigit():
    pass
else:
    time_end = input('Invalid end time, please try again: ')
    if time_end.replace(':', '').isdigit():
        pass
    else:
        print('Invalid Input.')
        quit()

if stu_num.isdigit() and int(stu_num) > 0:
    pass
else:
    stu_num = input('Invalid number of students, please try again: ')
    if stu_num.isdigit() == False or int(stu_num) <= 0:
        print('Invalid Input.')
        quit()
    else:
        pass
    
#Room Matching aka finding an available room from inputs using if-elif

if room_cap > stu_num:
    suitability = "Classroom found, but there will be extra seats."
elif room_cap < stu_num:
    suitability = "No classroom found."
else:
    suitability = "Classroom found, but there will not be extra seats."
 
#Output Titles
print('\n\n')
print('-' * 115)
print('\nCOURSE #\tSEC\tHRS\tROOM\t\tDAYS\tSTART\tEND\tINSTRUCTOR\tENROLL\t\tSUITABILITY')
print(f'{course_name.upper()}\t\t{sect_num}\t{credit_hours}\t{room_num.upper()}\t{days_avail.upper()}\t{time_start}\t{time_end}\t{prof_name.title()}\t{stu_num}\t\t{suitability}')