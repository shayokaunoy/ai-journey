import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

games = pd.read_csv("games.csv")
print(games)
games.to_sql("games", conn, index=False)


sales = pd.DataFrame([
    {"name": "GTA VI", "copies": 25},
    {"name": "Red Dead Redemption 3", "copies": 12},
    {"name": "Cyberpunk 2078", "copies": 8},
    {"name": "Elden Ring 2", "copies": 5}

])
sales.to_sql("sales", conn, index=False)

# result = pd.read_sql("SELECT COALESCE(games.name, sales.name) AS name, games.price, sales.copies FROM games FULL OUTER JOIN sales ON games.name = sales.name", conn)
# result["copies"] = result["copies"].fillna(0)
# result["price"] = result["price"].fillna(20)
# print(result)

# result = pd.read_sql("SELECT games.name, games.price, sales.copies FROM games JOIN sales ON games.name = sales.name WHERE sales.copies >= 10 ORDER BY sales.copies DESC", conn)
# print(result)

result = pd.read_sql("SELECT genre, SUM(games.price*sales.copies) AS total_revenue FROM games JOIN sales ON games.name = sales.name GROUP BY genre ORDER BY total_revenue DESC", conn)
print(result)
