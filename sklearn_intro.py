import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([[10], [20], [30], [40], [50]])
price = np.array([25, 45, 65, 85, 105])

model = LinearRegression()
model.fit(hours, price)

print(model.predict([[60]]))

print(model.coef_)
print(model.intercept_)