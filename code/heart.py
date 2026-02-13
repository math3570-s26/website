import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi + 0.01, 0.01)
xhrt = 16 * (np.sin(x) ** 3)
yhrt = 13 * np.cos(x) - 5 * np.cos(2*x) - 2 * np.cos(3*x) - np.cos(4*x)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(xhrt, yhrt, linewidth=2)
ax.fill(xhrt, yhrt, color="red", edgecolor="none")

px = np.array([10, -10, -15, 15])
py = np.array([-10, -10, 10, 10])

for xi, yi in zip(px, py):
    ax.text(xi, yi, "♥", fontsize=22, ha="center", va="center")

ax.text(0, 0, "Happy Valentine's Day!", color="pink", fontsize=20, 
        fontweight="bold", ha="center", va="center")
ax.axis("off")
plt.show()
