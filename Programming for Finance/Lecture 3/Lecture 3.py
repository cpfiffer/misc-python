"""
This class took place on February 21st, 2017.

We're going to do a bit of work on the project and the stuff we need to do it.
"""

# I first made an excel file with some random variables. Two columns, ten observations.
# We import xlrd to import from excel files.
from xlrd import open_workbook

def read_from_excel():
    book = open_workbook("data.xlsx")
    sheet = book.sheet_by_index(0)
    x = []
    y = []

    for i in range(1, sheet.nrows):
        x.append(sheet.cell_value(i,0))
        y.append(sheet.cell_value(i,1))

    return x, y

def sum_of_list(x):

    """
    Sums all the elements of a list.
    """

    su = 0
    for i in range(0,len(x)):
        su = su + x[i]
    return su

#This function returns the average for the list. Pretty easy.
def avg_list(x):
    su = sum_of_list(x)
    return (su/len(x))

[xvar,yvar] = read_from_excel()
print(xvar)
print(yvar)
print('\n')

#Woo. Can't stop me now.
listy = [1,2,3,4,5]
su = sum_of_list(listy)
print("Sum of the list: ", su)

avg = avg_list(listy)
print("Average of list: ", avg)

x_avg = avg_list(xvar)
y_avg = avg_list(yvar)

print("Average of X: ", x_avg)
print("Average of Y: ", y_avg)

print((int(4.9)))

def median_list(x):
    sort = sorted(x)
    midpoint = len(sort)/2
    if type(midpoint) == float:
        return sort[]
