import numpy as np
import matplotlib.pyplot as plt

def simulate_point_cloud(n=200):
    angles = np.random.uniform(-0.7, 0.7, n)
    distances = np.random.uniform(1, 15, n)
    velocity = np.random.uniform(-4, 4, n)

    x = distances * np.sin(angles)
    y = distances * np.cos(angles)

    return x, y, velocity

x, y, velocity = simulate_point_cloud()

plt.scatter(x, y, c=velocity)
plt.colorbar(label="velocity")
plt.title("Simple point cloud example")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
