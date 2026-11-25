import numpy as np

prices = np.array([30, 60, 15, 45, 50])
names = np.array(["GTA VI", "Red Dead Redemption 3", "Assassins Creed", "Battlefield 2050", "Cyberpunk 2078"])
# print(prices)
# print(prices + 5)
# print(prices * 2)
# print(prices.sum())
# print(prices.max())
# print(prices.mean())

# print(prices > 40)
# print(prices[prices > 40])

copies = np.array([25, 12, 6, 0, 8])
revenue = prices * copies
# print(revenue)
# print(revenue.sum())

# result = revenue[revenue > 500]
# print(result)
# print(result.sum())

# print(names[prices > 40])
# print(copies[prices > 40])

print(names[(prices < 50) & (copies > 5)])