from funсs import ArrayMakerFun, DynSysFuns
import config

def makeArrayEX1(*params):
    # params - h, a, b, r
    xyz = ArrayMakerFun.doPortrait(DynSysFuns.resslerSystem, *params, **config.createConfig())
    return xyz
