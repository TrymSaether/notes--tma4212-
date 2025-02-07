import numpy as np
import matplotlib.pyplot as plt

# Define the domain
x = np.linspace(-2, 2, 100)
t = np.linspace(0, 2, 100)
X, T = np.meshgrid(x, t)

# Initial condition (you can modify this)
def u0(x):
    return np.sin(x)  # Example initial condition

# Solution using method of characteristics
def u(x, t):
    x0 = np.log(np.exp(x) - t)
    return u0(x0)

# Calculate solution on the grid
Z = np.zeros_like(X)
for i in range(len(t)):
    for j in range(len(x)):
        # Only calculate where x0 is real (exp(x) - t > 0)
        if np.exp(x[j]) - t[i] > 0:
            Z[i,j] = u(x[j], t[i])
        else:
            Z[i,j] = np.nan

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, T, Z, cmap='viridis')

# Labels and title
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u(x,t)')
ax.set_title('Solution of u_t + e^{-x}u_x = 0')

# Add colorbar
fig.colorbar(surf)

plt.show()