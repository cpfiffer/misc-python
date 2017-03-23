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

def load_data():
    #Import our data from munge.py
    data = pd.read_pickle("data.csv")
    return data
def get_returns(data):
    #Converts the dataframe of prices into returns.
    returns = data.ix[:,0:10].pct_change(1)
    returns["KY"] = data["KY"]
    returns = returns[2:]
    returns.to_pickle("returns.csv") #In case I need this elsewhere.
    return returns
def key_returns(returns):
    #What were the returns on key dates?
    k_event = returns[returns.KY!=0]
    return k_event

if __name__ == '__main__':
    data = load_data()
    returns = get_returns(data)
    k_event = key_returns(returns)
    print(k_event.head())
