import csv

lname = []
fname = []
dob = []


with open("Lab 6/lab6A.csv") as csvf:
    f = csv.reader(csvf)
    
    for r in f:
        lname.append(r[0])
        fname.append(r[1])
        dob.append(r[2])


answer = "y"

while(answer == "y" or answer == "Y"):
    item = input("Enter the last name you are searching for: ")

    searchCount = 0
    min = 0
    max = len(lname)-1

    g = int((min+max) / 2)

    while(min < max and item != lname[g]):
        searchCount +=1

        if item < lname[g]:
            max = g - 1
        else:
            min = g + 1
        
        g = int(((min+max)/2))

    if(item == lname[g]):
        print("Found {} at index {} in {} searches".format(item, g, searchCount))
    else:
         print("Couldn't find {} in {} searches(Searches are case sensitive)".format(item, searchCount))

    answer = input("Would you like to search again?(Y/N): ")