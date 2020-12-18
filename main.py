import alpha
import mai
import positiveNorm
import view
import numpy as np
import pandas as pd
import alpha_graphics
import matplotlib.pyplot as plt

# test data
a = np.array([
    [1, 1, 1/2, 1/5, 1/9, 1/9],
    [1, 1, 1/2, 1/5, 1/9, 1/9],
    [2, 2, 1, 1/5, 1/9, 1/9],
    [5, 5, 5, 1, 1/5, 1/5],
    [9, 9, 9, 5, 1, 1/2],
    [9, 9, 9, 3, 2, 1]
    ])

# relative weights
weights = mai.MAI(a)

view.show('movehubcostofliving.csv', weights)

# quality vector
df = pd.read_csv('movehubqualityoflife.csv')
df = view.minmax_normalization(df)
df = df.sort_values(by=df.columns[0])
indicators = df['Movehub Rating']

# judgment matrix
df = pd.read_csv('movehubcostofliving.csv')
df = view.minmax_normalization(df)
df = df.sort_values(by=df.columns[0])
a_matrix = df[df.columns[1:]].to_numpy()

# alpha-concordance
alpha_graphics.weight_graphs(a_matrix, weights, indicators)

dict = {}
for i in range(101):
    a = float(i / 100)
    dict[a] = alpha.alpha(a, a_matrix, weights, indicators)
min_value = dict[0]
min_alpha = 0
for i in range(101):
    alpha = float(i / 100)
    if (dict[alpha] < min_value):
        min_value = dict[alpha]
        min_alpha = alpha
lists = (dict.items())
x, y = zip(*lists)

plt.plot(x, y)
plt.show()