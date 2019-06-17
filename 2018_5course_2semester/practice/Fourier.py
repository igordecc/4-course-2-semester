import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of sample points
N = 500
T = 1.0 / 1000.0

# frequency example
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
print(x)
print(y)

# solution - Fourier analysis building
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N)
# plots
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf))
plt.grid()
plt.show()
