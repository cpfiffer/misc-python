# This lecture took place on February 28th, 2017.
# Andreas has just revised the project, we now have an extra month and fewer questions.

# To start, I modified the Excel sheet I'm using in the project for GBP/USD
# to include a boolean for key dates.

from xlrd import open_workbook
import numpy as np

def read_excel():
    book = open_workbook("data.xlsx")
    sheet = book.sheet_by_index(0)
    x = []
    y = []
    z = []

    for i in range(1, sheet.nrows):
        x.append(sheet.cell_value(i,0))
        y.append(sheet.cell_value(i,1))
        z.append(sheet.cell_value(i,2))

        return x, y, z
def priceret(prices):
    returns = []
    for i in range(1, len(prices)-1):
        returns.append((np.log(prices[i]) - np.log(prices[i-1]))/np.log(prices[i-1]))
    return returns
def listAverage(ist):
    sum = 0
    for i in range(0, len(ist)):
        sum = sum + ist[i]

    average = sum/len(ist)
    return (average)
def key_ret(returns, key):
    kreturn = []
    for i in range(0,len(key)):
        if key[i] == 1:
            kreturn.append(returns[i-1])
    return (listAverage(kreturn))

[x, y, z] = read_excel()

#Check first couple of lines
#print(x[0:4], y[0:4], z[0:4])

returns = priceret(y)
allreturn = listAverage(returns)
kreturn = key_ret(returns,z)

print("The average return on all of our dates is: ", allreturn)
print("The average return on our key dates is: ", kreturn)
