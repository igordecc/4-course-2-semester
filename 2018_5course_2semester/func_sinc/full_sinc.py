# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy

def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = -params["w"]*y - z + params["E"]*(x2 - x)
    dydt = params["w"]*x + params["a"]*y
    dzdt = params["p"] + z*(x - params["c"])
    newstate = [dxdt, dydt, dzdt]
    return newstate

def update_state(state_d, params):
    state_osc1 = state_d["osc1"][-1]
    state_osc2 = state_d["osc2"][-1]
    d_dt_osc1 = bec_ressler(state_osc1, state_osc2, params["osc1"])
    buff = zip(state_osc1, d_dt_osc1)
    new_state_osc1 = list(map(lambda x: x[0] + x[1] * params["dt"], buff))

    d_dt_osc2 = bec_ressler(state_osc2, state_osc1, params["osc2"])
    buff = zip(state_osc2, d_dt_osc2)
    new_state_osc2 = list(map(lambda x: x[0] + x[1] * params["dt"], buff))

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
            "w": 0.89,  # change here [0.89 - 1.01]
            "E": 0.1,
        },
        "osc2": {
            "a": 0.15,
            "p": 0.2,
            "c": 10,
            "w": 0.95,  # const
            "E": 0.1,
        },
        "dt": 0.1,
    }



    state_d = {
        "time": [t for t in numpy.arange(0, 100.0001, params["dt"])],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.2, 0.2, 0.2], ]
    }

    make_timestep(state_d, params)

    import matplotlib.pyplot as plt
    # map it
    starfrom = 500
    x_osc1 = list(map(lambda x: x[0], state_d["osc1"][starfrom:]))
    x_osc2 = list(map(lambda x: x[0], state_d["osc2"][starfrom:]))

    plt.plot(x_osc1, x_osc2, "r.")
    plt.grid()
    plt.show()
    print(x_osc1)