

def file_name(file):
    real_list =[]
    with open(file, 'r') as infile:
        for m in infile:
            x = m.strip().split(',')
            
            if len(x) == 5:
                real_list.append(x)
            else:
                print('Error in number of values - Must be 5.')
                quit()
                
    return real_list 

#Validate Time
def time_validate(time):
    hour, minutes = time.split(":")
    while int(hour) < 8:
        print("Error. Class must start at 8 or after")
        time = input("Enter start time again")
        hour, minutes = time.split(":")
    return time

# validate room capacity and room enrollment
def number_validate(nbr):
    while int(nbr) < 0 and int(nbr) > 500:
        print("error. enter room capacity again")
        nbr = input("Enter room capacity again: ")
    return nbr

# validate classrom day
def classroom_day_validate(day):
    selected_day = ["MW", "MWF", "TTH"]
    while day not in selected_day:
        print("Error. enter Classroom day again")
        day = input("Enter Classroom day again: ")
    return day

#Collect room info
def room_info():
    room_nbr = input("Enter the classroom number: ")
    room_capacity = input("Enter the classroom room capacity: ")
    room_capacity = number_validate(room_capacity)
    classroom_day = input("Enter the availble day for the classroom (EX. Tuesday&Thursday = TTH): ").upper()
    classroom_day = classroom_day_validate(classroom_day)
    start_time = input("Enter the class start time for the classroom (Ex. 15:55): ")
    start_time = time_validate(start_time)
    end_time = input("Enter the class end time for the classroom (17:10): ")
    end_time = time_validate(end_time)
    return room_nbr, room_capacity, classroom_day, start_time, end_time


# Collect Course Data


def course_info():
    faculty_member_name = input("Enter the faculty member's name: ")
    course_name = input("Enter course name(Ex. COB291): ")
    section_name = input("Enter the course section: ")
    nbr_credit_hrs = input("Enter the course credit hours: ")
    course_enrollment = input("Enter number of students enrolled in course: ")
    course_enrollment = number_validate(course_enrollment)
    return faculty_member_name, course_name, section_name, nbr_credit_hrs, course_enrollment


# main function 

def main():
    matched = []
    rooms = []
    courses = []
   
    #Do you want to keep going
    keep_going = ["y", "yes"]
    user_answer = "y"
    
    
    file = int(input('Import room info file  '))
    if file == 1:
        fileName = input('Enter file name (without extension name)')
        #f-string will keep the file name the same and appends the .txt to the file name since we cant enter it all together
        file_full_name = (f'{fileName}.txt')
        #calls function
        football = file_name(file_full_name)
        for x in football:
            rooms.append(x)     
           
    starwars = int(input('Enter Course info\n 1)Import file\n 2) Enter manually'))
    if starwars == 1:
        coursefile = input('Enter file name (without extension name)')
        course_file_full_name = (f'{coursefile}.txt')
        #course_file(course_file_full_name)
        coursefilez = file_name(course_file_full_name)
        for x in coursefilez:
            courses.append(x)
         
    else:
        keep_going_again = ["y", "yes"]
        user_answer1 = "y"
        while user_answer1 in keep_going_again:
            coursex = course_info()
            courses.append(coursex)
            user_answer1 = input("Do you want to enter another course? (yes/no):    ")
    
#matching
    unmatched_course = []
    unmatched_room = (rooms)        
    
    for coursey in courses:
        for room in unmatched_room:
            if int(coursey[4]) <= int(room[1]):
                matched.append((coursey, room))
                unmatched_room.remove(room)
                break
        else:
            unmatched_course.append(coursey)
            
    export = int(input('Would you like to Print file or Export file?\n1)Print\n2)Export'))
    if export == 1:
        print('Course Matching Status:')
        print()
        print("-" * 100)
        print("COURSE #\t SEC\t HRS\t ROOM\t DAYS\t START\t END\t INSTRUCTOR\t ENRL\t SUITABILITY")

        for course, room in matched:
            if int(room[1]) > int(course[4]):
                suitability = "Match found but room is larger than required"
            elif int(room[1]) == int(course[4]):
                suitability = "match found with full capacity "
            else:
                suitability = 'Match found.'
            print(f'{course[1]}\t \t {course[2]}\t{course[3]}\t{room[0]}\t{room[2]}\t {room[3]}\t{room[4]}\t  {course[0]}     {course[4]}          {suitability}')
    
    
    
        for course in courses:
            suit1 = 'no suitable room found'
            print(f'{course[1]}\t \t  {course[2]}\t {course[3]}         N/A\t   N/A\t    N/A   N/A    {course[0]}        {course[4]}     {suit1}')
          #unmatched rooms   
        if len(rooms) > 0:
            print('Unmatched Rooms:')
            for roomz in rooms:
                print(f' {roomz[0]}\t {roomz[1]}\t {roomz[2]}\t {roomz[3]}\t{roomz[4]}')
 
    elif export == 2:
        file_out = input('What would you like to name the file?') + '.txt'
        with open(file_out, 'w') as file_out_carl:
            file_out_carl.write('Course Matching Status:\n')
            file_out_carl.write("-" * 100)

            for course, room in matched:
                if int(room[1]) > int(course[4]):
                    suitability = "Match found but room is larger than required"
                elif int(room[1]) == int(course[4]):
                    suitability = "match found with full capacity "
                else:
                    suitability = 'Match found.'
                    
                file_out_carl.write(f'{course[1]}\t \t {course[2]}\t{course[3]}\t{room[0]}\t{room[2]}\t {room[3]}\t{room[4]}\t  {course[0]}     {course[4]}          {suitability}\n')

        
            print('file has been written')
        
main()

