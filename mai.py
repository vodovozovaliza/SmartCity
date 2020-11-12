def coherence(arr, w):
    n = len(arr[0])
    p = [0 for i in range(n)]
    for i in range(n):
        p[i] = 0
        for j in range(n):
            p[i] += arr[i][j] * w[j]
    for i in range(n):
        p[i] /= w[i]
    lam = 0
    for i in range(n):
        lam += p[i]
    lam /= n
    ci = (lam - n) / (n - 1)
    ri = 1.98 * (n - 2) / n
    cr = ci / ri
    return cr

def MAI(arr):
    n = len(arr[0])
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[j][i]
        for j in range(n):
            arr[j][i] /= s
    res = [0 for i in range(n)]
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[i][j]
        s /= n
        res[i] = s
    coh = coherence(arr, res)
    if coh > 0.1:
        return [-1]
    return res

if __name__ == '__main__':
    a = [[1, 2, 1/3, 1/5, 1/7], [1/2, 1, 1/6, 1/9, 1/9], [3, 6, 1, 1/2, 1/2], [5, 9, 2, 1, 1/2], [7, 9, 2, 2, 1]]
    sz = len(a)
    for i in range(sz):
        print(a[i])
    res = [0 for i in range(sz)]
    res = MAI(a)
    print(res)
    