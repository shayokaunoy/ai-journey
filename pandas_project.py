import pandas as pd

table = pd.read_csv("games.csv")

print(table)

low_price = table[table["price"] < 50]
sorted_games = low_price.sort_values("rating", ascending=False)

print(sorted_games["name"])

table["price_per_rating"] = table["price"] / table["rating"]

result = table.groupby("genre")["price_per_rating"].mean().sort_values(ascending=True)

print(result)