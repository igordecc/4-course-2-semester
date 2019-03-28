import numpy as np
coord = np.dtype([
    ("x", int),
    ("y", np.int64),
    ("z", np.float64),
])
# a1 = np.zeros(10, dtype=coord)
a2 = np.linspace(0,10,100, dtype=coord)

print(a2)