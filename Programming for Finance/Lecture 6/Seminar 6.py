# Tutorial 5 - Regression Analysis

import pandas as pd
import numpy as np
import urllib.request
import matplotlib.pyplot as plt

es_url="https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt"
vs_url="https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt"
"""
#urllib.request.urlretrieve(es_url, "es.txt")
#urllib.request.urlretrieve(vs_url, "vs.txt")

lines = open("es.txt", "r").readlines()
lines = [line.replace(" ", "") for line in lines]

lines[:6]

for line in lines[3883:3899]:
    print(line[:41])

new_file= open("es50.txt","w")
new_file.writelines('date'+lines[3][:-1]+';DEL' + lines[3][-1])
new_file.writelines(lines[4:])
new_file.close()

new_lines = open("es50.txt", "r").readlines()
new_lines[:5]
"""
es=pd.read_csv('es50.txt', sep=';',dayfirst=True,parse_dates=True, index_col=0)

del es['DEL']

cols=['SX5P','SX5E','SXXP','SX bXE','SXXF','SXXA','DK5F','DKXF']
es=pd.read_csv('es50.txt', sep=';',dayfirst=True,parse_dates=True, index_col=0,
                skiprows=1, header=None, names=cols)

vs = pd.read_csv('vs.txt', index_col=0, header=2, parse_dates=True, sep=',', dayfirst=True)

import datetime as dt
data1=pd.DataFrame({'EUROSTOXX': es['SX5E'][es.index > dt.datetime(1999,1,1)] })
data1=pd.DataFrame({'EUROSTOXX': data1['EUROSTOXX'][data1.index < dt.datetime(2016,2,13)]})

data2=pd.DataFrame({'VSTOXX': vs['V2TX'][vs.index > dt.datetime(1999,1,1)] })
data2=pd.DataFrame({'VSTOXX': data2['VSTOXX'][data2.index < dt.datetime(2016,2,13)]})

data=data1.join(data2)

data = data.fillna(method='ffill')

#data.plot(subplots=True,grid=True,style='b',figsize=(8,6))

rets= np.log(data/data.shift(1))

rets=rets[1:]

#rets.plot(subplots=True, grid=True, style='b', figsize=(8,6))

import statsmodels.formula.api as sm
import statsmodels.tools

xdata=rets['EUROSTOXX']
ydata=rets['VSTOXX']

result= sm.OLS(ydata,statsmodels.tools.add_constant(xdata)).fit()
print(result.summary())
"""
plt.plot(xdata,ydata, 'r.')
ax = plt.axis()
#now we create a series of x values to plot along 0 and 1.
#I'll use this later to draw a line.
x = np.linspace(ax[0], ax[1]+0.01, 1000)
y = result.params[0] + (x*result.params[1])
plt.plot(x, y, lw = 3)
plt.grid(True)
plt.axis('tight')
plt.xlabel("EUROSTOXX for Days")
plt.ylabel("VSTOXX for Centuries")
plt.title("Returns and some other stuff")

#plt.show()
"""
pd.rolling_corr(rets["EUROSTOXX"], rets["VSTOXX"], window = 360).plot(grid = True,style = 'b')
plt.show()
