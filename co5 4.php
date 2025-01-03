import csv
filename 1=input("Enter the CSV file name:")
with open(filename1,'r')as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        print(row
