import matplotlib.pyplot as plt
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties


# console output result of wavelet transform
def console_output(signal, wt, invwt):
    size = []
    for i in signal, wt, invwt:
        size.append(len(i))
    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(min(size)):
        print('  %2d  %10f  %10f  %10f' % (i, signal[i], wt[i], invwt[i]))


# output result of wavelet transform to txt file
def file_output(filename, signal, wt, invwt):
    size = []
    for i in signal, wt, invwt:
        size.append(len(i))
    f = open(filename, 'w')
    f.write('   i      U(i)        H(U)(i)  Hinv(H(U))(i)' + '\n')
    f.write('\n')
    for i in range(min(size)):
        f.write('  %2d  %10f  %10f  %10f' % (i, signal[i], wt[i], invwt[i]) + '\n')
    f.close()


# save results as png format
def plot_wt(type_signal="none", type_transform="none", *args):
    for i in args:
        plt.plot(i)
    grid(True)
    plt.title(type_signal + " signal WT")
    figure(1, figsize=(10, 8))
    xlabel('$Argument, x$')
    plt.ylabel('$Functions, u$')
    legend(('u(x)', 'H(u(x))', 'Hinv(H(u))(x)'), prop=FontProperties(size=12))
    savefig('pics/' + type_signal + '_' + type_transform + '.png', dpi=150)
    plt.clf()


# 1d array output to file
def write_to_file(array, filename):
    f = open(filename, 'w')
    for index in array:
        f.write(str(index) + '\n')
    f.close()


# 1d array input from file
def write_to_list(f):
    data_list = list()
    with open(f, "r") as file:
        for line in file:  # file.readlines()
            data_list = data_list + list(map(float, line.split()))
    return(data_list)
