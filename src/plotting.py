import numpy as np 
import pandas as pd
from pandas.io import parsers 
from dataframe import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def bar_graph_over_time(ax, df):
    x = range(0, len(df['Year']))
    ax.bar(x, df['Global_Sales'])
    ax.set_xticks(x)
    ax.set_xticklabels(df['Year'])



def multiple_line_graphs(ax, df_dict):
    x = range(0, len(df_dict[next(iter(df_dict))]['Year']))
    for key in df_dict.keys():
        y = df_dict[key]['Global_Sales']
        ax.plot(x, y, label=key)
    ax.set_xticks(x)
    ax.set_xticklabels(df_dict[next(iter(df_dict))]['Year'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Genres')
    ax.set_title('Genre Popularity in Relation to Time')
    ax.legend(loc = 2)



if __name__ == '__main__':
    
    fig, ax_line = plt.subplots(figsize = (12, 4))
    fig, ax_bar = plt.subplots(figsize = (20, 4))
    df = pd.read_csv('../data/cleaned_data.csv')
    df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
    genre_list_year = ['Genre', 'Year']
    platform_list = ['Genre', 'Platform']
    sort_list = [ 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    genres = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle'
                , 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
    interesting_genres = ['Action', 'Shooter', 'Sports', 'Role-Playing', 'Platform']

    # df_platforms = create_dataframe_groupby(df, platform_list, sort_list)
    # df_platforms = df_platforms[df_platforms['Platform']]

    df_global_sales = create_dataframe_groupby(df, ['Year'], ['Global_Sales']).reset_index()
    df_genres_years =  create_dataframe_groupby(df, genre_list_year, sort_list).reset_index()
    df_genres_years = df_genres_years[(df_genres_years['Year'] >= 1995) & (df_genres_years['Year'] < 2016)]
    df_global_sales = df_global_sales[(df_global_sales['Year'] >= 1950) & (df_global_sales['Year'] < 2016)]
    df_genres = df_genres_years.drop('Year', axis=1).groupby('Genre').sum()
    
    
    
    df_genres_years_global_sales = df_genres_years.drop(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], axis = 1)
    genre_dataframes = create_multiple_dataframes(df_genres_years_global_sales, interesting_genres, 'Genre')

    

    multiple_line_graphs(ax_line, genre_dataframes)
    bar_graph_over_time(ax_bar, df_global_sales)
    plt.show()
    
    