import numpy as np
import math


# calculating HAAR matrices for linear array
def HaarMatrices(n):

    # check input parameter and make sure it's the power of 2
    Level1 = math.log(n, 2)
    Level = int(Level1)+1

    # Initialization,
    H = [1]
    NC = 1 / math.sqrt(2)   # NC - normalization constant
    LP = [1, 1]
    HP = [1, -1]

    # The core of the calculation; H - the result matrix
    for i in range(1, Level):
        H = np.dot(NC, np.concatenate([np.matrix(np.kron(H, LP)), np.matrix(np.kron(np.eye(len(H)), HP))]))
    H = np.array(H)

    return H


# haar transform
def haar_1d(n, x):

    # calculate haar matrices
    H = HaarMatrices(n)

    # create new input parameters
    x = x[0:len(H)]
    n = len(H)

    # calculate HWT
    y = H.dot(x)
    y = np.array(y)

    return y


# haar inverse transform
def haar_1d_inverse(n, y):

    # calculate haar matrices
    H = HaarMatrices(n)

    # create new input parameters
    y = y[0:len(H)]
    n = len(H)

    # calculate HWT
    x1 = H.transpose().dot(y.transpose())
    x1 = np.array(x1)

    return x1.transpose()
import random

n = 256
#u = [i*random.randint(0,1)for i in range(n)]
u = [math.exp(i/10)+random.randint(0,1)/10 for i in range(n)]   # input signal
v = haar_1d(n, u)

w = haar_1d_inverse(n, v)
print(u)
# print(v)
# print(w)
import matplotlib.pyplot as plt
"""
plt.plot(u)
plt.plot(v) # Detalization
plt.plot(w)
plt.grid()
plt.ylabel('u, H(u), H_inv(H(u))')
plt.xlabel('x')
plt.show()

"""
f,a = plt.subplots(1,2)

plt.show()
