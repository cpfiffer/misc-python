'''

Perform the analysis of 2) and 3) up to -5 days before a key event date, and up to +5 days
after a key event date. Plot the prices and returns of days T-5, T-4, T-3, T-2, T-1, T, T+1,
T+2, T+3, T+4, T+5 for the stock markets, the exchange rates and the sovereign bond
yields. What do you notice? Is there any movement in the markets before key event dates?
Do financial markets react positively or negatively before, after, and on the days of key
events? Repeat the steps 2) and 3) using cumulative returns from five days before the event
to one day after the event. What do you observe? What happens if you consider the
cumulative returns from five days before the event to three days after the event? What do
you learn about the impact of these events? Comment on the sign and persistence of the
information shock.
'''

import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as mp
from pandas.tseries.offsets import *

def load_returns():
    df = pd.read_pickle("returns.csv")
    return df
def load_prices():
    df = pd.read_pickle("data.csv")
    return df
def t10(date, returns, boffset = 5, eoffset = 5):
    '''
    This function returns a dataframe with the returns +/- 5 days from a specific
    date.
    '''
    boff = boffset * BDay()
    eoff = eoffset * BDay()
    b = date - boff
    e = date + eoff
    df = returns.loc[b:e]
    return df
def cumu_returns(df):
    cumu = df.cumsum(axis = 0)
    return cumu
def plot_returns(tf, num, title = "No title"):
    mp.clf()
    mp.plot(tf.index, tf["FTSE"])
    mp.plot(tf.index, tf["SNP"])
    mp.plot(tf.index, tf["DAX"])
    mp.plot(tf.index, tf["UKGILT"])
    mp.plot(tf.index, tf["GBPUSD"])
    mp.plot(tf.index, tf["GBPEUR"])
    mp.xlabel("Date")
    mp.ylabel("Daily Return")
    mp.xticks(rotation=45)
    mp.title(title)
    mp.grid(True)
    mp.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    mp.gcf().subplots_adjust(bottom=0.15, right = .75)
    mp.savefig("{}.png".format(num))
    #mp.show()
    return 0
def create_matrix(date, returns):
    t = t10(date, returns)


if __name__ == '__main__':
    labels = ["Cameron promises referendum", "Conservative party wins", "Referendum date selected",
                "Referendum held", "Results announced", "Cameron resigns, May steps in"]
    returns = load_returns()
    prices = load_prices()
    num_dates = len(returns[returns.KY == 1].index)
    #This iterates throughout each requirement of the question and produces
    #all the necessary graphs.
    for i in range(0,1):
        date = returns[returns.KY == 1].index[4]
        tf = t10(date, returns)

        plot_returns(tf, 1, title = "{}, +/- 5 days, actual returns".format(labels[4]))
        '''
        Repeat the steps 2) and 3) using cumulative returns from five days before the event
        to one day after the event.
        '''
        tf2 = t10(date, returns, eoffset = 1)
        cumu = cumu_returns(tf2)
        plot_returns(cumu, 2, title = "{}, -5, +1 day, cumulative sum".format(labels[4]))

        '''
        What happens if you consider the
        cumulative returns from five days before the event to three days after the event?
        '''
        tf3 = t10(date, returns, eoffset = 3)
        cumu2 = cumu_returns(tf3)
        plot_returns(cumu2, 3, title = "{}, -5, +3 days, cumulative sum".format(labels[4]))

        tf4 = t10(date, returns, eoffset = 5)
        cumu3 = cumu_returns(tf4)
        cumu3
        plot_returns(cumu3, 4, title = "{}, +/- 5 days, cumulative sum".format(labels[4]))

        print(date)
