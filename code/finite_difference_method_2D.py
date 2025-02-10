import numpy as np
import matplotlib.pyplot as plt


a = 0.16
b = 0.66

def f(x, y):
    return np.exp(-(x**2) / a - y**2 / b)


x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
xx, yy = np.meshgrid(x, y)

# analytical
f_anl = f(xx, yy)

fig = plt.figure(figsize=(12, 8))
ax_anl = fig.add_subplot(1, 2, 1, projection="3d")
ax_anl.plot_surface(xx, yy, f_anl, cmap=plt.cm.coolwarm)



# Finite difference method
