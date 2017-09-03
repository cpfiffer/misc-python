import pandas as pd
import matplotlib as mp

def read_csv():
    filename = "data.csv"
    df = pd.read_csv(filename)
    return df

df = read_csv()
