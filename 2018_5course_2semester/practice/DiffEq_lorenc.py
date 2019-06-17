import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import os
import FourierPlot as ffp #DONT work
# import WorkWFiles                     DONT WORK
from matplotlib.font_manager import FontProperties
from pylab import figure, plot, xlabel, grid, legend, title, savefig


# Equation System func, ε - relation parameter 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.24
# [0.85, 0.9, 0.95, 1.05, 1.1]
eps = 10
# Equation System
def f_x(x):
    return 10*x[1] - 10*x[0]
def f_y(x):
    return 40*x[0] - x[0]*x[2] - x[1]
def f_z(x):
    return x[0]*x[1] - 8/3*x[2]
def f_u(x):
    return 10*x[4] - 10*x[3] + eps*(x[0] - x[3])  # relation cases: strong(ε = 20) or weak(ε = 0.2)
def f_v(x):
    return 35*x[3] - x[3]*x[5] - x[4]
def f_w(x):
    return x[3]*x[4] - 8/3*x[5]


# Runge Kutta solution
def rKN(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x
def solve():
    f = [f_x, f_y, f_z, f_u, f_v, f_w]
    x = [1, 1, 0, 0.1, 0.1, 0.1]
    hs = 0.01
    X =[]; Y=[]; Z=[]; U=[]; V=[]; W=[]
    for i in range(15000):
        x = rKN(x, f, 6, hs)
        X.append(x[0]); Y.append(x[1]); Z.append(x[2])
        U.append(x[3]); V.append(x[4]); W.append(x[5])
    return [X, Y, Z, U, V, W]


# work with arrays of phases
def do_phase_shift_np(X, Y):
    X = np.array(X); Y = np.array(Y)
    return np.arctan2(Y, X)
def do_diff_arrays(x, y):
    x = np.array(x); y = np.array(y)
    return x - y
def do_phase_shift(X, Y):
    n = min(len(X), len(Y))
    phase_array = []
    for i in range(n):
     #   if math.atan2(Y[i], X[i]) > math.pi:
      #      phase_array.append(math.atan2(Y[i], X[i]) - math.pi)
       # if math.atan2(Y[i], X[i]) < - math.pi:
        #    phase_array.append(math.atan2(Y[i], X[i]) + math.pi)
       # else:
            phase_array.append(math.atan2(Y[i], X[i]))
    return phase_array


# save solution results in text files
def save(s):
    WorkWFiles.write_to_file(s[0], 'solutions/'+ str(omega_d) + '_x_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[1], 'solutions/'+ str(omega_d) + '_y_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[2], 'solutions/'+ str(omega_d) + '_z_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[3], 'solutions/'+ str(omega_d) + '_u_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[4], 'solutions/'+ str(omega_d) + '_v_eps=' + str(eps) + '.dat')
    WorkWFiles.write_to_file(s[5], 'solutions/'+ str(omega_d) + '_w_eps=' + str(eps) + '.dat')
def phase_diff(s):
    phase = do_diff_arrays(do_phase_shift(s[0], s[1]), do_phase_shift(s[3], s[4]))  # task 3.1
    # for i in range(len(phase) - 1):
    #    if (phase[i + 1] - phase[i] > 2*math.pi):
    #        phase[i+1] = phase[i+1] - 2*math.pi
    #   if (phase[i + 1] - phase[i] < - 2*math.pi):
    #        phase[i+1] = phase[i+1] + 2*math.pi
    # WorkWFiles.write_to_file(phase, 'phases/'+ str(omega_d) + '_eps=' + str(eps) + '.dat')
    return phase


# plotting
def plot_f(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z)
    plt.show()
def do_plot(*args):
    for i in args:
        plt.plot(i, '.')
    plt.show()


if __name__ == '__main__':
    s = solve()
    s1 = phase_diff(s)
    plt.plot(s1[5000:6000], "-")
    # plt.yscale("log")
    plt.show()

"""
метод диагносцирования фазовой синхронизации разностью фаз
"""