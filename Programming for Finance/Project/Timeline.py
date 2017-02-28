import matplotlib.pyplot as mp
import matplotlib.dates as md
import pandas as pd
import datetime as dt

#Grab pound/USD information
fx = pd.read_csv("CUR-GBP.csv", parse_dates= True, dayfirst = False, keep_date_col=True)
fx2 = fx.set_index(["DATE"]) #Re-index the above into something we we can search
fx2 = fx2.loc["2013-01-01":] # Remove un-needed data
fx2 = 1/fx2 # Convert GBP/USD to USD/GBP

#Make significant dates
dates = [dt.date(2013,1,23), dt.date(2016,1,22), dt.date(2016,6,23),
         dt.date(2016,6,24), dt.date(2016,7,13)]

#Labels for annotation
labels = ["Cameron promises referendum", "Referendum date selected",
            "Referendum held", "Results announced", "Cameron resigns, May steps in"]

fig, ax = mp.subplots()
ax.plot_date(fx2.index, fx2, 'b-', xdate = True) #Needs to be subset to first date

#Place annotations here for all i in dates. The following code is suggested from http://stackoverflow.com/questions/11067368/annotate-time-series-plot-in-matplotlib
for i in range(0,5):
    ax.annotate(labels[i], (md.date2num(dates[i]), fx2.loc[str(dates[i])]),
                textcoords='data', xytext= (dates[i],fx2.loc[str(dates[i])] + 0.05), arrowprops=dict(arrowstyle='-|>'))

fig.autofmt_xdate()
mp.ylabel("USD/GBP Exchange Rate")
mp.xlabel("Date")
mp.title("Dollar to Pound Sterling Exchange Rate on Key Brexit Dates")
mp.grid(True)

#Show the plot we've made.
mp.show()
