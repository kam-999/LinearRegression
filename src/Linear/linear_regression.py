import numpy as np

def hello():
    print("hello")

class LinearRegression:
    def __init__(self):
        self.m = 0
        self.c = 0

    def fit(self,X, Y):

        n = len(X)
        sum_x = np.sum(X)
        sum_y = np.sum(Y)
        sum_xy = np.sum(X * Y)
        sum_x2 = np.sum(X ** 2)
        self.m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        self.c = (sum_y - self.m * sum_x) / n

    def predict(self, X):
        y = self.m * X + self.c
        return y