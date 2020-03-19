import numpy
import matplotlib.pyplot as plt

x = numpy.array([i for i in numpy.linspace(1,4,100)])
y = 1.5*x**0.5
plt.plot(x,y)
plt.show()

