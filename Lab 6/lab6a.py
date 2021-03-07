# Lucas Johnson
# 
# Lab #6A
#
# 2/27/2021
#
# SE126_202120
#
# Write a Python program that reads the data from the file and stores all data into appropriate lists.
# The program should then prompt the user for the person’s last name they are searching for and display
# all available information on that person if they are found.  You must use the binary search method.
# The program should allow the user to search for as many people as they want. The program should also
# print a statement telling the user how many iterations of the search loop the program went through
# before finding (or not finding) the requested person.
#
#   VARIABLE DICTIONARY:
#       lname       The list for the last name field
#       fname       The list for the first name field
#       dob         The list for the date of birth field
#       item        The item the user is searching for
#       searchCount The ammount of times the program searches for the item
#       answer      The user's answer for wheather they want search for another item

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