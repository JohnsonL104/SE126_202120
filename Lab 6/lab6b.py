

seatA = ['A', 'A', 'A', 'A', 'A', 'A', 'D']
seatB = ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC = ['C', 'C', 'X', 'C', 'C', 'C', 'C']
seatD = ['D', 'D', 'D', 'D', 'D', 'D', 'D']


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





















