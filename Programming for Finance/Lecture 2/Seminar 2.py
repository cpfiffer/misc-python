#This seminar took place on February 8th, 2017.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as urr

#The URL's for our datasets
es_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt" #This one has a problem with semicolons
vs_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt"

#Print a concantenated output of the two URLs.
#print(es_url + '\n' + vs_url)

#Retrieve the page as a file.
urr.urlretrieve(es_url, "es.txt")
urr.urlretrieve(vs_url, "vs.txt")

lines = open("es.txt")
lines2 = lines.readlines()
lines3 = [lines2.replace(' ', '') for line in lines]

print(lines2.line)

#We didn't even make it to the same point me made it to last week. God damn.
