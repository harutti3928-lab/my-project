import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


#np.random.seed(0)

N = 200
X = np.random.randn(N, 2)
y = (X[:, 1] > -X[:, 0]).astype(int)

# 初期値は z = 0 * x1 + 1 * x2 + 0 = x2 = 0
# つまり、境界は y = 0 の水平線から開始する
w = np.array([-1.0, 1.0])
b = 0.0

learning_rate = 0.1
epochs = 200
history = []

for _ in range(epochs):
    z = X @ w + b
    y_pred = sigmoid(z)

    grad_w = (1 / N) * X.T @ (y_pred - y)
    grad_b = (1 / N) * np.sum(y_pred - y)

    w -= learning_rate * grad_w
    b -= learning_rate * grad_b

    history.append((w.copy(), b))

fig, ax = plt.subplots(figsize=(6, 5))

x1_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
line, = ax.plot([], [], color='black', linewidth=2, label='Decision Boundary')

ax.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='skyblue', label='Class 0')
ax.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='orange', label='Class 1')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Logistic Regression: from y = 0 to learned boundary')
ax.grid(alpha=0.3)
ax.legend()


def update(frame):
    w_frame, b_frame = history[frame]
    w1, w2 = w_frame

    if abs(w2) < 1e-12:
        x2_values = np.zeros_like(x1_values)
    else:
        x2_values = -(w1 * x1_values + b_frame) / w2

    line.set_data(x1_values, x2_values)
    return line,


animation = FuncAnimation(
    fig,
    update,
    frames=len(history),
    interval=30,
    blit=True,
)

plt.tight_layout()
plt.show()
