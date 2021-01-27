# Lucas Johnson
# 
# Lab #2A
#
# 1/23/2021
#
# SE126_202120
#
#  You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. 
#  Your report should look like the following sample output.  The last line should print the number 
#  of computers in the file.
#  Each row will have 8 or 9 columns.  The number of columns depends on how many hard disk drives a computer has.
#
#
#   VARIABLE DICTIONARY:
#       csvf            The csv file
#       f               The reader for the csv file
#       r               The current record for the csv file in the for loop
#       type            The type of the current computer
#       brand           The brand of the current computer
#       


import csv

type = []
brand = []
cpu = []
ram = []
disk1 = []
noDisk = []
disk2 = []
os = []
yr = []



with open("Lab 2/lab2b.csv") as csvf:
    f = csv.reader(csvf)

    print("{0:8} {1:8} {2:4} {3:4} {4:9} {5:8} {6:9} {7:4} {8:3}".format("Type", "Brand", "CPU", "Ram", "1st Disk", "No. HDD",  "2nd Disk" , "OS", "YR"))

    for r in f:
        if(r[0] == "D"):
            type.append("Desktop")
        else:
            type.append("Laptop")

        
        if(r[1] == "DL"):
            brand.append("Dell")
        elif(r[1] == "GW"):
            brand.append("Gateway")
        else:
            brand.append("HP")

        cpu.append(r[2])
        ram.append(int(r[3]))
        disk1.append(r[4])
        noDisk.append(int(r[5]))
        if(int(r[5]) == 2):
            disk2.append(r[6])
            os.append(r[7])
            yr.append(int(r[8]))
        else:
            disk2.append("")
            os.append(r[6])
            yr.append(int(r[7]))
        


    for i in range(0, len(type)):
        print("{0:8} {1:8} {2:4} {3:4} {4:9} {5:8} {6:9} {7:4} {8:3}".format(type[i], brand[i], cpu[i], ram[i], disk1[i], noDisk[i], disk2[i], os[i], yr[i]))

    noReplaceDesktops = 0
    noReplaceLaptops = 0

    for i in range(0, len(type)):
        if(yr[i] <= 16):
            if(type[i] == "Desktop"):
                noReplaceDesktops += 1
            else:
                noReplaceLaptops += 1

    print("\n\tTo replace {0} Desktops it will cost: ${1:.2f}".format(noReplaceDesktops, noReplaceDesktops*2000))
    print("\tTo replace {0} Laptops it will cost:  ${1:.2f}".format(noReplaceLaptops, noReplaceLaptops*1500))




