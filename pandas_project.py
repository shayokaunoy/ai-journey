import pandas as pd

table = pd.read_csv("games.csv")

print(table)

high_rating = table[table["rating"] >= 7]

# sorted_game = high_price.sort_values("price", ascending=False)
# print(sorted_game["name"])


# top_price = table.groupby("genre")["price"].max()
# print(top_price.sort_values(ascending=True))
# print(high_rating.groupby("genre")["name"].count())

# top_price = table[table["price"] >= 30]
# sorted_games_byrated = top_price.groupby("genre")["rating"].mean()
# print(sorted_games_byrated.sort_values(ascending=False))

table["hours"] = [60, 80, 30, 20, 50]
hour_calc = table.groupby("genre")["hours"].mean()
print(hour_calc.sort_values(ascending=False))

long_hour = table[table["hours"] >= 50]

long_hour.to_csv("long_games.csv", index=False)