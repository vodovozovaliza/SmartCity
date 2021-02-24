import numpy as np


def coherence(arr, w):
    """
    :param arr: matrix
    :param w: weights
    :return: coherence of the matrix
    :does: finds the coherence through concordance factor and random index, using the maximum eigenvalue of matrixЯ
    """
    # calculate maximum eigenvalue of matrix
    n = arr[0].size
    p = arr @ w
    p /= w
    lam = p.sum()
    lam /= n

    print('lam: ' + str(lam))
    # calculate concordance factor
    ci = (lam - n) / (n - 1)
    print('ci: ' + str(ci))
    # calculate random index
    ri = 1.98 * (n - 2) / n
    print('ri: ' + str(ri))
    # calculate coherence
    cr = ci / ri
    print('cr: ' + str(cr))
    return cr


def mai(arr):
    """
    :param arr: matrix of pairwise comparisons of features
    :return: a vector that contains weights of features
    :does: normalizes the matrix, calculates the relative weights of indicators
           and then checks if matrix coherence is satisfying
    """
    n = arr[0].size
    init = np.copy(arr)
    # normalize the matrix
    for i in range(n):
        s = 0
        for j in range(n):
            s += init[j][i]
        for j in range(n):
            init[j][i] /= s

    print('Norm. matrix')
    print(init)

    # calculate the relative weights of indicators
    res = np.arange(n, dtype=float)
    for i in range(n):
        res[i] = init[i].sum() / n
    # check if matrix coherence is satisfying
    coh = coherence(arr, res)
    print('MAI.coh: ' + str(coh))
    if coh > 0.1:
        return [-1]
    return res
