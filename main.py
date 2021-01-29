import alpha  # alpha-concordance of weights and indicators
import mai  # calculates the relative weights of indicators
import numpy as np
import pandas as pd

# def get_new_weights(data_file='testdata.csv', indicator_file='testindicators.csv',):


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
    # Sort values by total score
    df_data.sort_values(by='Total score', ascending=True, inplace=True)
    # Reset indedxes after sorrt
    df_data = df_data.reset_index(drop=True)
    return df_data


def get_new_weights(df_data, df_indicator):
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

if __name__ == '__main__':
    df1 = pd.read_csv('testdata.csv')
    df1 = minmax_normalization(df1)
    df2 = pd.read_csv('testindicators.csv')
    #df2 = minmax_normalization(df2)
    print(get_new_weights(df1, df2))