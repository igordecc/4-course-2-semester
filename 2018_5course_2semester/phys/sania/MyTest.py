import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import AKF
import LogMap


if __name__ == '__main__':
    # y = WorkWFiles.write_to_list('RR.txt')
    # ExtendedFunc.do_dfa(y, 1024)
    t = np.linspace(0, 1, 500, endpoint=False)
    x = signal.square(2 * np.pi * 5 * t)
    y = LogMap.do_map()
    plt.plot(y)
    plt.show()
    AKF.do_all_akf(y)
