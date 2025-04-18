import pandas as pd

data = {
    'date': pd.date_range(start='2025-04-01', periods=10, freq='D'),
    'John': [True, False, True, False, True, False, False, True, False, True],
    'Judy': [True, False, False, True, True, False, True, False, False, True]
}

df = pd.DataFrame(data)

df['party'] = df['John'] & df['Judy']

df['days_til_party'] = df.index[::-1]
df['days_til_party'] = df['days_til_party'].where(df['party'])
df['days_til_party'] = df['days_til_party'].bfill()
df['days_til_party'] -= df.index

df['days_til_party'] = df['days_til_party'].astype(int)

df.drop(columns=['party'], inplace=True)

print(df)
