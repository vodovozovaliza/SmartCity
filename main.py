import alpha  # alpha-concordance of weights and indicators
import mai  # calculates the relative weights of indicators
import LS  # calculates the relative weights of indicators
import numpy as np
import pandas as pd

# def get_new_weights(data_file='testdata.csv', indicator_file='testindicators.csv',):

ALPHA = 0

def minmax_normalization(df):
    """
    :does: normalizez the data for that it numbers are between 0 and 1
    """
    result = df.copy()
    for feature_name in df.columns[1:]:
        # Minimum
        min_value = df[feature_name].min()
        # Maximum
        max_value = df[feature_name].max()

        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


def get_df_res(df_data, weights):
    # Data processing
    df_data['Total score'] = (df_data[df_data.columns[1:]] * weights).sum(axis=1)
    #max_value = df[feature_name].max()
    #df_data['Total score'] = df_data['Total score'] / max_value * 100
    # df_data['Total score'] = (df_data['Total score']- - df_data['Total score'].mean()) / (df_data['Total score'].max() - df_data['Total score'].min()) * 100
    # Sort values by total score
    df_data.sort_values(by='Total score', ascending=True, inplace=True)
    # Reset indedxes after sorrt
    df_data = df_data.reset_index(drop=True)
    return df_data


def get_new_weights(df_data, df_indicator = pd.read_csv("testindicators.csv")):
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
    weights = mai.mai(a)
    # coh = mai.coherence(a, weights)
    # view.show('testdata.csv', weights)

    # quality vector
    df_indicator = df_indicator.sort_values(by=df_indicator.columns[0])

    indicators = df_indicator['Rating']

    # judgment matrix
    df_data = df_data.sort_values(by=df_data.columns[0])
    a_matrix = df_data[df_data.columns[1:]].to_numpy()

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
    # dq = indicators.var(ddof=0)
    print('dq: ' + str(dq))

    # print(a)
    # print(weights)

    coh = mai.coherence(a, weights)
    # sum |A*w - q0|
    # coh = np.absolute((a_matrix * weights).sum(axis=1) - indicators).sum()
    print('coh: ' + str(coh))

    alpha_coef = dq / coh
    ALPHA = alpha_coef
    print('alpha_coef: ' + str(alpha_coef))

    w_new = alpha.alpha(alpha_coef, a_matrix, weights, indicators)
    print('w_new: ' + str(w_new))
    return w_new

    # alpha-concordance
    # alpha_graphics.weight_graphs(a_matrix, weights, indicators)

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

def testLS(df_data, df_indicator):
    a = np.array([
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [2, 2, 1, 1 / 5, 1 / 9, 1 / 9],
        [5, 5, 5, 1, 1 / 5, 1 / 5],
        [9, 9, 9, 5, 1, 1 / 2],
        [9, 9, 9, 3, 2, 1]
    ])
    w = mai.mai(a)
    df_data = df_data.sort_values(by=df_data.columns[0])
    a_matrix = df_data[df_data.columns[1:]].to_numpy()
    df_indicator = df_indicator.sort_values(by=df_indicator.columns[0])
    indicators = df_indicator['Rating'].to_numpy()

    res1 = LS.leastSquares1(a_matrix, indicators)

    alph = ALPHA
    res3 = np.array([-1,-1])
    while True in (res3 < 0):
        print('alpha_coef: ', alph)
        print('w: ' + str(res3))
        alph += 0.01
        res3 = LS.leastSquares3(a_matrix, indicators, ALPHA, w)

    res2 = LS.leastSquares2(a_matrix, indicators, ALPHA, w)
    #res3 = LS.leastSquares3(a_matrix, indicators, ALPHA, w)
    res1 = np.around(res1, decimals = 3)
    res2 = np.around(res2, decimals = 3)
    res3 = np.around(res3, decimals = 3)
    res1.shape = (len(res1), 1)
    res2.shape = (len(res2), 1)
    print("\nRESULT 1:\n")
    print(res1)
    print("\nRESULT 2:\n")
    print(res2)
    print("\nRESULT 3:\n")
    print(res3)

if __name__ == '__main__':
    df1 = pd.read_csv('testdata.csv')
    df1 = minmax_normalization(df1)
    df2 = pd.read_csv('testindicators.csv')
    print(df2)
    df2 = df2.sort_values(by=df2.columns[0])
    print(df2['Rating'].to_numpy())
    df2 = minmax_normalization(df2)
    print(get_new_weights(df1, df2))
    print("LEAST SQUARES\n")
    testLS(df1, df2)