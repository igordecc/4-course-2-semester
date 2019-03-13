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
k = 200
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

x_array = stf.iterate(_lambda, stf.logistic_map, k, 0, x0)
# print(x_array)


# should be function
for n in range(0, len(x_array) - 1):
    plt.vlines(x_array[n], x_array[n], x_array[n + 1], "b")
    plt.hlines(x_array[n + 1], x_array[n], x_array[n + 1], "b")

plt.grid()
plt.show()

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

r_array = numpy.arange(0,1.5,0.05)

D_array = list(map(find_D_corr, r_array))

plt.plot(r_array, D_array, "r.")
plt.grid()
plt.show()
# plt.clf()