import numpy as np 
import pandas as pd 


if __name__ == '__main__':
    df = pd.read_csv('../data/cleaned_data.csv')
    print(df.columns)
    print(df.groupby(['Name',  'Genre', 'Publisher']).sum().sort_values(['Rank']))