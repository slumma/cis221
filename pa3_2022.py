# Programmer names: Sam Ogden , Luke Fisher
# Purpose: Display option menu and display functions based on user input.
# For this paired-programming assignment, I worked with Luke Fisher. We have neither received
# nor given unauthorized assistance in writing this program.

# import necessary libraries
import sys
import random
import webbrowser

# define globals

error_msg = 'That\'s not correct -- try again.\n'
good_msg = 'You are correct!\n'
zero = 0
counter = 0
user_answer = 0


# define functions

def randomnum(strt, end):  # gather random numbers to be used throughout program
    rand = random.randint(strt, end)
    return rand


def option1():
    num_q = int(input('How many problems do you want to try?\t'))

    for x in range(num_q):
        zero = 0
        while zero != num_q:
            dividend = randomnum(1, 15)
            divisor = randomnum(1, 6)
            if divisor > dividend:
                dividend, divisor = divisor, dividend

            while user_answer == zero:
                usr_answer = int(input(f'What is {dividend} // {divisor}?\t'))
                true_ans = dividend // divisor

                if true_ans == usr_answer:
                    print(good_msg)
                    break

                elif true_ans != usr_answer:
                    print(error_msg)

                if counter == num_q:
                    break
            zero += 1


def option2():
    num1 = randomnum(1, 15)
    num2 = randomnum(1, 5)

    while zero == 0:
        user_answer = int(input(f'What is {num1} * {num2}?\t'))
        true_ans = num1 * num2
        if true_ans == user_answer:
            print(good_msg)
            decision = input('Do you want to try again (Y or N)?\t')
            decision = decision.lower()
            if decision == 'y':
                num1 = randomnum(1, 16)
                num2 = randomnum(1, 16)
                pass
            else:
                sys.exit()

        else:
            print(error_msg)


def option3():
    num1 = randomnum(5, 15)
    num2 = randomnum(0, 5)
    num3 = num1 + num2
    user_answer1 = int(input(f'What is {num1} += {num2}?  '))
    while user_answer1 != num3:
        print(error_msg)
        user_answer1 = int(input(f'What is {num1} += {num2}?  '))
    print(good_msg)

    num4 = num1 - num2
    user_answer2 = int(input(f'What is {num1} -= {num2}?  '))
    while user_answer2 != num4:
        print(error_msg)
        user_answer2 = int(input(f'What is {num1} -= {num2}?  '))
    print(good_msg)

    num5 = num1 * num2
    user_answer3 = int(input(f'What is {num1} *= {num2}?  '))
    while user_answer3 != num5:
        print(error_msg)
        user_answer3 = int(input(f'What is {num1} *= {num2}?  '))
    print(good_msg)


def option4():
    webbrowser.open('https://realpython.com/python-operators-expressions/')


def optionE():
    sys.exit()


def menu():
    menu = '''          --------------------------------------------
            Options Menu\n
            Select a problem type:
            \t1 - Integer Division
            \t2 - Multiplication
            \t3 - Augmented Assignment Operators
            \t4 - Learn About Python Operators\n
            \tE - Exit
          --------------------------------------------\n'''
    print(menu.center(20))


# assemble program w functions
def main():
    zero = 0
    while zero == 0:
        menu()
        option = input('Type in your selection:\t')
        option = option.upper()

        if option == '1':
            option1()

        elif option == '2':
            option2()

        elif option == '3':
            option3()

        elif option == '4':
            option4()

        elif option == 'E':
            optionE()
            zero += 1


# run main
main()