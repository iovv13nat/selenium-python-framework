import csv
def getCSVData(fileName):
    #create an empty list to store rows
    rows = []
    # open the csv file
    dataFile = open(fileName, "r")
    #create a csv Reader from csv file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    #add rows from data to list
    for row in reader:
        rows.append(row)
    return rows