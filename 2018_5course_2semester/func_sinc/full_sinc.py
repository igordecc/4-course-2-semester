# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy
from functools import reduce
import matplotlib.pyplot as plt

def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = -params["w"]*y - z + params["E"]*(x2 - x)
    dydt = params["w"]*x + params["a"]*y
    dzdt = params["p"] + z*(x - params["c"])
    newstate = [dxdt, dydt, dzdt]
    return newstate


def norm(vector):
    norm_value = (reduce(lambda a, x: a + x**2, vector, 0))**0.5
    return norm_value

def euler_method(state, increment, dt):
    new_state = list(map(lambda x: x[0] + x[1] * dt, zip(state, increment)))
    return new_state

def update_state(state_d, params):
    state_osc1 = state_d["osc1"][-1]
    state_osc2 = state_d["osc2"][-1]
    # print("state_osc1 ", state_osc1)
    # print("state_osc2 ", state_osc2)
    increment_osc1 = bec_ressler(state_osc1, state_osc2, params["osc1"])
    increment_osc2 = bec_ressler(state_osc2, state_osc1, params["osc2"])
    # print("increment_osc1", increment_osc1)
    # print("increment_osc2", increment_osc2)
    dt = params["dt"]

    new_state_osc1 = euler_method(state_osc1, increment_osc1, dt)
    new_state_osc2 = euler_method(state_osc2, increment_osc2, dt)

    if len(state_d["savedtime"])>params["startfrom"]:
        vector_difference = map(lambda x: x[0] - x[1], zip(increment_osc1, increment_osc2))
        e_error_integral = euler_method([state_d["e_error_norm"][-1]], [norm(vector_difference)], dt)[0]
        state_d["e_error_norm"].append(e_error_integral)
        # print(state_d["e_error_norm"][-1] - state_d["e_error_norm"][-2])

    state_d["osc1"].append(new_state_osc1)
    state_d["osc2"].append(new_state_osc2)

    state_d["savedtime"].append(state_d["time"].pop(0))

def make_timestep(state_d, params):
    while state_d["time"]:
        update_state(state_d, params)


if __name__ == '__main__':
    # art of state evolution
    params = {
        "osc1": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.8,  # change here [0.89 - 1.01]
            "E": 0.1,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.8,  # const
            "E": 0.1,
        },
        "dt": 0.1,
        "startfrom": 500
    }



    state_d = {
        "time": [t for t in numpy.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.1, 0.1, 0.1], ],
        "e_error_norm": [0, ]
    }

    make_timestep(state_d, params)

    # map it

    x_osc1 = list(map(lambda x: x[0], state_d["osc1"][params["startfrom"]:]))
    x_osc2 = list(map(lambda x: x[0], state_d["osc2"][params["startfrom"]:]))
    plt.plot(x_osc1, x_osc2, "r.")
    plt.grid()
    plt.show()

    def e_error():
        return state_d["e_error_norm"][-1] / (state_d["savedtime"][-1] - state_d["savedtime"][params["startfrom"]])

    print("e_error: ", e_error())