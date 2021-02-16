import numpy as np
from numpy import linalg as LA

def leastSquares1(x, y):
    y.shape = (len(y), 1)
    return LA.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)
def leastSquares2(x, y, a, w0):
    y.shape = (len(y), 1)
    sz = x.shape
    I = np.identity(sz[1])
    return (LA.inv(I * a + x.transpose().dot(x)).dot(x.transpose()).dot(y) + a * w0)[:,0]
def leastSquares3(x, y, a, w0):
    y.shape = (len(y), 1)
    m = x.shape[1]
    I = np.identity(m)
    e = np.ones(m).transpose()
    P = I - e.dot(e.transpose()) / m
    return (P.dot(LA.inv(I * a + x.transpose().dot(x))).dot(x.transpose()).dot(y) + a * P.dot(w0) + e / m)[:,0]
