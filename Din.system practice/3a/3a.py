import matplotlib.pyplot as pp
import numpy as np

def logistic_map(x0, lambd, betta):
    return lambd - betta*x0 + x0**3

def final_point(x0, N, lambd, betta, additional_points):
    for i in range(N-additional_points):
        x0 = logistic_map(x0, lambd, betta)
        
    x0_add = []
    for i in range(additional_points):
        x0 = logistic_map(x0, lambd, betta)
        x0_add.append(x0)

    return x0_add

#TODO read numpy guide, please
#TODO learn how to do level color 2D maps
#TODO Learn how to do interactive regime

if __name__=='__main__':
    N = 1000
    x0 = 0
    additional_points = 5       # return 5 dots instead of 1 on diagram plot
    lambd_0 = -0.6
    lambd_d = 0.001
    lambd_N = 0.6 + lambd_d

    betta_0 = 0.8
    betta_d = 0.001
    betta_N = 2.5 + betta_d
    map_lambd = np.arange(lambd_0, lambd_N, lambd_d) #numpy array of all mabda stuff
    map_betta = np.arange(betta_0, betta_N, betta_d)
####CHANGE np.zeros to list
    map_x0 = np.zeros(shape=(len(map_lambd), len(map_betta), len(additional_points)))
    
    for i in map_lambd:
        for j in map_betta:
            x0_map[i][j] = final_point(x0, N, i, j, additional_points)
            

    for i in range(additional_points):
        pp.plot(map_lambd, map_x0[i], 'm.')

    pp.grid()
    pp.show()
