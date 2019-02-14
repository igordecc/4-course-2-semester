import numpy
import matplotlib.pyplot


def logistic_map(x, _lambda):
    x_new = 1 - _lambda * x ** 2
    return x_new

# TODO
# create logistic_map() function - CHECK
# plot bifurcation tree - NOT
# review point's vicinity (x_0 = 0, _lambda = l_critical) - NOT
# NOTE l_critical can be the point of the first bifurcation

#plot bifurcation tree:
# - iterate for certain _lambda
# - find stationary dots - u don't need that
# - mark on the plot
# -  - will use matplotlib library
# - repeat for all others _lambdas in interval [0;5]


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

def iterate_v2(_lambda,
             fn,
             k,
             delta,
             x0):
    # iterate function for iterating 1 dimension map
    x_array = [fn(x0, _lambda)]
    for i in range(k):      #k+1, or not?
        x_array.append(fn(x_array[i],_lambda))
    if delta==0:
        return x_array
    else:
        return x_array[-delta:]

# lets test it!
# TODO test! - OK!
# unit tests - tests of each single element of our program - CHECK
# integration tests - global test of 1 feature from _todo - will be at the end

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

def plot_bifdiag():
    times = 1000
    delta = 200
    x0 = 0.1
    lmin, lmax, ld = 0.5, 1.7, 0.01
    x,y = allLambda(lmin, lmax, ld, logistic_map, times, delta, x0)
    matplotlib.pyplot.plot(x, y , 'g.', alpha=0.1, markersize = 2 )
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()

def plot_iterdiag():
    _lambda = 0.75
    k = 20
    x0 = 0.1


    # plot basic figures
    na = numpy.arange(-1, 1.00, 0.02)
    f_array =[logistic_map(x, _lambda) for x in na]
    x = [x for x in na]
    zero_array = [0 for x in na]
    matplotlib.pyplot.plot(x,f_array)
    matplotlib.pyplot.plot(x,x)
    matplotlib.pyplot.plot(x, zero_array)
    matplotlib.pyplot.plot(zero_array, x)

    x_array = iterate_v2(_lambda, logistic_map, k, 0, x0)
    print(x_array)


    # should be function
    for n in range(0, len(x_array)-1):
        matplotlib.pyplot.vlines(x_array[n], x_array[n], x_array[n+1], "b")
        matplotlib.pyplot.hlines(x_array[n+1], x_array[n], x_array[n+1], "b")


    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()
    matplotlib.pyplot.clf()
    ...


if __name__ == '__main__':
    #plot_bifdiag()
    plot_iterdiag()