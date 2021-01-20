#Week 2 Day 1: Importing Data from a File

#YOU MUST IMPORT THE CSV LIBRARY IN ORDER FOR FILES TO BE ACCESSED

#CSV: Comma Separated Values
#RECORDS: rows of the file, different types of data all belonging together
#FIELDS: columns of the file, sets of data (all data in a column is the same "type" ie names, ages, salaries, email addresses, etc)

#BASE PROGRAM CODE-------------------------------------------------------------------


import csv

totalRecords = 0
totalSalaries = 0

with open("W2/example.csv") as csvf:

    file = csv.reader(csvf)

    print("\nName \t Age \t Salary")
    for rec in file:

        totalRecords +=1


        print("{0} \t {1} \t ${2:.2f}".format(rec[0], rec[1], float(rec[2])))
        

        totalSalaries += float(rec[2])
    
    csvf.close()


print("\n\n{:.2f}".format(totalSalaries))
 
