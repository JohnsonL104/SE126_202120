# Lucas Johnson
# 
# Lab #2A
#
# 1/23/2021
#
# SE126_202120
#
#  The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate,
#  and the number of people currently registered for the event.  Write a program that displays all rooms that
#  are over the maximum limit of people and the number of people that have to be notified that they will have
#  to be put on the wait list. After the file is completely processed the program should display the number of
#  records processed and the number of rooms that are over the limit.
#
#
#   VARIABLE DICTIONARY:
#       overLimit               The ammount of rooms that are over the limit
#       recordsProcessed        The ammount of rooms that were processed
#       csvf                    The csv file
#       f                       The csv file reader
#       r                       The current record in the csv file in the for loop
#       name                    The name of the current room in the for loop
#       max                     The max ammount of people aloud in the current room
#       current                 The current people attending the meeting for the current room





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