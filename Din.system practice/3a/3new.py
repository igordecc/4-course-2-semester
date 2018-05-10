from matplotlib import pyplot as plt
from matplotlib import transforms as trns
import numpy as np

#карта динамических режимов

def logistic_map(x0, a, b):
    return a - b*x0 + x0**3

def final_point(x0, a, b, additional_points=100, N=1000):
    for i in range(N-additional_points):
        x0 = logistic_map(x0, a, b)

    x0_additional_points = []
    for i in range(additional_points):
        x0 = logistic_map(x0, a, b)
        x0_additional_points.append(x0)

    return x0_additional_points


def make_array(x0, a, b, ap):
    a = np.arange(*a, dtype=np.float64)
    b = np.arange(*b, dtype=np.float64)
    abmap = [ [final_point(x0, i, j, ap) for j in b] for i in a]
    return np.array(abmap) #.shape((a.__len__(), b.__len__(), -1))

def interpret_map(abmap):
    colormap = [[len(set(j)) for j in i] for i in abmap]
    #abmap = [set(j, 4) for j in for i in abmap] # remove duplicates
    #colormap = len()
    return colormap

#TODO 1 read how to make color map, please (matplotlib)
#TODO СТЯНИ ПЕРЕД РАБОТОЙ
#TODO 2 find "кубическое уравнение" in a book

#todo 1a make a,b axies
#todo 1b make collor conture map ///////
#todo 1bb manage collor conture map ///////
#todo 1c turn the map to 90 degrees



if __name__=="__main__":
    x0 = 0
    a = (-0.6, 0.6, 0.04)
    b = (0.8, 2.5, 0.04)
    abmap = make_array(x0, a, b, ap=20)
    colormap = interpret_map(abmap)
    #contour = plt.contour(colormap)
    #plt.get_cmap('inferno')

    #NUMPY TRANSFORM
    colormap = np.matrix.transpose(np.array(colormap))
    pcm = plt.pcolormesh(colormap)#, color=(0.1,0.1,0.1))
    #pcm = plt.pcolormesh(rot+base)
    #pcm.set_color(((0.8,0.1,0.1), (0.1,0.1,0.8)))
    ###plt.xticks(np.arange(0, 42, 3.5), np.arange(-0.6, 0.6, 0.1))
    ###plt.yticks(np.arange(0, 35, 2), np.arange(0.8, 2.5, 0.1))
    plt.autoscale()

    plt.figure().add_axes(np.arange(-0.6, 0.6, 0.3) )

    #im = plt.pcolormesh(np.arange(100).reshape((10, 10)))
    #plt.colorbar(im)
    ####plt.axes().
    #plt.plot(transform=rot)
    plt.show()