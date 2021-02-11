import numpy as np
import main
import pandas as pd
from numpy import linalg as LA
def leastSquares(a, b):
    b.shape = (len(b), 1)
    # return LA.inv((a.transpose().dot(a))).dot(a.transpose()).dot(b)

    # V = LA.inv((a.dot(a.transpose())) / (a.shape[1] - 1))
    V = np.cov(a)
    return LA.inv(a.transpose().dot(V).dot(a)).dot(a.transpose()).dot(V).dot(b)

if __name__ == '__main__':
    df = pd.read_csv('testdata.csv')
    # df = main.minmax_normalization(df)
    A = df[df.columns[1:]].to_numpy()
    df2 = pd.read_csv('testindicators.csv')
    # df2 = main.minmax_normalization(df2)
    B = df2['Rating'].to_numpy()
    res = leastSquares(A, B)
    print(res)