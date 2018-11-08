import matplotlib
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy

def ressler(x, y, z, a = .1, b = .2, r = 5.7, h = 0.01 ):     #a = 0.2, b = 0.2, r = 5.7
    new_x = - y - z
    new_y = x + a*y
    new_z = b + (x-r)*z
    return x + h*new_x, y + h*new_y, z + h*new_z


def integrate(f, x):
    return y

if __name__ == '__main__':
    #matplotlib.rcParams['legend.fontsize'] = 10

    fig = pyplot.figure()
    ax = fig.gca(projection="3d")

    x0, y0, z0 = .1, .1, .1

    evaluateNum = 100000
    xyz = numpy.empty((evaluateNum, 3))
        
    xyz[0] = [x0, y0, z0]
    for i in range(1,evaluateNum):
        xyz[i] = ressler(*xyz[i-1])

    xyz = numpy.transpose(xyz)
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    ax.plot(x, y, z, label="ressler's attractor")
    ax.legend()

    #Axes3D.plot(xyz)

    print(xyz)
    pyplot.show()