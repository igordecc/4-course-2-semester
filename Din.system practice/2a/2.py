import matplotlib.pyplot as pp
import numpy as np

def logistic_map(x0, lambd):
    return lambd - x0*x0

def final_point(x0, N, lambd, additional_points):
    for i in range(N-additional_points):
        x0 = logistic_map(x0, lambd)

    x0_additional_points = []
    for i in range(additional_points):
        x0 = logistic_map(x0, lambd)
        x0_additional_points.append(x0)

    return x0_additional_points

if __name__=='__main__':
    N = 1000
    x0 = 0
    additional_points = 5       # return 5 dots instead of 1 on diagram plot
    x0 = [0 for i in range(additional_points)]
    lambd_0 = 0
    lambd_d = 0.001
    lambd_N = 2.5 + lambd_d

    map_x0 = [[] for i in range(additional_points)]
    map_lambd = np.arange(lambd_0, lambd_N, lambd_d) #numpy array of all mabda stuff

    for i in np.arange(lambd_0, lambd_N, lambd_d):
        x0 = final_point(x0[additional_points-1], N, i, additional_points)

        for j in range(additional_points):
            map_x0[j].append(x0[j])

    for i in range(additional_points):
        pp.plot(map_lambd, map_x0[i], 'm.')

    pp.grid()
    pp.show()