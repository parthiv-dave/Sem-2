import pandas as pd

asking_prices = pd.Series([15000, 18000, 22000, 25000, 17000])
fair_prices = pd.Series([16000, 17500, 23000, 24000, 18000])

good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print("Good deals are at indices:", good_deals)