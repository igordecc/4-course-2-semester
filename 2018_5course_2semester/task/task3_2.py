# redo from f(iter) to f(Q) - does not work
# TODO f(Q) for not discrete Qs is DONE, now: build the map, like logistic map.

import numpy
import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
import matplotlib.widgets
import matplotlib.widgets as wdt
import sup_task_funcs as stf
import timeit
from copy import deepcopy

def circular_map_kwargs(x, Omega=0.6066, K=1):
    result_x = x + Omega +( (K / (2*numpy.pi) * numpy.sin(x%(2*numpy.pi))) ) #RIGHT VERTION
    return result_x

params = {
    "args" : [],
    "kwargs": {
        "Omega": 0.06066,
        "K": 1,
    },
    "iter_number": 100,
    "dt": 0.01,
    "time_limits": [0, 100, 0.01],
    "skip": 1000,
}
state_d = {
    "x_array": numpy.array( [0.01, ] ),
}


# ===========evaluate system
def evaluate(state_d, params):#(system, state_d, params):
    # we need params from the system
    kwargs = params["kwargs"] # must be list
    buff_array = [state_d["x_array"][0], ]

    for i in np.arange( *params["time_limits"] ):
        result = circular_map_kwargs(buff_array[-1], **kwargs)
        buff_array.append(result)
    state_d["x_array"] = numpy.array( buff_array[ params["skip"]: ] )
    return state_d, params # state_dictionary must be with computed results



def detect_periods(state_d, params, precision = 10**-5):
    """
    precision -> multiplier  
    state_d * multiplier -> applicable_state_d
    np.unique(applicable_state_d) -> unique values and number of unique values | for test they should be mach
    
    :param state_d: 
    :param params: 
    :return: 
    """
    """
    detect_periods(with_precision)
    """
    multiplier = precision**-1
    applicable_x_array = [np.int(i*multiplier) for i in state_d["x_array"]]

    unique_array = np.unique(applicable_x_array)
    print("unique_array: ",unique_array)
    print("len of array: ",len(unique_array))
    print("count of unique elements: ", np.unique(applicable_x_array, return_counts=True)[1])
    # print(np.unique(applicable_x_array))


def compute_parameter_map(state_d, params):
    """
    IT'S NOT DONE and NOT REVIEWED

    :param state_d:
    :param params:
    :return:
    """

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





# ================time test!====

# def test_all_units():
#     def test_list_append():
#         evaluate(state_d, params)#(circular_map_kwargs, deepcopy(state_d), deepcopy(params))
#
#     print(timeit.timeit(test_list_append, number=100)/100, " - list append")

    # def detect_periods(state_d, params, precision=10 ** -5):
    #     """
    #     precision -> multiplier
    #     state_d * multiplier -> applicable_state_d
    #     np.unique(applicable_state_d) -> unique values and number of unique values | for test they should be mach
    #
    #     :param state_d:
    #     :param params:
    #     :return:
    #     """
    #     """
    #     detect_periods(with_precision)
    #     """
    #     multiplier = precision ** -1
    #     applicable_x_array = [np.int(i * multiplier) for i in state_d["x_array"]]
    #
    #     unique_array = np.unique(applicable_x_array)
    #     print("unique_array: ", unique_array)
    #     print("len of array: ", len(unique_array))
    #     print("count of unique elements: ", np.unique(applicable_x_array, return_counts=True)[1])
    #     # print(np.unique(applicable_x_array))


if __name__ == '__main__':
    """
    PLAN
    deepcopy state_d params
    pipe line:
        evaluate
        detect_priods
        comp[ute_parameter_map
    """

    state_d, params = evaluate(deepcopy(state_d), deepcopy(params))
    detect_periods(state_d, params)

