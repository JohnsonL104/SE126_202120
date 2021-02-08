# Lucas Johnson
# 
# Lab #4A
#
# 2/8/2021
#
# SE126_202120
#
# In Python, process the text file “lab5.txt” to store each field into its own corresponding list:
#   FIELD0      FIELD1      FIELD2      FIELD3      FIELD4
#   Firstname   LastnameAge Nickname    House       Allegiance
# Then: 
#   Process the lists to print the them as they appear in the file
#   Re-process the lists to add the House Motto (dependent on Field4/Allegiance)
#       -Re-Process the lists to print each record fully with the House Mottos
#   Re-process the lists to find the average age within the list, then
#       -Print the total number of people in the list
#       -Print the average age
#       -Print tallies for each allegiance (Field4)
#
#   VARIABLE DICTIONARY:
#       fname           The list for the first name field
#       lname           The list for the last name field
#       age             The list for the age field
#       nickname        The list for the nickname field
#       house           The list for the house field       
#       stark           The tally number for House Stark
#       baratheon       The tally number for House Baratheon
#       tully           The tally number for House Tully
#       nightsWatch     The tally number for The Night's Watch
#       lannister       The tally number for House Lannister
#       targaryen       The tally number for House Targaryen
#       totalAge        The sum of everyone's age
#       longest         The longest field width of a list
#       motto           The motto for the house of the current person being processed

import csv

fname = []
lname = []
age = []
nickname = []
house = []

stark = 0
baratheon = 0
tully = 0
nightsWatch = 0
lannister = 0
targaryen = 0

totalAge = 0

# wanted to try making a function that would get me the max field width of a field + 2 to make seperating them while printing easier.
def getFW(list):
    longest = 0
    for i in range(0, len(list)):
        if(len(str(list[i])) > longest):
            longest = len(str(list[i]))
    return longest + 2


with open("Lab 4/lab4.csv") as csvf:
    f = csv.reader(csvf)

    for i in f:
        fname.append(i[0])
        lname.append(i[1])
        age.append(i[2])
        nickname.append(i[3])
        house.append(i[4])

for i in range(0, len(fname)):
    print("{0:{5}}{1:{6}}{2:5}{3:{7}}{4:{8}}".format(fname[i], lname[i], age[i], nickname[i], house[i], getFW(fname), getFW(lname), getFW(nickname), getFW(house)))


print("\n\n")

for i in range(0, len(fname)):
    motto = ""
    if(house[i] == "House Stark"):
        motto = "Winter is Coming"
    elif(house[i] == "House Baratheon"):
        motto = "Ours is the fury."
    elif(house[i] == "House Tully"):
        motto = "Family. Duty. Honor."
    elif(house[i] == "Night's Watch"):
        motto = "And now my watch begins."
    elif(house[i] == "House Lannister"):
        motto = "Hear me roar!"
    elif(house[i] == "House Targaryen"):
        motto = "Fire & Blood"

    print("{0:{6}}{1:{7}}{2:5}{3:{8}}{4:{9}}{5:26}".format(fname[i], lname[i], age[i], nickname[i], house[i], motto, getFW(fname), getFW(lname), getFW(nickname), getFW(house)))

for i in range(0, len(fname)):
    totalAge += int(age[i])

    if(house[i] == "House Stark"):
        stark += 1
    elif(house[i] == "House Baratheon"):
        baratheon += 1
    elif(house[i] == "House Tully"):
        tully += 1
    elif(house[i] == "Night's Watch"):
        nightsWatch += 1
    elif(house[i] == "House Lannister"):
        lannister += 1
    elif(house[i] == "House Targaryen"):
        targaryen += 1

print("\n\nTotal Number of People: {0}\nAverage Age: {1:0.0f}\nHouse Stark: {2}\nHouse Baratheon: {3}\nHouse Tully: {4}\nNight's Watch: {5}\nHouse Lannister: {6}\nHouse Targaryen: {7}".format(len(fname), totalAge/len(fname), stark, baratheon, tully, nightsWatch, lannister, targaryen))