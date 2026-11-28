import pandas as pd

#1. CSV file read kore table banano
table = pd.read_csv("game.csv")
print(table)

#2. ekta column neya
print(table["price"])

#3. column er upor calculation
print(table["price"].sum())
print(table["price"].max())
print(table["price"].min())
print(table["price"].mean())
print(table["price"].count())

#4. filert: ekta condition

expensive = table[table["price"] > 40]
print(expensive["name"])

#5. filter: duita condition (& = and, | = or)), protita condition nijer bracket e
both = table[(table["price"] < 50) & (table["rating"] >= 7)]
print(both["name"])

either = table[(table["price"] > 50) | (table["price"] >= 7)]
print(either["name"])

#6. sort: choto theke boro (default)
print(table.sort_values("price"))

#7. sort: boro theke choto
print(table.sort_values("rating", ascending=False))

#8. filter + sort + shudhu name
good = table[table["rating"] >= 8]
print(good.sort_values("price")["name"])  #this is tough to write 

#9. notun column banano
table["sales_price"] = table["price"] * 0.9
table["price_per_rating"] = table["price"]/table["rating"]
print(table)    # in this new column adding topic what if i already have data and which doenst need to calculate then how can i made a new column with those data?

#10. table ke notun CSV file e save kora
table.to_csv("games_sale.csv", index=False)  #i am not familier with this 

#11. groupby: protita genre er hishab
print(table.groupby("genre")["price"].mean())
print(table.groupby("genre")["price"].max())
print(table.groupby("genre")["price"].count())

#12. groupby + sort
print(table.groupby("genre")["price"].sum().sort_values(ascending=False))  #this is tough

#13. missing values: kon column e koyta ghor khali
print(table.isna().sum())

#14. khali ghor ache emon row bad deya
clean = table.dropna()
rated = table.dropna(subset=["rating"]) #i forgot about the part of subset. like whats its task
print(rated("name"))

#15. khali ghor bore dewa
table["genre"] = table["genre"].fillna("unknow")
avg = table["price"].mean()
table["price"] = table["price"].fillna(avg)  # same question like prevuous what if i already have numbers and noo need to calculation then how to fill?

#16. puro table er summery(count, mean, std, min, 25%, 50%, 75%, max)
print(table.describe())
