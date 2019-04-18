import sup_task_funcs as stf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as wgt
from mpl_toolkits.mplot3d import Axes3D


def plot_xarray():
    # point 1
    x0 = 0.1
    _lambda = 1.7499 # от порядка к хаосу через перемежаемость 1.75 -> 1.7499
    k = 1000
    delta = 0
    x_array = stf.iterate(_lambda, stf.logistic_map, k, delta, x0)

    # plt.plot(x_array, '.')
    # plt.grid()
    # plt.show()
    # plt.clf()
    fig = plt.figure()
    ax = fig.gca()
    the_plot, = ax.plot(x_array, ".")
    plt.ylabel("x values")
    ax.legend()
    axlambd = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor="b")
    lambd_slider = wgt.Slider(axlambd, "lambda", 1.748, 1.752, valinit=1.7499, valstep=0.00001, valfmt="%1.5f")


    def update_for_slider(val):
        lambd_local = lambd_slider.val
        the_plot.set_ydata(stf.iterate(lambd_local, stf.logistic_map, k, delta, x0))
        fig.canvas.draw_idle()

    lambd_slider.on_changed(update_for_slider)

    plt.show()
    return x_array, k



def lyapunov_index(fn,
                   x0,
                   params,
                   nsum ):
    x = [x0]
    dx = 0.0001     # precision need to be high enough
    lyap_sum = 0
    delta = nsum // 2
    for i in range(nsum):
        if i>delta:
            dfdx = stf.diff(fn, x[i], params, dx)
            lyap_sum += np.log(abs(dfdx))
        x.append(fn(x[i], params))
    lyap_sum /= (nsum-delta)
    return lyap_sum

def plot_lyapunov():
    # point 2
    x0 = 0.1
    _lambda = 1.751
    nsum = 1000
    lindex = lyapunov_index(stf.logistic_map, x0, _lambda, nsum)
    print(lindex)

def do_lyapunov_map():
    x0 = 0.1
    nsum = 1000
    #TODO change proximity
    lrange = np.arange(1.35, 1.505, 0.0001)     # can change _lambda here
    lindex = [lyapunov_index(stf.logistic_map, x0, _lambda, nsum) for _lambda in lrange]
    zeros = np.zeros(len(lrange))
    plt.plot(lrange, lindex)
    plt.plot(lrange, zeros)   # horizontal line
    plt.grid()
    plt.show()
    plt.clf()

def do_count_laminar():

    # x values
    x_array, k = plot_xarray()
    dimension = int(np.log10(k))
    print(dimension)

    xmax = round(max(x_array), dimension)
    xmin = round(min(x_array), dimension)


    dx = round(0.1**dimension, dimension)
    print(dx)
    # SALVATION *10**3, take int() from them, save in the list
    xline = [round(i, dimension) for i in  np.arange(xmin, xmax, dx)]
    print(xline)
    # count_array = np.zeros((xline.len(), k))

    # turn_x_array_to_countdict()
    x_dict = dict()
    # x_dict = x_dict.fromkeys(xline) DOESNOT WORK - thank u, floats
    #TODO how to make dict from list of float numbers?

    for i in xline:
        x_dict[i] = None
    print(x_dict)
    for i in x_array:
        x_dict[round(i, dimension)] += 1

    plt.grid()
    plt.plot(x_dict)
    plt.show()
    plt.clf()


if __name__ == '__main__':
    plot_xarray()
    #plot_lyapunov()
    #do_lyapunov_map()
    #do_count_laminar()