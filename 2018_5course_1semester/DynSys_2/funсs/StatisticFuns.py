from matplotlib import pyplot
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np
import numpy

def slicer(x,y,z, sectionx=2):
    np.array(x)
    np.ndenumerate(x)
    listt = [i < sectionx for i in x]
    pairedListt = [i for i in zip([0] + listt, listt + [0])][1:-2]
    numberList = [i[0] for i in enumerate(pairedListt) if
                  (i[1] == (False, True))]  # Puankare sectrion from one side only

    slicex = []
    slicey = []
    slicez = []
    for i in numberList:
        slicex.append(x[i])
        slicey.append(y[i])
        slicez.append(z[i])
    return slicex, slicey, slicez


def plotPhase(x, y, z):
    slicex, slicey, slicez = slicer(x,y,z)

    fig = pyplot.figure()
    #ax = fig.gca(projection="3d")
    ax = Axes3D(fig)
    ax.plot(x, y, z, label="ressler's attractor")
    ax.plot(slicex, slicey, slicez, label="ressler's attractor", color = "r")

    ax.legend()
    pyplot.show()


def plotSlice(x, y, z):
    slicex, slicey, slicez = slicer(x, y, z)
    pyplot.plot(slicey, slicez, "ro", label="ressler's attractor")
    pyplot.show()

def plotDiagram(x, y, z, a = .25, b = .15):
    fig = pyplot.figure()
    ax = fig.gca(projection="3d")

    rRange = [r for r in numpy.arange(2, 5, 0.05)]
    rDiagramData = []
    for r in rRange:

        slicex, slicey, slicez = slicer(x, y, z)
        for y, z in zip(slicey, slicez):
            rDiagramData.append([r,y,z])

    rDiagramData = numpy.transpose(rDiagramData)
    y = rDiagramData[1]
    r = rDiagramData[0]
    z = rDiagramData[2]

    ax.plot(r, y, z, "g.", label="biffurcation diagram")

    ax.legend()
    pyplot.show()