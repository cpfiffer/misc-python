'''
Try to separate the key events into positive, negative and neutral. What is your rationale
between splitting days into positive, negative, neutral? What is the reaction on the markets
on such days? Is there any difference in the reaction of financial markets among days that
you classify as positive/negative/neutral? How do the other financial markets in your
sample perform on days that you classify as positive/negative/neutral? Do financial markets
move in the same direction? Or in opposite directions? Do financial markets (for the UK
and the other countries) react differently on days T-5, T-4, … , T, … , T+4, T+5 when
“positive”, “negative” or “neutral” events occur on day T? Are financial markets able to
“forecast” whether the events of day T will be “positive”, “negative” or “neutral”? Or do
they just react to events? To perform this analysis, you can calculate the returns on each of
the days in the interval [T-5, T+5], but also the mean returns for these intervals. What is
your explanation for what you observe? Create variables that take the values 0 in days (in
the interval [T-5, T+5]) with positive events, and 1 in days with negative events, and
calculate the correlations and a regression analysis between these variables and the returns
of financial assets.
'''

import pandas as pd
from Question4 import load_returns, t10
import statsmodels.formula.api as sm

def classrow(row):
    # Mean, Standard deviation, Actual
    nodevs = 1
    confidence = nodevs * row[1]
    upper = row[0] + confidence
    lower = row[0] - confidence

    upper
    lower

    row[2] > upper
    row[2] < lower
    if row[2] > upper:
        return 0
    if row[2] < lower:
        return 1
    else:
        return -1

def classify_key1(returns):
    '''
    This method classifies events as positive or negative based simple on the
    mean return of all assets on the day of the event. It's a fairly crude
    instrument and I suspect it's a poor indicator. See classify_key2 for
    hopefully an improved tactic.
    '''
    ky = returns[returns.KY == 1]
    ky = ky[["UKGILT","GBPUSD", "GBPEUR", "FTSE"]]
    finky = ky
    finky["MEAN"] = ky.mean(axis = 1)
    finky["CLS"] = 0
    finky.ix[1, "CLS"] = 1
    for i in range(0, len(finky)):
        if finky["MEAN"].ix[i] > 0:
            finky.ix[i, "CLS"] = "Positive"
        if finky["MEAN"].ix[i] < 0:
            finky.ix[i, "CLS"] = "Negative"
    return finky
def classify_key2(returns):
    ky = returns[returns.KY == 1]
    num_dates = len(ky)
    dates = []
    #get dates of key events so we can pass it to the t10 function, imported
    #from Question4.py
    for i in range(0,num_dates):
        dates.append(ky.index[i])

    #this loop iterates through each date, receives a dataframe of +/- 5 days
    #from the t10 function, runs a regression of each variable in turn for the
    #11 day period, extracts the coefficient and p-value of the KY variable,,
    #and classifies each key event as positive/negative/neutral.
    ky = ky.assign(PARAM = 0, PVAL = 0, CLS = "Neutral")
    ky.loc[dates[1], "PARAM"]
    for i in range(0,num_dates):
        tf = t10(dates[i], returns, boffset = 20, eoffset = 0)
        result = sm.ols(formula = "GBPEUR ~ KY", data = tf).fit()
        ky.loc[dates[i], "PARAM"] = result.params[1]
        ky.loc[dates[i], "PVAL"] = result.pvalues[1]
        if ky.loc[dates[i], "PVAL"] <= 0.05 and ky.loc[dates[i], "PARAM"] < 0:
            ky.loc[dates[i], "CLS"] = "Negative"
        if ky.loc[dates[i], "PVAL"] <= 0.05 and ky.loc[dates[i], "PARAM"] > 0:
            ky.loc[dates[i], "CLS"] = "Positive"
    ky = ky[["GBPEUR", "PARAM", "PVAL", "CLS"]]
    ky = ky.assign(DES = ["Cameron promises referendum", "Conservative party wins",
                "Referendum date selected", "Referendum held", "Results announced", "Cameron resigns, May steps in"])
    return ky
def classify_key3(returns):
    '''
    This method classifies positive, negative, or neutral events by both average
    and standard deviation. For each date, we find the standard deviation and
    average return for the previous twenty days.
    '''
    # This variable changes how many days to use in the rolling window.
    con = 30
    var = "GBPEUR"

    roll = returns[var].rolling(window = con)
    stdev = roll.std()
    mean = roll.mean()
    stdev.name = "Stdev"
    mean.name = "Mean"
    event = pd.concat([mean, stdev], axis =1)
    event = event.shift(1)
    event = pd.concat([event, returns[var], returns["KY"]], axis =1)
    event
    event["Classification"] = event.apply(classrow, axis =1)
    return event
def regression(regret):
    print("Regression 1...")
    #Change the "predicted" variable to what you want returned.
    predicted = ["GBPUSD", "GBPEUR", "FTSE", "UKGILT", "SNP", "HSI", "DAX", "CAC", "FTMIB", "MICEX"]
    #Iterate through each predictor variable and regress it on a constant and
    #the key events variable.

    composite = pd.DataFrame(columns = ["Variable","Coefficient", "P-Value", "R-Squared" ])
    for i in range(0, len(predicted)):
        result = sm.ols(formula = '{} ~ Classification'.format(predicted[i]), data = regret).fit()
        composite.loc[i] = [predicted[i], result.params[1], result.pvalues[1], result.rsquared]
    composite
    return composite

if __name__ == '__main__':
    returns = load_returns()
    classified = classify_key1(returns)
    classified2 = classify_key2(returns)
    classified3 = classify_key3(returns)
    key_dates = returns.index[returns.KY == 1]
    clsreturns = returns.join(classified3.Classification)
    key = classified3.loc[key_dates]
    key["Description"] = ["Cameron promises referendum", "Conservative party wins","Referendum date selected", "Referendum held", "Results announced", "Cameron resigns, May steps in"]
    dateclass = t10(key_dates[4],clsreturns)

    neg = clsreturns[clsreturns.Classification == 1]
    pos = clsreturns[clsreturns.Classification == 0]
    neu = clsreturns[clsreturns.Classification == -1]

    regret = clsreturns[clsreturns.Classification == 1]
    regret = regret.append(clsreturns[clsreturns.Classification == 0])

    regret

    result = regression(regret)
    result
