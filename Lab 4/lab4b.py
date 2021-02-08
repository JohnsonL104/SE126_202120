# Lucas Johnson
# 
# Lab #4b
#
# 2/8/2021
#
# SE126_202120
#
# After completing 4A, use it as a basis for 4B.  You should have the following lists for each person in the original file:
#   LIST0           LIST1           LIST2               LIST3               LIST4               LIST5
#   Firstname       Lastname        Age                 Nickname            House Allegiance    House Motto
#  
# Build a program, utilizing these lists, that allows a user to select options from a menu:
#
#                   MENU
#   1.    Print all First, Last, and nicknames
#   2.    Print Last names with House Allegiance and Motto
#   3.    Print full records
#   4.    EXIT
#
# Based on the user’s selection, print what they have requested.  They should immediately be returned to the menu unless they
# have chosen “4. EXIT” in which case they should see a Goodbye message.  
#
#   VARIABLE DICTIONARY:
#       fname           The list for the first name field
#       lname           The list for the last name field
#       age             The list for the age field
#       nickname        The list for the nickname field
#       house           The list for the house field  
#       motto           The list for the motto of the current person     
#       longest         The longest field width of a list
#       answer          The user's answer to what option they want to choose

import csv

fname = []
lname = []
age = []
nickname = []
house = []
motto = []



# wanted to try making a function that would get me the max field width of a field + 2 to make seperating them while printing easier. 
def getFW(list):
    longest = 0
    for i in range(0, len(list)):
        if(len(str(list[i])) > longest):
            longest = len(str(list[i]))
    return longest + 2

# print first, last and nicknames
def printFLNnames():
    print("\n\n")
    for i in range(0, len(fname)):
        print("{0:{3}}{1:{4}}{2:{5}}".format(fname[i], lname[i], nickname[i], getFW(fname), getFW(lname), getFW(nickname)))
    print("\n\n")

#print last name, house, and motto
def printLnameAndHouse():
    print("\n\n")
    for i in range(0, len(fname)):
        print("{0:{3}}{1:{4}}{2:{5}}".format(lname[i], house[i], motto[i], getFW(lname), getFW(house), getFW(motto)))
    print("\n\n")

# print everything
def printAll():
    print("\n\n")
    for i in range(0, len(fname)):
        print("{0:{6}}{1:{7}}{2:5}{3:{8}}{4:{9}}{5:{10}}".format(fname[i], lname[i], age[i], nickname[i], house[i], motto[i], getFW(fname), getFW(lname), getFW(nickname), getFW(house), getFW(motto)))
    print("\n\n")

# print the menu and return the answer
def menu():
    answer = int(input("\n\t\t\tMenu\n\n\t1.    Print all First, Last, and nicknames\n\t2.    Print Last names with House Allegiance and Motto\n\t3.    Print full records\n\t4.    EXIT\n\n"))
    while(answer != 1 and answer != 2 and answer != 3 and answer != 4):
        print("That is not a valid answer try again.")
        answer = int(input("\n\t\t\tMenu\n\n\t1.    Print all First, Last, and nicknames\n\t2.    Print Last names with House Allegiance and Motto\n\t3.    Print full records\n\t4.    EXIT\n\n"))
    return answer

# print goodbye message
def goodbye():
    print("Goodbye!")

with open("Lab 4/lab4.csv") as csvf:
    f = csv.reader(csvf)
    for i in f:
        fname.append(i[0])
        lname.append(i[1])
        age.append(i[2])
        nickname.append(i[3])
        house.append(i[4])
        if(i[4] == "House Stark"):
            motto.append("Winter is Coming")
        elif(i[4] == "House Baratheon"):
            motto.append("Ours is the fury.")
        elif(i[4] == "House Tully"):
            motto.append("Family. Duty. Honor.")
        elif(i[4] == "Night's Watch"):
            motto.append("And now my watch begins.")
        elif(i[4] == "House Lannister"):
            motto.append("Hear me roar!")
        elif(i[4] == "House Targaryen"):
            motto.append("Fire & Blood")

answer = menu()
while(answer != 4):
    if(answer == 1):
        printFLNnames()
    elif(answer == 2):
        printLnameAndHouse()
    elif(answer == 3):
        printAll()
    answer = menu()
goodbye()