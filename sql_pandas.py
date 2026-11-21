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

result = pd.read_sql("SELECT name, price FROM games WHERE rating >= 7", conn)
result["sale_price"] = result["price"]*0.9
print(result)