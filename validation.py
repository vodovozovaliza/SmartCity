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
            for e in errors:
                if e.column != 'City':
                    data_clean[e.column] = pd.to_numeric(data_clean[e.column])
            return [True, data_clean, errors]
    else:
        return [False, ['The criteria names are incorrect.']]

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
