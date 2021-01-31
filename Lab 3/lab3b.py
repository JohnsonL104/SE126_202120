# Lucas Johnson
# 
# Lab #3a
#
# 1/30/2021
#
# SE126_202120
#
#  Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.
#  Store the field data into respective lists, and then process the lists to determine
#  the 5 final output values (make sure they are clearly labeled!). This final solution
#  should have NO input() statements and when the console is ran it should print all 5
#  totals (you may reprint the data from the lists/fie if you would like)  Use your original
#  Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to
#  a file and store data into lists, then use a for loop to process each voter and their data
#  to find the 5 totals. 
#
#   VARIABLE DICTIONARY:
#       nonEligible             The ammount of Not old enough entries
#       eligibleNonRegistered   The ammount of Non registerd of age entries
#       eligibleNonVoted        The ammount of Of age registered but didn't  vote entries
#       noVoted                 The ammount of entries that voted
#       id                      The list for the id field
#       age                     The list for the age field
#       registered              The list for the registered field
#       voted                   The list for the voted field
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