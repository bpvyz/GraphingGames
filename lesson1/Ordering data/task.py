import pandas as pd

df = pd.read_csv('../dataset.csv')

filter_list = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_df = df[df['platform'].isin(filter_list)][['platform', 'genre']]

genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)

platform_order = ['PS4', 'XOne', 'PC', 'WiiU']
genre_counts_reindexed = genre_counts.reindex(platform_order)