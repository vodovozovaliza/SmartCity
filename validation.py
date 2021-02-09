import pandas as pd
import pandas_schema
from pandas_schema import Column
from pandas_schema.validation import CustomElementValidation
import numpy as np


def check_float(f):
    """
        :param f: unknown value
        :return: True or False
        :does: checks whether a value is float
    """
    try:
        val = float(f)
    except ValueError:
        return False
    return True


def data_validation(filename):
    """
        :param filename: name of the csv file with data
        :return: dataframe if the data is correct, list of errors
        :does: validates the data in the csv file
    """
    # read the data
    try:
        data = pd.read_csv(filename)
    except Exception:
        return [False, ['Error reading a file.']]
    # check column names
    if (data.columns.to_list() == ['City', 'Cappuccino', 'Cinema', 'Wine', 'Gasoline', 'Avg Rent',
       'Avg Disposable Income']):

        # define validation elements
        decimal_validation = [CustomElementValidation(lambda d: check_float(d),
                                                      'Must be decimal')]
        null_validation = [CustomElementValidation(lambda d: d is not np.nan,
                                                   'Must not be nan')]

        # define validation schema
        schema = pandas_schema.Schema([
                Column('City', null_validation),
                Column('Cappuccino', decimal_validation + null_validation),
                Column('Cinema', decimal_validation + null_validation),
                Column('Wine', decimal_validation + null_validation),
                Column('Gasoline', decimal_validation + null_validation),
                Column('Avg Rent', decimal_validation + null_validation),
                Column('Avg Disposable Income', decimal_validation + null_validation)])

        # apply validation
        errors = schema.validate(data)
        errors_index_rows = [e.row for e in errors]
        data_clean = data.drop(index=errors_index_rows)

        # save data
        # data_clean.to_csv('clean_data.csv')

        if errors is not None and len(errors) == len(data['City']):
            return [False, errors]
        else:
            return [True, data_clean, errors]
    else:
        return [False, ['The criteria names are incorrect.']]

'''
def indicators_validation(filename, df):
    """
        :param filename: name of the csv file with data
        :return: dataframe if the data is correct and the number of errors otherwise
        :does: validates the data in the csv file
    """
    # read the data
    try:
        data = pd.read_csv(filename)
    except Exception:
        return [False, ['Ошибка чтения файла']]

    # check Column names
    if data.columns.to_list() == ['City', 'Rating']:

        # compare city names
        data.sort_values(by=data.columns[0])
        l1 = df['City'].to_list()
        l2 = data['City'].to_list()
        errors1 = [x for x in range(len(l1)) if l1[x] not in l2]
        errors2 = [x for x in range(len(l2)) if l2[x] not in l1]
        df = df.drop(index=errors1)
        data = data.drop(index=errors2)

        # define validation elements
        decimal_validation = [CustomElementValidation(lambda d: check_float(d),
                                                      'Значение должно быть числом в виде десятичной дроби')]
        null_validation = [CustomElementValidation(lambda d: d is not np.nan,
                                                   'Значение не может быть пустым')]

        # define validation schema
        schema = pandas_schema.Schema([
                Column('City', null_validation),
                Column('Rating', decimal_validation + null_validation)])

        # apply validation
        errors = schema.validate(data)
        errors_index_rows = [e.row for e in errors]
        data_clean = data.drop(index=errors_index_rows)

        # save data
        data_clean.to_csv('clean_data.csv')

        if errors is not None and len(errors) == len(data['City']):
            return [False, errors]
        else:
            return [True, data_clean, df, errors]
    else:
        return [False, ['Названия критериев не совпадают.']]
'''


if __name__ == '__main__':
    # true -> df -> lest of errors
    # false -> list of errors
    filename = 'testdata.csv'
    val = data_validation('testindicators.csv')
    if val[0]:
        for error in val[-1]:
            if error.column == 'City':
                print('row: ' + str(error.row) + ', column: City, City name must not be empty.')
            else:
                print('row: ' + str(error.row) + ', column: ' + error.column + ', "' + error.value + '" must be a decimal value.')
