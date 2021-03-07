# Lucas Johnson
# 
# Lab #6A
#
# 2/27/2021
#
# SE126_202120
#
# Write a Python program to assign passengers seats in an airplane.
#
#   VARIABLE DICTIONARY:
#       seatA       The list for the A column of seats
#       seatB       The list for the B column of seats
#       seatC       The list for the C column of seats
#       seatD       The list for the D column of seats
#       row         The user's answer for what row they would like to reserve
#       seat        The user's answer for what seat they would like to reserve
#       answer      The user's answer for wheather they want to reserve another seat

import os

seatA = ['A', 'A', 'A', 'A', 'A', 'A', 'D']
seatB = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
seatD = ['D', 'D', 'D', 'D', 'D', 'D', 'D']

#I edited this function from https://www.geeksforgeeks.org/clear-screen-python/
def clear():   
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 
  

def displaySeats():
    print("\nRow\t\tSeat\tSeat\tSeat\tSeat")
    for i in range(0, len(seatA)):
        print("{0}\t\t{1}\t{2}\t{3}\t{4}".format(i+1, seatA[i], seatB[i], seatC[i], seatD[i]))




def reserveSeat():
    row = int(input("What row would you like to reserve(1-7): "))-1
    seat = input("What seat would you like to reserve(A-D): ")

    if(seat.upper() == "A"):
        if(seatA[row] != "X"):
            seatA[row] = "X"
            return(1)
        else:
            print("this seat is already taken and i think i need to do something about it")
            return(0)
    elif(seat.upper() == "B"):
        if(seatB[row] != "X"):
            seatB[row] = "X"
            return(1)
        else:
            print("this seat is already taken and i think i need to do something about it")
            return(0)
    elif(seat.upper() == "C"):
        if(seatC[row] != "X"):
            seatC[row] = "X"
            return(1)
        else:
            print("this seat is already taken and i think i need to do something about it")
            return(0)
    elif(seat.upper() == "D"):
        if(seatD[row] != "X"):
            seatD[row] = "X"
            return(1)
        else:
            print("this seat is already taken and i think i need to do something about it")
            return(0)



def mainMenu():
    answer = "y"
    while(answer == "y" or answer == "Y"):
        displaySeats()
        if(reserveSeat() == 1):
            answer = input("Would you like to reserve another seat?(Y/N): ")
            while(answer != "Y" and answer != "y" and answer != "N" and answer != "n"):
                answer = input("Incorect input\nWould you like to reserve another seat?(Y/N): ")
        
        clear()
    clear()
    print("This is the final seat arrangement:")
    displaySeats()


mainMenu()






