# Lucas Johnson
# 
# Midterm
#
# 2/16/2021
#
# SE126_202120
#
# This program Reads a csv file given by the user and does one of two things with it:
#       1. Creates a new html template file with the formated table containing the csv file's data and opens it in the browser
#       2. Prints a formatted html table wiht the csv file's data in it to be copied to an already created html file
# This program comes with test.csv for testing purposes but can be given any csv file's path
#
#   VARIABLE DICTIONARY:
#       htmlFile        The string containing the template of the html file with a pair of brackets for the table to be formatted into
#       records         The list containing all the record lists
#       finalSTR        This string containing the formated html table to be printed
#       finalHTMLSTR    The same as finalSTR but with two extra tabs to account for it being in the body tag of the html
#       answer          The user's choice of what option they would like to pick in the menu



import csv

#used to get the absolute path of the html file created and open the html file in the defaul browswer
import os

htmlFile = '<!DOCTYPE html>\n<html lang = "en">\n\t<head>\n\t\t<meta charset="UTF-8">\n\t\t<meta name = "viewport" content="width=device-width, initial-scale=1.0">\n\t\t<meta name = "description" content = "">\n\t\t<meta name = "author" content = "">\n\t\t<title></title>\n\t</head>\n\t<body>\n{}\n\t</body>\n</html>'


def readCSV():
    csvPath = input("\nWhat is the path of the CSV file: ").replace("\\", "/")
    records = []
    with open(csvPath) as csvf:
        f = csv.reader(csvf)
        for i in f:
            #appends each record into the records list creating a list of lists: [[field 1 of record 1, field 2 of record 1], [field 1 of record 2, field 2 of record 2]]
            records.append(i)
    return records


def toFinalSTR(list):
    finalSTR = "<table>\r\n"
    for i in list:
        finalSTR += "\t<tr>\r\n"
        for y in i:
            finalSTR += "\t\t<td>{}</td>\r\n".format(y)
        finalSTR += "\t</tr>\r\n"
    finalSTR += "</table>"
    return finalSTR


def toHTMLFile(list):
    finalHTMLSTR = "\t\t<table>\n"
    for i in list:
        finalHTMLSTR += "\t\t\t<tr>\n"
        for y in i:
            finalHTMLSTR += "\t\t\t\t<td>{}</td>\n".format(y)
        finalHTMLSTR += "\t\t\t</tr>\n"
    finalHTMLSTR += "\t\t</table>"
    #creates a new file if one is not already created, or opens the file in write mode(meaning it can only write to the file and overwrites everything previously in the file) and writes the html file string to it
    with open("output.html", "w") as f:
        f.write(htmlFile.format(finalHTMLSTR))
        f.close() 
    # os.path.abspath("output.html") just returns the absolute path of the file
    print("\nYour new HTML file can be found at {}".format(os.path.abspath("output.html")))
    #os.system just runs a cmd command in this case opening output.html in the default browser
    os.system("output.html")




answer = ''

while (answer != '1' and answer != '2' and answer != '4'):
    answer = input("\nWhat mode would you like to transfer a csv file to html table:\n\t1. To New HTML File\n\t2. To Print\n\t3. Help\n\t4. Exit\nEnter Your answer here: ")
    
    if (answer == '1'):
        toHTMLFile(readCSV())
    elif(answer == '2'):
        print("\n{}".format(toFinalSTR(readCSV())))
    elif(answer == '3'):
        print("\n\tFirst choose one of the two options of converting the csv file:\n\t\t1. To New HTML file - Creates a new html file template with the table in the body, then prints the absolute path to the file and opens it in the defualt browser(This will overwrite the html file everytime)\n\t\t2. To Print - Prints the table by it's self with proper formating\n\n\tSecond give the relative or final path to the CSV file you would like to convert")
    elif(answer != '4'):
        print("\nInvalid Answer Please try again")