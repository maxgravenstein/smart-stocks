#Steps
#1. Read the csv file
#2. Convert the dates to numbers
#3. Plot (date, number)
import csv

with open('bitcoin.csv') as file:
    count = 0
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
        if count > 5:
            break
        count +=1