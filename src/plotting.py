from matplotlib.pyplot import title
import numpy as np 
import pandas as pd
from pandas.io import parsers 
from dataframe import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def pandas_bar_cheat(df, title, y_label, x_label, save_title, stack = True):
    '''
    Uses the base of a pandas plot and updates it according to arguments

    ARGS:
        df - dataframe
        title - string
        y_label - string
        x_label - string
        save_title - string
        stack - Boolean
    RETURNS:
        Bar Graph either stacked or unstacked
    '''
    ax = df.plot.bar(stacked = stack)
    ax.set_title(title, fontsize = 16)
    ax.set_ylabel(y_label, fontsize = 16)
    ax.set_xlabel(x_label, fontsize = 16)
    ax.tick_params(axis='both', which='major', labelsize='12')
    fig.tight_layout()
    ax.legend(loc = 0, prop={'size': 20})
    plt.savefig(save_title)

def bar_graph(ax, df, x_col, y_col, title, ylabel, save_title):
    '''
    Creates a bar graph

    ARGS:
        ax - axes
        df - dataframe
        x_col - string
        y_col - string
        title - string
        ylabel - string
        save_title - string
    '''
    x = range(0, len(df[x_col]))
    ax.bar(x, df[y_col])
    ax.set_xticks(x)
    ax.set_xticklabels(df[x_col])
    ax.set_xlabel(x_col, fontsize = 16)
    ax.set_ylabel(ylabel, fontsize = 16)
    ax.set_title(title, fontsize = 20)
    ax.tick_params(axis='both', which='major', labelsize='12')
    ax.legend()
    fig.tight_layout()
    plt.savefig(save_title)

def multi_line_graphs(ax, df_dict, x_col, y_col):
    '''
    Creates a graph with multiple lines on it

    ARGS:
        ax - axes
        df - dataframe
        x_col - string
        y_col - string
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
    ## Instantiating the figures and axes for graphs
    fig, ax_line = plt.subplots(figsize = (18, 4))
    fig, ax_bar = plt.subplots(figsize = (20, 4))
    
    ## Various objects instantiated for later plugging into functions to make dataframes
    df = pd.read_csv('../data/cleaned_data.csv')
    df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
    genre_list_year = ['Genre', 'Year']
    platform_list = ['Platform']
    sort_list = [ 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    genres = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle'
                , 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
    interesting_genres = ['Action', 'Shooter', 'Sports', 'Role-Playing', 'Platform']

    ##Instatiating multiple dataframes grouped by various lists made before
    df_global_sales = df_group(df, ['Year'], ['Global_Sales']).reset_index()
    df_genres_years =  df_group(df, genre_list_year, sort_list).reset_index()
    df_genres_platform = df_group(df, platform_list, sort_list).reset_index()

    ##Mapping the dataframes to a specific range of years if needed
    df_genres_years = df_genres_years[(df_genres_years['Year'] >= 1991) & (df_genres_years['Year'] < 2016)]
    df_genres_years_1 = df_genres_years[(df_genres_years['Year'] >= 2010) & (df_genres_years['Year'] < 2018)]
    df_global_sales = df_global_sales[(df_global_sales['Year'] >= 1950) & (df_global_sales['Year'] < 2016)]

    ##Instanstiating my final dataframes to be graphed
    df_genres = drop_col(df_genres_years_1, ['Year', 'Global_Sales'], ['Genre'])
    df_genres_platform = df_genres_platform[(df_genres_platform['Platform'] == 'XOne') 
                                            | (df_genres_platform['Platform'] == 'PS4') 
                                            | (df_genres_platform['Platform'] == 'WiiU')]
    df_genres_platform = drop_col(df_genres_platform, ['Global_Sales'])
    df_genres_platform = df_genres_platform.set_index('Platform')
    df_genres_years_global_sales = df_genres_years.drop(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], axis = 1)

    ##Creating a dictionary of dataframes for Genres to graph from
    genre_dataframes = df_dict(df_genres_years_global_sales, interesting_genres, 'Genre')

    ## Creating the multitude of graphs
    multi_line_graphs(ax_line, genre_dataframes, 'Year', 'Global_Sales')
    bar_graph(ax_bar, df_global_sales, 'Year', 'Global_Sales', '# of Global Sales in Relation to Time' ,'# of Global Sales in The Millions', 'bar_over_time')
    pandas_bar_cheat(df_genres_platform, 'Video Game Sales by Region in Relation to Platform'
                            , '# of Video Game Sales Globally in Millions', 'Platforms', 'platforms')
    pandas_bar_cheat(df_genres, 'Sales of Video Games by Region in Relation to Genre'
                            , '# of Sales for Video Games Globally in Millions', 'Genre', 'genre', False)
        
    # plt.show()

    # print(df.head().to_markdown())