import pandas as pd

table = pd.read_csv("games_missing.csv")

table["genre"] = table["genre"].fillna("FPS")
avg = table["price"].mean()
table["price"] = table["price"].fillna(avg)
print(table)

avg2 = table["rating"].mean()
table["rating"] = table["rating"].fillna(avg2)
print(table)

print(table.isna().sum())
print(table.describe())