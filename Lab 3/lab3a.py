# Lucas Johnson
# 
# Lab #3a
#
# 1/30/2021
#
# SE126_202120
#
# Your CIO (Chief Information Officer) has asked you to determine how much it would cost the
# company to replace all machines that are from 2016 and earlier. He plans on spending not more
# than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv
# into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2B)
# and also produce an end report that lists the number of desktops that will be replaced, the cost to
# replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.
#
#
#   VARIABLE DICTIONARY:
#       csvf                The csv file
#       f                   The reader for the csv file
#       r                   The current record for the csv file in the for loop
#       type                The list for the type field
#       brand               the list for the brand field
#       cpu                 The list for the cpu field
#       ram                 The list for the ram field
#       disk1               The list for the 1st disk field
#       noDisk              The list for the number of disk's field
#       disk2               The list for the 2nd disk field
#       os                  The list for the os field
#       yr                  The list for the yr field
#       noReplaceDesktops   The ammount of desktops that need to be replaced
#       noReplaceLaptops    The ammount of laptops that need to be replaced

 
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

    print("{0:8} {1:8} {2:4} {3:>4} {4:>9} {5:>8} {6:>9} {7:>4} {8:>3}".format("Type", "Brand", "CPU", "Ram", "1st Disk", "No. HDD",  "2nd Disk" , "OS", "YR"))

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
        print("{0:8} {1:8} {2:4} {3:>4} {4:>9} {5:>8} {6:>9} {7:>4} {8:>3}".format(type[i], brand[i], cpu[i], ram[i], disk1[i], noDisk[i], disk2[i], os[i], yr[i]))

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


