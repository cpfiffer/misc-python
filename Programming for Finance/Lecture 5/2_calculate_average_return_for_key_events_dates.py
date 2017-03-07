# we import xlrd which is the package used for reading excel files
# more information for xlrd can be found at https://pypi.python.org/pypi/xlrd
from xlrd import open_workbook
# numpy is the main scientific computing package of python
# more information can be found at http://www.numpy.org/
import numpy as np

#
# importing the data from excel using the code of lecture 3
def read_from_excel():
    # creation of an xlrd book and sheet based on the path to the excel file
    book = open_workbook('data.xlsx')
    sheet = book.sheet_by_index(0)

    # the excel file has three variables, the dates, the prices and the key events
    # which we append with values from the file
    dates = []
    prices = []
    key_events = []
    for i in range(1, sheet.nrows):
        dates.append(sheet.cell_value(i,0))
        prices.append(sheet.cell_value(i,1))
        key_events.append(sheet.cell_value(i,2))

    # after the for loop, the results are returned to the user
    return dates, prices, key_events


# calculate and return the returns from prices
def calculate_returns_from_prices(input_prices):
    returns = ["-"]
    for i in range(1,len(input_prices)):
        return_in_position_i = np.log(input_prices[i])-np.log(input_prices[i-1])
        returns.append(return_in_position_i)
    return returns

# calculate and return the average return on the key events dates
def calculate_average_return_of_key_events_dates(returns_on_key_events_dates):
    sum_of_returns=0
    for i in range(0,len(returns_on_key_events_dates)):
        sum_of_returns=sum_of_returns+returns_on_key_events_dates[i]
    print(len(returns_on_key_events_dates))
    average_return_of_key_events_dates=sum_of_returns/len(returns_on_key_events_dates)
    return average_return_of_key_events_dates

# keep returns only for key events dates
# by checking whether the value in the key events variable
# column is equal to 1.0
def f_returns_on_key_events_dates(all_returns, key_events_variable):
    returns_on_key_events_dates=[]
    for i in range(0,len(all_returns)):
        if key_events_variable[i]==1.0:
            returns_on_key_events_dates.append(all_returns[i])
    return returns_on_key_events_dates

def median (x):
    sort = sorted(x)
    midpoint = int(len(sort)/2)
    if len(sort) % 2 == 0:
        x1 = sort[midpoint]
        x2 = sort[(midpoint-1)]
        return (x1+x2)/2
    else:
        return (sort[midpoint])



[dates,prices,key_events] = read_from_excel()
returns = calculate_returns_from_prices(prices)
returns_on_key_events_dates = f_returns_on_key_events_dates(returns,key_events)
median_return_of_key_events_dates = median(returns_on_key_events_dates)


print("median return on key events dates is : ", median_return_of_key_events_dates)

#for i in range(0,len(prices)):
#    print(len(dates), len(prices), len(key_events), len(returns))
#    print("Date is : ", dates[i])
#    print("Price is : ", prices[i])
#    print("Key event indicator variable is : ", key_events[i])
#    print("Return is : ", returns[i])
