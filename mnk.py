import numpy as np
from numpy import linalg as LA
import mai
import pandas as pd
import main
import alpha_graphics


def classic_ls(x, q): # (XtX)^-1*Xt*q
    q.shape = (len(q), 1)
    return LA.inv(x.transpose().dot(x)).dot(x.transpose()).dot(q)


def regularized_ls(x, q, a, w0): # (aI + XtX)^-1*(Xtq+aw0)
    # print('x = \n', x)
    # print('q = \n', q)
    # print('a = \n', a)
    # print('w0 = \n', w0)
    w0.shape = (len(w0), 1)

    m = x.shape[1]
    # print('m = \n', m)
    I = np.eye(m)
    # print('I = \n', I)
    '''
    print('aI = \n', a * I)
    print('XtX = \n', x.transpose().dot(x))
    print('(aI + XtX)^-1 = \n', LA.inv(I * a + x.transpose().dot(x)))
    print('Xtq = \n', x.transpose().dot(q))
    print('aw0 = \n', a * w0)
    print('(Xtq+aw0) = \n', x.transpose().dot(q) + a * w0)
    print('(aI + XtX)^-1*(Xtq+aw0) = \n', LA.inv(I * a + x.transpose().dot(x)).dot(x.transpose().dot(q) + a * w0))
    '''
    return LA.inv(I * a + x.transpose().dot(x)).dot(x.transpose().dot(q) + a * w0)


def limit_ls(x, q, a, w0):
    # print('x = \n', x)
    # print('q = \n', q)
    # print('a = \n', a)
    w0.shape = (len(w0), 1)
    # print('w0 = \n', w0)

    m = x.shape[1]
    # print('m = \n', m)
    e = np.ones(len(w0))
    e.shape = (len(e), 1)
    # print('e = \n', e)
    # print('et*w0 = \n', e.transpose().dot(w0))
    I = np.eye(m)
    # print('I = \n', I)
    # print('aI + XtX = \n', a*I + x.transpose().dot(x))
    P = LA.inv(a*I + x.transpose().dot(x))
    # print('P = \n', P)
    w_val = e.transpose().dot(P).dot(e)
    # print('w_val = ', w_val)
    Pm = I - (1 / w_val) * P.dot(e).dot(e.transpose())
    # print('Pm = \n', Pm)
    # print('et*Pm = \n', e.transpose().dot(Pm))

    return Pm.dot(P).dot(x.transpose().dot(q) + a*w0) + (1/w_val)*P.dot(e)

if __name__ == '__main__':
    df1 = pd.read_csv('testdata.csv')
    df1 = df1.sort_values(by=df1.columns[0])
    df1 = main.minmax_normalization(df1)
    df2 = pd.read_csv('testindicators.csv')
    df2 = df2.sort_values(by=df2.columns[0])
    df2 = main.minmax_normalization(df2)

    a = np.array([
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [2, 2, 1, 1 / 5, 1 / 9, 1 / 9],
        [5, 5, 5, 1, 1 / 5, 1 / 5],
        [9, 9, 9, 5, 1, 1 / 2],
        [9, 9, 9, 3, 2, 1]
    ])

    w = mai.mai(a)
    a_matrix = df1[df1.columns[1:]].to_numpy()
    indicators = df2['Rating'].to_numpy()

    dq = indicators.var(ddof=0)
    coh = mai.coherence(a, w)
    alpha_coef = dq / coh
    # print('X = \n', np.around(a_matrix, 2))
    print('XtX = \n', a_matrix.transpose().dot(a_matrix))
    # print('(XtX)^-1 = \n')
    # print_m(LA.inv(a_matrix.transpose().dot(a_matrix)))
    # print('w0 = \n', w)

    # print("\nКласичний метод найменших квадратів\n")
    w1 = classic_ls(a_matrix, indicators)
    # print('w1 = \n', np.around(w1.transpose(), 3))
    # print('||q-Xw||^2 = \n', (LA.norm(indicators - a_matrix.dot(w1))) ** 2)
    # print('||q-Xw0||^2 = \n', (LA.norm(indicators - a_matrix.dot(w))) ** 2)

    print("\nРегуляризований метод найменших квадратів\n")

    print('alpha = \n', 5)
    w2 = regularized_ls(a_matrix, indicators, 5, w)
    I = np.eye(6)
    # print('I = \n', I)
    print('aI + XtX = \n', 5 * I + a_matrix.transpose().dot(a_matrix))
    P = LA.inv(5 * I + a_matrix.transpose().dot(a_matrix))
    print('P = \n', P)
    print('w2 = \n', np.around(w2, 3))
    print('||q-Xw||^2 = \n', (LA.norm(indicators - a_matrix.dot(w2))) ** 2)
    print('||w0-w||^2 = \n', (LA.norm(w - w2)) ** 2)

    print('alpha = \n', alpha_coef)
    w2 = regularized_ls(a_matrix, indicators, alpha_coef, w)
    I = np.eye(6)
    # print('I = \n', I)
    print('aI + XtX = \n', alpha_coef * I + a_matrix.transpose().dot(a_matrix))
    P = LA.inv(alpha_coef * I + a_matrix.transpose().dot(a_matrix))
    print('P = \n', P)
    print('w2 = \n', np.around(w2, 3))
    print('||q-Xw||^2 = \n', (LA.norm(indicators - a_matrix.dot(w2))) ** 2)
    print('||w0-w||^2 = \n', (LA.norm(w - w2)) ** 2)

    alpha_new = 3.1
    while (True in (w2 < 0)):
        w2 = regularized_ls(a_matrix, indicators, alpha_new, w)
        alpha_new += 0.001

    print('a = ', alpha_new)
    print('w2 = \n', w2)
    print('aI + XtX = \n', alpha_new * I + a_matrix.transpose().dot(a_matrix))
    P = LA.inv(alpha_new * I + a_matrix.transpose().dot(a_matrix))
    print('P = \n', P)
    print('||q-Xw||^2 = \n', (LA.norm(indicators - a_matrix.dot(w2))) ** 2)
    print('||w0-w||^2 = \n', (LA.norm(w - w2)) ** 2)

    print("\nРегуляризований метод найменших квадратів з нормувальними обмеженнями\n")
    w3 = limit_ls(a_matrix, indicators, alpha_coef, w)
    print('w3 = \n', w3)

    alpha_new =69.8
    while (True in (w3 < 0)):
        w3 = limit_ls(a_matrix, indicators, alpha_new, w)
        alpha_new += 0.01
        if (alpha_new == 200):
            break
    print('a = ', alpha_new)
    print('w3 = ', w3)

    alpha_graphics.weight_graphs_mnk(a_matrix, w, indicators)


'''
1/2 * ((q-xw), (q-xw)) -> min
w ≥ 0
1/2 * (q, q) + 1/2 * wtXtXw - (qXt, w)
quadprog(... A = [], B = [], Aeq = [], LB (array) = 0, UB (array) = 0)
(0.037, 0.002, 0.055, 0.208, 0.321, 0.378)
'''