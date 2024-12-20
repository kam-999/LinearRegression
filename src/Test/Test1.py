from src.Linear.linear_regression import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5])  # Independent variable
Y = np.array([10, 11, 12, 13, 14]) 

model = LinearRegression()

model.fit(X,Y)

X_ = 6
y = model.predict(X_)

print(y)