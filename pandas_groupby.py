import pandas as pd

table =pd.read_csv("games.csv")
print(table)

# print(table.groupby("genre")["price"].mean())
# print(table.groupby("genre")["price"].max())
# print(table.groupby("genre")["rating"].count())
# print(table.groupby("genre")["price"].mean())
# print(table.groupby("genre")["price"].sum().sort_values(ascending=False))

game_7 = table[table["rating"] >= 7]
print(game_7.groupby("genre")["price"].mean().sort_values(ascending=False))