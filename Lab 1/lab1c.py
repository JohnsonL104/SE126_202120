

def capacity():
    ''' gets the capacity of the room '''
    return int(input("What is the max capacity of the room? "))

def attendees():
    ''' gets the ammount of people attending the meeting'''
    return int(input("How many people will be attending the meeting? "))

def register(max, ppl):
    return max - ppl

def check():
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
