# Lucas Johnson
# 
# Lab #5B
#
# 11/22/2020
#
# 202110_SE116.11 Program Essentials with Python
#
#Construct a program that will analyze potenial voters. The program should generate the following totals:
#1. Number of individuals not eligible to register.
#2. Number of individuals who are old enough to vote but have not registered.
#3. Number of individuals who are eligible to vote but did not vote.
#4. Number of individuals who did vote.
#5. Number of records processed.
#The program must prompt the user for the ID number, age, if the person is registered to vote, and if the
#person voted. You will also have to prompt to see if the user has more data to enter.
#
#   VARIABLE DICTIONARY:
#       anotherEntry            Wheather the user is going to enter another entry
#       voterList               The list of a list of data for each entry
#       nonEligible             The ammount of Not old enough entries
#       eligibleNonRegistered   The ammount of Non registerd of age entries
#       eligibleNonVoted        The ammount of Of age registered but didn't  vote entries
#       voted                   The ammount of entries that voted
#       records                 The ammount of entries
#       id                      The id number of the person that is being entered
#       age                     The age of the person that is being entered
#       registered              Wheather the person that is being entered is registered or not
#       hasVoted                Wheather the person that is being entered has voted or not
#       voter                   The current itteration in the voterList

import csv

id = []
age = []
registered = []
voted = []

nonEligible = 0
eligibleNonRegistered = 0
eligibleNonVoted = 0
noVoted = 0

with open("Lab 3/lab3b.csv") as csvf:
    f = csv.reader(csvf)
    for i in f:
        id.append(i[0])
        age.append(int(i[1]))
        registered.append(i[2])
        voted.append(i[3])





for i in range(0, len(id)):
    if(age[i] < 18):
        nonEligible += 1
    elif(registered[i] == "N"):
        eligibleNonRegistered += 1
    elif(voted[i] == "N"):
        eligibleNonVoted += 1
    else:
        noVoted += 1

    

print("Not of Age: {0}\nOf Age Non-Registered: {1}\nEligible Non-Voted: {2}\nVoted: {3}\nRecords: {4}".format(nonEligible, eligibleNonRegistered, eligibleNonVoted, noVoted, len(id)))