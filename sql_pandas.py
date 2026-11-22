# import sqlite3
# import pandas as pd

# table = pd.read_csv("games.csv")

# conn = sqlite3.connect(":memory:")
# table.to_sql("games", conn)

# result = pd.read_sql("SELECT * FROM games WHERE price > 40", conn)
# print(result)
 
import sqlite3
import pandas as pd

table = pd.read_csv("games.csv")
print(table)
conn = sqlite3.connect(":memory:")
table.to_sql("games", conn, index=False)

# result = pd.read_sql('SELECT genre, MAX(price) AS "MAX Price" FROM games GROUP BY genre', conn)
# output = result.sort_values("MAX Price", ascending=False)
# print(output)

# result = pd.read_sql("SELECT genre, AVG(rating) AS avg_rating FROM games GROUP BY genre", conn)
# output = result[result["avg_rating"] >= 7.5]
# print(output)

# result = pd.read_sql("SELECT name, price FROM games GROUP BY genre", conn)
# condition = result["price"] < 40
# exact = result[condition]
# print(exact)

# result = pd.read_sql("SELECT genre, name, price FROM games", conn)
# output = result[result["price"] < 40]
# print(output)

result = pd.read_sql("SELECT MAX(price) FROM games", conn)
print(result)

result2 = pd.read_sql("SELECT genre, MIN(price) AS min_price FROM games GROUP BY genre", conn)
final = result2.sort_values("min_price", ascending=True)
print(final)