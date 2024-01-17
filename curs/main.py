import numpy as np
from numpy.linalg import pinv, inv


A = np.matrix([[0.4, 0.2, 0.6], [0.5, 0.7, 0.2]])

M = np.matrix([[0.01, 0.017, 0.05], [0.03, 0.02, 0.03]])

N = np.matrix([[0.02, 0.03, 0.02], [0.03, 0.02, 0.04]])

b = np.matrix([[2], [3]])

g = np.matrix([[1], [2]])

h = np.matrix([[2], [1.5]])

if __name__ == "__main__":
    print(pinv(A))
    print(b)
    x = pinv(A) * b
    y = pinv(A) * (g - M * x)
    z = pinv(A) * (h - N * x)

    # X = np.matrix([x, y, z])

    print("x:", x)
    print("y:", y)
    print("z:", z)
