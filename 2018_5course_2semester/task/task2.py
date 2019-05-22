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
    x0 = 0.01
    nsum = 10000
    #TODO change proximity
    lambd_crit = 1.75
    lrange = np.arange(1.7495, lambd_crit, 0.00001)     # can change _lambda here
    lindex = np.log([lyapunov_index(stf.logistic_map, x0, _lambda, nsum) for _lambda in lrange])
    zeros = np.zeros(len(lrange))
    lrange = np.log(np.ones(lrange.shape) * lambd_crit - lrange)
    #polifitting
    polifited = np.poly1d(np.polyfit(lrange, lindex, 3))

    plt.plot(lrange, lindex, ".")
    #plt.plot(lrange, polifited(lrange), "--")
    plt.plot(lrange, zeros)   # horizontal line
    plt.grid()
    plt.show()
    plt.clf()
    import scipy

def do_draw_laminar():

    # x values
    x_array, k = plot_xarray()
    dimension = int(np.log10(k))
    print(dimension)

    # why - somehow k - itteration number meens our round capability?
    # probaly need to make "dimmention" constant
    xmax = round(max(x_array), dimension)
    xmin = round(min(x_array), dimension)


    dx = round(0.1**dimension, dimension)
    #print(dx)
    # SALVATION *10**3, take int() from them, save in the list
    xline = [round(i, dimension) for i in np.arange(xmin, xmax, dx)]
    print(xline)
    xline = [i for i in np.arange(xmin, xmax, dx)]
    print(xline)
    #print(xline)
    # count_array = np.zeros((xline.len(), k))

    # turn_x_array_to_countdict()
    x_dict = dict()
    # x_dict = x_dict.fromkeys(xline) DOESNOT WORK - thank u, floats
    #TODO how to make dict from list of float numbers?

    for i in xline:
        x_dict[i] = None
    #print(x_dict)
    for i in x_array:
        x_dict[round(i, dimension)] += 1

    plt.grid()
    plt.plot(x_dict)
    plt.show()
    plt.clf()

def do_count_unique():

    def unique_for_lambda(_lambda):
        # point 1
        x0 = 0.1
         # от порядка к хаосу через перемежаемость 1.75 -> 1.7499
        k = 1000
        delta = 0
        x_array = stf.iterate(_lambda, stf.logistic_map, k, delta, x0)

        # # x values
        # x_array, k = plot_xarray()

        precision = 10**-4
        multiplier = np.int(1/precision)
        x_array_rounded = (np.array(x_array)*multiplier).astype(np.int)
        unique_array = np.unique( x_array_rounded )

        return len(unique_array)

    lambda_list = np.arange(1.748, 1.75, 0.000001)   #1.748 - 1.75
    unique_values_list = list(map(unique_for_lambda, lambda_list))

    plt.plot(lambda_list, unique_values_list)
    plt.show()

def do_count_laminar():

    def unique_for_lambda(_lambda):
        # point 1
        x0 = 0.1
         # от порядка к хаосу через перемежаемость 1.75 -> 1.7499
        k = 1000
        delta = 0
        x_array = stf.iterate(_lambda, stf.logistic_map, k, delta, x0)

        # # x values
        # x_array, k = plot_xarray()

        precision = 10**-2
        multiplier = np.int(1/precision)
        x_array_rounded = (np.array(x_array)*multiplier).astype(np.int)
        x_array_rounded = x_array_rounded[1:]   # make array from 1001 to 1000

        # we descretizes array to groups with group_size. laminar or toorbulent each group will be?
        # then we will understand where toorbulent and where laminar states is on whole array
        group_size = 20 # star from 20, 40, 100
        grouped_array = x_array_rounded.reshape(len(x_array_rounded) // group_size, group_size)
        len_array = [len(np.unique(group)) for group in grouped_array]
        # from marked array we can find all laminar states apearing

        #  if _len<(group_size//4)  (if _len mini-unique_array is small) then state is laminar, otherwise it's chaotic, means turbulent
        mark_array = [1 if _len<(group_size//4) else 0 for _len in len_array]

        # print("lambda: ", _lambda," sum mark array: ", sum(mark_array))

        unique_array = np.unique( x_array_rounded )

        return len(unique_array)

    lambda_list = np.arange(1.749, 1.75, 0.000001)   #1.748 - 1.75
    unique_values_list = list(map(unique_for_lambda, lambda_list))

    # plt.plot(lambda_list, unique_values_list) # ORIGINAL PLOT
    # plt.show()

    plt.plot(np.abs(lambda_list-lambda_list[-1]), unique_values_list)
    plt.xscale("log")
    plt.yscale("log")

    plt.show()

def do_count_laminar2():

    def unique_for_lambda(_lambda):
        # point 1
        x0 = 0.1
         # от порядка к хаосу через перемежаемость 1.75 -> 1.7499
        k = 1000
        delta = 0
        x_array = stf.iterate(_lambda, stf.logistic_map, k, delta, x0)

        # # x values
        # x_array, k = plot_xarray()

        precision = 10**-2
        multiplier = np.int(1/precision)
        x_array_rounded = (np.array(x_array)*multiplier).astype(np.int)
        x_array_rounded = x_array_rounded[1:]   # make array from 1001 to 1000

        # we descretizes array to groups with group_size. laminar or toorbulent each group will be?
        # then we will understand where toorbulent and where laminar states is on whole array
        group_size = 20 # star from 20, 40, 100
        grouped_array = x_array_rounded.reshape(len(x_array_rounded) // group_size, group_size)
        len_array = [len(np.unique(group)) for group in grouped_array]
        # from marked array we can find all laminar states apearing

        #  if _len<(group_size//4)  (if _len mini-unique_array is small) then state is laminar, otherwise it's chaotic, means turbulent
        mark_array = [1 if _len<(group_size//4) else 0 for _len in len_array]

        # print("lambda: ", _lambda," sum mark array: ", sum(mark_array))

        # unique_array = np.unique( x_array_rounded )

        return sum(mark_array)

    lambda_list = np.arange(1.749, 1.75, 0.000001)   #1.748 - 1.75
    unique_values_list = list(map(unique_for_lambda, lambda_list))

    # plt.plot(lambda_list, unique_values_list) # ORIGINAL PLOT
    # plt.show()
    from scipy import polyval, polyfit, stats

    lambda_list = np.log(lambda_list)
    unique_values_list = np.log(unique_values_list)

    slope, intercept, r_value, p_value, std_err = stats.linregress(lambda_list, unique_values_list)
    print(slope, intercept, r_value, p_value, std_err)

    plt.plot(lambda_list, unique_values_list, ".")
    # we need to calculate tilt coefficient
    a,b = polyfit(lambda_list, unique_values_list, 1)

    y_predicted = polyval([a,b], lambda_list)

    plt.plot(lambda_list, y_predicted, "r")

    # plt.xscale("log")
    # plt.yscale("log")

    plt.show() # k =~ 8750



# TODO
    # plot len laminar phase from distanse to lambda crit
    # log x log y
    # aproximate to line


if __name__ == '__main__':
    #plot_xarray()
    #plot_lyapunov()
    #do_lyapunov_map()
    # do_draw_laminar() # page 253 in Kuznecov
    # do_count_unique()

    do_count_laminar2()
    # import timeit
    # x = timeit.timeit(plot_lyapunov, number=1)
    # print(x, " ms")