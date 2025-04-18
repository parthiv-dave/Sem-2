import pandas as pd
import itertools

concerts = pd.DataFrame({
    'date': pd.to_datetime([
        '2024-01-05', '2024-01-10', '2024-02-15', '2024-02-20', 
        '2024-03-25', '2024-01-07', '2024-03-30', '2024-02-28'
    ]),
    'artist': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'venue': ['X', 'Y', 'X', 'Z', 'Y', 'Z', 'X', 'Y']
})

concerts['year_month'] = concerts['date'].dt.to_period('M')

concert_counts = concerts.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

artists = concerts['artist'].unique()
venues = concerts['venue'].unique()
artist_venue_pairs = list(itertools.product(artists, venues))

all_combinations = pd.MultiIndex.from_product([concerts['year_month'].unique(), artist_venue_pairs], names=['year_month', 'artist_venue'])
all_combinations = all_combinations.to_frame(index=False)
all_combinations[['artist', 'venue']] = pd.DataFrame(all_combinations['artist_venue'].tolist(), index=all_combinations.index)
all_combinations.drop(columns=['artist_venue'], inplace=True)

full_data = all_combinations.merge(concert_counts, on=['year_month', 'artist', 'venue'], how='left').fillna(0)

wide_table = full_data.pivot(index='year_month', columns=['artist', 'venue'], values='count').fillna(0)

print(wide_table)