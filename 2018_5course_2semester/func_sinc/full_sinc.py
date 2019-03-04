# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy

def bec_ressler(state, alienstate, params):
    # state dict of list of "osc1":[[x,y,z], [x,y,z], [x,y,z]]
    # marker = "osc1", or "osc2"
    # alienmarker = "osc1", or "osc2"
    x, y, z = state
    x2, y2, z2 = alienstate
    dx = -params["w"]*y - z + params["E"]*(x2 - x)
    dy = params["w"]*x + params["a"]*y
    dz = params["p"] + z*(x - params["c"])
    newstate = [dx, dy, dz]
    return newstate

def update_state(state_d, params):
    state_osc1 = state_d["osc1"][-1]
    state_osc2 = state_d["osc2"][-1]
    new_state_osc1 = bec_ressler(state_osc1, state_osc2, params["osc1"])
    new_state_osc2 = bec_ressler(state_osc2, state_osc1, params["osc2"])
    state_d["osc1"].append(new_state_osc1)
    state_d["osc2"].append(new_state_osc2)
    state_d["savedtime"].append(state_d["time"].pop(0))

# def make_timestep(state_d, params):
#     update_state(state_d, params)
#     if state_d["time"]:
#         make_timestep(state_d, params)
# Notes: it works, but python cant resolve recurtion
# make it loop, though

def make_timestep(state_d, params):
    while state_d["time"]:
        update_state(state_d, params)
        print(state_d["savedtime"][-1])


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
    }

    state_d = {
        "time": [t for t in numpy.arange(0, 100.0001, 0.1)],
        "savedtime": [],
        "osc1": [[0.1, 0.1, 0.1], ],
        "osc2": [[0.2, 0.2, 0.2], ]
    }

    make_timestep(state_d, params)