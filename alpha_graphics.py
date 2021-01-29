import alpha
import matplotlib.pyplot as plt


def weight_graphs(matrix_a, weights, q0):
    """
    :param q0: zero-coordinate on alpha
    :return: nothing
    :does: displays a graph of the dependence of weights
    """
    w_a = []
    for i in range(len(weights)):
        w_a.append({})

    for i in range(1, 101):
        a = float(i / 100)
        w_new = alpha.alpha(a, matrix_a, weights, q0)
        for j in range(len(w_new)):
            w_a[j][a] = w_new[j]

    figure = plt.figure(dpi=100, figsize=(1980 / 100, 1080 / 100))
    for j in range(len(weights)):
        ax = figure.add_subplot(len(weights) / 2, len(weights) - (len(weights) / 2), j+1)
        ax.set_title('W' + str(j))

        lists = (w_a[j].items())
        # print(lists)
        x, y = zip(*lists)
        ax.scatter(x, y)

    plt.savefig('result_100.png')
    plt.show()