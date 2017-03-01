# The following is copied from the work we did in the last couple of weeks.
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
#urr.urlretrieve(es_url, "es.txt")
#urr.urlretrieve(vs_url, "vs.txt")

lines = open("es.txt", "r").readlines()
lines = [line.replace(" ", "") for line in lines]

# Open a file, set it to write.
# Then we put in a header, which is the header of the "lines" list.
# Then we post the remaining sections of lines, and close the file.
new_file = open("es50.txt", "w")
new_file.writelines("Date" + lines[3][:-1] + ";DEL" + lines[3][-1])
new_file.writelines(lines[4:])
new_file.close()

# new_lines = open("es50.txt", "r").readlines()

pdl = pd.read_csv("es50.txt", sep = ";")
# print(pdl.ix[0:4,:]) # A look before we delete the DEL column
del pdl["DEL"] # This removes the column we're talking about.
print(pdl.tail()) # Now we have a normal ass data frame.
