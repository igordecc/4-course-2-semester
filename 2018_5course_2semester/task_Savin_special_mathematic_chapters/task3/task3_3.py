
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

# WITHOUT (MOD 1)
def circular_map_kwargs(x, Omega=0.6066, K=1):
    result_x = x + Omega + (K / (2*numpy.pi) * numpy.sin(x*2*numpy.pi))  #RIGHT VERTION
    return result_x

params = {
    "args" : [],
    "kwargs": {
        "Omega": 0.06066,
        "K": 1,
    },
    # "iter_number": 100,
    "dt": 0.01,
    "time_limits": [0, 10., 0.01],
    "skip": 1000,
}

state_d = {
    "x_array": numpy.array( [0.01, ] ),
    "w": [0,] ,
}


# ===========evaluate system
def evaluate(state_d, params):#(system, state_d, params):
    # we need params from the system
    kwargs = params["kwargs"] # must be list
    buff_array = [state_d["x_array"][0], ]

    time_list = np.arange(*params["time_limits"])
    for i in time_list:
        result = circular_map_kwargs(buff_array[-1], **kwargs)
        buff_array.append(result)

    print("first: ", buff_array[0], " last: ", buff_array[-1])

    rotation_number = (buff_array[-1] - buff_array[0])/len(time_list)

    state_d["w"].append(rotation_number)
    return state_d, params # state_dictionary must be with computed results



def compute_parameter_map(state_d, params):
    """
    assemple differnt K and omega list, boot and plot results
    in one word:  making parameter picture
    """

    # Omega = 0.60666666 # K = 1
    omega_array = np.arange(0, 1, 0.001) # [minimum, maximum, delta]

    # K_omega_list = np.array([ [ [K,omega] for K in K_array] for omega in omega_array ])
    # print(K_omega_list)
    params_list = []
    state_d_list = []
    params["kwargs"]["K"] = 1

    for omega in omega_array:
        params["kwargs"]["Omega"] = omega
        state_d, params = evaluate(state_d, params)



    # for omega in omega_array:
    #     params["kwargs"]["Omega"] = omega
    #     params_list.append(deepcopy(params))
    #     state_d_list.append(deepcopy(state_d))
    #
    #
    # def make_in_parallel(state_d, params):
    #     state_d, params = evaluate(state_d, params)
    #     return state_d["w"]     # rotation number
    #
    # # periods_array = np.array(list( map(make_in_parallel, state_d_list, params_list) )).reshape(len(K_array), len(omega_array))
    # rotation_array = np.array(list( map(make_in_parallel, state_d_list, params_list) ))
    #
    # print("done mapping!")

    # plt plotting============ change to something more sensible or comfy
    # plt.matshow(periods_array,cmap=plt.get_cmap("terrain"))
    # plt.xticks([0,100],[0,1])
    # plt.yticks([0,60,80], [4,1,0])
    # plt.xaxis.set_ticks_position(position="bottom")
    plt.plot(omega_array, state_d["w"][1:])
    plt.xlabel("Omega")
    plt.ylabel("w")
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


