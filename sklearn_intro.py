import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

X = np.array([[60, 2020], [80, 2027], [30, 2014], [20, 2025], [50, 2026],
              [40, 2018], [70, 2023], [10, 2027], [90, 2016], [35, 2024]])
y = np.array([30, 60, 15, 45, 50, 25, 40, 55, 20, 45])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_test)
print(y_test)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_train, y_train))
print(model.score(X_test, y_test))