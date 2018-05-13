import numpy as np

thearray = np.ndarray((3, 2, 2))
thearray.ndim #= 3
thearray.shape #= (3, 2, 2)
assert thearray.size #== 3*2*2
thearray.dtype = np.float64
assert thearray.itemsize == 8 #Itemsize count in in bytes. float 64 has itemsize=64/8=8

