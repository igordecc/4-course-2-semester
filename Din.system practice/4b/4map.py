from matplotlib import pyplot as plt
from matplotlib import transforms as trns
import numpy as np

#карта динамических режимов

def VDP_f(x, y, *lambd):
    """
    main Van-der-Pole equation
    :param x: x
    :param y: y = x'
    :param lambd: parameters lambda and  a: lambda - 0; a - 1.
    :return: y'
    """
    return (lambd[0] - x**2)*y - lambd[1] - (x + 1)**2

def VDP_g(x, y, *lambd):
    """

    :param x:
    :param y:
    :param lambd:
    :return: x'
    """
    return y
""" DOESNT WORK
def VDP():
    return VDP_f, VDP_g
"""


def method_euler(x0, y0, result0, f, h, *lambd):
    """
    do calculate for tn moment
    :param x0: 1st variable
    :param y0: 2d variable
    :param result0: previous result, list
    :param f: vector of functions
    :param h: if there is t0 and tn, then tn = t0 + n*h
    :param lambd: parameters, like a,b and others
    :return: new result1, list
    """
    result1 = [result0[i] + h * f[i](x0, y0, *lambd) for i in range(len(f))]
    return result1

def getxylist(x0, y0, VDP, h, tn, *lambd, t0=0 ):
    result0 = [x0, y0]
    xylist = [result0]
    for t in np.arange(t0, tn, h):
        result0 = method_euler(xylist[-1][0],xylist[-1][1], result0, VDP, h, *lambd)
        print(result0)
        xylist.append(result0)
    xylist = np.array(xylist)
    xlist = xylist[:][0]
    ylist = xylist[:][1]
    return xlist, ylist

def makesystem(f,g, *lambd):
    return lambda x,y: ( f(x,y,*lambd), g(x,y,*lambd) )

def euler(x,y, f, h=1e-4):
    xp, yp = f(x,y)
    return x + h*xp, y + h*yp

#TODO fix (Google) "OverflowError: (34, 'Result too large')"
#TODO read lambda functions
#TODO ask for reading (from Kostya) about Functional programming

if __name__=="__main__":
    x0 = 0.1
    y0 = 0.1
    lambd = .5#(-0.6, 0.6, 0.04)
    b = 1 #(0.8, 2.5, 0.04)
    tn = 100
    h = .1
    VDP = VDP_f, VDP_g
    xlist, ylist = getxylist(x0, y0, VDP, h, tn, lambd, b)
    plt.plot(xlist, ylist)
    print(xlist, ylist)
    plt.autoscale()

    #im = plt.pcolormesh(np.arange(100).reshape((10, 10)))
    #plt.colorbar(im)
    ####plt.axes().
    #plt.plot(transform=rot)
    plt.show()