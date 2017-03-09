# The following is copied from the work we did in the last couple of weeks.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as urr
import datetime as dt
import statsmodels.formula.api as sm
import statsmodels.tools

#The URL's for our datasets
es_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt" #This one has a problem with semicolons
vs_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt"

#Print a concantenated output of the two URLs.
#print(es_url + '\n' + vs_url)

#Retrieve the page as a file.
#urr.urlretrieve(es_url, "es.txt")
#urr.urlretrieve(vs_url, "vs.txt")

lines = open("es.txt", "r").readlines()
lines = [line.replace(" ", "") for line in lines]

# Open a file, set it to write.
# Then we put in a header, which is the header of the "lines" list.
# Then we post the remaining sections of lines, and close the file.
new_file = open("es50.txt", "w")
new_file.writelines("Date" + lines[3][:-1] + ";DEL" + lines[3][-1])
new_file.writelines(lines[4:])
new_file.close()

# new_lines = open("es50.txt", "r").readlines()

es = pd.read_csv("es50.txt", sep = ";", parse_dates=True, dayfirst=True, index_col=0)
# print(pdl.ix[0:4,:]) # A look before we delete the DEL column
del es["DEL"] # This removes the column we're talking about.
#print(es.head()) # Now we have a normal ass data frame.

#Read in our other file.
vs = pd.read_csv("vs.txt", sep = ",", parse_dates=True, header = 2, index_col=0, dayfirst=True)
#print(vs.head())

data1 = pd.DataFrame({"EUROSTOXX":es['SX5E'][es.index > dt.datetime(1999, 1, 1)]})
data1 = pd.DataFrame({"EUROSTOXX":data1['EUROSTOXX'][data1.index < dt.datetime(2016,2,13)]})

data2 = pd.DataFrame({"VSTOXX":vs["V2TX"][vs.index > dt.datetime(1999, 1, 1)]})
data2 = pd.DataFrame({"VSTOXX":data2["VSTOXX"][vs.index < dt.datetime(2016, 2, 13)]})


"""
The tutor recommends using .fillna('ffill') to pull down the
previous day's values, though that doesn't seem right to me.

The code for the recommended thing is as follows, though from
here the seminar tutor and I have diverged substantially.
If you want to revert to the "actual" method, remove
the inner join argument from the joiner below, and uncomment
the statement below the join.

It may also be that it's more 'realistic', but I would have
to know more about VSTOXX. I have no idea what it represents.
"""
data = data1.join(data2)
data = data.fillna(method = 'ffill')

data.plot(subplots=True, grid=True, style = 'b', figsize=(8,6))

rets = np.log(data/data.shift(-1))
#print(rets.head())

rets = rets[1:]

rets.plot(subplots=True, grid=True, style = 'b', figsize=(8,6))

#REVEAL
#plt.show()

xdata = rets['EUROSTOXX']
ydata = rets['VSTOXX']

print(xdata.head(), '\n', ydata.head())

result = sm.OLS(ydata, statsmodels.tools.add_constant(xdata)).fit()
print(result.summary())
