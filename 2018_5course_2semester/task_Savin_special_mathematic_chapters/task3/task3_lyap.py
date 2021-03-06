# IT's copy of task3_2
# TODO rebuild program for lyapunov exponent calculations

import numpy
import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
import matplotlib.widgets
import matplotlib.widgets as wdt
import sup_task_funcs as stf
import timeit
from copy import deepcopy
import matplotlib.axis as axis

def circular_map_kwargs(x, Omega=0.6066, K=1):
    result_x = (x + Omega + (K / (2*numpy.pi) * numpy.sin(x*2*numpy.pi)) )%1 #RIGHT VERTION
    return result_x

params = {
    "args" : [],
    "kwargs": {
        "Omega": 0.06066,
        "K": 1,
    },
    # "iter_number": 100,
    "dt": 0.01,
    "time_limits": [0, 10.65, 0.01],
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
    detect_periods(with_precision)
    """
    multiplier = precision**-1
    applicable_x_array = (deepcopy(state_d["x_array"])*multiplier).astype(np.int)
    unique_array = np.unique(applicable_x_array)

    # print("unique_array: ",unique_array)
    # print("len of array: ",len(unique_array))
    # print("count of unique elements: ", np.unique(applicable_x_array, return_counts=True)[1])

    period_number = len(unique_array)   # because this is the easiest way of detecting p_number
    return period_number

def compute_parameter_map(state_d, params):
    """
    assemple differnt K and omega list, boot and plot results
    in one word:  making parameter picture
    """

    # Omega = 0.60666666 # K = 1
    omega_array = np.arange(0, 1, 0.01) # [minimum, maximum, delta]
    K_array = np.arange(4, 0, -0.05)

    # K_omega_list = np.array([ [ [K,omega] for K in K_array] for omega in omega_array ])
    # print(K_omega_list)
    params_list = []
    state_d_list = []
    for omega in omega_array:
        for K in K_array:
            params["kwargs"]["Omega"] = omega
            params["kwargs"]["K"] = K
            params_list.append(deepcopy(params))
            state_d_list.append(deepcopy(state_d))

    def make_in_parallel(state_d, params):
        def diff(fn,
                 x,
                 kwargs,
                 dx):
            return (fn(x + dx, **kwargs) - fn(x, **kwargs)) / dx

        def lyapunov_index(fn,
                           x0,
                           kwargs,
                           nsum):   # number of iterrations that will be summed
            x = [x0]
            dx = 0.0001  # precision need to be high enough
            lyap_sum = 0
            delta = nsum // 2
            for i in range(nsum):
                if i > delta:
                    dfdx = diff(fn, x[i], kwargs, dx)
                    lyap_sum += numpy.log(abs(dfdx))
                x.append(fn(x[i], **kwargs))
            lyap_sum /= (nsum - delta)
            return lyap_sum

        lyapunov_index_value = lyapunov_index(circular_map_kwargs, state_d["x_array"][0], params["kwargs"],nsum=1000)
        return lyapunov_index_value

    # periods_array = np.array(list( map(make_in_parallel, state_d_list, params_list) )).reshape(len(K_array), len(omega_array))
    periods_array = np.array(list( map(make_in_parallel, state_d_list, params_list) )).reshape(len(omega_array), len(K_array))
    periods_array = np.transpose(periods_array)
    periods_array[periods_array>0] *= 40
    periods_array[periods_array<0] *= 20
    periods_array[periods_array>40] = 40
    periods_array[periods_array<-20] = -20
    # periods_array[periods_array<-4] = periods_array/4
    print("done mapping!")

    # plt plotting============ change to something more sensible or comfy

    plt.matshow(periods_array, cmap=plt.get_cmap("coolwarm"))
    plt.xticks([0,100],[0,1])
    plt.yticks([0,60,80], [4,1,0])
    # plt.xaxis.set_ticks_position(position="bottom")
    plt.xlabel("Omega")
    plt.ylabel("K")
    plt.show()



if __name__ == '__main__':
    """
    PLAN
    deepcopy state_d params
    pipe line:
        evaluate - to get x_array
        detect_priods - to determin number of periods
        compute_parameter_map - do again and again previous points to get a map 
    """


