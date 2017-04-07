import matplotlib.pyplot as mp
import matplotlib.dates as md
import pandas as pd
import datetime as dt

#Grab pound/USD information
fx = pd.read_pickle("data.csv")
fx = fx[["GBPUSD", "GBPEUR", "KY"]]
fx2 = fx.loc["2013-01-01":] # Remove un-needed data
fx3 = fx2[["GBPUSD", "GBPEUR"]]

#Make significant dates
dates = [dt.date(2013,1,23), dt.date(2016,1,22), dt.date(2016,6,23),
         dt.date(2016,6,24), dt.date(2016,7,13)]

#Labels for annotation
labels = ["Cameron promises referendum", "Conservative party wins", "Referendum date selected",
            "Referendum held", "Results announced", "Cameron resigns, May steps in"]

#fx2.plot()

fig, ax = mp.subplots()

ax.plot(fx3['GBPUSD'], label = "GBP/USD")
ax.plot(fx3['GBPEUR'], label = "GBP/EUR")


labi = 0
for i in range(0,len(fx2)):
    if fx2["KY"][i] == 1:
        ax.annotate(labels[labi], xy = (fx2.index[i], fx2['GBPUSD'][i]),
        textcoords='data', xytext= (fx2.index[i], fx2['GBPUSD'][i]+0.1), arrowprops=dict(arrowstyle='->'))
        labi = labi + 1

'''
#Place annotations here for all i in dates. The following code is suggested
from http://stackoverflow.com/questions/11067368/annotate-time-series-plot-in-matplotlib

for i in range(0,5):
    ax.annotate(labels[i], (md.date2num(dates[i]), fx2.loc[str(dates[i])]),
                textcoords='data', xytext= (dates[i],fx2.loc[str(dates[i])] + 0.05), arrowprops=dict(arrowstyle='-|>'))
'''
mp.legend()
mp.ylabel("GBP vs. Euro and Dollar")
mp.xlabel("Date")
mp.title("Exchange Rates on Key Brexit Dates")
mp.xticks(rotation=45)
mp.grid(True)

#Show the plot we've made.
mp.savefig("timeline.png")
mp.show()
