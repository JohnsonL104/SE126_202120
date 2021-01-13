# Lucas Johnson
# 
# Lab #1B
#
# 1/13/2021
#
# SE126_202120
#
# Edit the program you created in Lab #1A so that when the user is prompted to continue, they can only answer with an uppercase or lowercase y or n. 
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

    while(answer != "Y" and answer != "y" and answer != "N" and answer != "n"):
        print("Invalid answer try again.")
        answer = input("Would you like to check another room?(Y/N): ")
