import alpha # alpha-concordance of weights and indicators
import mai # calculates the relative weights of indicators
import view # displays the diagram of indicators
import numpy as np
import pandas as pd

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
coh = mai.coherence(a, weights)
#view.show('testdata.csv', weights)

# quality vector
df = pd.read_csv('testindicators.csv')
df = df.sort_values(by=df.columns[0])
#
df = view.minmax_normalization(df)
#
indicators = df['Movehub Rating']

# judgment matrix
df = pd.read_csv('testdata.csv')
df = view.minmax_normalization(df)
df = df.sort_values(by=df.columns[0])
a_matrix = df[df.columns[1:]].to_numpy()

# normalize indicators
indicators_norm = np.copy(indicators)
print('indicators')
print(indicators)

n = indicators_norm.size
'''s = 0
for i in range(n):
    s += indicators_norm[i]
for i in range(n):
    indicators_norm[i] /= s'''

mn = indicators_norm.min()
mx = indicators_norm.max()
for i in range(n):
    indicators_norm[i] = (indicators_norm[i] - mn) / (mx - mn)

print('indicators_norm')
print(indicators_norm)

dq = indicators_norm.var(ddof=0)
#dq = indicators.var(ddof=0)
print('dq: ' + str(dq))

#print(a)
#print(weights)

coh = mai.coherence(a, weights)
# sum |A*w - q0|
#coh = np.absolute((a_matrix * weights).sum(axis=1) - indicators).sum()
print('coh: ' + str(coh))

alpha_coef = dq / coh
print('alpha_coef: ' + str(alpha_coef))

sys.exit()

w_new = alpha.alpha(alpha_coef, a_matrix, weights, indicators)
print('w_new: ' + str(w_new))

# alpha-concordance
#alpha_graphics.weight_graphs(a_matrix, weights, indicators)

'''
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
'''