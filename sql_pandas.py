import sqlite3
import pandas as pd

table = pd.read_csv("games.csv")
print(table)
conn = sqlite3.connect(":memory:")
table.to_sql("games", conn, index=False)


result = pd.read_sql("SELECT genre, AVG(rating) AS avg_rating FROM games GROUP BY genre", conn)
output = result[result["avg_rating"] < 8]
print(output)