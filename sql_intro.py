import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute("CREATE TABLE games (name TEXT, price INTEGER, rating INTEGER, genre TEXT)")

conn.execute("INSERT INTO games VALUES ('GTA VI', 30, 9, 'action')")
conn.execute("INSERT INTO games VALUES ('Red Dead Redemption 3', 60, 8, 'action')")
conn.execute("INSERT INTO games VALUES ('Assassins Creed', 15, 6, 'adventure')")
conn.execute("INSERT INTO games VALUES ('Battlefield 2050', 45,7, 'shooter')")

# rows = conn.execute("SELECT genre, SUM(price) FROM games GROUP BY genre ORDER BY SUM(price) DESC").fetchall()
# print(rows)


rows = conn.execute("SELECT genre, AVG(rating) FROM games GROUP BY genre ORDER BY AVG(rating) DESC").fetchall()
print(rows)
