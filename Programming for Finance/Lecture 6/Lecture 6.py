import pandas as pd
import statsmodels.api as sm

# This is a dataframe of advertising data.
"""
# This code saves the data to file.
url = "http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv"
advert = pd.read_csv(url, index_col = 0)
advert.to_pickle("advert.csv")
"""
advert = pd.read_pickle("advert.csv")
#Tv, Radio, Newspaper, Sales, by spending.
#Can we predict which advertising medium is the most efficient?
#I.e. multiple regression to find sales influence.
x = advert[["TV", "Radio", "Newspaper"]]
y = advert["Sales"]

x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
print(est.summary())
