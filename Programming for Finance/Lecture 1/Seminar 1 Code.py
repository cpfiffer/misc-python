import numpy as np
import pandas as pd
import urllib.request as urr
import matplotlib as plt

es_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt" #Fucky one
vs_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt"

#These two commands pull the file and dump it into the named document.
urr.urlretrieve(es_url, "es.txt")
urr.urlretrieve(vs_url, "vs.txt")

lines = open("es.txt", 'r')
lines = lines.readlines()
lines = [line.replace(' ', '') for line in lines]


#turns out this data starts using a semicolon at the end of the line starting from row 3,887.
es = pd.read_csv("es.txt", index_col = 0, parse_dates = True, sep = ';', dayfirst = True)
