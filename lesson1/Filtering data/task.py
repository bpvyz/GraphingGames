import pandas as pd

df = pd.read_csv('../dataset.csv')

filter_list = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_df = df[df['platform'].isin(filter_list)][['platform', 'genre']]

print(filtered_df.head())
