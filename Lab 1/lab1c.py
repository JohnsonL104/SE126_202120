# Lucas Johnson
# 
# Lab #1C
#
# 1/13/2021
#
# SE126_202120
#
#   Rewrite Lab #1A using functions.  You must have the following functions:
#
#           A.  A function that asks the user for the maximum capacity of the rooms and returns that value.Use capacity for the name of    
#               the function.
#           B.  A function that asks the user for the number of people (attendees) attending the conference and returns that value. Use attendees 
#               for the name of the function.
#           C.  A function that accepts/is passed the values returned by the functions capacity andattendees and returns the difference between
#               the room capacity and the attendees. Use register for the name of the function.
#           D.  A function that prompts the user to see if they want to check anymore rooms. This function should only return if the user selects 
#               a lower/uppercase selects a lower/uppercase y or n.
#
#   The main part of the program should determine whether the meeting can be held. If the number of people exceeds the maximum room capacity, 
#   the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in  
#   order to meet the fire regulations.
#   
# 
#   VARIABLE DICTIONARY:
#       answer          The answer to whether the user is going to enter another room
#       max             The max capacity of the room being entered
#       ppl             The ammount of people attending the meeting being entered
#       availible       The availible amount of space in the meeting if there is room
#       remove          The ammount of people needed to be removed from the meeting if there are too many people being attended



def capacity():
    ''' gets the capacity of the room '''
    return int(input("What is the max capacity of the room? "))

def attendees():
    ''' gets the ammount of people attending the meeting'''
    return int(input("How many people will be attending the meeting? "))

def register(max, ppl):
    return max - ppl

def check():
    ''' check if the user would like to enter another room '''
    return input("Would you like to check another room?(Y/N): ")

answer = 'y'

while(answer == "y"):
    max = capacity()

    ppl = attendees()

    if(max > ppl):
        availible = register(max, ppl)

        print("It is safe for the meeting to be held and there are {0} more available spaces".format(availible))

    elif(max < ppl):
        remove = register(max, ppl)*-1

        print("It is not safe for the meeting to be held {0} need to be removed".format(remove))

    else:
        print("It is safe for the meeting to be held and there are no more available spaces")

    answer = check() 

    while(answer != "Y" and answer != "y" and answer != "N" and answer != "n"):
        print("Invalid answer try again.")
        answer = check()
