# single function in this darkness
# one direction coupled ressler
# be-coupled ressler oscillator
import numpy
from functools import reduce
import matplotlib.pyplot as plt
from copy import deepcopy
from functools import reduce
import numpy as np
import math

# TODO change for another system
def bec_ressler(state, alienstate, params):
    x, y, z = state
    x2, y2, z2 = alienstate
    dxdt = -y - z + params["E"]*np.cos(params["w"]*state_d["time"][0]) + params["noise_amp"]*np.random.normal(0,1) #noise
    dydt = x + params["a"]*y
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
    # what we do? - calculate error parametr e, from our after-evaluation-data
    # why? - we need to estimate synchronisation in our system somehow. e_error can tell us about degree of synchronisation in a system if we toss it  system's data.
    e_value = sum(state_d["e_error_norm"]) / len(state_d["e_error_norm"]) / (
                state_d["savedtime"][-1] - state_d["savedtime"][params["startfrom"]])
    return e_value


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

def make_timestep_local(data):
    # why - we need to compute evaluate system for one set of parameters
    # data -> state_d, params -> make_timestep() -> state_d, params with results
    state_d, params = data
    make_timestep(state_d, params)
    return state_d, params

def pipeline_each(data, fns):
    result = reduce(lambda a, x: list(map(x, a)),
                    fns,
                    data)
    return result

if __name__ == '__main__':
    # art of state evolution
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

    def part1_x1fromx2(state_d, params):
        make_timestep(state_d, params)

        x_osc1 = list(map(lambda x: x[0], state_d["osc1"][params["startfrom"]:]))
        x_osc2 = list(map(lambda x: x[0], state_d["osc2"][params["startfrom"]:]))
        print("e_error: ", e_error(state_d, params))
        plt.plot(x_osc1, x_osc2, "r.")
        plt.xlim(-15,20)
        plt.ylim(-15,20)
        plt.grid()
        plt.show()

    #part1_x1fromx2(deepcopy(state_d), deepcopy(params))

    def part2_efromE(state_d, params):
        """
        state-> make_elist() -> E_osc1 changing [Emin, Emax] and elist, calculated from them.
        what is it? - its wrapper function. we plot e from E1(, E2) inside it.
        why? - we looking for synchronisation and it's dependence from bound-parameters.
        Also, This wrapper-function can be used to watch system dependence from any kind of parameters. For this jump "to stage 0" in make_elist, type parameter u want and remake updater (updateEs function) TODO Remake updater
        :param state_d: dictionary
        :param params: dictionary
        :return: plot
        """


        def make_elist(state_d, params):
            """
            what are we doing? - making e from E1(, E2) dependence
            why - we need to make plot with e and E1
            E1 - connection parameter of the system, give by default.
            e - synchronisation error parameter, calculated in make_elist.
            :param state_d: dict
            :param params: dict
            :return: (list, list, list)
            """

            def e_list_append(data):
                # why - we need to find e_error for 1 case of parameters
                # data -> state_d, params -> e_error() -> state_d, params with results
                state_d, params = data
                params["e_error"] = e_error(state_d, params)
                return state_d, params

            def updateEs(p_E_sample):
                # what is it - support update-function, being used in prepare stage (stage 1)
                # why - we need to write to params values of E (bounding coeffitient, wich is one of params)
                params, E_osc1, E_osc2 = p_E_sample[0], p_E_sample[1], p_E_sample[2]
                params["osc1"]["E"] = E_osc1
                params["osc2"]["E"] = E_osc2
                return params

            # stage 0 - determine values we will whatch # TODO change for another system
            E_osc1 = [i for i in numpy.arange(0, 25, 0.5)]
            E_osc2 = [i for i in numpy.arange(0, 25, 0.5)]

            # stage 1 - prepare default values
            # why we do that? - we are coping and preparing our state and params dictionaries for the next stage
            paramlist = [deepcopy(params) for i in E_osc1]      # why - we need paramslist with length of list E_osc1
            params_and_E = list(zip(paramlist, E_osc1, E_osc2))
            paramlist = list(map(updateEs, params_and_E))
            state_d_list = [deepcopy(state_d) for i in E_osc1]

            data = list(zip(state_d_list, paramlist))

            # stage 2 - pipeline our data
            # what we do - evaluate our system and making list of e values we are looking for.
            new_data = pipeline_each(data, [make_timestep_local,
                                 e_list_append
                                 ])

            # stage 3 - we collect all calculated e_error data. e - synchronisation error parameter.
            # why - to build a plot from this data next.
            e_list = list(map(lambda x: x[1]["e_error"], new_data))
            return E_osc1, E_osc2, e_list

        # what are we doing? - this is wrapper-function area. We plot all plots here to invoke (or make) them by single function call.
        # why? - (We do all side-staff here) because it's very convenient! And because we need to plot e from E1 curve.
        E_osc1, E_osc2, e_list = make_elist(state_d, params)
        plt.plot(E_osc1, e_list, "b-")
        plt.yscale("log")

        plt.grid()
        plt.show()
        # print(e_list)

    #part2_efromE(deepcopy(state_d), deepcopy(params)) # now we can call the function and get all plots!


    def part51_phase(state_d, params):
        make_timestep(state_d, params)
        x_osc1 = np.array(list(map(lambda x: x[0], state_d["osc1"][params["startfrom"]:])))

        def do_phase(osc="osc1"):
            x_osc1 = np.array(list(map(lambda x: x[0], state_d[osc][params["startfrom"]:])))
            y_osc1 = np.array(list(map(lambda x: x[1], state_d[osc][params["startfrom"]:])))
            phase_osc1 = np.arctan2(y_osc1, x_osc1)
            return phase_osc1
        phase_osc1 = do_phase("osc1")
        phase_osc2 = do_phase("osc2")
        import scipy.fftpack
        fourier_spk1 = scipy.fftpack.fft(phase_osc1)
        fourier_spk2 = scipy.fftpack.fft(phase_osc2)


        delta_spk = fourier_spk1-fourier_spk2
        delta_spk_pre = abs(scipy.fftpack.fft(phase_osc1-phase_osc2))
        #delta_phase = abs(phase_osc1-phase_osc2)

        # x_osc2 = list(map(lambda x: x[0], state_d["osc2"][params["startfrom"]:]))
        # print("e_error: ", e_error(state_d, params))
        # plt.plot(x_osc1, phase_osc1, "r.")
        plt.plot(x_osc1, delta_spk_pre, "r")
        #plt.xlim(-15,15)
        #plt.ylim(0,1)
        plt.grid()
        plt.show()

    #part51_phase(deepcopy(state_d), deepcopy(params))

    def diagnose_lagsync(state_d, params):
        """
        for diagnosing lag synchronisation you dont need to change the system
        what we need - check the synchronisation between oscillators simultaneously dislocating data on T steps. Boom - lag synchronisation.
        how? - write check-function S2(T)
        why - we need to diagnose lag synchronisation in task 1 and 7.3
        :param state_d: dict copy
        :param params: dict copy
        :return: plots S from T. On minimums will be it (lag. sync.)
        """



        def checkout_allT(state_d, params):
            # what we doing?- finding S2(T) for different Ts.
            # can return minimum S or all S series from T
            # why? - we need to calculate S2
            make_timestep(state_d, params)

            def S2(state_d_and_T):
                """

                :param state_d:
                :param T: int - number timesteps to skip
                :return: S_value for certain T
                """
                # why? - we need to unpack, bbefor we can use it
                np_osc1, np_osc2, T = state_d_and_T
                S2_value = np.sum(np.abs(np_osc2 - np_osc1) ** 2) / np.sqrt(
                    np.sum(np.abs(np_osc1) ** 2) * np.sum(np.abs(np_osc2) ** 2))
                return np.sqrt(S2_value), T  # why? - because S2 is S**2 and we what S. Not the big difference.

            #why - we want make it map, so we need all T and state_d_list to feed the map() function
            Tmax = len(state_d["osc1"])//100
            T_list = np.arange(1, Tmax)

            # why make it numpy? - for usefullness later
            np_osc1 = np.array(state_d["osc1"])
            np_osc2 = np.array(state_d["osc2"])

            # what we doing? we making time-lag slice
            # why? - for lag synchronisation check
            np_osc1 = [np_osc1[:-T] for T in T_list]
            np_osc2 = [np_osc2[T:] for T in T_list]

            state_d_and_T = zip(np_osc1, np_osc2, T_list)
            list_of_S_and_T = np.array(list(map(S2, state_d_and_T)))

            list_of_S_and_T = list_of_S_and_T.transpose() # now it's [[Smin walues], [Tvalues]]
            return list_of_S_and_T

        def update_param(p_sample):
            # what is it - support update-function, being used in prepare stage (stage 1)
            # why - we need to write to params values of E (bounding coeffitient, wich is one of params)
            params, p_osc1, p_osc2, param_name = p_sample
            params["osc1"][param_name] = p_osc1
            params["osc2"][param_name] = p_osc2
            return params

        def Smin_and_T_list_append(data):
            # why - we need to find Smin and corresponding T for 1 case of parameters
            # data -> state_d, params -> e_error() -> state_d, params with results
            state_d, params = data
            numpySandT = checkout_allT(state_d, params)

            # why? - we want find the minimum parameter and it's index
            Smin_num = np.where(numpySandT[0] == numpySandT[0].min())[0]
            min_S_and_T = numpySandT[:, Smin_num]

            params["s_min"] = min_S_and_T[0]
            params["t_for_s"] = min_S_and_T[1]

            return state_d, params

        # stage 0 - determine values we will whatch # TODO change for another system
        Emin = 0
        Emax = 12
        dE = 0.4

        E_osc1 = [i for i in numpy.arange(Emin, Emax, dE)]
        E_osc2 = [i for i in numpy.arange(Emin, Emax, dE)]

        # stage 1 - prepare default values
        paramlist = [deepcopy(params) for i in E_osc1]  # why - we need paramslist with length of list E_osc1
        param_name_list = ["E" for i in E_osc2]
        data_to_update = list(zip(paramlist, E_osc1, E_osc2, param_name_list))
        paramlist = list(map(update_param, data_to_update))
        state_d_list = [deepcopy(state_d) for i in E_osc1]

        data = list(zip(state_d_list, paramlist))

        # stage 2 - pipeline our data
        # what we do - evaluate our system and making list of e values we are looking for.
        new_data = pipeline_each(data, [make_timestep_local,
                                        Smin_and_T_list_append
                                        ])

        # stage 3 - we collect all calculated e_error data. e - synchronisation error parameter.
        # why - to build a plot from this data next.
        s_min_list = list(map(lambda x: x[1]["s_min"], new_data))
        t_for_s_list = list(map(lambda x: x[1]["t_for_s"], new_data))

        plt.plot(E_osc1, s_min_list, "b.")
        #plt.plot(E_osc1, t_for_s_list, "r.")
        plt.grid()
        plt.show()


    diagnose_lagsync(deepcopy(state_d), deepcopy(params))

    def add_noise_and_plot_all(state_d, params):
        noise_amp = 0.2
        params["osc1"]["noise_amp"] = noise_amp
        params["osc2"]["noise_amp"] = noise_amp
        part1_x1fromx2(deepcopy(state_d), deepcopy(params))
        part2_efromE(deepcopy(state_d), deepcopy(params))
        diagnose_lagsync(deepcopy(state_d), deepcopy(params))

    #add_noise_and_plot_all(deepcopy(state_d), deepcopy(params))

    def do_phase_plot(state_d, params):
        make_timestep(state_d, params)

        xyz1 = numpy.transpose(state_d["osc1"][params["startfrom"]:])
        xyz2 = numpy.transpose(state_d["osc2"][params["startfrom"]:])

        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        ax.plot(xyz1[0],xyz1[1],xyz1[2], "r")
        ax.plot(xyz2[0],xyz2[1],xyz2[2], "b")
        plt.grid()
        plt.show()


    #do_phase_plot(deepcopy(state_d), deepcopy(params))

    def plot_E_from_D(state_d, params):

        def update_data(zipped):
            data, update_value, flag, flag1 = zipped
            if flag1 is not None:
                data[flag][flag1] = update_value
            else:
                data[flag] = update_value
            return data

        def find_e_from_static_D(zipped):
            state_d, params = zipped
            make_timestep(state_d, params)
            return e_error(state_d, params)

        noise_amp_list = np.linspace(0, 10, 100)

        state_d_list = [deepcopy(state_d) for i in noise_amp_list]
        params_list = [deepcopy(params) for i in noise_amp_list]

        # why? - we need to update here params for different calulations
        params_list = list(map(update_data, zip(params_list, noise_amp_list, ["osc1" for i in noise_amp_list], ["noise_amp" for i in noise_amp_list])))
        params_list = list(map(update_data, zip(params_list, noise_amp_list, ["osc2" for i in noise_amp_list], ["noise_amp" for i in noise_amp_list])))

        # we map find_e to statistic D
        e_value_list = list(map(find_e_from_static_D, zip(state_d_list, params_list)))

        plt.plot(noise_amp_list, e_value_list)
        plt.xlabel("noise amp")
        plt.ylabel("e error")
        plt.grid()
        plt.show()


    #plot_E_from_D(deepcopy(state_d), deepcopy(params))
