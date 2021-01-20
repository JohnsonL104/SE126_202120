import csv

overLimit = 0
recordsProcessed = 0

with open("Lab 2\lab2a.csv") as csvf:
    f = csv.reader(csvf)
    
    print("\n{0:20}  {1:>4}  {2:>10}  {3:>4}".format("Room", "Max", "Attending", "Over"))

    for r in f:
        name = r[0]
        max = int(r[1])
        current = int(r[2])
        recordsProcessed += 1
        if(current > max):
            print("{0:20}  {1:4}  {2:10}  {3:4}".format(name, max, current, current-max))
            overLimit += 1
    
    print("\nProcessed {} rooms".format(recordsProcessed))
    print("There are {} rooms over the limit".format(overLimit))

    input("\nPress Enter to continue...")