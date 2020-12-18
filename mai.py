import numpy as np
def coherence(arr, w):
    #calculate maximum eigenvalue of matrix
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

def MAI(arr):
    n = arr[0].size
    init = np.copy(arr)
    # normalize the matrix
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[j][i]
        for j in range(n):
            arr[j][i] /= s

    print('Norm. matrix')
    print(arr)

    # calculate the relative weights of indicators
    res = np.arange(n, dtype=float)
    for i in range(n):
        res[i] = arr[i].sum() / n
    # check if matrix coherence is satisfying
    if coherence(init, res) > 0.1:
        return [-1]
    return res

if __name__ == '__main__':
    #initialize data
    a = np.array([[1, 2, 1/3, 1/5, 1/7], [1/2, 1, 1/6, 1/9, 1/9], [3, 6, 1, 1/2, 1/2], [5, 9, 2, 1, 1/2], [7, 9, 2, 2, 1]])
    #print initial data
    print(a)
    #print resulting data
    print(MAI(a))