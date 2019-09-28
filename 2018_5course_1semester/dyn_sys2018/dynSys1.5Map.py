#--------------------------------------------------------------------------------------
import numpy


def rk4(t0, t1, y0, F, param, steps=100):
    h = (t1 - t0) / steps
    t = t0
    y = y0.copy()
    # for i in range(steps):
    #     # k1
    #     k = h * F(t, y, *param) / 2.0
    #     r = k / 3.0
    #
    #     # k2
    #     k = h * F(t + h / 2.0, y + k, *param) / 2.0
    #     r += k * (2.0 / 3.0)
    #
    #     # k3
    #     k = h * F(t + h / 2.0, y + k, *param)
    #     r += k / 3.0
    #
    #     # k4
    #     pass
    #
    #     y += r + h * F(t + h, y + k, *param) / 6.0

    for i in range(steps):
        y += h * F(t, y, *param)
        t += h
    return y


def Lorenz(t, X, sig=10, bet=8/3, r=28):
    x, y, z = X[0], X[1], X[2]
    res = numpy.empty(shape=(12,), dtype=numpy.float)

    res[0] = sig*(y - x)

    res[1] = -x*z + r*x - y

    res[2] = x*y - bet*z

    #        m
    # cij = sum aik*bkj
    #       k-1

    # 0 0
    res[3] = -sig * X[3] + sig * X[4]
    # 1 0
    res[4] = (r - z) * X[3] - X[4] - x * X[5]
    # 2 0
    res[5] = y * X[3] + x * X[4] - bet * X[5]
    # 0 1
    res[6] = -sig * X[6] + sig * X[7]
    # 1 1
    res[7] = (r - z) * X[6] - X[7] - x * X[8]
    # 2 1
    res[8] = y * X[6] + x * X[7] - bet * X[8]
    # 0 2
    res[9] = -sig * X[9] + sig * X[10]
    # 1 2
    res[10] = (r - z) * X[9] - X[10] - x * X[11]
    # 2 2
    res[11] = y * X[9] + x * X[10] - bet * X[11]

    return res

def ResslerVar(x,y,z, x_, y_, z_, a, b, r):

    return (
        - y_ - z_,
        x_ + a*y_,
        x_*z + x*z_ - r*z_
    )

def Ressler(t, X, a=.25, b=.15, r=2.5):
    x, y, z = X[0], X[1], X[2]
    res = numpy.empty(shape=(12,), dtype=numpy.float)

    res[0] = - y - z

    res[1] = x + a*y

    res[2] = b + (x-r)*z

    #        m
    # cij = sum aik*bkj
    #       k-1

    res[3:6] = ResslerVar(X[0], X[1], X[2], X[3], X[4], X[5], a, b, r)
    res[6:9] = ResslerVar(X[0], X[1], X[2], X[6], X[7], X[8], a, b, r)
    res[9:12] = ResslerVar(X[0], X[1], X[2], X[9], X[10], X[11], a, b, r)

    return res

def lyapunov(n, fn, tStart, tStep, tEnd, y0, param):
    totalIter = int((tEnd - tStart) / tStep)

    y = numpy.zeros((n + 1, n), numpy.float)
    S = numpy.zeros((n,), numpy.float)

    gsc = numpy.empty((n,), numpy.float)
    norms = numpy.empty((n,), numpy.float)
    series = numpy.empty((totalIter, n + 1), dtype=numpy.float)

    y[0] = y0
    y[1:] = numpy.eye(n)

    t = tStart

    for i in range(totalIter):
        y = rk4(t, t + tStep, y.flat, fn, param).reshape((n + 1, n))
        t += tStep

        w = y[1:]
        for j in range(n):
            for k in range(j):
                gsc[k] = numpy.dot(w[j], w[k])

            for k in range(j):
                w[j] -= numpy.dot(gsc[k], w[k])

            norms[j] = numpy.linalg.norm(w[j])
            w[j] /= norms[j]
        y[1:] = w

        S += numpy.log(norms)
        series[i] = (t, *(S / (t - tStart)))

        # if (i + 1) % 10 == 0:
        #     print(*map(lambda x: "%.3f" % x, series[i]))
        #     print("%.3f" % sum(series[i][1:]))

    return series

if __name__ == '__main__':
    #param = .25, .15, 2.5
    mapArray = []
    for a in numpy.arange(0, 0.5, 0.05):
        tempArray = []
        for b in numpy.arange(0.1, 1, 0.05):

            param = a, b, 2.5
            try:
                series = lyapunov(3, Ressler, 0, 1, 150, (1,2,3), param)
                if (series[-1][1] < 0) and (series[-1][2] < 0) and (series[-1][3] < 0):
                    tempArray.append(".")
                elif (numpy.round(series[-1][1], res) == .0) and (series[-1][2] < 0) and (series[-1][3] < 0):
                    tempArray.append("0")
                elif (numpy.round(series[-1][1], res) == .0) and (numpy.round(series[-1][2], res) == .0) and (series[-1][3] < 0):
                    tempArray.append("+")
                elif (series[-1][1] > 0) and (numpy.round(series[-1][2], res) == .0) and (series[-1][3] < 0):
                    tempArray.append("X")
                else:
                    tempArray.append("N")
            except:
                tempArray.append("N")
            res = 1

            #tempArray.append(series[-1])
        mapArray.append(tempArray)
    mapArray = numpy.array(mapArray)
    print(mapArray)



    # import matplotlib.pyplot as pp
    # pp.plot(mapArray)
    # pp.show()

    """
    tCurent, 1, 2, 3-q,
    sum 1+2+3
    """
    """
    print(t, 1, 2, 3)
    """