from matplotlib.pyplot import title
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

def bar_graph_pandas_cheat(df, title, y_label, x_label, save_title, stack = True):
    '''
    Uses the base of a pandas plot and updates it according to arguments
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
    x = range(0, len(df[x_col]))
    if isinstance(y_col, str):
        ax.bar(x, df[y_col](x))
    else:
        for item in y_col:
            ax.bar(x, df[item])
    ax.set_xticks(x)
    ax.set_xticklabels(df[x_col])
    ax.set_xlabel(x_col, fontsize = 16)
    ax.set_ylabel(ylabel, fontsize = 16)
    ax.set_title(title, fontsize = 20)
    ax.tick_params(axis='both', which='major', labelsize='12')
    ax.legend()
    fig.tight_layout()
    plt.savefig(save_title)

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
    # fig, ax_line = plt.subplots(figsize = (18, 4))
    fig, ax = plt.subplots(figsize = (20, 4))
    
    ## Various objects instantiated for later plugging into dataframes.
    df = pd.read_csv('../data/cleaned_data.csv')
    df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales']
    genre_list_year = ['Genre', 'Year']
    platform_list = ['Platform']
    sort_list = [ 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    genres = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle'
                , 'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 'Simulation', 'Sports', 'Strategy']
    interesting_genres = ['Action', 'Shooter', 'Sports', 'Role-Playing', 'Platform']

    df_global_sales = create_dataframe_groupby(df, ['Year'], ['Global_Sales']).reset_index()
    df_genres_years =  create_dataframe_groupby(df, genre_list_year, sort_list).reset_index()
    df_genres_platform = create_dataframe_groupby(df, platform_list, sort_list).reset_index()


    df_genres_years_1 = df_genres_years[(df_genres_years['Year'] >= 2010) & (df_genres_years['Year'] < 2018)]
    df_genres_years = df_genres_years[(df_genres_years['Year'] >= 1991) & (df_genres_years['Year'] < 2016)]
    df_global_sales = df_global_sales[(df_global_sales['Year'] >= 1950) & (df_global_sales['Year'] < 2016)]

    df_genres = df_genres_years_1.drop(['Year', 'Global_Sales'], axis=1).groupby('Genre').sum()


    df_genres_platform = df_genres_platform[(df_genres_platform['Platform'] == 'XOne') | (df_genres_platform['Platform'] == 'PS4') | (df_genres_platform['Platform'] == 'WiiU')]
    df_genres_platform = drop_col(df_genres_platform, ['Global_Sales'])
    df_genres_platform = df_genres_platform.set_index('Platform')
    ax = df_genres_platform.plot.bar(stacked = True)
    ax.set_title('Whatevs')

    
    # df_genres.plot.bar()

    df_genres_years_global_sales = df_genres_years.drop(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], axis = 1)
    genre_dataframes = create_multiple_dataframes(df_genres_years_global_sales, interesting_genres, 'Genre')

    
    

    # multiple_line_graphs(ax_line, genre_dataframes, 'Year', 'Global_Sales')
    # bar_graph_over_time(ax_bar, df_global_sales, 'Year', 'Global_Sales', '# of Global Sales in Relation to Time' 
    # ,'# of Global Sales in The Millions', 'bar_over_time')
    #bar_graph(ax_bar, df_genres_platform, 'Platform', ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], 'Console', '# of Sales in Millions', 'Console Sales in relation to Region', 'bar_console')
    #bar_graph_pandas_cheat(df_genres_platform, 'Video Game Sales by Region in Relation to Platform', '# of Video Game Sales Globally in Millions', 'Platforms', 'platforms')
    bar_graph_pandas_cheat(df_genres, 'Sales of Video Games by Region in Relation to Genre', '# of Sales for Video Games Globally in Millions', 'Genre', 'genre', False)
        
    plt.show()