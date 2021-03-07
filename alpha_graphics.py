import alpha
import matplotlib.pyplot as plt
import mnk

def weight_graph(matrix_a, weights, q0):
    """
    :param q0: zero-coordinate on alpha
    :return: nothing
    :does: displays a graph of the dependence of weights
    """
    plt.rcParams.update({'font.size': 22})
    w_a = []
    for i in range(len(weights)):
        w_a.append({})
    w_a.append({})

    for i in range(1, 1001):
        a = float(i / 100)
        w_new = alpha.alpha(a, matrix_a, weights, q0)
        """
        w_new = []
        w_mnk = mnk.regularized_ls(matrix_a, q0, a, weights)
        for elem in w_mnk:
            w_new.append(elem[0])
        """
        for j in range(len(w_new)):
            w_a[j][a] = w_new[j]

        w_a[len(weights)][a] = 0
    # figure = plt.figure(dpi=100, figsize=(1980 / 100, 1080 / 100))
    figure, ax = plt.subplots(dpi=100, figsize=(1980 / 100, 1080 / 100))
    plt.xlim(0, 10)
    plt.xticks(range(11))
    ax.grid(which='major', color='k')

    # ax.set_title('W' + str(j))

    ax_colors = ["red", "blue", "green", "orange", "yellow", "pink", "black"]
    ax_labels = ["w1", "w2", "w3", "w4", "w5", "w6", "Ox"]

    for j in range(len(weights) + 1):
        # ax = figure.add_subplot(len(weights) / 2, len(weights) - (len(weights) / 2), j+1)
        # ax.set_title('W' + str(j))

        lists = (w_a[j].items())
        # print(lists)
        x, y = zip(*lists)
        ax.scatter(x, y, c=ax_colors[j], label=ax_labels[j])

    ax.legend(loc='upper right', prop={'size': 20})
    plt.savefig('result.png')
    plt.show()