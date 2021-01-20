import csv

with open("Lab 2/lab2b.csv") as csvf:
    f = csv.reader(csvf)

    print(print("{0:8} {1:8} {2:4} {3:4} {4:9} {5:8} {6:9} {7:4} {8:3}".format("Type", "Brand", "CPU", "Ram", "1st Disk", "No. HDD",  "2nd Disk" , "OS", "YR")))

    for r in f:
        if(r[0] == "D"):
            type = "Desktop"
        else:
            type = "Laptop"
        
        if(r[1] == "DL"):
            brand = "Dell"
        elif(r[1] == "GW"):
            brand = "Gateway"

        if(int(r[5]) == 2):
            print("{0:8} {1:8} {2:4} {3:4} {4:9} {5:8} {6:9} {7:4} {8:3}".format(type, brand, r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        else:
            print("{0:8} {1:8} {2:4} {3:4} {4:9} {5:8} {6:9} {7:4} {8:3}".format(type, brand, r[2], r[3], r[4], r[5],  "" , r[6], r[7]))