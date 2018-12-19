import matplotlib
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
import numpy as np

# def ressler(x, y, z, a = .25, b = 0.15, r = 2.5, h = 0.01 ):     #a = 0.2, b = 0.2, r = 5.7
#     new_x = - y - z
#     new_y = x + a*y
#     new_z = b + (x-r)*z
#     return x + h*new_x, y + h*new_y, z + h*new_z

def ressler(x, y, z, a=1.4, b=0.3, r=2.5, h=0.01):
    new_x = 1 - a*x**2 + b*y
    new_y = x
    new_z = 0
    return new_x, new_y, new_z

# get the slice's points coordinates
# slicex = [1,2,3,4,5,6,7,8,9]
# slicey = [1,2,3,4,5,6,7,8,9]
# slicez = [1,2,3,4,5,6,7,8,9]
def doPortret(ressler=ressler, a=1.4, b=0.3, r=2.5, evaluateNum=10000,):
    xyz = numpy.empty((evaluateNum, 3))

    x0 = .1
    y0 = .1
    z0 = .1
    xyz[0] = [x0, y0, z0]
    for i in range(1, evaluateNum):
        xyz[i] = ressler(*xyz[i - 1], a, b, r) # DONT TOCH!!!!!!!!!!!!!!!!!

    xyz = xyz[(evaluateNum // 10):]  # 0. избавиться - переходный процесс
    xyz = numpy.transpose(xyz)
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    return x,y,z

# system has points.
# get number of points wich in the slice sectionx=2
# get arrays slicex, slicey, slicez
def slicer(x,y,z, sectionx=0.0):
    slicex = []
    slicey = []
    slicez = []
    x,y,z = numpy.array(x), numpy.array(y), numpy.array(z)
    for i in range(len(y)):

        if sectionx == numpy.round(y[i], 2):

            slicex.append(x[i])
            slicey.append(y[i])
            slicez.append(z[i])

    # listt = [i < sectionx for i in x]
    # pairedListt = [i for i in zip([0] + listt, listt + [0])][1:-2]
    # numberList = [i[0] for i in enumerate(pairedListt) if
    #               (i[1] == (False, True))]  # Puankare sectrion from one side only
    return slicex, slicey, slicez

# def slicer(x,y,z, sectionx=0.0):
#     np.array(x)
#     np.ndenumerate(x)
#     listt = [i < sectionx for i in x]
#     pairedListt = [i for i in zip([0] + listt, listt + [0])][1:-2]
#     numberList = [i[0] for i in enumerate(pairedListt) if
#                   (i[1] == (False, True))]  # Puankare sectrion from one side only
#     print(x)
#     slicex = []
#     slicey = []
#     slicez = []
#     for i in numberList:
#         slicex.append(x[i])
#         slicey.append(y[i])
#         slicez.append(z[i])
#     return slicex, slicey, slicez


def plotPhase():
    x, y, z = doPortret()
    slicex, slicey, slicez = slicer(x,y,z)

    fig = pyplot.figure()
    ax = fig.gca(projection="3d")
    ax.plot(x, y, z, "b.", ms=0.1,label="ressler's attractor")
    ax.plot(slicex, slicey, slicez, "r.", label="ressler's attractor", color = "r")

    ax.legend()
    pyplot.show()

def d3BiffDiagram(PARAM):
    for i in range(PARAM):
        x, y, z = doPortret()
    slicex, slicey, slicez = slicer(x,y,z)

    fig = pyplot.figure()
    ax = fig.gca(projection="3d")
    ax.plot(x, y, z, "b.", ms=0.1,label="ressler's attractor")
    ax.plot(slicex, slicey, slicez, "r.", label="ressler's attractor", color = "r")

    ax.legend()
    pyplot.show()


def plotSlice():
    x, y, z = doPortret()
    slicex, slicey, slicez = slicer(x, y, z)
    pyplot.plot(slicey, slicez, "ro", label="ressler's attractor")
    pyplot.show()

def plotDiagram(a=1.4, b=0.3, r=0):
    fig = pyplot.figure()
    ax = fig.gca(projection="3d")

    #rRange = [r for r in numpy.arange(2, 5, 0.05)]
    Range = [b for b in numpy.arange(1, 1.5, 0.001)]
    rDiagramData = []
    for param in Range:

        x, y, z = doPortret(ressler, param, b,r, evaluateNum=10000)
        slicex, slicey, slicez = slicer(x, y, z)
        for y, z in zip(slicey, slicez):
            rDiagramData.append([param,y,z])


    rDiagramData = numpy.transpose(rDiagramData)
    r = rDiagramData[0]
    y = rDiagramData[1]
    z = rDiagramData[2]

    ax.plot(r, y, z, "g.", ms=5, label="biffurcation diagram")

    ax.legend()
    pyplot.show()

#4 exercise
def partialDerivative(argNum, f, eps):
    def _f(*args):
        v = f(*args)
        args = list(args)
        args[argNum] += eps
        return ( f(*args) - v )/eps
    return _f


def doLyapunovIndex(f):
    numpy.log(f)
    ...

#TODO make partial derivative matrix (матрица чатсных производных) см. скрины в ./DynSys

if __name__ == '__main__':
    plotPhase()
    #plotSlice()
    #plotDiagram()
