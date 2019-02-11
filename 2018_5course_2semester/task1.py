import numpy


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


def iterate(_lambda, lmapfn, times, delta, x0):

    x = x0
    for i in range(times-delta):    #sjould be: delta < times
        x = lmapfn(x, _lambda)
    # we are looking for Certain stable x values here
    # it's good to remember ALL x value to find certain ones later on.
    x_array = numpy.zeros(delta)
    #delta is the number of x, wich we want to remember
    x_array[0] = lmapfn(x, _lambda)
    for i in range(0, delta-1):
        x_array[i+1] = lmapfn(x_array[i], _lambda)

    return x_array
    # again, we can define several cut all random point and live only stable one
    # but we will try solve our problem FIRST
    # and add features SECOND


# lets test it!
# TODO test! - OK!
# unit tests - tests of each single element of our program - CHECK
# integration tests - global test of 1 feature from _todo - will be at the end

def allLambda(lmin, lmax, ld, *args):
    diagramList = []
    _lambdaRow = numpy.arange(lmin, lmax, ld)
    for _lambda in _lambdaRow:
        diagramList.append(iterate(_lambda, *args))
    return _lambdaRow, diagramList

if __name__ == '__main__':
    times = 1000
    delta = 200
    x0 = 0.1
    _lambda = 1.4
    x_array = iterate(_lambda, logistic_map, times, delta, x0)
    import matplotlib.pyplot
    #matplotlib.pyplot.plot(x_array, '.')
    #matplotlib.pyplot.grid()
    #matplotlib.pyplot.show()

    matplotlib.pyplot.clf()
    lmin, lmax, ld = 0.5, 1.7, 0.01
    x,y = allLambda(lmin, lmax, ld, logistic_map, times, delta, x0)
    matplotlib.pyplot.plot(x, y , 'g.', alpha=0.1, markersize = 2 )
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()

    #come up with how scalle graphic around Critical point