import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

dpi = 80

def show(input_filename, weights):

    df = pd.read_csv(input_filename)
    columns = []
    for i in df:
        columns.append(i)
    n = len(columns)

    #data = [['Kharkiv', 8652], ['Kiev', 9124], ['Odessa', 7592]]
    data = []
    for i in range(len(df[columns[0]])):
        kpi = 0
        for j in range(1, n):
            kpi += weights[j-1] * df[columns[j]][i]
        data.append([df[columns[0]][i], kpi])

    data = sorted(data, key=lambda a: a[1])

    data_names = []
    data_values = []
    for i in data:
        data_names.append(i[0])
        data_values.append(i[1])

    mpl.rcParams.update({'font.size': 9})
    _, ax = plt.subplots(dpi = dpi, figsize = (512 / dpi, 384 / dpi), num = 'Test')
    ax.xaxis.grid(True, zorder = 1)
    ax.set_title('Test')
    xs = range(len(data_values))

    plt.barh([x for x in xs], data_values,
            height = 0.2, color = 'blue', alpha = 0.7, label = 'KPI',
            zorder = 2)
    plt.yticks(xs, data_names, rotation = 10)

    plt.legend(loc='upper right')
    plt.savefig('result.png')
    plt.show()

if __name__ == '__main__':
    #show('movehubcostofliving.csv', [0.1, 0.1, 0.1, 0.2, 0.2, 0.4])
    show('test.csv', [0.1, 0.1, 0.1, 0.2, 0.2, 0.4])