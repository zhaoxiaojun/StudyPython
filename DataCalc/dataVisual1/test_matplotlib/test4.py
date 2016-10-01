#coding=utf8
import numpy as np
import pylab as pl

#直方图（Histograms）

# make an array of random numbers
data = np.random.normal(5.0, 3.0, 1000)

# make a histogram of the data array
pl.hist(data)
#pl.hist(data, histtype='stepfilled')

pl.show()


