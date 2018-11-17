import scipy.optimize as op

def partialDerivative(argNum, f, eps):
    def _f(*args):
        v = f(*args)
        args = list(args)
        args[argNum] += eps
        return ( f(*args) - v )/eps
    return _f

a = .2
b = .2
r = 5.7

def ressler(state0, t):  # a = 0.2, b = 0.2, r = 5.7
    """

    :param state: Начальные условия
    :param t: временной интервал
    :return: [xd, yd, zd]
    """
    x = state0[0]
    y = state0[1]
    z = state0[2]

    xd = - y - z
    yd = x + a * y
    zd = b + (x - r) * z
    return [xd, yd, zd]

class ressler:
    def __init__(self, a = .2, b = .2, r = 5.7):
        self.a = a
        self.b = b
        self.r = r
    # def __call__(self, x, y, z):
    #     self.f1dx = - y - z
    #     self.f2dy = x + self.a * y
    #     self.f3dz = self.b + (x - self.r) * z
    #     return
    def f1dx(self, x, y, z):
        return - y - z
    def f2dy(self, x, y, z):
        return x + self.a * y
    def f3dz(self, x, y, z):
        return self.b + (x - self.r) * z
f_ressler = ressler()

def Section(x, y, z):
    return x+2

dS = partialDerivative(0, Section, 0.01)
print(dS(1,1,1))

dsdx = partialDerivative(0, Section, 0.01)
dsdy = partialDerivative(1, Section, 0.01)
dsdz = partialDerivative(2, Section, 0.01)

"""
0. избавиться - переходный процесс
1. задание плоскости x=2
2. моделировать систему и отслеживать x: x<2? или нет? x_2<2?
3. при x1<2 и x2>2 - пересечение
4. изменить нестандартный шаг H=1 на H(x,y,z) (см. страница 96)
"""
def H(x,y,z):
    args = [x,y,z]
    return dsdx(*args)*f_ressler.f1dx(*args) + dsdy(args)*f_ressler.f1dy(*args) + dsdz(*args)*f_ressler.f1dz(*args)
#find Product by nuton differentiation
dxds = f_ressler.f1dx(*args)/H(x,y,z)
dyds = f_ressler.f1dx(*args)/H(x,y,z)
dzds = f_ressler.f1dx(*args)/H(x,y,z)
dtds = 1/H(x,y,z)
