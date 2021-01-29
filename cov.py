import numpy as np


def cov1(m):
    return np.cov(m)


def cov2(m):
    mn = np.mean(m, axis=0)
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = m[i][j] - mn[j]
    m = m @ np.transpose(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = m[i][j] / (len(m) - 1)
    return m


def covariation(x, y):
    x_m = np.mean(x)
    y_m = np.mean(y)
    xy_new = np.empty(len(x))
    for i in range(len(x)):
        xy_new[i] = (x[i] - x_m) * (y[i] - y_m)
    return np.mean(xy_new)


def covMatrix(x):
    res = np.empty((len(x), len(x[0])))
    for i in range(len(x)):
        for j in range(len(x)):
            res[i][j] = covariation(x[i], x[j])
    return res


a = np.array([[1, 2, 3], [6, 2, 4], [1, 6, 6]], dtype=float)
a1 = np.copy(a)
a2 = np.copy(a)
a3 = np.copy(a)
print(a1)
print(covMatrix(a3))
print(cov1(a1))
print(cov2(a2))
