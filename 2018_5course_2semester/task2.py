from task1 import logistic_map, iterate_v2, lyapunov_index
import matplotlib.pyplot
import numpy

def plot_xarray():
    # point 1
    x0 = 0.1
    _lambda = 1.7499 # от порядка к хаосу через перемежаемость 1.75 -> 1.7499
    k = 1000
    delta = 0
    x_array = iterate_v2(_lambda, logistic_map, k, delta, x0)

    matplotlib.pyplot.plot(x_array, '.')
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()

    return x_array, k

def plot_lyapunov():
    # point 2
    x0 = 0.1
    _lambda = 1.751
    nsum = 1000
    lindex = lyapunov_index(logistic_map, x0, _lambda, nsum)
    print(lindex)

def do_lyapunov_map():
    x0 = 0.1
    nsum = 1000
    lrange = numpy.arange(1.76, 1.745, -0.0001)     # can change _lambda here
    lindex = [  lyapunov_index(logistic_map, x0, _lambda, nsum) for _lambda in lrange]
    zeros = numpy.zeros(len(lrange))
    matplotlib.pyplot.plot(lrange ,lindex)
    matplotlib.pyplot.plot(lrange, zeros)
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()

def do_count_laminar():

    # x values
    x_array, k = plot_xarray()
    dimension = int(numpy.log10(k))
    print(dimension)

    xmax = round(max(x_array), dimension)
    xmin = round(min(x_array), dimension)


    dx = round(0.1**dimension, dimension)
    print(dx)
    xline = [round(i, dimension) for i in  numpy.arange(xmin, xmax, dx)]
    print(xline)
    # count_array = numpy.zeros((xline.len(), k))

    # turn_x_array_to_countdict()
    x_dict = dict()
    # x_dict = x_dict.fromkeys(xline) DOESNOT WORK - thank u, floats
    #TODO how to make dict from list of float numbers?
    for i in xline:
        x_dict[i] = None
    print(x_dict)
    for i in x_array:
        x_dict[round(i, dimension)] += 1

    matplotlib.pyplot.grid()
    matplotlib.pyplot.plot(x_dict)
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()


if __name__ == '__main__':
    #plot_xarray()
    #plot_lyapunov()
    #do_lyapunov_map()
    do_count_laminar()