import numpy as np
def cov1(M):
    return np.cov(M)
def cov2(M):
    mn = np.mean(M, axis = 0)
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = M[i][j] - mn[j]
    M = M @ np.transpose(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = M[i][j] / (len(M) - 1)
    return M
def covariation(x, y):
    x_m = np.mean(x);
    y_m = np.mean(y);
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
a = np.array([[1,2,3],[6,2,4],[1,6,6]], dtype = float)
a1 = np.copy(a)
a2 = np.copy(a)
a3 = np.copy(a)
print(a1)
print(covMatrix(a3))
print(cov1(a1))
print(cov2(a2))
