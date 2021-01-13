# Lucas Johnson
# 
# Lab #1A
#
# 1/13/2021
#
# SE126_202120
#
# Write a program that determines whether a meeting room is in violation of fire regulations 
# regarding the maximum room capacity. The program will accept the maximum room capacity and 
# the number of people attending the meeting. If the number of people is less than or equal 
# to the maximum room capacity, the program announces that it is legal to hold the meeting 
# and tells how many additional people may legally attend.  If the number of people exceeds 
# the maximum room capacity, the program announces that the meeting cannot be held as planned 
# due to the fire regulation and tells how many people must be excluded in order to meet the 
# fire regulations.  The user should be allowed to enter as many rooms as the want.  
#
#   VARIABLE DICTIONARY:
#       answer          The answer to whether the user is going to enter another room
#       max             The max capacity of the room being entered
#       ppl             The ammount of people attending the meeting being entered
#       availible       The availible amount of space in the meeting if there is room
#       remove          The ammount of people needed to be removed from the meeting if there are too many people being attended




answer = 'y'

while(answer == "y"):
    max = int(input("What is the max capacity of the room? "))

    ppl = int(input("How many people will be attending the meeting? "))

    if(max > ppl):
        availible = max - ppl

        print("It is safe for the meeting to be held and there are {0} more available spaces".format(availible))

    elif(max < ppl):
        remove = ppl - max

        print("It is not safe for the meeting to be held {0} need to be removed".format(remove))

    else:
        print("It is safe for the meeting to be held and there are no more available spaces")

    answer = input("Would you like to check another room?(Y/N): ")
