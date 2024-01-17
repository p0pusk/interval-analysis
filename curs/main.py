import numpy as np
from numpy.linalg import pinv, inv


A = np.matrix([[15, 5, 1], [10, 25, 1]])

M = np.matrix([[1, 2, 0.001], [5, 3, 0.001]])

N = np.matrix([[4, 9, 0.002], [6, 4, 0.002]])

b = np.matrix([10, 20]).transpose()

g = np.matrix([15, 30]).transpose()

h = np.matrix([25, 40]).transpose()


def inv_matrix_solve(
    A: np.matrix, N: np.matrix, M: np.matrix, b: np.matrix, g: np.matrix
):
    print(pinv(A))
    x = pinv(A) * b
    y = pinv(A) * (g - M * x)
    z = pinv(A) * (h - N * x)
    return x, y, z


def read_input():
    print("Input n dimenstion:")
    n = int(input())
    print("Input m dimension:")
    m = int(input())

    for i in range(n):
        for j in range(m):
            print(f"Input a_{i},{j}")
            A[i, j] = float(input())
            print(f"Input alpha_{i},{j}")
            M[i, j] = float(input())
            print(f"Input beta_{i},{j}")
            N[i, j] = float(input())

    for i in range(n):
        print(f"Input b_{i}")
        b[i] = float(input())
        print(f"Input gamma_{i}")
        g[i] = float(input())
        print(f"Input delta_{i}")
        h[i] = float(input())


if __name__ == "__main__":
    # read_input()

    print("==========INPUT===========")
    print("A:")
    print(A)
    print("M:")
    print(M)
    print("N:")
    print(N)
    print("b:")
    print(b)
    print("g:")
    print(g)
    print("h:")
    print(h)
    print("==========RESULT==========")
    x, y, z = inv_matrix_solve(A, N, M, b, g)

    print("x:", x)
    print("y:", y)
    print("z:", z)
