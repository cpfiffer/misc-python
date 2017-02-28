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

[x, y, z] = read_excel()

#Check first couple of lines
#print(x[0:4], y[0:4], z[0:4])

returns = priceret(y)
print(returns)
