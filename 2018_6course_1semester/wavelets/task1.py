# Haar DWT
# TODO how to create Haar matrix

import numpy as np
import math


def HaarMatrices(n):
    # check input parameter and make sure it's the power of 2
    Level1 = math.log(n, 2)
    Level = int(Level1)+1

    #Initialization
    H = [1]
    normalization_constant = 1 / math.sqrt(2)
    LP = [1, 1]
    HP = [1, -1]
    # TODO examplain this awkward part


    for i in range(1, Level):
        H = np.dot(normalization_constant,
                   np.concatenate(
                       [np.matrix(np.kron(H, LP)),
                        np.matrix(np.kron(np.eye(len(H)),
                                          HP
                                          )
                                  )
                        ]
                    )
                   )
    return H


def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16]
    n = len(x)
    H = HaarMatrices(n)

    # haar transformation
    y = H.dot(x)
    print(y)

    # haar inverse transform
    x1 = H.transpose().dot(y.transpose())
    print(x1.transpose())


if __name__ == "__main__":
    main()