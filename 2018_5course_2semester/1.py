import numpy


def logistic_map(x, _lambda):
    x_new = x - _lambda * x ** 2
    return x_new

# TODO
# create logistic_map() function - CHECK
# plot bifurcation tree - NOT
# review point's vicinity (x_0 = 0, _lambda = l_critical) - NOT
# NOTE l_critical can be the point of the first bifurcation

#plot bifurcation tree:
# - iterate for sertain _lambda
# - find stationar dots
# - mark on the plot
# -  - will use matplotlib library
# - repeat for all others _lambdas in interval [0;5]


def iterate(lmap, times, delta, x0, _lambda):

    x = x0
    for i in range(times-delta):    #sjould be: delta < times
        x = lmap(x, _lambda)
    # we are looking for Certain stable x values here
    # it's good to remember ALL x value to find certain ones later on.
    x_array = numpy.zeros(delta)
    #delta is the number of x, wich we want to remember
    x_array[0] = lmap(x, _lambda)
    for i in range(1, delta):
        x_array[i+1] = lmap(x_array[i], _lambda)

    return x_array
    # again, we can define several cut all random point and live only stable one
    # but we will try solve our problem FIRST
    # and add features SECOND




# lets test it!