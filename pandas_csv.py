import pandas as pd

table = pd.read_csv("games.csv")


table["sale_price"] = table["price"] * 0.9
table["price_per_rating"] = table["price"] / table["rating"]
print(table.sort_values("price_per_rating")["name"])