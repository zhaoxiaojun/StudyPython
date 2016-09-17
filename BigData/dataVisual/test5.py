#coding=utf8
#直方图 Histograms
import numpy as np
import pylab as pl

# make an array of random numbers with a gaussian distribution with
# mean = 5.0
# rms = 3.0
# number of points = 1000
data = np.random.normal(5.0, 3.0, 1000)
# make a histogram of the data array
#pl.hist(data)
pl.hist(data, histtype='stepfilled')
# make plot labels

bins = np.arange(-5., 16., 1.) #浮点数版本的range
pl.hist(data, bins, histtype='stepfilled')

pl.xlabel('data')
pl.show()


