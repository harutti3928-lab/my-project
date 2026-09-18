import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = 2 * x**2 + x + np.random.normal(0, 1, 100)

a, b, c = np.polyfit(x, y, 2)
y_pred = a * x**2 + b * x + c

print(f"a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")

plt.scatter(x, y, label="Data")
plt.plot(x, y_pred, label="Fit", color='red')
plt.legend()
plt.show()