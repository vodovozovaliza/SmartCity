import numpy as np
from numpy import linalg as LA


def leastSquares1(x, y):
    print("\nКласичний метод найменших квадратів\n")
    y.shape = (len(y), 1)
    res = x.transpose().dot(x)
    print("Xt*X\n")
    print(np.around(res, decimals = 3))
    print("\n")
    res = LA.inv(res)
    print("(Xt*X)^(-1)\n")
    print(np.around(res, decimals = 3))
    print("\n")
    res = res.dot(x.transpose())
    print("(Xt*X)^(-1)*Xt\n")
    print(np.around(res, decimals = 3))
    print("\n")
    res = res.dot(y)
    print("(Xt*X)^(-1)*Xt*q\n")
    print(np.around(res, decimals = 3))
    print("\n")
    return res
    #return LA.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)

def leastSquares2(x, y, a, w0):

    print("\nРегуляризований метод найменших квадратів\n")
    print("\nw0: ")
    print(w0)
    print("\nsum w0: ")
    print(np.sum(w0))
    print("\n")
    y.shape = (len(y), 1)
    sz = x.shape
    I = np.identity(sz[1])
    print("\nXt*X\n")
    res = x.transpose().dot(x)
    print(np.around(res, decimals=3))
    print("\n")

    print("I*a + Xt*X\n")
    res = I * a + res
    print(np.around(res, decimals=3))
    print("\n")

    print("(I*a + Xt*X)^(-1)\n")
    res = LA.inv(res)
    print(np.around(res, decimals=3))
    print("\n")

    print("(I*a + Xt*X)^(-1)*Xt\n")
    res = res.dot(x.transpose())
    print(np.around(res, decimals=3))
    print("\n")

    print("(I*a + Xt*X)^(-1)*Xt*q\n")
    res = res.dot(y)
    print(np.around(res, decimals=3))
    print("\n")

    print("(I*a + Xt*X)^(-1)*Xt*q + a*w0\n")
    res = res + a * w0
    res = res[:, 0][:, np.newaxis]
    print(np.around(res, decimals=3))
    print("\n")



    return (LA.inv(I * a + x.transpose().dot(x)).dot(x.transpose()).dot(y) + a * w0)[:,0]
def leastSquares3(x, y, a, w0):
    print("\nРегуляризований метод найменших квадратів  з нормувальними обмеженнями\n")
    y.shape = (len(y), 1)
    m = x.shape[1]
    I = np.identity(m)
    e = np.ones(m).transpose()
    P = I - e.dot(e.transpose()) / m

    print("\nMatrix П\n")
    print(P)

    print("\nXt*X\n")
    res = x.transpose().dot(x)
    print(np.around(res, decimals = 3))
    print("\n")

    print("I*a + Xt*X\n")
    res = I * a + res
    print(np.around(res, decimals = 3))
    print("\n")

    print("(I*a + Xt*X)^(-1)\n")
    res = LA.inv(res)
    print(np.around(res, decimals = 3))
    print("\n")

    print("P*(I*a + Xt*X)^(-1)\n")
    res = P.dot(res)
    print(np.around(res, decimals=3))
    print("\n")

    print("P*(I*a + Xt*X)^(-1)*Xt\n")
    res = res.dot(x.transpose())
    print(np.around(res, decimals=3))
    print("\n")

    print("P*(I*a + Xt*X)^(-1)*Xt*q\n")
    res = res.dot(y)
    print(np.around(res, decimals=3))
    print("\n")

    print("P*(I*a + Xt*X)^(-1)*Xt*q + a*P*w0\n")
    res = res + a*P.dot(w0)
    res = res[:,0][:,np.newaxis]
    print(np.around(res, decimals=3))
    print("\n")

    print("P*(I*a + Xt*X)^(-1)*Xt*q + a*P*w0 + e/m\n")
    res = res + e/m
    res = res[:,0][:,np.newaxis]
    print(np.around(res, decimals=3))
    print("\n")
    return res

    #return (P.dot(LA.inv(I * a + x.transpose().dot(x))).dot(x.transpose()).dot(y) + a * P.dot(w0) + e / m)[:,0]
