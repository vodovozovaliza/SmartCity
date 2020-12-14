import numpy as np

def alpha(a, matrix_A, w0, q0):
    m = w0.size
    n = q0.size
    print('alpha')

    e_vec = np.ones(m)

    I_m = np.identity(m)

    I_n = np.identity(n)

    P_m = I_m - (1 / m) * e_vec.transpose() * e_vec

    Psi_n = matrix_A.dot(P_m).dot(matrix_A.transpose())
    P_n = I_n.dot(a) + Psi_n

    w_new = w0 + P_m.dot(matrix_A.transpose()).dot(np.linalg.inv(P_n)).dot(q0 - matrix_A.dot(w0))
    print('w_new: ' + str(w_new))
    q_new = matrix_A.dot(w0) + Psi_n.dot(np.linalg.inv(P_n)).dot(q0 - matrix_A.dot(w0))
    #print('q_new:' + str(q_new))
    return w_new