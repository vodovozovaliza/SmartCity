import numpy as np

def alpha(a, matrix_A, w0, q0):
    """
    :param a: alpha coefficient
    :param matrix_A: the matrix
    :param w0: weights
    :param q0: indicator
    :return: new, more accurate weights
    """
    m = w0.size
    n = q0.size
    print('alpha')

    I_n = np.identity(n)

    P_m = np.identity(m) - (1 / m) * np.ones(m).dot(np.ones(m))

    Psi_n = matrix_A.dot(P_m).dot(matrix_A.transpose())
    P_n = a * I_n + Psi_n

    w_new = w0 + P_m.dot(matrix_A.transpose()).dot(np.linalg.inv(P_n)).dot(q0 - matrix_A.dot(w0))
    print('w_new: ' + str(w_new))
    q_new = matrix_A.dot(w0) + Psi_n.dot(np.linalg.inv(P_n)).dot(q0 - matrix_A.dot(w0))

    return w_new
