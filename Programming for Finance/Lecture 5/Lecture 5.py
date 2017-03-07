#This course took place on March 7th, 2017.
#

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
