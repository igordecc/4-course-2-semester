import numpy
import numpy as np
from tqdm import tqdm
import cmath as c
from math import pi
import matplotlib.pyplot as plt

#===BULSHIT FUNCTIONS
def wiener_khinchin(
        akf: numpy.ndarray,
):
    pass
    if len(akf.shape) > 1:
        akf = akf[:, -1]

    size = len(akf)
    f_size = int(size/2)

    cplx_res = numpy.zeros(shape=f_size, dtype=numpy.complex)

    for fIdx in tqdm(range(f_size), desc="Wiener-Khinchin computing"):
        minusJByTwoPif = complex(0.0, -2.0*pi*fIdx/size)

        res = complex(0.0, 0.0)
        for k in range(size):
            res += akf[k] * c.exp(minusJByTwoPif * k)
        cplx_res[fIdx] = res

    return abs(cplx_res)/f_size

def correlation(
        x: numpy.ndarray,
        y: numpy.ndarray,
        tau             # int or list[int]
):
    if len(x.shape) > 1:
        x = x[:, -1]

    if len(y.shape) > 1:
        y = y[:, -1]

    if hasattr(tau, '__iter__'):
        cor = numpy.empty((len(tau), 2))
        for idx in tqdm(range(len(tau)), desc="computing corelation"):
            t = tau[idx]
            cor[idx] = (float(t), correlation(x, y, int(t)))
        return cor

    else:
        size = min(len(x), len(y))
        x_mean = x.sum()/size
        y_mean = y.sum()/size

        cor = 0.0
        for t in range(size - int(tau)):
            cor += (x[t] - x_mean) * (y[t + tau] - y_mean)
        return cor / (size - tau)

def dft(
        x: numpy.ndarray,
):
    pass
    if len(x.shape) > 1:
        x = x[:, -1]

    size = len(x)
    f_size = int(size/2)
    # f_size = int(size)

    jByMinus2Pi: complex = complex(0, -2.0*pi)
    cplx_res = numpy.zeros(shape=f_size, dtype=numpy.complex)

    for fIdx in tqdm(range(f_size), desc="DFT computing"):
        jByMinus2PiByKOverN = jByMinus2Pi * fIdx / size

        resultK = complex(0.0, 0.0)
        for tIdx in range(size):
            resultK += complex(x[tIdx], 0) * c.exp(jByMinus2PiByKOverN*tIdx)
        cplx_res[fIdx] = resultK

    return abs(cplx_res[1:]) / size
#==============





def log_map(x, r):
    return r * x * (1 - x)

def do_map(
        itter_n=1000,
        x_array=[0.1],
        r=3.8):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return np.array(x_array)


#============ ROUND2
from math import sin, cos
def do_map2():
    count = 1000

    data = [ (i, sin(i/2) + sin(i/8) + cos(i/4)) for i in range(count)]
    data = np.array(data)
    return data
#==============


def autocorr1(x, lags_list):
    '''manualy compute, non partial'''
    mean = np.mean(x)
    var = np.var(x)
    xp = x - mean
    # print("xp: ", xp)
    # print("var: ", var)     # omega^2
    # print("mean: ", mean)
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

    #========2 ========
    x_array = do_map2()
    y_array = do_map2()

    num_of_elements = 1000
    tau = [i for i in range(num_of_elements//2)]

    data2 = correlation(
                x_array,
                y_array,
                tau)


    # ========1
    data = wiener_khinchin(data2)
    assert type(data) == np.ndarray
    # plt.plot(data)
    # plt.grid()
    # plt.show()


    #========3 ========

    data3 = dft(x_array)


    #============== subplots ===========
    fig, axlist = plt.subplots(2,2)

    axlist[0][0].set_title("Cигнал sin(i/2) + sin(8/2)+ cos(i/4)")
    axlist[0][0].plot(x_array.T[1])

    axlist[1][0].set_title("AKF")
    axlist[1][0].plot(*data2.transpose())  #.T - it's numpy.transpose

    axlist[0][1].set_title("DFT")
    axlist[0][1].plot(data3)


    axlist[1][1].set_title("теорема Винера-Хинчина, DFT")
    axlist[1][1].plot(data3, label="DFT")

    axlist[1][1].plot(range(0,len(data)*2,2),data, label="Винер-Хинчин")


    for i in axlist:
        for j in i:
            j.grid()

    #========== HRAY!!!
    plt.subplots_adjust(hspace=0.6)
    fig.tight_layout()

    plt.show()

    #TODO
    ## periodic function sin(i/2) + sin(i/4) + cos(i /4)
    ## periodic function y coordinat from Henon map [
    # henon1_init_state = (0.0, 0.0)
    # henon2_init_state = (0.1, 0.1)
    # count = 1000
    #
    # def henon(
    #         state,
    #         other_state,
    #         eps,do_last_funcs.py
    #         a=1.4,
    #         b=0.3
    # ):
    #     def f(x_1, x_2):
    #         return 1.0 - a * x_1 * x_1 + x_2
    #
    #     return (
    #         f(*state) + eps * (f(*other_state) - f(*state)),
    #         b * state[0]
    #     )
    #
    #
    # first_state = henon1_init_state
    # second_state = henon2_init_state
    # eps = 0.1706 # generalised sync
    #
    # for idx in range(count):
    #     first_state, second_state = henon(first_state, second_state, eps), henon(second_state, first_state, eps)
    #     x_array = first_state
    #     y_array = second_state
