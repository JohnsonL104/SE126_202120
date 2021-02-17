import csv

id = []
name = []
age = []
color = []


with open("W5/binary.csv") as csvfile:

    f = csv.reader(csvfile)
    for rec in f:
        id.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])



answer = "y"

while(answer == "y"):
    item = input("\nEnter the NAME you are searching for: ")

    found = -1

    for i in range(0, len(id)):
        if (name[i] == item):
            found = i
    if found < 0:
        print("Couldn't find(Searches are case sensitive)")
    else:
        print("Found {} at {}".format(item, found))
    
    answer = input("\nDone searching run again?: ")