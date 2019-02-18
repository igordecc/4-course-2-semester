import matplotlib.pyplot
import numpy
from task1 import logistic_map

def scale(x_scale_point,
          y_scale_point,
          x_scale_coefficient,
          y_scale_coefficient,
          xmin,
          xmax,
          ymin,
          ymax
          ):
    #Universal scaling funtion

    # xmin = .5
    # xmax = 1.8
    # ymin = -1
    # ymax = 1
    # x_scale_point = 1.4
    # y_scale_point = 0
    # x_scale_coefficient = 1
    # y_scale_coefficient = 0.5
    # # scaling point
    # # x_scale_point = 1.1
    # # y_scale_point = DON'T SCALE

    # nxmin, nxmax = xmin * x_scale_coefficient, xmax * x_scale_coefficient
    # nymin, nymax = ymin * y_scale_coefficient, ymax * y_scale_coefficient

    x_proportions = x_scale_point -  xmin, xmax - x_scale_point
    n_x_proportions = [ i * x_scale_coefficient for i in x_proportions ]
    n_xmin, n_xmax = x_scale_point - n_x_proportions[0], x_scale_point + n_x_proportions[1]

    y_proportions = y_scale_point - ymin, ymax - y_scale_point
    n_y_proportions = [i * y_scale_coefficient for i in y_proportions]
    n_ymin, n_ymax = y_scale_point - n_y_proportions[0], y_scale_point + n_y_proportions[1]

    return matplotlib.pyplot.axis(n_xmin, n_xmax, n_ymin, n_ymax)

def iterate(_lambda,
            lfn,
            k,
            delta,
            x0
            ):
    x = x0
    for i in range(k - delta):    #sjould be: delta < times
        x = lfn(x, _lambda)
    # we are looking for Certain stable x values here
    # it's good to remember ALL x value to find certain ones later on.
    x_array = numpy.zeros(delta)
    #delta is the number of x, wich we want to remember
    x_array[0] = lfn(x, _lambda)
    for i in range(0, delta-1):
        x_array[i+1] = lfn(x_array[i], _lambda)

    return x_array
    # again, we can define several cut all random point and live only stable one
    # but we will try solve our problem FIRST
    # and add features SECOND

def allLambda(lmin,
              lmax,
              ld,
              *args
              ):
    diagramList = []
    _lambdaRow = numpy.arange(lmin, lmax, ld)
    for _lambda in _lambdaRow:
        diagramList.append(iterate(_lambda, *args))
    return _lambdaRow, diagramList

def plot_xarray():
    times = 1000
    delta = 200
    x0 = 0.1
    _lambda = 1.4
    x_array = iterate(_lambda, logistic_map, times, delta, x0)
    matplotlib.pyplot.plot(x_array, '.')
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()