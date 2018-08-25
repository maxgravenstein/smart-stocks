#Steps
#1. Read the csv file 
#2. Convert the dates to numbers
#3. Plot (date, number)
import csv
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

with open('bitcoin.csv') as file:
    count = 0
    reader = csv.reader(file)
    next(reader, None) #skip the headers
    
    for row in reader:
        x = dt.datetime.strptime(row[0][0:10], '%Y-%m-%d').date()
        y = float(row[1])
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.plot(x,y)
        plt.gcf().autofmt_xdate()
        
        print(x,y)
        if count > 5:
            break
        count +=1

#datetime format: %Y-%m-%d