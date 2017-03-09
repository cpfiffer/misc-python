#This course took place on March 7th, 2017.
#
import math
#Calculate the median of a list
def median (x):
    sort = sorted(x)
    midpoint = int(len(sort)/2)
    if len(sort) % 2 == 0:
        x1 = sort[midpoint]
        x2 = sort[(midpoint-1)]
        return (x1+x2)/2
    else:
        return (sort[midpoint])

def mean(x):
    su = sum(x)
    average = su/len(x)
    return average

def variance(x):
    average = mean(x)
    n = len(x)
    error = []
    for element in x:
        ie = (element - average)**2
        error.append(ie)
    return sum(error)/n

def correlation(x, y):
    if len(x) != len(y):
        return ("The lists are not the same size!")
    topsum = 0
    xmean = mean(x)
    ymean = mean(y)
    xdev = variance(x)**0.5
    ydev = variance(y)**0.5
    for i in range(0,len(x)):
        product = (x[i] - xmean)*(y[i] - ymean)
        topsum = topsum + product
    correlation = (topsum/((len(x) -1) * xdev * ydev))
    return correlation


"""
The __name__ thing is based on the way that Python interacts with the rest of
the computing environment. When a Python file is run, every statement is
executed. When a Python file is self-executed, it's name is __main__, but
if the script is being called by something else, it's name is set to the
process running it.
"""

if __name__ == '__main__':
    #Median should be 8.
    olist = [1,5,8,9,10]
    #Median should be 6.5.
    elist = [1,5,8,9]

    o_median = median(olist)
    e_median = median(elist)

    print("The odd list of ", olist, " has a median of ", o_median,
          " and the even list of ", elist, "has a median of ", e_median, ".")

    vlist = [1,9,9,100,5]

    v_var = variance(vlist)
    stdev = v_var**0.5

    print("The variance of list", vlist, "is ", v_var, ".")
    print("The standard deviation of the same list is", stdev, ".")

    x_list = [3,0.5,3,4,0.5,2]
    y_list = [6,1,6,8,1,4]

    corr = correlation(x_list, y_list)

    print()
    print("The correlation between our two lists is", corr)

#And with that, we finish the lecture. Not bad!
#Well, everyone else is kinda bored, but I'm having fun.
