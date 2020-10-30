import numpy as np 
import pandas as pd
from pandas.io import parsers 
from dataframe import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def drop_col(df, col, groupby = [], mod =sum):
    if groupby == []:
        new_df = df.drop(col, axis=1)
    else:
        new_df = df.drop(col, axis=1).groupby(groupby).sum()
    return new_df

def multi_bar_graph(ax, df, stack=False):
    x = range(0, len(df['']))
    pass
def bar_graph_over_time(ax, df):
    x = range(0, len(df['Year']))
    ax.bar(x, df['Global_Sales'])
    ax.set_xticks(x)
    ax.set_xticklabels(df['Year'])

def multiple_line_graphs(ax, df_dict, x_col, y_col):
    '''
    Creates a 
    '''
    x = range(0, len(df_dict[next(iter(df_dict))][x_col]))
    for key in df_dict.keys():
        y = df_dict[key][y_col]
        ax.plot(x, y, label=key)
    ax.set_xticks(x)
    ax.set_xticklabels(df_dict[next(iter(df_dict))][x_col])
    ax.set_xlabel('Year', fontsize = 16)
    ax.set_ylabel('# of Global Sales In The Millions', fontsize = 16)
    ax.set_title('Genre Popularity in Relation to Time', fontsize = 18)
    ax.legend(loc = 2)
    fig.tight_layout()
    plt.savefig('gen_over_time')


if __name__ == '__main__':
    fig, ax_line = plt.subplots(figsize = (18, 4))
    # fig, ax_bar = plt.subplots(figsize = (20, 4))
    
    df = pd.read_csv('../data/cleaned_data.csv')
    df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
    genre_list_year = ['Genre', 'Year']
    platform_list = ['Platform']
    sort_list = [ 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    genres = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle'
                , 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
    interesting_genres = ['Action', 'Shooter', 'Sports', 'Role-Playing', 'Platform']



    # df_platforms = create_dataframe_groupby(df, platform_list, sort_list)
    # df_platforms = df_platforms[df_platforms['Platform']]

    df_global_sales = create_dataframe_groupby(df, ['Year'], ['Global_Sales']).reset_index()
    df_genres_years =  create_dataframe_groupby(df, genre_list_year, sort_list).reset_index()
    df_genres_platform = create_dataframe_groupby(df, platform_list, sort_list).reset_index()


    df_genres_years_1 = df_genres_years[(df_genres_years['Year'] >= 2010) & (df_genres_years['Year'] < 2018)]
    df_genres_years = df_genres_years[(df_genres_years['Year'] >= 1991) & (df_genres_years['Year'] < 2016)]
    df_global_sales = df_global_sales[(df_global_sales['Year'] >= 1950) & (df_global_sales['Year'] < 2016)]

    df_genres = df_genres_years_1.drop(['Year', 'Global_Sales'], axis=1).groupby('Genre').sum()


    df_genres_platform = df_genres_platform[(df_genres_platform['Platform'] == 'XOne') | (df_genres_platform['Platform'] == 'PS4') | (df_genres_platform['Platform'] == 'WiiU')]
    df_genres_platform = drop_col(df_genres_platform, ['Global_Sales'])
    # df_genres_platform = df_genres_platform.set_index('Platform')
    # df_genres_platform.plot.bar(stacked = True)

    
    # df_genres.plot.bar()

    df_genres_years_global_sales = df_genres_years.drop(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], axis = 1)
    genre_dataframes = create_multiple_dataframes(df_genres_years_global_sales, interesting_genres, 'Genre')


    

    multiple_line_graphs(ax_line, genre_dataframes, 'Year', 'Global_Sales')
    # bar_graph_over_time(ax_bar, df_global_sales)
    plt.show()
    
    