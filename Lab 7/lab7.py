import csv
from os import system, name 
idCode = []
lname = []
fname = []
age = []
allegiance = []

with open("Lab 7/GOT_bubble_sort_7.csv") as csvf:
    f = csv.reader(csvf)

    for rec in f:
        idCode.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])

 
def clear():  
     if name == 'nt':
          _ = system('cls')  
     else:  
          _ = system('clear') 

#list to string
def lts(l):
    s = ''
    for i in range(0, len(l)):
        if(i == 0):
            s = str(l[i])
        else:    
            s += ", {}".format(str(l[i]))
    return s

def swap(i):
    tempI = idCode[i+1]
    tempF = fname[i+1]
    tempL = lname[i+1]
    tempAG = age[i+1]
    tempAL = allegiance[i+1]
    idCode[i+1] = idCode[i]
    fname[i+1] = fname[i]
    lname[i+1] = lname[i]
    age[i+1] = age[i]
    allegiance[i+1] = allegiance[i]
    idCode[i] = tempI
    fname[i] = tempF
    lname[i] = tempL
    age[i] = tempAG
    allegiance[i] = tempAL

def sortBy(l):
    for j in range(0, len(fname)):
            for i in range(0, len(fname)):
                tempI = ""
                tempF = ""
                tempL = ""
                tempAG = ""
                tempAL = ""
                if(i < len(fname)-1):
                    if(l[i] > l[i+1]):
                        swap(i)

def binarySearch(item, l):
    sortBy(l)
    min = 0
    max = len(l)-1

    guess = int(((min + max)/2))
    while(min<max and l[guess] != item):
        if(l[guess]>item):
            max = guess-1
        elif(l[guess]<item):
            min = guess +1
        guess = int(((min + max)/2))
    if(item == l[guess]):
        return(0, guess)
    else:
        return(1, 0)

def seqSearch(item, l):
    indexs = []
    for i in range(0, len(l)):
        if(item == l[i]):
            indexs.append(i)
    if(len(indexs)>0):
        return(0, indexs)
    else:
        return(1, indexs)

def menu():
    a = input("\t\t   Search Menu\n\t\t1. Search ID Code\n\t\t2. First Name\n\t\t3. Last Name\n\t\t4. Allegiance\nWhich option would you like to choose: ")
    if(a == '1'):
        item = input("\nWhat ID code would you like to search for: ")
        _, i = binarySearch(item, idCode)
        clear()
        if(_ == 0):
            print("Found {0} at index {1}".format(item, i))
            print("\nID Code: {0}\nFirst Name: {2}\nLast Name: {1}\nAge: {3}\nAllegiance: {4}".format(idCode[i], lname[i], fname[i], age[i], allegiance[i]))
        else:
            print("Could not find {0}(Searches are case sensitive)".format(item))
    elif(a == '2'):
        item = input("\nWhat first name would you like to search for: ")
        _, i = binarySearch(item, fname)
        clear()
        if(_ == 0):
            print("\nFound {0} at index {1}".format(item, i))
            print("\nID Code: {0}\nFirst Name: {2}\nLast Name: {1}\nAge: {3}\nAllegiance: {4}".format(idCode[i], lname[i], fname[i], age[i], allegiance[i]))
        else:
            print("Could not find {0}(Searches are case sensitive)".format(item))
    elif(a == '3'):
        item = input("\nWhat last name would you like to search for: ")
        _, indexs = seqSearch(item, lname)
        clear()
        if(_ == 0):
            print("\nFound {0} at index\\s {1}".format(item, lts(indexs)))
            for i in range(0, len(indexs)):
                print("\nID Code: {0}\nFirst Name: {2}\nLast Name: {1}\nAge: {3}\nAllegiance: {4}".format(idCode[indexs[i]], lname[indexs[i]], fname[indexs[i]], age[indexs[i]], allegiance[indexs[i]]))
        else:
            print("Could not find {0}(Searches are case sensitive)".format(item))
    elif(a == '4'):
        item = input("\nWhat allegiance would you like to search for: ")
        _, indexs = seqSearch(item, allegiance)
        clear()
        if(_ == 0):
            print("\nFound {0} at index\\s {1}".format(item, lts(indexs)))
            for i in range(0, len(indexs)):
                print("\nID Code: {0}\nFirst Name: {2}\nLast Name: {1}\nAge: {3}\nAllegiance: {4}".format(idCode[indexs[i]], lname[indexs[i]], fname[indexs[i]], age[indexs[i]], allegiance[indexs[i]]))
        else:
            print("Could not find {0}(Searches are case sensitive)".format(item))  
    else:
        print("That is not a valid option")      

def again():
    a = input("\nWould you like to search again?(Y/N): ")
    while(a != 'y' and a != 'Y' and a != 'N' and a != 'n'):
        a = input("\nIncorrect Input Try again.\nWould you like to search again?(Y/N): ")
    if(a == 'y' or a == "Y"):
        return 'y'
    else: 
        return 'n'

a = 'y'
while(a == 'y'):
    clear()
    menu()
    a = again()
    