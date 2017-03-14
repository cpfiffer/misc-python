import pandas as pd
import statsmodels.api as sm

def priceRet(input_prices):
    returns = ["-"]
    for i in range(1,len(input_prices)):
        return_in_position_i = np.log(input_prices[i])-np.log(input_prices[i-1])
        returns.append(return_in_position_i)
    return returns


key = pd.read_excel("excel_key_events_2.xlsx"

print(key)
