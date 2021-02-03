import csv

records = 0
class_total = 0

fname = []
lname = []
t1 = []
t2 = []
t3 = []

avg = []
letterAvg = []


def getFW(list):
    longest = 0
    for i in range(0, len(list)):
        if(len(str(list[i])) > longest):
            longest = len(str(list[i]))
    return longest + 1

with open("W4/listPractice1.csv") as csvf:
    f = csv.reader(csvf)
    
     
    for i in f:
        records += 1
        fname.append(i[0])
        lname.append(i[1])
        t1.append(int(i[2]))
        t2.append(int(i[3]))
        t3.append(int(i[4]))

for i in range(0, records):
    print("{0:{2}}{1:{3}}".format(fname[i], lname[i], getFW(fname), getFW(lname)))


