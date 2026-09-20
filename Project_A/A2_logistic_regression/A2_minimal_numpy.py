import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, learning_rate=0.01, num_iterations=1000):
    m, n = X.shape  #(100, 2を想定)
    theta = np.zeros(n)  #(0, 0)の形状のゼロベクトルを作成
    
    for _ in range(num_iterations):
        z = np.dot(X, theta)
        h = sigmoid(z)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient
        
    return theta

# データの生成
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)  # ラベルを生成

# バイアス項を追加
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # バイアス項を追加

# ロジスティック回帰の実行
theta = logistic_regression(X_b, y)

print(f"Learned parameters: {theta}")

# データの可視化
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Class 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Class 1')
# 決定境界の描画
x_values = np.linspace(-3, 3, 100)
y_values = -(theta[0] + theta[1] * x_values) / theta[2]
plt.plot(x_values, y_values, label='Decision Boundary', color='green')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Logistic Regression Decision Boundary')
plt.show()