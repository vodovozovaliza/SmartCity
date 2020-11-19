def coherence(arr, w):
    #calculate maximum eigenvalue of matrix
    n = len(arr[0])
    p = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            p[i] += arr[i][j] * w[j]
    for i in range(n):
        p[i] /= w[i]
    lam = 0
    for i in range(n):
        lam += p[i]
    lam /= n
    #calculate concordance factor
    ci = (lam - n) / (n - 1)
    #calculate random index
    ri = 1.98 * (n - 2) / n
    #calculate coherence
    cr = ci / ri
    return cr

def MAI(arr):
    n = len(arr[0])
    #normalize the matrix
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[j][i]
        for j in range(n):
            arr[j][i] /= s
    #calculate the relative weights of indicators
    res = [0 for i in range(n)]
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[i][j]
        s /= n
        res[i] = s
    #check if matrix coherence is satisfying
    coh = coherence(arr, res)
    if coh > 0.1:
        return [-1]
    return res

if __name__ == '__main__':
    #initialize data
    a = [[1, 2, 1/3, 1/5, 1/7], [1/2, 1, 1/6, 1/9, 1/9], [3, 6, 1, 1/2, 1/2], [5, 9, 2, 1, 1/2], [7, 9, 2, 2, 1]]
    sz = len(a)
    #print initial data
    for i in range(sz):
        print(a[i])
    res = MAI(a)
    #print resulting data
    print(res)
    