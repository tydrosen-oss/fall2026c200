###############################################
# Prof. Dalkilic
# CH200 Introduction to Computers & Programming
# Fall 2026
# Lab/HW 8 
# Ursala gets a cookie
###############################################

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
import pandas as pd


data =[(1.0, 2.0), (2.0, 3.8), (3.0, 9.5),
        (4.0, 8.0), (5.0, 10.0), (6.0, 12.0)]

data_train = [(1.0, 2.0), (2.0, 3.8), (3.0, 9.5)]
data_test = [(4.0, 8.0), (5.0, 10.0), (6.0, 12.0)]

# (1) get data
path = "D:/tyrosenbaum/fall2026c200/week8"
filename = "data.csv"
df = pd.read_csv(path+filename, header=None)

# see the data frame
print(df)

# (2) split into test and training data
# convert to NumPy array
data_train = df[0:3].values
data_test = df[3:].values

# see the split
# print(data_test)
# print(data_train)

# (3) split x,y & reshape x for sklearn
x_train = data_train[:,0].reshape(-1,1)
y_train = data_train[:,1]

# see the arrays
# print(x_train,y_train)

# (4) split x,y & reshape
x_test = data_test[:,0].reshape(-1,1)
y_test = data_test[:,1]

# see the arrays
# print(x_test, y_test)

# (5) build models
model_ols = LinearRegression(fit_intercept=False).fit(x_train, y_train)
model_ridge = Ridge(alpha=5.0, fit_intercept=False).fit(x_train, y_train)

# (6) calculate MSE: 
ols_mse = mean_squared_error(y_test, model_ols.predict(x_test))
ridge_mse = mean_squared_error(y_test, model_ridge.predict(x_test))

# display MSE for both
print(f"OLS slope:   {model_ols.coef_[0]:.2f} | Test MSE: {ols_mse:.2f}")
print(f"ridge slope: {model_ridge.coef_[0]:.2f} | Test MSE: {ridge_mse:.4f}")

# abscissa for plotting
x_line = np.linspace(0, 6.5, 100).reshape(-1, 1)

# (7) matplotlib 
# plot points
plt.scatter(x_train, y_train, color='blue', s=60, label='data')
plt.scatter(x_test, y_test, color='green', s=60, label=r'Actual model $f(x)=2x$)')

# plot lines
plt.plot(x_line, model_ols.predict(x_line), 'r--', label=f'OLS (m={model_ols.coef_[0]:.2f})')
plt.plot(x_line, model_ridge.predict(x_line), 'k-', linewidth=2, label=f'Ridge (m={model_ridge.coef_[0]:.2f})')
plt.legend()
plt.grid(True)
plt.title("CH200 OLS vs Ridge")
plt.show()
