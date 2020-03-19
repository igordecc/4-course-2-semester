from numpy import sqrt, roll, concatenate as concat
from matplotlib import pyplot
import numpy

N_POINTS = 128

def quadratic_with_noise(n=N_POINTS, mean=0, std=1000):
    base = numpy.array([(i + 2) ** 2 - 3 for i in range(n)])
    noise = numpy.random.normal(mean, std, base.shape)
    return base + noise

def dobeshi(signal):
    S = signal
    n = len(S)

    s1 = S[::2] + sqrt(3) * S[1::2]
    d1 = S[1::2] - sqrt(3)/4 * s1 - (sqrt(3) - 2) / 4 * concat(((s1[-1],), s1[:-1]))
    s2 = s1 - concat((d1[1:n//2], (d1[0],)))

    s = (sqrt(3)-1) / sqrt(2) * s2
    d = -(sqrt(3)+1) / sqrt(2) * d1

    d1 = d * ((sqrt(3)-1)/sqrt(2))
    s2 = s * ((sqrt(3)+1)/sqrt(2))
    s1 = s2 + roll(d1, -1)
    S[1::2] = d1 + sqrt(3)/4*s1 + (sqrt(3)-2)/4*roll(s1, 1)
    S[::2] = s1 - sqrt(3) * S[1::2]

    return d, S


if __name__ == '__main__':
    signal = quadratic_with_noise()
    transformed, reconstructed = dobeshi(signal)

    assert all(signal == reconstructed)

    fig, axes = pyplot.subplots(1, 3, squeeze=False, figsize=(15, 12))

    axes[0, 0].plot(signal, "b")
    axes[0, 0].grid()
    axes[0, 1].plot(transformed, "g")
    axes[0, 1].grid()
    axes[0, 2].plot(reconstructed, "r")
    axes[0, 2].grid()


    pyplot.show()