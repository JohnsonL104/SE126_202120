
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
