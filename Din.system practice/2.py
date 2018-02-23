import matplotlib.pyplot as pp
import numpy as np

def logistic_map(x0, lambd):
    return lambd - x0*x0

def final_point(x0, N, lambd):
    for i in range(N):
        x0 = logistic_map(x0, lambd)
        #добавить возвращение трёх-пяти последний точек (для построения полной диаграммы)
    return x0

if __name__=='__main__':
    N = 1000
    x0 = 0
    lambd_0 = 0
    lambd_d = 0.001
    lambd_N = 2.5 + lambd_d

    map_x0 = []
    map_lambd = np.arange(lambd_0, lambd_N, lambd_d) #numpy array of all mabda stuff

    for i in np.arange(lambd_0, lambd_N, lambd_d):
        x0 = final_point(x0, N, lambd = i)
        map_x0.append(x0)
        #print(i, x0)
    #print(map_x0)
    pp.plot(map_lambd, map_x0, '.')
    pp.show()