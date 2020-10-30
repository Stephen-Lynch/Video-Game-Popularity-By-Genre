from os import name
import numpy as np
from numpy.core.fromnumeric import sort 
import pandas as pd 



def df_group(df, groupby, col = [], mod = 'sum' ):
    '''
    Creates a groupby dataframe and changes modifier based on mod

    ARGS:
        df - dataframe
        groupby - string or list of strings
        col - string or list of strings
        mod - string
    RETURNS:
        dataframe grouped by groupby list, modified by sum 
    '''

    if mod == 'sum':
        if col == []:
            return df.groupby(groupby).sum()
        else:
            return df.groupby(groupby)[col].sum()
    elif mod == 'max':
        if col == []:
            return df.groupby(groupby).max()
        else:
            return df.groupby(groupby)[col].max()
    elif mod == 'min':
        if col == []:
            return df.groupby(groupby).min()
        else:
            return df.groupby(groupby)[col].min()
    elif mod == 'max':
        if col == []:
            return df.groupby(groupby).max()
        else:
            return df.groupby(groupby)[col].max()
    elif mod == 'count':
        if col == []:
            return df.groupby(groupby).count()
        else:
            return df.groupby(groupby)[col].count()

def drop_col(df, col, groupby = []):
    '''
    Drops a column and groups by sum if needed (Need to add more modifiers later).
    
    ARGS:
        df - dataframe
        col - dataframe column
        groupby - string or list of strings
    RETURNS:
        dataframe with dropped column and grouped by if needed
    '''

    if groupby == []:
        new_df = df.drop(col, axis=1)
    else:
        new_df = df.drop(col, axis=1).groupby(groupby).sum()
    return new_df

def df_dict(df, key, col):
    '''
    Creates a dictionary for values within a column in a df 
    based on sort_list (values) and sort (column).

    ARGS:
    df - dataframe
    val - list of strings
    col - string or list of strings

    RETURNS:
    Dictionary with keys linked with their respective dataframes
    '''
    d = {}
    for item in key:
        d[item] = df[df[col] == item]
    return d  

