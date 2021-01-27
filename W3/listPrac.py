import csv

records = 0

name = []
age = []
animal = []
color = []
number = []

dog = 0
cat = 0
tiger = 0
elephant = 0
bird = 0
chicken = 0
bunny = 0
horse = 0
bat = 0



with open("W3/classList.txt") as csvf:
    f = csv.reader(csvf)
    

    for r in f:
        records += 1

        name.append(r[0])
        age.append(int(r[1]))
        animal.append(r[2])
        color.append(r[3])
        number.append(int(r[4]))


for i in range(0, records):
    print("INDEX: {0}\t{1}\t{2}\t{3:8}\t{4}\t{5}".format(i, name[i], age[i], animal[i], color[i], number[i]))

#Processing Average Age

total_age = 0
for i in range(0,records):
    total_age += age[i]


#Processing Average Favorite Number
totalFavNumber = 0
for i in range(0, records):
    totalFavNumber += number[i]

print("\n\t{0:25}{1:5}\n\t{2:25}{3:5.2f}\n\t{4:25}{5:5.2f}".format("Total Records: ", records, "Average Age: ",total_age/(records), "Average Favorite Number: ", totalFavNumber/(records)))

#Processing Favorite animals count
for i in range(0, records):
    if(animal[i] == "Dog"):
        dog+=1
    elif(animal[i] == "Cat"):
        cat+=1
    elif(animal[i]=="Tiger"):
        tiger+=1
    elif(animal[i]=="Elephant"):
        elephant+=1
    elif(animal[i]=="Bird"):
        bird+=1
    elif(animal[i]=="Chicken"):
        chicken+=1
    elif(animal[i]=="Bunny"):
        bunny+=1
    elif(animal[i]=="Horse"):
        horse+=1
    elif(animal[i]=="Bat"):
        bat+=1
    

print("\nDog: {0}\nCat: {1}\nTiger: {2}\nElephant: {3}\nBird: {4}\nChicken: {5}\nBunny: {6}\nHorse: {7}\nBat: {8}".format(dog,cat,tiger,elephant,bird,chicken,bunny,horse,bat))

