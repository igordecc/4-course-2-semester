import numpy as np

# system 0
def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    # print('params["E"]', params["E"]) #TESTs
    # print("x2 ", x2)
    # print('x ', x)
    dxdt = -params["w"]*y - z + params["E"]*(x2 - x) + params["noise_amp"]*np.random.normal(0,1) #noise
    dydt = params["w"]*x + params["a"]*y
    dzdt = params["p"] + z*(x - params["c"])
    newstate = [dxdt, dydt, dzdt]
    return newstate

params = {
        "osc1": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 1.0,  # change here [0.89 - 1.01]
            "E": .4,
            "noise_amp": 0,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.95,  # const
            "E": .4,
            "noise_amp": 0,
        },
        "dt": 0.01,
        "startfrom": 3000,
        "e_error": 0,
    }

state_d = {
        "time": [t for t in np.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.1, 0.1, 0.1], ],
        "e_error_norm": [0, ]
    }

# system 1
def _lorenc(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = params["sigma"] *(y - x) + params["E"]*(x2 - x) + params["noise_amp"]*np.random.normal(0,1)
    dydt = params["r"]*x - y - x*z
    dzdt = -params["b"]*z + x*y
    newstate = [dxdt, dydt, dzdt]
    return newstate

params = {
        "osc1": {
            "sigma": 10,
            "b": 8/3,
            "r": 40.0,
            "E": 0,
            "noise_amp": 0,
        },
        "osc2": {
            "sigma": 10,
            "b": 8/3,
            "r": 35.0,
            "E": 0.4,
            "noise_amp": 0,
        },
        "dt": 0.01,
        "startfrom": 3000,
        "e_error": 0,
    }

state_d = {
        "time": [t for t in np.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.1, 0.1, 0.1], ],
        "e_error_norm": [0, ]
    }

# system 2
def garmonic_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = -y - z + params["E"]*np.cos(params["w"]*state_d["time"][0]) + params["noise_amp"]*np.random.normal(0,1) #noise
    dydt = x + params["a"]*y
    dzdt = params["p"] + z*(x - params["c"])
    newstate = [dxdt, dydt, dzdt]
    return newstate

params = {
        "osc1": {
            "a": 0.15,
            "p": 0.4,
            "c": 8.5,
            "w": 1.0,  # change here [0.9 - 1.1]
            "E": .4,
            "noise_amp": 0,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.95,  # const
            "E": .4,
            "noise_amp": 0,
        },
        "dt": 0.01,
        "startfrom": 3000,
        "e_error": 0,
    }

state_d = {
        "time": [t for t in np.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.1, 0.1, 0.1], ],
        "e_error_norm": [0, ]
    }