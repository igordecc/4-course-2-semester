import matplotlib.pyplot as plt
import numpy
import sup_task_funcs as stf
from functools import reduce

# import matplotlib.widgets as wdg
# 
# def do_slider(pos, name, min, max, valinit, update_fn, fig):
#     slide_ax = plt.axes(pos)
#     slider = wdg.Slider(slide_ax, name, min, max, valinit)
# 
#     def update(val):
#         slider_value = slider.val
#         update_fn(slider_value)
#         fig.canvas.draw_idle()
#     slider.on_changed(update)
# 
# if __name__ == '__main__':
#     slider_position = [0, 0, 1, 1]

_lambda = 1.4011
iterate = 2000
delete_steps = 200
x0 = 0

# plot basic figures
na = numpy.arange(-1, 1.00, 0.02)
f_array = [stf.logistic_map(x, _lambda) for x in na]  # parabola
x = na
zero_array = [0 for x in na]
plt.plot(x, f_array)  # parabola
plt.plot(x, x)  # diagonal
plt.plot(x, zero_array)  # x axes
plt.plot(zero_array, x)  # y axes

x_array = stf.iterate(_lambda, stf.logistic_map, iterate, delete_steps, x0)

import random


# print(x_array)


# should be function
for n in range(0, len(x_array) - 1):
    plt.vlines(x_array[n], x_array[n], x_array[n + 1], "b")
    plt.hlines(x_array[n + 1], x_array[n], x_array[n + 1], "b")

# x_array = numpy.random.uniform(0,1,100)
# plt.grid()
# plt.show()
from scipy.stats import linregress
def do_D2_corr(x_array):
    # for every dot there wil be a number
    r = 0.5
    n = len(x_array)  # количество точек

    def find_C_corr(r=0.5):

        count_array = [0 for i in x_array]
        count_array = map(lambda xi: reduce(lambda a, x: a + (1 if abs(xi - x) <= r else 0),
                                            x_array, 0),
                          x_array)
        count_array = list(count_array)
        C = sum(count_array) / n ** 2
        return C

    r_array = numpy.arange(0, 1.5, 0.005)

    C_array = list(map(find_C_corr, r_array))

    D = sum(C_array) / sum(r_array)
    D1 = (max(C_array)-min(C_array)) / (max(r_array)-min(r_array))
    D2 = linregress(r_array, C_array)
    print("D corelational  avarage: ", D)
    print("D corelational max avarage: ", D1)
    print("D corelational lg: ", D2)
    plt.clf()
    plt.plot(r_array, C_array, "g.")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid()
    plt.show()
    # plt.clf()


do_D2_corr(x_array)

# =========================================================
def hausdorf_D(x_array):
    xmin = min(x_array)
    xmax = max(x_array)

    box_number = 100
    def do_delta_and_N(box_number):
        xdelta = (xmax - xmin) / box_number

        box_indexes_of_x_array = map(lambda x: (x - xmin) // xdelta, x_array)
        box_indexes_of_x_array = list(map(int, box_indexes_of_x_array))
        from collections import Counter
        the_number_of_not_empty_boxes = stf.pipeline_each([box_indexes_of_x_array], [Counter,
                                                                      sorted,
                                                                      len]
                                                      )[0]
        return xdelta, the_number_of_not_empty_boxes

    box_number = numpy.arange(10, 1000, 10)

    delta_and_n = list(map(do_delta_and_N, box_number))
    delta = [i[0] for i in delta_and_n]
    n_number_of_not_empy_boxes = [i[1] for i in delta_and_n]

    D_Hausdorff = -sum(numpy.log(n_number_of_not_empy_boxes))/sum(numpy.log(delta))    # y / x
    D_Hausdorff1 = (max(numpy.log(n_number_of_not_empy_boxes)) - min(numpy.log(n_number_of_not_empy_boxes))) / (max(numpy.log(delta)) - min(numpy.log(delta)))    # y / x
    D_Hausdorff2 = linregress(numpy.log(delta), numpy.log(n_number_of_not_empy_boxes))

    print("D Hausdorff's a: ", D_Hausdorff)
    print("D Hausdorff ma: ", D_Hausdorff1)
    print("D Hausdorff lr: ", D_Hausdorff2)

    plt.clf()
    plt.plot(delta, n_number_of_not_empy_boxes, "g.")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid()
    plt.show()

    # print(delta)
    # print(n_number_of_not_empy_boxes)


# hausdorf_D(x_array)

#огибающая корелляциоонной функции для хаотического сигнала