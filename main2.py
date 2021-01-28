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
a = np.matrix([[1,2,3],[6,2,4],[1,6,6],[5,5,1]], dtype = float)
print(a)
print(cov1(a))
print(cov2(a))
