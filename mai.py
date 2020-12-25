import numpy as np
def coherence(arr, w):
    """
    :param arr: matrix
    :param w: weights
    :return: coherence of the matrix
    :does: finds the coherence through concordance factor and random index, using the maximum eigenvalue of matrixЯ
    """
    #calculate maximum eigenvalue of matrix
    n = arr[0].size
    p = arr @ w
    p /= w
    lam = p.sum()
    lam /= n

    #p = np.linalg.eigvals(arr)
    #print('p')
    #print(p)
    #lam = p[0]
    #for i in p:
    #    lam = max(lam, i)

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

def MAI(arr):
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
    #if coherence(init, res) > 0.1:
    coh = coherence(arr, res)
    print('MAI.coh: ' + str(coh))
    if coh > 0.1:
        return [-1]
    return res
'''
if __name__ == '__main__':
    #initialize data
    a = np.array([[1, 2, 1/3, 1/5, 1/7], [1/2, 1, 1/6, 1/9, 1/9], [3, 6, 1, 1/2, 1/2], [5, 9, 2, 1, 1/2], [7, 9, 2, 2, 1]])
    #print initial data
    print(a)
    #print resulting data
    print(MAI(a))
'''