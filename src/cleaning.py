import numpy as np 
import pandas as pd 



def check_for_nulls(df, columns):
    '''
    Checks for null values inside of a dataset and will tell you how many nulls
    are in each column.

    ARGS:
        df - dataframe
        columns - index of columns
    RETURN:
        Print statement with columns listed that have null values if there are any.
    '''

    true_values = {}
    for col in columns:
        true_values[col] = df[col].isnull().sum()
    return true_values

def show_nulls(df):
    '''
    Shows the rows with null values to get a better picture at what needs to be fixed.

    ARGS:
        df - dataframe
    RETURNS
        dataframe which only has rows with null values
    '''

    is_NaN = df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    return df[row_has_NaN].head(25)

def replace_null_values(df, column, phrase):
    '''
    Allows you to replace the null values inside of a column with whatever you would like.

    ARGS:
        df- dataframe
        column - dataframe column name as str
        phrase - string
    RETURNS:
        dataframe with null values inside of column replaced
    '''

    df = df[column].fillna(phrase, inplace = True)

def replace_floats_with_int(df, column):
    '''
    Allows you to replace floats of a column if you would rather they would be intergers.

    ARGS:
        df - dataframe
        column - dataframe column name as str
    RETURNS:
        dataframe with given row converted to integer
    '''

    df[column] = df[column].astype(int)

def user_input_replace_rows(df, first_column,  search_column, search, trials=10):
    '''
    Allows you to manually enter new data into a column.

    ARGS:
        df - dataframe
        column - dataframe column name as str
        search - int, or string that you want to search for in column
        trials - Amount of rows you want to search as int
    RETURN:
        dataframe with rows updated with manually entered data
    '''

    for index in df[df[search_column] == search].head(trials).index:
        data = input("{} {} ".format(df.loc[index, first_column], search))
        df.loc[index, search_column] = data
    

if __name__ == '__main__':
    df = pd.read_csv('../data/vgsalesGlobale.csv')
    replace_null_values(df, 'Publisher', "Unkown")
    replace_null_values(df, 'Year', 0)
    replace_floats_with_int(df, 'Year')
    df.to_csv('cleaned_data.csv', index=False)
    

