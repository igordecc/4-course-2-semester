# redo from f(iter) to f(Q) - does not work
# TODO first - build f(Q) for not discrete Qs, after - build the map, like logistic map.

import numpy
import matplotlib.pyplot
import matplotlib.widgets

def circular_map(x, Omega, K):
    equation = x + Omega +( (K / (2*numpy.pi) * numpy.sin(x%(2*numpy.pi))) ) #RIGHT VERTION
    return equation

def do_map():
    #Omega = 0.60666666
    Omega = 0.6
    K = 1
    x = 0
    iter_number = 100

    def iter_map(x, Omega, K, iter_number):
        x_array = [x]
        for i in range(iter_number):
            x_array.append( circular_map(x_array[i], Omega, K) )
        return x_array

    fig, ax = matplotlib.pyplot.subplots()

    x_array = iter_map(x, Omega, K, iter_number)

    #my_plot, = matplotlib.pyplot.plot(x_array[:-1],x_array[1:])
    my_plot, = matplotlib.pyplot.plot(x_array)
    slider_ax1 = matplotlib.pyplot.axes([0.25, 0.1, 0.65, 0.03])
    slider_ax2 = matplotlib.pyplot.axes([0.25, 0.15, 0.65, 0.03])
    slider_Omega = matplotlib.widgets.Slider(slider_ax1, "Omega", 0.1, 5, valinit=Omega) #, valstep=0.1)
    slider_K = matplotlib.widgets.Slider(slider_ax2, "K", 0.1, 5, valinit=K) #, valstep=0.1) Does not exist anymore?


    def update(val):
        Omega = slider_Omega.val
        K = slider_K.val
        x_array = iter_map(x, Omega, K, iter_number)
        my_plot.set_ydata(x_array)
        # my_plot.set_xdata(x_array[:-1])
        # my_plot.set_ydata(x_array[1:])



        fig.canvas.draw_idle()

    slider_Omega.on_changed(update)
    slider_K.on_changed(update)

    matplotlib.pyplot.show()

if __name__ == '__main__':
    do_map()