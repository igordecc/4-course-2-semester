import numpy
import matplotlib.pyplot as plt
import matplotlib.widgets as wgt

import sup_task_funcs as stf


# TODO
# create stf.logistic_map() function - CHECK
# plot bifurcation tree - NOT
# review point's vicinity (x_0 = 0, _lambda = l_critical) - NOT
# NOTE l_critical can be the point of the first bifurcation

#plot bifurcation tree:
# - iterate for certain _lambda
# - find stationary dots - u don't need that
# - mark on the plot
# -  - will use matplotlib library
# - repeat for all others _lambdas in interval [0;5]



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
        diagramList.append(stf.iterate(_lambda, *args))
    return _lambdaRow, diagramList

def diff(fn,
         x,
         params,
         dx):
    return ( fn(x + dx, params) - fn(x, params) ) / dx


def taskA_plot_bifdiag2():
    fig = plt.figure(1, figsize=(6,5))
    left, bottom = 0.1, 0.1
    width, height = 0.8, 0.8
    pl_axes = plt.axes([left, bottom, width, height ])
    def do_plot(lmin = 0.60115, lmax=2.20115, ymin=-1, ymax=1):
        times = 1000
        delta = 200
        x0 = 0.1
        ld = (lmax-lmin)/1000
        x,y = allLambda(lmin, lmax, ld, stf.logistic_map, times, delta, x0)
        pl_axes.clear()
        pl_axes.set_ylim((ymin, ymax))
        pl_axes.plot(x, y , 'g.', alpha=0.1, markersize = 2 )

        print(lmin, lmax, ymin, ymax)
        return lmin, lmax, ymin, ymax

    def rescale(lmin, lmax, ymin, ymax, lcr):
        alpha = 2.5029
        delta = 4.6692
        nu = lmax - lcr
        mu = lcr - lmin
        nu = nu/delta
        mu = mu/delta
        newlmax = lcr + nu
        newlmin = lcr - mu
        ymin, ymax = ymax/alpha, ymin/alpha  # mirrored image
        return newlmin, newlmax, ymin, ymax


    lmin, lmax, ymin, ymax = do_plot()
    lcr = 1.40115
    plt.grid()

    b_axes = plt.axes([0.8, .025, 0.1, 0.04])
    scale_button = wgt.Button(b_axes, "Scale")
    def scale(event):

        nonlocal lmin, lmax, ymin, ymax, lcr
        newlmin, newlmax, ymin, ymax = rescale(lmin, lmax, ymin, ymax, lcr)
        lmin, lmax, ymin, ymax = do_plot(newlmin, newlmax, ymin, ymax)
        plt.draw()

    scale_button.on_clicked(scale)
    plt._auto_draw_if_interactive(fig, pl_axes)
    plt.show()

def taskB_plot_iterdiag():
    _lambda = 1.4011
    k = 200
    x0 = 0


    # plot basic figures
    na = numpy.arange(-1, 1.00, 0.02)
    f_array =[stf.logistic_map(x, _lambda) for x in na] # parabola
    x = [x for x in na]
    zero_array = [0 for x in na]
    plt.plot(x,f_array) # parabola
    plt.plot(x,x) #diagonal
    plt.plot(x, zero_array) # x axes
    plt.plot(zero_array, x) # y axes

    x_array = stf.iterate(_lambda, stf.logistic_map, k, 0, x0)
    #print(x_array)


    # should be function
    for n in range(0, len(x_array)-1):
        plt.vlines(x_array[n], x_array[n], x_array[n+1], "b")
        plt.hlines(x_array[n+1], x_array[n], x_array[n+1], "b")


    plt.grid()
    plt.show()
    # plt.clf()

    #-----------------------
    def logistic(x, lam):
        return 1.0 - lam * x ** 2

    def RG(fn, k):
        def make_next(fk):
            return lambda x: fk(fk(x * fk(fk(0)))) / fk(fk(0))

        for _ in range(k):
            fn = make_next(fn)

        return fn


    rgs = [RG(lambda x: logistic(x, 1.401), k) for k in range(3)]

    xs = numpy.linspace(-1, 1)
    ys = lambda f: [f(x) for x in xs]
    plt.plot(
        xs, ys(rgs[0]), "r-",
        xs, ys(rgs[1]), "g-",
        xs, ys(rgs[2]), "b-",
    )
    plt.grid()
    plt.show()


def taskD_doFeig():
    def findFeigdelta(_lambda0,
                      _lambda1,
                      _lambda2,
                      ):
        delta = (_lambda1 - _lambda0) / (_lambda2 - _lambda1)
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
        _lambda2 = (_lambda1 - _lambda0) / delta + _lambda1
        return _lambda2

    # delta = 4.669
    # _lambda1 = 1.40115329085
    # _lambda2 = 1.40115518909
    # _lambda0 = findFeig_lambda0(delta, _lambda1, _lambda2)
    # print("_lambda0", _lambda0)

    _lambda0 = 0
    _lambda1 = 1
    _lambda2 = 1.31070264134
    _iteri = 50

    def simple_iterration(x0, fn, params, iter_number):
        x1 = x0

        for i in range(iter_number):
            x0 = x1
            x1 = x0 - fn(x0) / diff(fn, x0, params, dx=0.01)
        return x1

    delta = findFeigdelta(_lambda0, _lambda1, _lambda2)
    print("delta", delta)

    for i in range(_iteri):
        print("lambda 0: ", _lambda0)
        print("lambda 1: ", _lambda1)
        print("lambda 2: ", _lambda2)
        # try:
        #     delta = findFeigdelta(_lambda0, _lambda1, _lambda2)
        # except:
        #     print("exception i =", i)
        #     break
        #TODO by nutons method or division/2 find super stable cicle

        _lambda0 = _lambda1
        _lambda1 = _lambda2
        _lambda2 = findFeig_lambda2(delta, _lambda0, _lambda1)
        # _lambda2 = simple_iterration(_lambda2, findFeig_lambda2, (delta, _lambda0, _lambda1), iter_number=100
    print("final delta", delta)


class taskC_dolyapunov_obj:
    def __init__(self,
                 lcenter = 1.40115,
                 ldelta = 0.1,
                 dl = 0.0001,
                 ):
        #TODO do things bellow
        # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html
        #TODO 1 create 6 subplots figure
        #TODO 2 add new subplot each call
        # ... why? - because we need scaling sequence of plots

        def lyapunov_index(fn,
                           x0,
                           params,
                           nsum):
            x = [x0]
            dx = 0.0001  # precision need to be high enough
            lyap_sum = 0
            delta = nsum // 2
            for i in range(nsum):
                if i > delta:
                    dfdx = stf.diff(fn, x[i], params, dx)
                    lyap_sum += numpy.log(abs(dfdx))
                x.append(fn(x[i], params))
            lyap_sum /= (nsum - delta)
            return lyap_sum

        x0 = 0.1
        nsum = 1000
        # TODO change proximity
        self.lcenter = 1.40115
        self.ldelta = 0.1
        self.dl = 0.0001

        self.lcenter = lcenter
        self.ldelta = ldelta
        self.dl = dl

        self.lmin = self.lcenter - self.ldelta
        self.lmax = self.lcenter + self.ldelta
        # self.lmin, self.lmax, self.dl = lmin, lmax, dl
        # self.ldelta = (self.lmax - self.lmin) / 2
        # self.lcenter = self.lmin + self.ldelta #1.40115
        self.lrange = numpy.arange(self.lmin, self.lmax, self.dl)  # can change _lambda here
        self.lindex = [lyapunov_index(stf.logistic_map, x0, _lambda, nsum) for _lambda in self.lrange]
        self.zeros = numpy.zeros(len(self.lrange))

        # creating subplots
        # we will plot in different windows. They will show scaling.
        self.fig = plt.figure()
        self.gs = self.fig.add_gridspec(1,1) # WARNING: don't change plot objects - u can break them. only add new.


    def __call__(self, *args, **kwargs):
        self.ax1 = self.fig.add_subplot(self.gs[0,0])
        self.ax1.plot(self.lrange, self.lindex)
        self.ax1.plot(self.lrange, self.zeros)  # horizontal line
        self.ax1.grid()


    def scale(self, scaling=0.5, num=1):
        self.ldelta = self.ldelta * scaling
        self.lmin = self.lcenter - self.ldelta
        self.lmax = self.lcenter + self.ldelta
        self.dl = self.dl*scaling
        self.__init__(self.lcenter, self.ldelta, self.dl)
        self.__call__()
        ...

def taskC_dolyapunov():
    sample = taskC_dolyapunov_obj() # initialising plot-object
    sample() # default plot call
    sample.scale() # calls for scale
    sample.scale()
    sample.scale()
    sample.scale()
    plt.show()

if __name__ == '__main__':
    #taskA_plot_bifdiag2()
    #taskB_plot_iterdiag()
    taskC_dolyapunov()
    #taskD_doFeig()







        # TODO MOVE SOME FUNCTIONS TO EXPLICIT EXTERNAL FILE
    ...
