# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy
from functools import reduce
import matplotlib.pyplot as plt

def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    # print('params["E"]', params["E"]) #TESTs
    # print("x2 ", x2)
    # print('x ', x)
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

def e_error(state_d, params):
    return sum(state_d["e_error_norm"]) / len(state_d["e_error_norm"])/(state_d["savedtime"][-1] - state_d["savedtime"][params["startfrom"]])

def update_state(state_d, params):
    state_osc1 = state_d["osc1"][-1]
    state_osc2 = state_d["osc2"][-1]
    # print("state_osc1 ", state_osc1)  #TESTs
    # print("state_osc2 ", state_osc2)
    increment_osc1 = bec_ressler(state_osc1, state_osc2, params["osc1"])
    increment_osc2 = bec_ressler(state_osc2, state_osc1, params["osc2"])
    # print("increment_osc1", increment_osc1)
    # print("increment_osc2", increment_osc2)
    dt = params["dt"]

    new_state_osc1 = euler_method(state_osc1, increment_osc1, dt)
    new_state_osc2 = euler_method(state_osc2, increment_osc2, dt)

    if (len(state_d["savedtime"])>params["startfrom"]) and abs(increment_osc1[0]) < 2**33:
        vector_difference = list(map(lambda x: x[0] - x[1], zip(increment_osc1, increment_osc2)))
        e_error_integral = euler_method([state_d["e_error_norm"][-1]], [norm(vector_difference)], dt)[0]
        # e_error_sum = norm(vector_difference)]       # backing variant, in case e_error_integral is not right thing - this thing is not right too.
        state_d["e_error_norm"].append(e_error_integral)
        # print(state_d["e_error_norm"][-1] - state_d["e_error_norm"][-2]) #TESTs

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
            "w": 0.81,  # change here [0.89 - 1.01]
            "E": 1.0,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.8,  # const
            "E": 1.0,
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
    state_d_default = state_d.copy()

    def part1_x1fromx2():
        make_timestep(state_d, params)

        x_osc1 = list(map(lambda x: x[0], state_d["osc1"][params["startfrom"]:]))
        x_osc2 = list(map(lambda x: x[0], state_d["osc2"][params["startfrom"]:]))
        plt.plot(x_osc1, x_osc2, "r.")
        plt.xlim(-15,20)
        plt.ylim(-15,20)
        plt.grid()
        plt.show()

        # TODO it's calculating now, but it's not Average. 1. Try make it average, by getting sum instead of integral
        print("e_error: ", e_error(state_d, params))

    part1_x1fromx2()
    def part2_efromE():
        E_osc1 = [i for i in numpy.arange(0, 2.5, 0.05)]
        E_osc2 = [i for i in numpy.arange(0, 2.5, 0.05)]
        e_list = []
        for E1, E2 in zip(E_osc1, E_osc2):
            state_d = state_d_default.copy()
            params["osc1"]["E"] = E1
            params["osc2"]["E"] = E2

            make_timestep(state_d, params)
            e_list.append(e_error(state_d, params))
            #TODO USE PIPE LINES

        map(make_timestep(state_d, params), state_d)