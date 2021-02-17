# Lucas Johnson
# 
# Lab #5B
#
# 2/17/2021
#
# SE126_202120
#
# 5B. Re-write lab 6A but instead of searching for a person’s name, 
# search for their birthday.  If the person is found, reprint their 
# entire record to the console.  The program should allow the user 
# to search for as many birthdays as they want. The program should 
# also print a statement telling the user how many iterations of the
# search loop the program went through before finding (or not finding) 
# the requested person.
# Extra Credit +10 points: print the user the found person, their data,
# along with their current age. 
#
#   VARIABLE DICTIONARY:
#       fname           The list for the first name field
#       lname           The list for the last name field
#       dob             The list for the date of birth field
#       answer          The user's answer to whether they want to perform another search
#       found           The flag variable for when an item is found in the sequential search
#       sn              The number of searches performed in a single search
#       item            The item the user is searching for

import csv

lname = []
fname = []
dob = []


#Function to get the length of the longest item in a list and retrun it +2 to make printing a bit easier
def getFW(list):
    longest = 0
    for i in range(0, len(list)):
        if(len(str(list[i])) > longest):
            longest = len(str(list[i]))
    return longest + 2



with open("Lab 5/lab5.csv") as csvf:
    f = csv.reader(csvf)
    for i in f:
        lname.append(i[0])
        fname.append(i[1])
        dob.append(i[2])


answer = 'y'

while(answer == 'y' or answer == "Y"):
    found = -1
    sn = 0

    item = input("What is the date of birth you would like to search for: ")

    #Sequential Search
    for i in range(0, len(lname)):
        sn += 1
        if(dob[i] == item):
            found = i

    if(found < 0):
        print("Could not find anyone with the date of birth {0} in {1} searches(Remember searches are case sensitive)".format(item, sn))
    else:
        print("\nFound someone with the date of birth {0} at index {1} in {2} searches:\n{3:{6}}{4:{7}}{5:{8}}\n{9} is {10} years old!".format(item, found, sn, lname[found], fname[found], dob[found], getFW(lname), getFW(fname), getFW(dob), fname[found], 2021-int(dob[found][-4:])))
    
    answer = input("\nWould you like to search again? (Y/N): ")