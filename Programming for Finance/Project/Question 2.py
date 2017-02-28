"""
What was the reaction of the UK stock market, the exchange rate (GBP to Euro, GBP to
USD) and the sovereign bond yields on these dates? Did the stock market go up or down?
By how much? What was the mean return on key events dates? What was the median?
What was the standard deviation? Create a variable that takes the value 0 on days without
key events and 1 on days with key events. Calculate the correlation between the key events
variable and the behaviour of the stock market, the exchange rate and the sovereign bond
yields. Perform a regression analysis between the previous variables
"""
import pandas as pd
import quandl
import datetime as dt

#Dates from Timeline.csv, in string format because it's easier.
dates = ["20130123", "20160122", "20160623", "20160624", "20160713"]

#import currency data
fx = pd.read_csv("CUR-GBP.csv", parse_dates=True)

#Cast the object type of date to a datetime format
fx["DATE"] = fx["DATE"].astype("datetime64[ns]")

#index the FX data by date, so we can search it later.
fx_di = fx.set_index('DATE')

print(fx_di.head(5))

for i in range(0, len(dates)):
    print(fx_di.loc[dates[i]])
