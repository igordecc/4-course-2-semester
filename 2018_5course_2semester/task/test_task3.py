from task3_2 import *
import timeit
from copy import deepcopy
import numpy as np
#================time test!====
params = {
    "args" : [],
    "kwargs": {
        "Omega": 0.06066,
        "K": 1,
    },
    "iter_number": 100,
    "dt": 0.01,
    "time_limits": [0, 20, 0.01],
    "skip": 1000,
}

state_d = {
    "x_array": np.array( [0.01, ] ),
}

def test_all_units():
    print()
    def test_list_append():
        evaluate(state_d, params)#(circular_map_kwargs, deepcopy(state_d), deepcopy(params))

    # print("time of all list appends: ",timeit.timeit(test_list_append, number=100)/100, " - list append")

    def _one_cell_time():

        global state_d, params
        state_d, params = evaluate(deepcopy(state_d), deepcopy(params))
        detect_periods(state_d, params)

    # print("time of the one cell:   ", timeit.timeit(_one_cell_time, number=1))

    def evaluate_time():
        global state_d, params
        state_d, params = evaluate(deepcopy(state_d), deepcopy(params))

    # print("time of one evaluation: ", timeit.timeit(evaluate_time, number=1))

    def compute_map():
        global state_d, params
        compute_parameter_map(deepcopy(state_d), deepcopy(params))

    print("time of compute_map: ", timeit.timeit(compute_map, number=1))