import numpy as np
names = np.array(["GTA VI", "Red Dead Redemption 3", "Assassins Creed Shadows", "Battlefield 2050", "Cyberpunk 2078"])
games = np.array([
    [30,20],
    [60,10],
    [15, 8],
    [45,12],
    [50,15]
])

# print(games)
# print(games.shape)

# print(games[4])
# print(games[:, 1])
# selected = names[games[:, 1] > 10]
# print(selected)

# revenues = games[:, 0] * games[:, 1]
# selected = revenues[games[:, 0] > 40]
# total = selected.sum()
# print(total)

# print(games.mean())
# print(games.mean(axis=0))
# print(games.sum(axis=0))
# print(games.mean(axis=1))
# print(games.sum(axis=1))
print(games.max(axis=0))
