# import random module and string module
import random
import string
# make a four list for Capital later and small later and number and punctuation
list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)
# make a var have a message to input the number of Character
input_pass = "please Enter the Number Of Character For Password: "
# input number of character
pass_number = input(input_pass)
# infinity loop but!!!!
while 1:
    # to check if the number is int and it is mor the 6 and less then 20
    try:
        pass_number = int(pass_number)
        if (pass_number < 6) or (pass_number > 20):
            print("you need more than 6 Character and less than 20 Character")
            print("please try again: ")
            pass_number = input(input_pass)
        else:
            # to go out from infinity loop
            break
    # if try not 1 it will except
    except:
        print("please Enter just Number")
        pass_number = input(input_pass)
# to be the list is not order
random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)
# if the number is even
if pass_number % 2 == 0:
    # to have 30% for LATER and 30% for later
    later_part = (round(pass_number * 30 / 100))
    # to have 20% for number and 20% for punctuation
    else_part = (round(pass_number * 20 / 100))
    # to make a var for password
    password = []
    # to and aa character to the password list
    for i in range(later_part):
        password.append(list1[i])
        password.append(list2[i])
    # to and aa character to the password list
    for i in range(else_part):
        password.append(list3[i])
        password.append(list4[i])
    # to make a password is not order
    random.shuffle(password)
    # to change the type of password from list to string
    password = "".join(password[:])
    # print the password
    print("the password is:", password)
# if the number is odd
else:
    # to have 30% for LATER and 30% for later
    later_part = (round(pass_number * 30 / 100))
    # to have 20% for number
    digit_part = (round(pass_number * 20 / 100))
    # to have 20% for punctuation
    else_part = (round(pass_number * 20 / 100))
    # to make a var for password
    password = []
    # to and aa character to the password list
    for i in range(later_part):
        password.append(list1[i])
        password.append(list2[i])
    # to and aa character to the password list and +1 is for the odd number
    for i in range(digit_part+1):
        password.append(list3[i])
    # to and a character to the password list
    for i in range(else_part):
        password.append(list4[i])
    # to make a password is not order
    random.shuffle(password)
    # to change the type of password from list to string
    password = "".join(password[:])
    # print the password
    print("the password is:", password)

    # # # # The End # # # #