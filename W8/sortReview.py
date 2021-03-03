import csv

lname = []
fname = []
age = []

with open("W8/GOT_bubble_sort.csv") as csvf:
    f = csv.reader(csvf)

    for rec in f:
        lname.append(rec[0])
        fname.append(rec[1])
        age.append(rec[2])

def sortBy(list):
    for j in range(0, len(fname)):
            for i in range(0, len(fname)):
                tempF = ""
                tempL = ""
                tempA = ""
                if(i < len(fname)-1):
                    if(list[i] > list[i+1]):
                        tempF = fname[i+1]
                        tempL = lname[i+1]
                        tempA = age[i+1]
                        fname[i+1] = fname[i]
                        lname[i+1] = lname[i]
                        age[i+1] = lname[i]
                        fname[i] = tempF
                        lname[i] = tempL
                        age[i] = tempA




def searchFName():
    item = input("What first name would you like to search: ")
    found = 0
    sortBy(fname)
    print(fname)
    min = 0
    max = len(fname )-1

    guess = int(((min + max)/2))
    while(min<max and fname[guess] != item):
        if(fname[guess]<item):
            max = guess-1
        elif(fname[guess]>item):
            min = guess +1
        guess = int(((min + max)/2))
    print(fname[guess])


searchFName()




