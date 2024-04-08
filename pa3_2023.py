# PA3_Final with no comments.
# code done by sam ogden

# VALIDATION FUNCTIONS
def validate_time(time):
    hh, mm = time.split(':')
    while int(hh) < 8 or int(mm) > 59:
        print('Error in time input.')
        time = input('Re-enter time in HH:MM format: ')
        hh, mm = time.split(':') 
    return time


def validate_day(day):
    days_available = ['MW', 'MWF', 'TTH'] 
    while day not in days_available:
        print('Error in day input.')
        day = input('Enter the days the classroom is available (e.g., MW, MWF, or TTH): ').upper()
    return day


def validate_enrollment(enroll):
    while int(enroll) <= 0 or int(enroll) >= 500:
        print('Error in capacity input. Must be positive integer less than 500.')
        enroll = input('Enter the number of students in the course (e.g., 30): ')
    return enroll


def validate_capacity(capac):
    while int(capac) <= 0 or int(capac) >= 500:
        print('Invalid capacity value. Must be greater than 0 and less than 500.')
        capac = input("Enter the maximum number of students the room can accommodate: ")
    return capac

# CREATING INPUT FUNCTIONS


def room_info():

    room_num = input("Enter the classroom number (e.g., ZSH 0217): ").upper() 
    room_cap = int(input("Enter the maximum number of students the room can accommodate: "))
    room_cap = int(validate_capacity(room_cap))
    days_avail = input("Enter the days the classroom is available (e.g., MW, MWF, or TTH): ").upper()
    days_avail = validate_day(days_avail)
    time_start = input("Enter the start time the classroom is available (HH:MM): ")
    time_start = validate_time(time_start)
    time_end = input("Enter the end time the classroom is available until (HH:MM): ")
    time_end = validate_time(time_end)

    return room_num, int(room_cap), days_avail, time_start, time_end
            

def course_info():

    prof_name = input("Enter the faculty member's name: ").upper()
    course_name = input("Enter the course name (e.g., COB291): ").upper()
    sect_num = input("Enter the section number (e.g., 1): ")
    credit_hours = input("Enter the number of credit hours (e.g., 3): ")
    stu_num = int(input("Enter the number of students in the course (e.g., 30): "))
    stu_num = int(validate_enrollment(stu_num))
        
    return prof_name, course_name, sect_num, credit_hours, int(stu_num)
        
# MAIN FUNCTION - COMPILES ALL OTHER FUNCTIONS WITHIN    


def main():
    rooms = []  # =>      [('Zsh 2017','45','tth','11:15','12:15'),('Hart 2009', '55', 'mwf', '13:45', '15:10')]                
    courses = []                           
    matched_courses = []                

    # CONTINUOUS LOOP TO GATHER ROOM INFORMATION FROM USER
    print('Enter Room Details:') 
    decision_cont = ['y', 'yes']    
    decision_room = 'y' 
    while decision_room in decision_cont:    
        x = room_info()        
        rooms.append(x)       # => ('Zsh 2017','45','tth','11:15','12:15')     ('Hart 2009', '55', 'mwf', '13:45', '15:10')      
        decision_room = input('Would you like to enter another room? (y/n): ').lower() 
        print() 
    
    print('Enter Course Details:')
    decision_cont = ['y', 'yes']
    decision_course = 'y'
    while decision_course in decision_cont:
        y = course_info()
        courses.append(y)
        decision_course = input('Would you like to enter another course? (y/n): ').lower()
        print()

    for course in courses: 
        for room in rooms:
            if course[4] <= room[1]:
                matched_courses.append((course, room))
                rooms.remove(room)
                courses.remove(course)
                break 
    
    # Output matching results
    print('Course Matching Status:\n')          
    print('-'*55)                              
    print('\nCOURSE #\tSEC\tHRS\tROOM\t\tDAYS\tSTART\tEND\tINSTRUCTOR\tENROLL\t\tSUITABILITY\n')                                                                                     

    for course, room in matched_courses: 
        if int(room[1]) > int(course[4]):
            suitability = "Match found, but room is larger than required."
        elif int(room[1]) < int(course[4]):
            suitability = "No classroom found."
        else:
            suitability = "Match found, but there will not be extra seats."

        print(f"{course[1]}\t\t{course[2]}\t{course[3]}\t{room[0]}\t{room[2]}\t{room[3]}\t{room[4]}\t{course[0]}\t{course[4]}\t\t{suitability}") 
        print()

    for course in courses: 
        suitability = 'No suitable room found.'
        print(f"{course[1]}\t\t{course[2]}\t{course[3]}\tN/A\t\tN/A\tN/A\tN/A\t{course[0]}\t{course[4]}\t\t{suitability}")
        print()

    # output unmatched rooms
    if len(rooms) > 0:  
        print('\nUnmatched Rooms:') 
        for room in rooms:
            print(f"Room: {room[0]}, Capacity: {room[1]}, Days: {room[2]}, Time: {room[3]}-{room[4]}")

# RUN MAIN FUNCTION


main()


