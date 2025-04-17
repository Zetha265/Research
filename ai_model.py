import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load CSV data
df = pd.read_csv("data.csv")

# Extract features and compute efficiency
X = df["water_liters"].values.reshape(-1, 1)
y = df["energy_wh"] / df["water_liters"]  # Efficiency: Wh per liter

# Polynomial regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Predict & plot
x_range = np.linspace(min(X)[0], max(X)[0], 100).reshape(-1, 1)
y_pred = model.predict(poly.transform(x_range))

plt.scatter(X, y, color='red', label="Data points")
plt.plot(x_range, y_pred, color='blue', label="Polynomial Fit")
plt.xlabel("Water Input (liters)")
plt.ylabel("Efficiency (Wh/L)")
plt.title("Ice Production Efficiency Curve")
plt.legend()
plt.grid(True)
plt.show()

# Optimal point
min_index = np.argmin(y_pred)
optimal_water = x_range[min_index][0]
optimal_eff = y_pred[min_index]
print(f"Optimal water input: {optimal_water:.2f} L")
print(f"Efficiency at this point: {optimal_eff:.2f} Wh/L")
