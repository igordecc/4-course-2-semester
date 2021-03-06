import numpy as np
import matplotlib.pyplot as plt


def cubic_map(x0, a, b):
    return a - b*x0 + x0**3

def list_creator(x0, a, b, idepth):
    xlist = [cubic_map(x0, a, b)]
    for i in range(idepth):
        xlist.append(cubic_map(xlist[-1], a, b))
        xlist.append(xlist[-1])
    return xlist


def plotlogmap(x0, a, b, idepth):


    x = np.linspace(-1.5, 1.5, 100)
    plt.plot(x, x, label="x(n+1) = x(n)")
    plt.plot(x, cubic_map(x, a, b), label='x(n+1) = a - b*x(n) - x(n)**3')


    xlist = list_creator( x0, a, b, idepth )
    ylist = [xlist[0]]+xlist[:-1]

    for i in range(50,len(xlist)-1):
        line = plt.plot( [ylist[i], ylist[i + 1]], [xlist[i], xlist[i + 1]], color="red")

    plt.xlabel('x_n')
    plt.ylabel('x_n+1')
    plt.title("One-Dimensional Mapping")
    #plt.legend()
    plt.show()

if __name__=="__main__":
    a = .5     #float(input("a: "))
    b = 1.9
    print(a, b)
    idepth = 100    #int(input("depth: "))
    x0 = 0
    plotlogmap(x0, a, b, idepth)