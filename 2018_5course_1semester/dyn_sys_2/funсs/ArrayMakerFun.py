import numpy
import config

#config: Initial Conditions
# x0 = .1
# y0 = .1
# z0 = .1
# config : array display boundaries
# left bound:    evaluateNum // 4):
# right bound:   evaluateNum

def doPortrait(fun, *param, **config):
    xyz = numpy.empty((config["evaluateNum"], 3))
    xyz[0] = [
        config["x0"],
        config["y0"],
        config["z0"]
    ]
    for i in range( 1, config["evaluateNum"] ):
        xyz[i] = fun(*xyz[i - 1], *param)

    xyz = xyz[config["leftBound"] : config["rightBound"]]  # 0. избавиться - переходный процесс
    xyz = numpy.transpose(xyz) # maybe return just this?
    # x = xyz[0]
    # y = xyz[1]
    # z = xyz[2]
    return xyz #???????????