import matplotlib.pyplot as plt
import numpy
import sup_task_funcs as stf
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
x = [x for x in na]
zero_array = [0 for x in na]
plt.plot(x, f_array)  # parabola
plt.plot(x, x)  # diagonal
plt.plot(x, zero_array)  # x axes
plt.plot(zero_array, x)  # y axes

x_array = stf.iterate(_lambda, stf.logistic_map, iterate, delete_steps, x0)
# print(x_array)


# should be function
for n in range(0, len(x_array) - 1):
    plt.vlines(x_array[n], x_array[n], x_array[n + 1], "b")
    plt.hlines(x_array[n + 1], x_array[n], x_array[n + 1], "b")

# plt.grid()
# plt.show()

def do_D2_corr(x_array):
    #for every dot there wil be a number
    r = 0.5
    n = len(x_array) #количество точек
    def find_D_corr(r=0.5):
        from functools import reduce
        count_array = [0 for i in x_array]
        count_array = map(lambda xi: reduce(lambda a, x: a + (1 if abs(xi-x)<=r else 0),
                                            x_array, 0),
                          x_array)
        count_array = list(count_array)
        D = sum(count_array)/n**2
        return D

    r_array = numpy.arange(0, 1.5, 0.005)

    C_array = list(map(find_D_corr, r_array))

    D = sum(C_array)/sum(r_array)
    print("D: ", D)
    plt.plot(r_array, C_array, "r.")
    plt.yscale("log")
    plt.xscale("log")
    plt.grid()
    plt.show()
    # plt.clf()

# do_D2_corr(x_array)

xmin = min(x_array)
xmax = max(x_array)

box_number = 100
xdelta = (xmax - xmin)/box_number
xminmax_array = numpy.arange(xmin, xmax + xdelta, xdelta)

# for i,j in :
#     if :
#         count += 1
#         break
#
# map(lambda xi: reduce(lambda a,i,j: a+(1 if (xi>=i)and(xi<=j) else 0),
#                       zip(xminmax_array[:-1], xminmax_array[1:]), 0),
#     x_array)

x_box_array = map(lambda xi: list(filter(lambda x: all([(xi>=x[0]),(x<=x[1])]),     # will filter only 1 box for each xi
                                         zip(xminmax_array[:-1], xminmax_array[1:]))
                                  ),
                            x_array)

x_box_array = list(x_box_array)
print(x_box_array)

box_count_array = numpy.zeros(100)
