from os import name
import numpy as np
from numpy.core.fromnumeric import sort 
import pandas as pd 

def create_dataframe_groupby(df, groupby_list, col_list = [], modifier = 'sum' ):
    '''
    
    '''
    if modifier == 'sum':
        if col_list == []:
            return df.groupby(groupby_list).sum()
        else:
            return df.groupby(groupby_list)[col_list].sum()
    elif modifier == 'max':
        if col_list == []:
            return df.groupby(groupby_list).max()
        else:
            return df.groupby(groupby_list)[col_list].max()
    elif modifier == 'min':
        if col_list == []:
            return df.groupby(groupby_list).min()
        else:
            return df.groupby(groupby_list)[col_list].min()
    elif modifier == 'max':
        if col_list == []:
            return df.groupby(groupby_list).max()
        else:
            return df.groupby(groupby_list)[col_list].max()
    elif modifier == 'count':
        if col_list == []:
            return df.groupby(groupby_list).count()
        else:
            return df.groupby(groupby_list)[col_list].count()

def create_multiple_dataframes(df, sort_list, sort):
    d = {}
    for item in sort_list:
        d[item] = df[df[sort] == item]
    return d  