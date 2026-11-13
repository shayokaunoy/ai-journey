import pandas as pd

games = [
    {"name": "GTA VI", "price": 30, "rating": 8},
    {"name": "Red Dead Redemption 3", "price": 60, "rating": 9},
    {"name": "Assassins Creed", "price": 15, "rating": 7},
    {"name": "Battlefield 2050", "price": 45, "rating": 6}
]

table = pd.DataFrame(games)
# print(table)

# # print(table["price"])
# # print(table["price"].sum())
# # print(table["price"].max())
# # print(table["price"].min())
# # print(table["price"].mean())
# # print(table["price"].count())
# print(table["rating"].max())
# print(table["rating"].min())
# print(table["rating"].mean())

# expensive = table[table["price"] > 40]    
# print(expensive["price"])                 
# print(expensive["name"])

# high_rating = table[table["rating"] >= 8]
# print(high_rating["name"])
# print(high_rating["price"].mean())

both = table[(table["price"] > 40) & (table["rating"] > 8)]
print(both)

either = table[(table["price"] > 40) | (table["rating"] > 8)]
print(either)