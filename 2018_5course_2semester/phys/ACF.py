"""
Program, that compute Autocorrelation function for discrete time-signal of logistic map
https://en.wikipedia.org/wiki/Autocorrelation
"""

import numpy as np
import matplotlib.pyplot as plt

def log_map(x, r):
    return r * x * (1 - x)

def do_map(
        itter_n=1000,
        x_array=[0.1],
        r=3.5):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array

def autocorr1(x, lags_list):
    '''manualy compute, non partial'''
    mean = np.mean(x)
    var = np.var(x)
    xp = x - mean
    print("xp: ", xp)
    print("var: ", var)     # omega^2
    print("mean: ", mean)
    corr = [1. if lag == 0 else np.sum(xp[:-lag]*xp[lag:])/len(x)/var for lag in lags_list]
    return np.array(corr)

def autocorr2(x, lags):
    '''np.correlate, non partial'''
    mean = x.mean()
    var = np.var(x)
    xp = x-mean
    corr = np.correlate(xp, xp, 'full')[len(x)-1:]/var/len(x)
    return corr[:len(lags)]

#TODO ADD with autocorr fft

if __name__ == '__main__':
    x_array = np.array(do_map())
    max_lag = 10
    lag_values = [i for i in range(max_lag)]
    corr_data1 = autocorr1(x_array, lag_values)
    corr_data2 = autocorr2(x_array, lag_values)
    # plt.plot(lag_values, corr_data1, "c")
    plt.plot(lag_values, corr_data2, "r")
    plt.show()
