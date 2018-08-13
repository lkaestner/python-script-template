#!/usr/bin/env python

# Template for Python Scripts

# Prerequisites
# 1. Python 3
# 2. pip install numpy pandas matplotlib

# declare a variable
myvar = "World"

# simple parameterized function
def myfunction(myparam):
    print("Hello " + myparam)
    
myfunction(myvar)

# conditions
def mycondition(mynumber):
    if mynumber > 2:
        print("Huuuge")
    else:
        print("Tiny")
        
mycondition(3)

# loops
def myloop(mycount):
    for i in range(1,mycount):
        print("Iteration: {}".format(i))
        
myloop(3)

# current datetime
def getdatetimestring():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print("Current Datetime: " + getdatetimestring())

# write file (with default parameters)
def writefile(myfilename="myfile.tmp", mytext="bar"):
    with open(myfilename, "w", encoding="UTF-8") as myfile:
        myfile.write("foo:" + mytext)

writefile(mytext="baar", myfilename="myfile.txt")

# read file
def readfile(myfilename):
    with open(myfilename, "r", encoding="UTF-8") as myfile:
        for line in myfile:
            print(line)
            
readfile("myfile.txt")

# some simple "science":
def doscience():
    # import libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # create a dataframe
    mydata = pd.DataFrame({"city":["New York", "Berlin", "Tokyo", "Mumbai", "Johannesburg"],
                           "employees":[16, 23, 13, 34, 5],
                           "sales":[1000.0, 1300.0, 900.0, 1900.0, 200.0]})
    print(mydata)

    # add a derived column
    mydata["sales_per_employee"] = mydata["sales"] / mydata["employees"]
    # sort by descending by the new column (inplace, don't return new dataframe)
    mydata.sort_values(by="sales_per_employee", ascending=False, inplace=True)
    # fix indexes
    mydata.reset_index(drop=True, inplace=True)
    print(mydata)

    # add a conditional column
    mydata["performance_flag"] = np.where(mydata.sales_per_employee > 60, "good", "bad")
    print(mydata)

    # calculate correlation of employee-count and sales-volume
    mycorrframe = mydata.corr()
    mycorrval = mycorrframe["employees"]["sales"]
    print(mycorrval)

    # plot the data:
    x = mydata["employees"]
    y = mydata["sales"]
    plt.scatter(x, y)
    # add labels:
    plt.title("Sales-Volume vs Employee-Count")
    plt.xlabel("Employee-Count")
    plt.ylabel("Sales-Volume")
    # add trendline:
    p = np.polyfit(x, y, 1)
    f = np.poly1d(p)
    plt.plot(x,f(x),"r-")
    # write to file:
    plt.savefig("myscatterplot.png")

doscience()
