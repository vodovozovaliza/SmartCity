import alpha  # alpha-concordance of weights and indicators
import mai  # calculates the relative weights of indicators
import mnk
import numpy as np
import pandas as pd
import alpha_graphics

# def get_new_weights(data_file='testdata.csv', indicator_file='testindicators.csv',):

ALPHA = 1.03

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
    """
    :does: calculation Total Score
    """
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
    """
    :does: return weigts after MAI and alpha
    """
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

    print()

    # print(a)
    # print(weights)

    coh = mai.coherence(a, weights)
    # sum |A*w - q0|
    # coh = np.absolute((a_matrix * weights).sum(axis=1) - indicators).sum()
    print('coh: ' + str(coh))

    alpha_coef = dq / coh
    print('alpha_coef: ' + str(alpha_coef))

    w_new = alpha.alpha(alpha_coef, a_matrix, weights, indicators)
    print('w_new: ' + str(w_new))
    while True in (w_new < 0):
        alpha_coef += 0.1
        w_new = alpha.alpha(alpha_coef, a_matrix, weights, indicators)
    print(alpha_coef)
    # alpha_graphics.weight_graphs(a_matrix, weights, indicators)
    return w_new

def test_ls(df_data, df_indicator):
    a = np.array([
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [1, 1, 1 / 2, 1 / 5, 1 / 9, 1 / 9],
        [2, 2, 1, 1 / 5, 1 / 9, 1 / 9],
        [5, 5, 5, 1, 1 / 5, 1 / 5],
        [9, 9, 9, 5, 1, 1 / 2],
        [9, 9, 9, 3, 2, 1]
    ])
    w = mai.mai(a)
    a_matrix = df_data[df_data.columns[1:]].to_numpy()
    indicators = df_indicator['Rating'].to_numpy()
    dq = indicators.var(ddof=0)
    coh = mai.coherence(a, w)
    alpha_coef = dq / coh

    print(mnk.classic_ls(a_matrix, indicators))
    print(mnk.regularized_ls(a_matrix, indicators, alpha_coef, w))
    print(mnk.limit_ls(a_matrix, indicators, alpha_coef, w))


if __name__ == '__main__':
    df1 = pd.read_csv('testdata.csv')
    df1 = df1.sort_values(by=df1.columns[0])
    df1 = minmax_normalization(df1)
    df2 = pd.read_csv('testindicators.csv')
    df2 = df2.sort_values(by=df2.columns[0])
    df2 = minmax_normalization(df2)
    res = get_new_weights(df1, df2)
    for weight in res:
        print(weight)
