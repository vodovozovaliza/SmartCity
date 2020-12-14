import alpha
import mai
import view
import numpy as np
import pandas as pd
import alpha_graphics
import matplotlib.pyplot as plt

# Allin test data
a = np.array([
    [1, 1, 1/2, 1/5, 1/9, 1/9],
    [1, 1, 1/2, 1/5, 1/9, 1/9],
    [2, 2, 1, 1/5, 1/9, 1/9],
    [5, 5, 5, 1, 1/5, 1/5],
    [9, 9, 9, 5, 1, 1/2],
    [9, 9, 9, 3, 2, 1]
    ])

for i in range(len(a)):
    print(a[i])

def round_(a):
    return round(a, 2)

# вектор весов
weights = mai.MAI(a)
print('weights ')
print(weights)

#view.show('movehubcostofliving.csv', weights)

#weights_round = weights
#weights_round = list(map(round_, weights_round))
#print('weights_rounded: ')
#print(weights_round)
#view.show('movehubcostofliving.csv', weights)
#alpha.alpha('movehubcostofliving.csv', weights)

# вектор оценок
df = pd.read_csv('movehubqualityoflife.csv')
df = view.normalize(df)
df = df.sort_values(by=df.columns[0])
#print('df: ')
#print(df)
indicators = df['Movehub Rating']
print('indicators: ')
print(str(indicators))

pd.set_option('display.max_columns', 300)
pd.set_option('display.max_rows', 300)

#indicators_round = indicators
#indicators_round = map(lambda x: round(x, 2), indicators_round)
#print('indicators_rounded: ')
#print(list(indicators_round))

#sys.exit()

# Матрица оценок
df = pd.read_csv('movehubcostofliving.csv')
df = view.normalize(df)
df = df.sort_values(by=df.columns[0])
#print('df: ')
#print(df)
a_matrix = df[df.columns[1:]].to_numpy()

#sys.exit()

print("alpha start")
#print(alpha.alpha(0.5, a_matrix, weights, indicators))
alpha_graphics.weight_graphs(a_matrix, weights, indicators)

sys.exit()

dict = {}
for i in range(101):
    a = float(i / 100)
    dict[a] = alpha.alpha(a, a_matrix, weights, indicators)
print(dict)
min_value = dict[0]
min_alpha = 0
for i in range(101):
    alpha = float(i / 100)
    if (dict[alpha] < min_value):
        min_value = dict[alpha]
        min_alpha = alpha
print(min_alpha)
print(min_value)
lists = (dict.items())
x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()

# print(alpha.alpha(0.5, a_matrix, weights, indicators))
