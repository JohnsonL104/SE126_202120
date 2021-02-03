# House Stark	Winter is Coming
# House Baratheon	Ours is the fury.
# House Tully	Family. Duty. Honor.
# Night's Watch	And now my watch begins.
# House Lannister	Hear me roar!
# House Targaryen	Fire & Blood

import csv

fname = []
lname = []
age = []
nickname = []
house = []

def getFW(list):
    longest = 0
    for i in range(0, len(list)):
        if(len(str(list[i])) > longest):
            longest = len(str(list[i]))
    return longest + 1


with open("Lab 4/lab4a.csv") as csvf:
    f = csv.reader(csvf)

    for i in f:
        fname.append(i[0])
        lname.append(i[1])
        age.append(i[2])
        nickname.append(i[3])
        house.append(i[4])

for i in range(0, len(fname)):
    print("{0:{5}}{1:{6}}{2:5}{3:{7}}{4:{8}}".format(fname[i], lname[i], age[i], nickname[i], house[i], getFW(fname), getFW(lname), getFW(nickname), getFW(house)))



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
    elif(house[i] == "House Tarkgaryen"):
        motto = "Fire & Blood"

    print("{0:{6}}{1:{7}}{2:5}{3:{8}}{4:{9}}{5:26}".format(fname[i], lname[i], age[i], nickname[i], house[i], motto, getFW(fname), getFW(lname), getFW(nickname), getFW(house)))


