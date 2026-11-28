import pandas as pd

table = pd.read_csv("games.csv")


table["sale_price"] = table["price"] * 0.9
# table.to_csv("games_sales.csv", index=False)

top = table[table["rating"] >= 8]
top.to_csv("top_games.csv", index=False)

