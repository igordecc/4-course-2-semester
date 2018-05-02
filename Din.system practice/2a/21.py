import numpy as np
import matplotlib.pyplot as plt


def logistic_map(x0, lambd):
    return lambd - x0*x0

def list_creator(x0,lambd, idepth):
    xlist = [logistic_map(x0, lambd)]
    for i in range(idepth):
        xlist.append( logistic_map(xlist[-1], lambd) )
        xlist.append(xlist[-1])
    return xlist

def itter_x(x0):
    yield logistic_map(x0, lambd)


def plotlogmap(x0, lambd, idepth):


    x = np.linspace(-lambd, lambd, 100)
    plt.plot(x, x, label="x(n+1) = x(n)")
    plt.plot(x, logistic_map(x, lambd), label='x(n+1) = Lx(n) - x(n)**2')


    xlist = list_creator(x0, lambd, idepth)
    ylist = [xlist[0]]+xlist[:-1]

    for i in range(len(xlist)-1):
        line = plt.plot([xlist[i], xlist[i + 1]], [ylist[i], ylist[i + 1]], color="red")

    plt.xlabel('x_n')
    plt.ylabel('x_n+1')
    plt.title("One-Dimensional Mapping. Logistic map")
    plt.legend()
    plt.show()

#TODO read numpy guide

if __name__=="__main__":
    lambd = 1.3     #float(input("lambd: "))
    idepth = 100    #int(input("depth: "))
    x0 = 0
    plotlogmap(x0,lambd, idepth)