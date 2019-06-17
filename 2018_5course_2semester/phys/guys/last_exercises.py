import numpy
from tqdm import tqdm
import cmath as c
from math import pi

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