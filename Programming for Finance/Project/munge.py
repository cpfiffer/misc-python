'''
This script reads from a pre-prepared excel sheet with all data needed,
separated on different sheets. Because dates may vary from asset to asset
and by country to country (FTSE vs. CAC), I separate perform and outer join
on each individual data series and create a composite dataframe. This script
"pickles" the data frame so that other scripts can simply load it into memory
when necessary.
'''

import pandas as pd

def read_excel():
    '''
    This reads the excel sheet containing all relevant closing prices, and
    turns them into a single pandas dataframe for later use. Because trading
    dates may vary between assets and across countries, I separate them by
    asset into a unique data frame and then combine a join on each component
    part.

    The worksheet index is as follows:
    0. GBPUSD
    1. GBPUSD
    2. FTSE
    3. S&P
    4. UKGILT
    5. HSI
    6. DAX
    7. CAC
    8. FTMIB
    9. MICEX
    10.KY (the key indicator boolean)
    '''
    df = pd.DataFrame()
    for i in range(0,11):
        book = pd.read_excel("Progdata.xlsx", sheetname=i,
                            index_col=0)
        df = df.join(book, how='outer')

    df["KY"] = df["KY"].fillna(0)
    df = df.fillna(method = 'ffill')
    df[["KY"]] = df[["KY"]].astype(int)
    return(df)

if __name__ == '__main__':

    df = read_excel()
    print(df.head())
    print(df.ix["2016-06-24"])
    print(df.dtypes)
    df.to_pickle("data.csv")
