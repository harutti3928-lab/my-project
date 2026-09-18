# A1の練習として、ここではある二次関数にノイズを加えたデータを生成し、
# 線形回帰モデルを用いてそのデータにフィットさせることを目的とします。

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def generate_data(a = 2, b = 1, c = 0, num_points=100):
    # 乱数のシードを固定することで、毎回同じ乱数を生成することができます。
    #np.random.seed(42)
    x = np.linspace(0, 10, num_points)
    noise = np.random.normal(0, 1, num_points)
    y = a * x**2 + b * x + c + noise
    return x, y

def polynomial_regression(x, y, learning_rate=1e-6, num_iterations=int(1e5)):
    # 二次多項式回帰モデルを作成し、データにフィットさせる
    a = 0
    b = 0
    c = 0
    N = len(y)

    # 勾配降下法でパラメータを更新する
    for _ in range(num_iterations):
        y_pred = a * x**2 + b * x + c
        loss = np.mean((y_pred - y) ** 2)
        da = (2/N) * np.sum((y_pred - y) * x**2)
        db = (2/N) * np.sum((y_pred - y) * x)
        dc = (2/N) * np.sum(y_pred - y)
        a -= learning_rate * da
        b -= learning_rate * db
        c -= learning_rate * dc

    y_pred = a * x**2 + b * x + c
    return a, b, c, y_pred

if __name__ == "__main__":
    # データを生成
    x, y = generate_data()

    # 二次多項式回帰を実行
    a, b, c, y_pred = polynomial_regression(x, y)

    # 結果を表示
    print("a =", a)
    print("b =", b)
    print("c =", c)

    # データをプロット
    plt.scatter(x, y, label="Data")

    # フィッティングした曲線をプロット
    plt.plot(x, y_pred, label="Fit", color='red')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
