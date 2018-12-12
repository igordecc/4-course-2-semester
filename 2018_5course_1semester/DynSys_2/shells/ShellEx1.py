from funсs import ArrayMakerFun, DynSysFuns, StatisticFuns
import config
import numpy
from matplotlib import pyplot

def makeArrayEX1(*params):
    # params - h, a, b, r

    xyz = ArrayMakerFun.doPortrait(DynSysFuns.resslerSystem, *params, **config.createConfig())
    return xyz

if __name__ == '__main__':
    xyz = makeArrayEX1(0.01, .25, 0.15, 2.5)
    # xslice = print(numpy.extract((xyz[0].any()<4.1)and(xyz[0].any()>4), xyz[0]))
    xslice, yslice, zslice = StatisticFuns.slicer(xyz[0], xyz[1], xyz[2])
    StatisticFuns.plotPhase(xyz[0], xyz[1], xyz[2])