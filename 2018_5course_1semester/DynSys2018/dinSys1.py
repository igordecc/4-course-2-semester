import matplotlib
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
import numpy as np

def ressler(x, y, z, a = .01, b = .2, r = 5.7, h = 0.01 ):     #a = 0.2, b = 0.2, r = 5.7
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

    xyz = xyz[(evaluateNum//4):]    # 0. избавиться - переходный процесс
    xyz = numpy.transpose(xyz)
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    #плоскость x=2
    #1. задание плоскости x=2



    #print(list(enumerate(np.array(x))))
    def getSliceNums(x, sectionx = 2):
        np.array(x)
        np.ndenumerate(x)
        listt = [i<sectionx  for i in x]
        pairedListt = [i for i in zip([0] + listt, listt + [0])][1:-2]
        numberList = [i[0] for i in enumerate(pairedListt) if (i[1] == (False, True)) ] # Puankare sectrion from one side only
        return numberList

    slicex = []
    slicey = []
    slicez = []
    for i in getSliceNums(x):
        slicex.append(x[i])
        slicey.append(y[i])
        slicez.append(z[i])

    ax.plot(x, y, z, label="ressler's attractor")
    ax.plot(slicex, slicey, slicez, label="ressler's attractor", color = "r")
    # Y = np.arange(-10, 10, 0.25)
    # Z = np.arange(-10, 10, 0.25)
    # Y, Z = np.meshgrid(Y, Z)
    # X = np.array([2 for i in np.arange(-10, 10, 0.25)])
    # ax.plot_surface(X,Y,Z, shade=True)
    ax.legend()


    #Axes3D.plot(xyz)

    #print(xyz)
    pyplot.show()
