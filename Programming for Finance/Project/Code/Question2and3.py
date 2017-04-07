"""
Question 2:

What was the reaction of the UK stock market, the exchange rate (GBP to Euro, GBP to
USD) and the sovereign bond yields on these dates? Did the stock market go up or down?
By how much? What was the mean return on key events dates? What was the median?
What was the standard deviation? Create a variable that takes the value 0 on days without
key events and 1 on days with key events. Calculate the correlation between the key events
variable and the behaviour of the stock market, the exchange rate and the sovereign bond
yields. Perform a regression analysis between the previous variables.

Question 3:

What was the reaction of the other major stock markets on the dates of these key events?
Perform the analysis of 2) for the major stock markets of the world: USA, China, Japan,
Germany, France, Italy, Russia. How do the stock markets of these countries perform when
a key event is taking place in the UK? If there is a negative return for the UK stock market,
what are the returns for the other stock markets? Are these returns negative as well? Or
not? What is your explanation for what you observe?

"""

import pandas as pd
import statsmodels.formula.api as sm

def load_data():
    #Import our data from munge.py
    data = pd.read_pickle("data.csv")
    print("Load data...")
    return data
def get_returns(data):
    #Converts the dataframe of prices into returns.
    returns = data.ix[:,0:10].pct_change(1)
    returns["KY"] = data["KY"]
    returns = returns[2:]
    returns.to_pickle("returns.csv") #In case I need this elsewhere.
    print("Get returns...")
    return returns
def key_returns(returns):
    #What were the returns on key dates?
    print(returns.head())
    k_event = returns[returns.KY!=0]
    print("Key returns...")
    k_event.to_csv("k_event.csv")
    return k_event
def regression(returns):
    print("Regression 1...")
    #Change the "predicted" variable to what you want returned.
    predicted = ["GBPUSD", "GBPEUR", "FTSE", "UKGILT", "SNP", "HSI", "DAX", "CAC", "FTMIB", "MICEX"]
    #Iterate through each predictor variable and regress it on a constant and
    #the key events variable.

    composite = pd.DataFrame(columns = ["Variable","Coefficient", "P-Value", "R-Squared" ])
    for i in range(0, len(predicted)):
        result = sm.ols(formula = '{} ~ KY'.format(predicted[i]), data = returns).fit()
        composite.loc[i] = [predicted[i], result.params[1], result.pvalues[1], result.rsquared]
    composite
    return composite

    return result
def regression3(returns):
    print("Regression 2...")
    result = sm.ols(formula = "KY ~ GBPUSD + GBPEUR + UKGILT + FTSE + SNP + HSI + DAX + CAC",
    data = returns).fit()
    t = open("Q3 Regression.txt", "w")
    t.write(str(result.summary()))
    t.close()
    return result
def get_correlation(returns):
    x = returns[["KY", "GBPUSD", "GBPEUR", "UKGILT", "FTSE"]]
    corr = x.corr()
    corr.to_csv("corr.csv")
    return corr
def correlation_q3(returns):
    corr3 = returns.corr()
    corr3.to_csv("Q3 Correlation.csv")
    return corr3
def neg_returns(returns):
    '''
    This function shows pretty clearly that other markets have negative returns
    when the UK markets have negative returns, within a very high degree of
    certainty. The only market that doesn't follow this structure is the Italian
    FTMIB, which is just barely not significant at the 5 percent level and is
    also negative.
    '''
    #Dataframe of returns where the FTSE is negative.
    df = returns[returns.FTSE < 0]
    result = sm.ols(formula = ("FTSE ~ CAC + DAX + HSI + SNP + MICEX + FTMIB"), data = df).fit()
    t = open("Q3 Neg Regression.txt", "w")
    t.write(str(result.summary()))
    t.close()
    return result

if __name__ == '__main__':
    data = load_data()
    returns = get_returns(data)

    #Question 2 variables.
    k_event = key_returns(returns)
    mean_kreturns = k_event.mean()
    median_kreturns = k_event.median()
    kstdev = k_event.std()
    corr2 = get_correlation(returns)
    result = regression(returns)

    #Here are the variables for question 3.
    corr3 = correlation_q3(returns)
    corr3
    result3 = regression3(returns)
    neg = neg_returns(returns)
    print(neg.summary())
