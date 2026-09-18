import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# データを生成
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, 100)
y = 2 * x**2 + x + noise

# x → [x, x^2] に変換
X = PolynomialFeatures(degree=2).fit_transform(x.reshape(-1, 1))

# 回帰モデルを作成して学習
model = LinearRegression()
model.fit(X, y)

# 予測
y_pred = model.predict(X)

# パラメータを表示
print("a =", model.coef_[2])
print("b =", model.coef_[1])
print("c =", model.intercept_)

# プロット
plt.scatter(x, y, label="Data")
plt.plot(x, y_pred, label="Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()