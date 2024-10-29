import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset.csv')

filter_list = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_df = df[df['platform'].isin(filter_list)][['platform', 'genre']]

genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)

platform_order = ['PS4', 'XOne', 'PC', 'WiiU']
genre_counts_reindexed = genre_counts.reindex(platform_order)

genre_counts_reindexed.plot(kind='bar', figsize=(10, 6))

plt.xlabel('platform')
plt.ylabel('count')
plt.xticks(rotation=0)
plt.legend(title='genre')
plt.tight_layout()

plt.show()
