import numpy
import matplotlib.pyplot as plt
import sup_task_funcs as stf

_lambda = 1.4011
iterate = 2000
delete_steps = 200
x0 = 0
x_array = stf.iterate(_lambda, stf.logistic_map, iterate, delete_steps, x0)

def plot_itter_diag(x_array, _lambda):

    # plot basic figures
    na = numpy.arange(-1, 1.00, 0.02)
    f_array = [stf.logistic_map(x, _lambda) for x in na]  # parabola
    x = na
    zero_array = [0 for x in na]
    plt.plot(x, f_array)  # parabola
    plt.plot(x, x)  # diagonal
    plt.plot(x, zero_array)  # x axes
    plt.plot(zero_array, x)  # y axes



    for n in range(0, len(x_array) - 1):
        plt.vlines(x_array[n], x_array[n], x_array[n + 1], "b")
        plt.hlines(x_array[n + 1], x_array[n], x_array[n + 1], "b")
    plt.grid()
    plt.show()

plot_itter_diag(x_array, _lambda)


def calculate_C_from_r():
    ...