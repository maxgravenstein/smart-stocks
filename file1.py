import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = ['2010-7-19', '2010-7-20', '2010-7-21', '2010-7-22', '2010-7-23']
x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
y = range(len(dates))
#plt.plot(x,y)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()
#print(x,y)