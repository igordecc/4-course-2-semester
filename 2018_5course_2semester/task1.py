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

def diff(fn,
         x,
         params,
         dx):
    return ( fn(x + dx, params) - fn(x, params) ) / dx

# def lyapunov_index(fn, x0, params, nsum):
#     # for one-dimension map
#     x = list(x0)
#     dx = list(1)  # x0 for variation equations
#     for i in range(nsum):
#         x.append(fn(x))
#         dx.append(diff(fn,x,dx[i]) * dx[i])

def lyapunov_index(fn,
                   x0,
                   params,
                   nsum):
    x = [x0]
    dx = 0.01
    lyap_sum = 0
    for i in range(nsum):
        dfdx = diff(fn, x[i], params, dx)
        lyap_sum += numpy.log(abs(dfdx))
        x.append(fn(x[i], params))
    lyap_sum /= nsum
    return lyap_sum

def findFeigdelta(_lambda0,
              _lambda1,
              _lambda2,
              ):
    delta = (_lambda1 - _lambda0)/(_lambda2 - _lambda1)
    return delta

def findFeig_lambda0(delta,
              _lambda1,
              _lambda2,
              ):
    # @delta = (_lambda1 - _lambda0)/(_lambda2 - _lambda1)
    _lambda0 = _lambda1 - delta * (_lambda2 - _lambda1)
    return _lambda0

def findFeig_lambda2(delta,
              _lambda0,
              _lambda1,
              ):
    # @delta = (_lambda1 - _lambda0)/(_lambda2 - _lambda1)
    _lambda2 = (_lambda1 - _lambda0)/delta +_lambda1
    return _lambda2


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

def dolyapunov():
    x0=0.1
    _lambda = 1.25
    nsum = 100
    lindex = lyapunov_index(logistic_map, x0, _lambda, nsum)
    print(lindex)

def doFeig():
    delta = 4.669
    _lambda1 = 1.40115329085
    _lambda2 = 1.40115518909
    _lambda0 = findFeig_lambda0(delta, _lambda1, _lambda2)
    print("_lambda0", _lambda0)

    _lambda0 = 0.75
    _lambda1 = 1.25
    _lambda2 = 1.36809893939
    _iteri = 50
    for i in range(_iteri):
        try:
            delta = findFeigdelta(_lambda0, _lambda1, _lambda2)
        except:
            print("exception i =", i)
            break
        print("delta", delta)
        _lambda0 = _lambda1
        _lambda1 = _lambda2
        _lambda2 = findFeig_lambda2(delta, _lambda0, _lambda1)
        print(_lambda1, _lambda2)
    print("final delta", delta)

    
if __name__ == '__main__':
    #plot_bifdiag()
    # plot_iterdiag()
    #dolyapunov()
    doFeig()