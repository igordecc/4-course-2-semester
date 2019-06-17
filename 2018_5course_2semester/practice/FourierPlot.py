import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.fftpack
from matplotlib.font_manager import FontProperties
from pylab import figure, plot, xlabel, grid, legend, title, savefig

# Number of sample points
N = 7500
T = 1.0 / 500.0

# frequency example
x = np.linspace(0.0, N*T, N)
y = np.sin(800.0 * 2.0*np.pi*x) + 0.5*np.sin(500.0 * 2.0*np.pi*x)


# fourier analysis building
def do_fourier_plot(s, path, title):
    yf = scipy.fftpack.fft(s)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

    # fourier plots
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.xlabel('Frequency[$f$]')
    plt.ylabel('x')
    # plt.ylim(0, 20)
    figure(1, figsize=(10, 8))
    xlabel('t')
    grid(True)
    legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
    plt.title(title)
    # savefig(path, dpi=100)
    plt.show()
