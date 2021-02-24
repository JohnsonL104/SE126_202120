import csv

id = []
name = []
age = []
color = []


with open("W7/binary.csv") as csvfile:

    f = csv.reader(csvfile)
    for rec in f:
        id.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])


def searchName():
    item = input("\nEnter the NAME you are searching for: ")
    sSearchCount = 0
    found = -1

    for i in range(0, len(id)):
        sSearchCount+=1
        if (name[i] == item):
            
            found = i
    if found < 0:
        print("Couldn't find(Searches are case sensitive)")
    else:
        print("Found {} at {} in {} searches".format(item, found, sSearchCount))
    
    answer = input("\nDone searching run again?: ")

    bSearchCount = 0
    
    min = 0

    max = len(id)-1

    g = int((min+max) / 2)

    while(min < max and item != name[g]):
        bSearchCount +=1

        if item < name[g]:
            max = g - 1
        else:
            min = g + 1
        
        g = int(((min+max)/2))

    if(item == name[g]):
        print("Found {} at {} in {} searches".format(item, g, bSearchCount))
    else:
         print("Couldn't find(Searches are case sensitive)")
        

def searchID():
    item = input("What is the ID you are searching for")

    found = -1
    sSearchCount = 0
    for i in range(0, len(id)):
        sSearchCount = 0
        if item == id:
            found = i
    if(found != -1):
        print("Sequential Search Found id number {} at index {} in {} searches".format(item, found, sSearchCount))

    bSearchCount = 0

    min = 0
    max = len(id)-1

    g = int(((min+max)/2))

    while(min < max and item != id[g]):
        bSearchCount += 1
        if(item < id[g]):
            max = g - 1
        else:
            min = g + 1
        
        g = int(((min+max)/2))
    
    if(item == id[g]):
        print("Sequential Search Found id number {} at index {} in {} searches".format(item, g, bSearchCount))
    


answer = "1"

while(answer == "1" or answer == "2"):

    answer = input("1. name 2. id")

    if(answer == "1"):
        searchName()
    elif(answer == "2"):
        searchID()





















