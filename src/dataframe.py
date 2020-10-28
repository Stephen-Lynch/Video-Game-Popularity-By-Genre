from os import name
import numpy as np
from numpy.core.fromnumeric import sort 
import pandas as pd 

def create_dataframe_groupby(df, groupby_list, col_list = [], modifier = 'sum' ):
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



        
if __name__ == '__main__':
    df = pd.read_csv('../data/cleaned_data.csv')
    df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
    genre_list_year = ['Genre', 'Year']
    platform_list = ['Genre', 'Platform']
    sort_list = [ 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    genres = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle'
                , 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']

    # df_platforms = create_dataframe_groupby(df, platform_list, sort_list)
    # df_platforms = df_platforms[df_platforms['Platform']]


    df_genres_years =  create_dataframe_groupby(df, genre_list_year, sort_list).reset_index()
    
    df_genres_years = df_genres_years[(df_genres_years['Year'] >= 2000) & (df_genres_years['Year'] < 2013)]
    df_genres = df_genres_years.drop('Year', axis=1).groupby('Genre').sum()
    
    genre_dataframes = create_multiple_dataframes(df_genres_years, genres, 'Genre')

    print(genre_dataframes['Action'])
    

    
    
    
